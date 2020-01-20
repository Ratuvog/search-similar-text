import React, {useCallback, useEffect, useState} from 'react';
import './App.css';
import {Divider, Layout} from "antd/es";
import TextList from "./components/text-list/TextList";
import SearchResultSection from "./components/search-result-section/SearchResultSection";
import TextAddSection from "./components/text-add-section/TextAddSection";
import TextSection from "./components/text-section/TextSection";
import Title from "antd/es/typography/Title";
import {SearchResult, Text} from './types/text';
import { texts as textsAPI } from "./api";
import {notification} from "antd";

const { Sider } = Layout;

const App: React.FC = () => {
  const [texts, setTexts] = useState([] as Text[]);
  const [activeText, setActiveText] = useState(null);
  const [similarTexts, setSimilarTexts] = useState([] as number[]);

  const addTextHandler = useCallback((data: string) => {
    textsAPI.addText(data).then((response) => {
      if (response.status !== 201) {
        notification.error({
          message: 'Add text error',
          description: response.data
        });
        return;
      }
      const newText = response.data as Text;
      if (newText) {
        const lastIndex = texts.length;
        setTexts([...texts, newText]);
        setActiveText(lastIndex as any);
      }
    });
  }, [texts]);

  const selectTextHandler = useCallback((index: number) => setActiveText(index as any), []);

  const searchSimilarTexts = useCallback((sentence_id: number) => {
    textsAPI.searchSimilarTexts(sentence_id).then((response) => {
      if (response.status !== 200) {
        notification.error({
          message: 'Search similar error',
          description: response.data
        });
        return;
      }
      const searchResult = response.data as SearchResult[];
      const searchResultIndexes = searchResult.map((res) => res.text_id);
      setSimilarTexts(searchResultIndexes)
    });

  }, []);

  useEffect(() => {
    textsAPI.fetchAll().then((response) => {
      if (response.status !== 200) {
        notification.error({
          message: 'Fetching error',
          description: response.data
        })
      }
      setTexts(response.data || [] as Text[]);
    });
  }, []);

  const selectedText = activeText !== null ? texts[activeText as any] : null;

  return (
    <Layout className="App">
      <Sider width={400} style={{ background: '#fff' }}>
        <Title style={{marginTop: '24px', marginLeft: '12px'}} level={4}>Stored texts</Title>
        <TextList texts={texts} onSelected={selectTextHandler}/>
      </Sider>
      <Layout style={{ padding: '24px' }}>
        <Title level={4}>Add new text</Title>
        <TextAddSection onAdded={addTextHandler}/>
        <Divider />
        <TextSection text={selectedText} onSelected={searchSimilarTexts}/>
      </Layout>
      <Sider width={400} style={{ background: '#fff' }}>
        <Title style={{marginTop: '24px', marginLeft: '12px'}} level={4}>Similar texts</Title>
        <SearchResultSection texts={texts} similarTexts={similarTexts} />
      </Sider>
    </Layout>
  );
};

export default App;
