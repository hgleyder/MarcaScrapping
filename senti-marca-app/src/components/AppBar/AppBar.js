import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

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
}));

function DenseAppBar() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit">
            SentiMARCA
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
export default DenseAppBar;