import React from 'react';
import NoticiaPage from '../components/NoticiaPage/NoticiaPage';
import styled from 'styled-components';
import CircularProgress from '@material-ui/core/CircularProgress';
import PropTypes from 'prop-types';

class Main extends React.Component {

    state={noticia: ''}

    static propTypes = {
        noticias: PropTypes.any,
    }
    static defaultProps = {
        noticias: [],
    }

    componentDidMount() {
      const { match: { params }, noticias } = this.props;
      this.setState({noticia: noticias.find(n => n.publishedAt === params.id)})
    }

  render(){
    return (
        <Container>
          {!this.props.noticias.length || !this.state.noticia ? 
            <CircularProgress /> : 
            <NoticiaPage noticia={this.state.noticia} />
          }
        </Container>
    );
  }
}

const Container = styled.div`
  width: 100%;
`;

export default Main;
