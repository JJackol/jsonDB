<template>
<div class="contener pa-3 pa-10">

<v-container fill-height>
  <v-row align="center"
      justify="center">

      <v-col>
        <MyStats v-bind:stat="data.stat"></MyStats>


        <AddJson></AddJson>


        <List_el v-bind:jsons="data.jsons"></List_el>

      </v-col>
  </v-row>
</v-container>



</div>
</template>

<script>
import axios from 'axios'
import MyStats from "./MyStats";
import List_el from './List_el'
import AddJson from "./AddJson";
import Vue from "vue";
import AxiosPlugin from "vue-axios-cors";

Vue.use(AxiosPlugin);
  export default {
    name: 'HelloWorld',
    components:{AddJson, MyStats, List_el},

    data: () => ({
      data:{
        jsons:[],
        stat:{},
      }
    }),

    created: function () {
            const options = {
                url: 'http://172.23.0.1:5000/list',
                method: 'GET',
                AccessControlAllowOrigin: "*",

            }
            axios(options)
                .then( res => this.data = res.data)
                .catch((err) => {
                    console.error('Login failed.', err);
                })
         },
    mounted() {
            const options = {
                url: 'http://172.23.0.1:5000/list',
                method: 'GET',
                AccessControlAllowOrigin: "*",

            }
            axios(options)
                .then( res => this.data = res.data)
                .catch((err) => {
                    console.error('Login failed.', err);
                })
         }

  }
</script>

<style>
.contener {
  margin: auto;
  padding-top: 20px;
  padding-bot: 20px;
  margin: fill;
  background-color: cornflowerblue;
  height: 100%;
}
</style>