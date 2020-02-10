import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'
import App from './App.vue'
import VueAxiosCors from 'vue-axios-cors'
import vuetify from './plugins/vuetify';
import AxiosPlugin from 'vue-axios-cors';


Vue.use(AxiosPlugin, Axios)
Vue.config.productionTip = false;
Vue.use(Vuex);
Vue.use(VueAxiosCors);

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app');


