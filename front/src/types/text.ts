export interface Sentence {
  id: number;
  sentence: string;
}

export interface Text {
  id: number;
  text: string;
  sentences: Sentence[]
}

export interface SearchResult {
  text_id: number;
  score: number;
}