import React from 'react';
import NewsContainer from '../components/NewsContainer/NewsContainer';
import styled from 'styled-components';
import CircularProgress from '@material-ui/core/CircularProgress';
import PropTypes from 'prop-types';

class Main extends React.Component {
    static propTypes = {
        noticias: PropTypes.any,
    }
    static defaultProps = {
        noticias: [],
    }
  render(){
    return (
        <Container>
          {!this.props.noticias.length ? <CircularProgress /> : this.props.noticias.map(noticia => 
              <NewsContainer key={noticia.publishedAt} noticia={noticia} />
            )}
        </Container>
    );
  }
}

const Container = styled.div`
  width: 100%;
`;

export default Main;
