import http from "./http";

export default {
  fetchAll: () => {
    return http.get(`/texts/`);
  },

  addText: (data: string) => {
    return http.post(`/texts/`, { text: data });
  },

  searchSimilarTexts: (sentence_id: number) => {
    return http.get(`texts/search-similar/${sentence_id}`);
  },
};
