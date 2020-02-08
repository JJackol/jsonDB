import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'

Vue.config.productionTip = false

import JSONView from "vue-json-component";
Vue.use(JSONView)
Vue.use(Vuex)

new Vue({
  render: h => h(App),
}).$mount('#app')


const store = new Vuex.Store({
  state: {
    jsons: {}
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

store.state;