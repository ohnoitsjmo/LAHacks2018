import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'
import { blue600 } from 'material-ui/styles/colors';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import AppBar from 'material-ui/AppBar';
import { Card } from 'material-ui/Card';

/* Styles */
import './App.css';

/* Pages (for router) */
import Home from './pages/Home';
import Analyze from './pages/Analyze';
import NotFound from './pages/NotFound';

const theme = getMuiTheme({
  palette: {
    primary1Color: blue600,
  },
});

const App = () => (
  <Router>
    <MuiThemeProvider muiTheme={theme}>
      <AppBar
        className="App-header"
        title="On The Go Lingo"
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
