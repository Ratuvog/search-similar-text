import React from 'react';
import './TextSection.css';
import Title from "antd/es/typography/Title";
import {Empty, Icon, List} from "antd";
import { Text } from "../../types/text";

interface PropsDef {
  text: Text|null;
  onSelected: (sentence_id: number) => void;
}

const TextSection: React.FC<PropsDef> = (props: PropsDef) => {
  if (!props.text) {
    return (<Empty description="Select text from list"/>);
  }

  return (
    <div className="">
      <Title style={{marginTop: '24px'}} level={4}>Text #{props.text.id}</Title>
      <List itemLayout="horizontal"
            dataSource={props.text.sentences}
            renderItem={item => (
              <List.Item onClick={() => props.onSelected(item.id)} className="ListItem">
                <List.Item.Meta
                  description={item.sentence}
                />
              </List.Item>
            )}
      />
    </div>
  );
};

export default TextSection;
