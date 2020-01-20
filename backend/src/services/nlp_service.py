from dataclasses import dataclass
from typing import Optional, Tuple, List

import numpy as np
import spacy
from spacy.language import Language
from spacy.tokens.doc import Doc

from src.db.models.text import Text

nlp: Optional[Language] = None


def init():
    global nlp
    nlp = spacy.load("en_core_web_md")


def process_sentence(sentence: Doc) -> Doc:
    result = []
    for token in sentence:
        if token.text.lower() in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    return nlp(" ".join(result))


def parse(text: str) -> Tuple[List[str], np.ndarray]:
    doc = nlp(text)
    sentences = []
    vectors = []
    for sent in doc.sents:
        sentences.append(str(sent))
        processed_sentence = process_sentence(sent)
        vectors.append(processed_sentence.vector)

    return sentences, np.array(vectors)


@dataclass
class SearchResult:
    text_id: int
    score: float


def search_similar(sentence: str, texts: List[Text]) -> List[SearchResult]:
    result = []
    processed_sentence = process_sentence(nlp(sentence))
    for text in texts:
        result.append(SearchResult(
            text_id=text.id,
            score=np.median(cos_matrix_multiplication(text.vector, processed_sentence.vector))
        ))
    result.sort(key=lambda x: x.score, reverse=True)
    return result


def cos_matrix_multiplication(matrix: np.ndarray, vector: np.ndarray):
    """
    Calculating pairwise cosine distance using matrix vector multiplication.
    """
    dotted = matrix.dot(vector)
    matrix_norms = np.linalg.norm(matrix, axis=1)
    vector_norm = np.linalg.norm(vector)
    matrix_vector_norms = np.multiply(matrix_norms, vector_norm)
    return np.divide(dotted, matrix_vector_norms)
