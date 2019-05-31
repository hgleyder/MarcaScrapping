import firebase from 'firebase';

var config = {
    apiKey: "AIzaSyARtfsU3m9cAIpSVVpVZ_3ue_sZMPJlQ94",
    authDomain: "sentimarca.firebaseapp.com",
    databaseURL: "https://sentimarca.firebaseio.com",
    projectId: "sentimarca",
    storageBucket: "sentimarca.appspot.com",
    messagingSenderId: "990897104382",
    appId: "1:990897104382:web:232f3be72a1f093c"
  };

firebase.initializeApp(config);

export default firebase.database();