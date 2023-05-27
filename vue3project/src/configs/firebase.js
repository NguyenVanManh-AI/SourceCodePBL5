// import firebase from 'firebase/app';
// import * as firebase from "firebase/app";
// import 'firebase/auth';
// import 'firebase/firestore';

import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';
import 'firebase/auth';

const  firebaseConfig = {
    apiKey: "AIzaSyAaJzU2JIjhqi-AJCXFU2W2hg_SfQNtG3w",
    authDomain: "pbl5-35471.firebaseapp.com",
    projectId: "pbl5-35471",
    storageBucket: "pbl5-35471.appspot.com",
    messagingSenderId: "749894916142",
    appId: "1:749894916142:web:8aa7c77f2326a7bda2a7bf",
    measurementId: "G-KEPXC1CM1V"
}
firebase.initializeApp(firebaseConfig)

const fireStoreCore = firebase.firestore()
export {fireStoreCore}

