import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import Button from '@material-ui/core/Button';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import PositivoEmoji from '../../assets/positivo.png';
import NegativoEmoji from '../../assets/negativo.png';
import styled from 'styled-components';

const styles = {
  card: {
    width: '80%',
    margin: '1rem 1%',
    display: 'inline-block',

  },
  media: {
    height: '25rem',
  },
  titulo: {
    marginBottom: '2rem'
  },
  contenido: {
    textAlign: 'justify',
    margin: '0rem 2rem'
  },
  button: {
    marginTop: '2rem',
    marginBottom: '3rem',
    fontSize: '1.2rem',
    fontWeight: '700',
  }
};

function MediaCard(props) {
  const { classes, noticia: { imageUrl, content, title, clasificacion, url } } = props;
  return (
    <Card className={classes.card}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image={imageUrl}
          title={title}
        />
        <ClasificacionImg src={clasificacion === "positivo"? PositivoEmoji : NegativoEmoji} />
        <CardContent>
          <Typography className={classes.titulo} gutterBottom variant="h3" component="h2">
            {title}
          </Typography>
          <Typography className={classes.contenido} component="h2" variant="h6">
            {content}
          </Typography>
          <Button variant="contained" href={url} target="_blank" color="secondary" className={classes.button}>
            Ver noticia en Marca.com
          </Button>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

MediaCard.propTypes = {
  classes: PropTypes.object.isRequired,
};

const ClasificacionImg = styled.img`
    position: relative;
    width: 12rem;
    bottom: 8rem;
    left: 34%;
    margin-bottom: -8rem;
`

export default withStyles(styles)(MediaCard);