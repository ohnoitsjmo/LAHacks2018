import React from 'react';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';

const Analyze = () => (
  <div>
    <h2>Input Text</h2>
    <TextField
      hintText="Paste or write text here"
      floatingLabelText="Text to interpret"
      multiLine={true}
      rows={4}
      fullWidth={true}
      style={{
        marginBottom: "1rem"
      }}
    />
    <RaisedButton label="Analyze" primary={true} />
  </div>
);

export default Analyze;
