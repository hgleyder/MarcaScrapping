import React from 'react';
import './App.css';
import AppBar from './components/AppBar/AppBar';
import { ThemeProvider } from '@material-ui/styles';
import theme from './theme';
import styled from 'styled-components';
import firebaseDatabase from './firebase';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Main from './Screens/Main';
import Noticia from './Screens/Noticia';
import _ from 'lodash';

class App extends React.Component {

  state= {
    noticias: [],
  }

  componentDidMount(){
    firebaseDatabase.ref('/news').on('value', snapshot => {
      const noticias =  Object.values(snapshot.val()).map(n => ({...n, date: new Date(n.publishedAt)}));
      this.setState({
        noticias: _.orderBy(noticias, ['date'], ['desc']),
      })
    })
  }

  render(){
    console.log(this.state.noticias)
    return (
      <div className="App">
      <Router>
      <ThemeProvider theme={theme}>
        <AppBar />
        <Container>
            <Route path="/" exact component={() => <Main noticias={this.state.noticias} />} />
            <Route path="/noticia/:id" component={(props) => <Noticia {...props} noticias={this.state.noticias} />} />
        </Container>
      </ThemeProvider>
      </Router>
    </div>
    );
  }
}

const Container = styled.div`
  width: 88%;
  margin: 4rem 6%;
`;

export default App;
