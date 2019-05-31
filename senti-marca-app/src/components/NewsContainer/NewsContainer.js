import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import PositivoEmoji from '../../assets/positivo.png';
import NegativoEmoji from '../../assets/negativo.png';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const styles = {
  card: {
    width: '23%',
    margin: '1rem 1%',
    display: 'inline-block',
    height: '32rem'

  },
  media: {
    height: 200,
  },
};

function MediaCard(props) {
  const { classes, noticia: { imageUrl, content, title, clasificacion, publishedAt } } = props;
  const previewContent = content.length > 150 ? content.substring(0,150)+"..." : content;
  return (

    <Link to={`/noticia/${publishedAt}`}>
    <Card className={classes.card}>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image={imageUrl}
            title={title}
          />
          <ClasificacionImg src={clasificacion === "positivo"? PositivoEmoji : NegativoEmoji} />
          <CardContent>
            <Typography gutterBottom variant="h5" component="h2">
              {title}
            </Typography>
            <Typography component="p">
              {previewContent}
            </Typography>
          </CardContent>
        </CardActionArea>
    </Card>

    </Link>
  );
}

MediaCard.propTypes = {
  classes: PropTypes.object.isRequired,
};

const ClasificacionImg = styled.img`
    position: relative;
    width: 6rem;
    bottom: 4rem;
    left: 34%;
    margin-bottom: -4rem;
`

export default withStyles(styles)(MediaCard);