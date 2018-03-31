import React from 'react';
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import { Card } from 'material-ui/Card';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import './App.css';

const Home = () => (
  <div>
    <h2>Welcome!</h2>
  </div>
);

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

const App = () => (
  <Router>
    <MuiThemeProvider>
      <AppBar
        className="App-header"
        title="Literally"
        showMenuIconButton={false}
        style={{
          padding: "0 10vw"
        }}
      />

      <Card className="App-card">
        <Route exact path="/" component={Home} />
        <Route path="/analyze" component={Analyze} />
      </Card>

    </MuiThemeProvider>
  </Router>
);

export default App;
