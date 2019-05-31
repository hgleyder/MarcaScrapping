import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Logo from '../../assets/SENTIMARCA.png'
import { Link } from 'react-router-dom';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    position: 'fixed',
    width: '100%',
    zIndex: '100',
    top: '0rem'
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  logo:{
    height: '3.5rem',
  },
}));

function DenseAppBar() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar variant="dense">
            <Link to="/">
              <img src={Logo} alt="logo" className={classes.logo} />
            </Link>
        </Toolbar>
      </AppBar>
    </div>
  );
}
export default DenseAppBar;