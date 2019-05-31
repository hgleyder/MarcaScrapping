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

class App extends React.Component {

  state= {
    noticias: [],
  }

  componentDidMount(){
    firebaseDatabase.ref('/news').on('value', snapshot => {
      this.setState({
        noticias: Object.values(snapshot.val()),
      })
    })
  }

  render(){
    console.log(this.state.noticias)
    return (
      <div className="App">
      <ThemeProvider theme={theme}>
        <AppBar />
        <Container>
          <Router>
            <Route path="/" exact component={() => <Main noticias={this.state.noticias} />} />
            <Route path="/noticia/:id" component={(props) => <Noticia {...props} noticias={this.state.noticias} />} />
          </Router>
        </Container>
      </ThemeProvider>
    </div>
    );
  }
}

const Container = styled.div`
  width: 94%;
  margin: 4rem 3%;
`;

export default App;
