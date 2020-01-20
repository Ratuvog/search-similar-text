import React from 'react';
import './TextList.css';
import {List, Icon, Empty} from "antd";
import { Text } from "../../types/text";

interface PropsDef {
  texts: Text[];
  onSelected: (index: number) => void;
}


const TextList: React.FC<PropsDef> = (props: PropsDef) => {
  if (props.texts.length === 0) {
    return (<Empty description="Add new text"/>);
  }

  return (
    <List itemLayout="horizontal"
          dataSource={props.texts}
          renderItem={(item, index) => (
              <List.Item onClick={() => props.onSelected(index)} className="ListItem">
                <List.Item.Meta
                    style={{marginLeft: '12px'}}
                    avatar={<Icon type="file-text" style={{ fontSize: '24px', color: '#08c' }} />}
                    title={<span >Text #{item.id}</span>}
                    description={item.text.substring(0, 150) + '...'}
                />
              </List.Item>
          )}
    />
  );
};

export default TextList;
