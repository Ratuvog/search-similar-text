from flask import Blueprint, make_response
from webargs.flaskparser import use_kwargs
from src.api.texts_schemes import AddTextSchema, TextSchema, SearchResultSchema
from src.db.connection import db
from src.db.models.sentence import Sentence
from src.db.models.text import Text
from src.services import nlp_service

texts_bp = Blueprint('texts', __name__, url_prefix='/texts')


@texts_bp.route('/', methods=['GET'])
def get_all_texts():
    texts = Text.query.all()
    response_data = TextSchema().dumps(texts, many=True)
    return make_response(response_data, 200, {'Content-Type': 'application/json'})


@texts_bp.route('/<int:text_id>', methods=['GET'])
def get_text_by_id(text_id: int):
    text = Text.query.get(text_id)
    if not text:
        return make_response('Object not found', 404, {'Content-Type': 'text/html'})
    response_data = TextSchema().dumps(text)
    return make_response(response_data, 200, {'Content-Type': 'application/json'})


@texts_bp.route('/', methods=['POST'])
@use_kwargs(AddTextSchema())
def add_text(text: str):
    sentences, text_vector = nlp_service.parse(text)
    new_text = Text(text=text, vector=text_vector)
    for sent in sentences:
        new_text.sentences.append(Sentence(sentence=sent))
    db.session.add(new_text)
    db.session.commit()
    response_data = TextSchema().dumps(new_text)
    return make_response(response_data, 201, {'Content-Type': 'application/json'})


@texts_bp.route('/search-similar/<int:sent_id>', methods=['GET'])
def search_similar_text_by_sentence(sent_id: int):
    sentence = Sentence.query.get(sent_id)
    if not sentence:
        return make_response('Object not found', 404, {'Content-Type': 'text/html'})

    texts = Text.query.filter(Text.id != sentence.text_id).all()
    search_result = nlp_service.search_similar(sentence.sentence, texts)
    response_data = SearchResultSchema().dumps(search_result, many=True)
    return make_response(response_data, 200, {'Content-Type': 'application/json'})
