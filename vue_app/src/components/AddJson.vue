<template>
    <div class="input" >
        <v-container fluid>

             <v-form ref="form" class="son" name="jsonstr" id="jsonstr" method="post" >

                <v-textarea
                        class="content"
                name="content"
                id = "content"
                filled
                label="Json input"
                auto-grow
                value=""
                color="#ffffff"
                background-color="#eeeeff"
              ></v-textarea>
          <v-btn id="content"  class="mr-4" @click="submit">submit</v-btn>
        </v-form>
        </v-container>


    </div>

</template>

<script>

//import {mapState, mapGetters, mapActions} from 'vuex'
//import axios from 'axios'
import Vue from "vue";
import AxiosPlugin from "vue-axios-cors";

Vue.use(AxiosPlugin, AxiosPlugin.default);

export default {
    name: "AddJson",
    data: () => ({
        d:{},
        json:String
      }),
    //props: {json:String},


      methods: {
        submit: function () {
            const options = {
                url: 'http://172.23.0.1:5000/list',
                method: 'POST',
                AccessControlAllowOrigin: "*",


            }
            this.$axios(options, new FormData(this.$refs.form.$el))
                .then( res => this.d = res.data )
                .catch((err) => {
                    alert("bad input "+ err.toString())
                })
         },
        clear () {
        },
      },
    }
</script>

<style scoped>

.input{
}
</style>