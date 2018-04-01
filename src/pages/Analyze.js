import React, { Component } from 'react';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import Highlighter from 'react-highlight-words';

class Analyze extends Component {
   constructor() {
      super();
      this.state = { 
         fullText: "",
         showAnalysis: false
      };
      this.handleChange = this.handleChange.bind(this);
      this.analyzeText = this.analyzeText.bind(this);
   }

   handleChange(e) {
      this.setState({ 'fullText': e.target.value });
   }

   analyzeText() {
      const analyzeText = this.state.showAnalysis;
      this.setState({ showAnalysis: !analyzeText });
   }

   render() {
      const showAnalysis = this.state.showAnalysis;
      return (
         <div>
            {!showAnalysis ? (
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
                      onChange={this.handleChange}
                  />
                  <RaisedButton 
                     label="Analyze" 
                     primary={true} 
                     onClick={this.analyzeText} />
               </div>
            ) : (
               <div>
                  <h2>Analyzed Text</h2>
                  <Highlighter
          	         highlightClassName="highlighted"
          	         searchWords={["asdf", "or", "the"]}
          	         autoEscape={true}
          	         textToHighlight={this.state.fullText}
          	      />
                  <br/>
                  <RaisedButton 
                     label="Input more text" 
                     primary={true} 
                     onClick={this.analyzeText} />
               </div>
            )}
      </div>
      );
   }
}

export default Analyze;
