import React from 'react';
import './SearchResultSection.css';
import {Empty, Icon, List} from "antd";
import { Text } from "../../types/text";

interface PropsDef {
  texts: Text[];
  similarTexts: number[];
}

const SearchResultSection: React.FC<PropsDef> = (props: PropsDef) => {
  if (!props.similarTexts.length) {
    return (<Empty description="Select sentence to search similar texts"/>);
  }

  const textsDict = props.texts.reduce((acc, text) => {
    return Object.assign(acc, {[text.id]: text})
  }, {}) as {[key: number]: Text};

  return (
    <List itemLayout="horizontal"
          dataSource={props.similarTexts}
          renderItem={(item: number) => (
            <List.Item>
              <List.Item.Meta
                style={{marginLeft: '12px'}}
                avatar={<Icon type="file-text" style={{ fontSize: '24px', color: '#08c' }} />}
                title={<span >Text #{item}</span>}
                description={textsDict[item].text}
              />
            </List.Item>
          )}
    />  );
};

export default SearchResultSection;
