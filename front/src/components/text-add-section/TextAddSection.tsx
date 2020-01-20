import React, {useCallback, useState} from 'react';
import './TextAddSection.css';
import TextArea from "antd/es/input/TextArea";
import {Button} from "antd";

interface PropsDef {
  onAdded: (data: string) => void;
}

const TextAddSection: React.FC<PropsDef> = (props: PropsDef) => {
  const defaultValue = 'Place your text here...'
  const [value, setValue] = useState(defaultValue);

  const clickHandler = useCallback(() => {
    props.onAdded(value);
    setValue(defaultValue);
  }, [props, value]);

  return (
    <div className="">
        <TextArea rows={5}
                  value={value}
                  onChange={(event) => setValue(event.target.value)}
        />
        <Button className="SaveButton"
                type="primary"
                onClick={clickHandler}>
          Save text
        </Button>
    </div>
  );
};

export default TextAddSection;
