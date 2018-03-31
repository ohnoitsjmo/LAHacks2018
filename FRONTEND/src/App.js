import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import { Card } from 'material-ui/Card';

/* Styles */
import './App.css';

/* Pages (for router) */
import Home from './pages/Home';
import Analyze from './pages/Analyze';
import NotFound from './pages/NotFound';

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
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/analyze" component={Analyze} />
          <Route component={NotFound} />
        </Switch>
      </Card>

    </MuiThemeProvider>
  </Router>
);

export default App;
