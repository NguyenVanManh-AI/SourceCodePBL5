import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'  
import router from './router/routes' 

import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import Paginate from "vuejs-paginate-next";

import storeConfigs  from './store/store'

import { quillEditor } from "vue3-quill";

import gAuthPlugin from 'vue3-google-oauth2';
let gauthClientId = "779842371071-gn56d5d8o7l8blerqn3nb75v3vnhsbqf.apps.googleusercontent.com";

import Notifications from "vue3-vt-notifications";
import "tailwindcss/dist/tailwind.css";

import DisableAutocomplete from 'vue-disable-autocomplete';
import print from 'vue3-print-nb'
import Particles from "particles.vue3";

import { fireStoreCore } from './configs/firebase';

const app = createApp(App);

app.use(gAuthPlugin, {
  clientId: gauthClientId,
  scope: 'email',
  prompt: 'consent',
})

app.use(router);
app.use(VueAxios, axios)
app.use(storeConfigs)
app.use(Paginate)
app.use( quillEditor )
app.use( Notifications )
app.use(DisableAutocomplete)
app.use(print)
app.use(Particles)
app.use(fireStoreCore)
app.mount('#app')
