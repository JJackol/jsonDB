<template>
    <div class="input" >
        <v-container fluid>

             <v-form ref="form" class="son" name="jsonstr" id="my_jsonstr" method="post" action="http://172.23.0.1:5000/list">

                <v-textarea
                type="text"
                class="content"
                name="content"
                id = "content"
                filled
                label="Json input"
                auto-grow
                color="#ffffff"
                background-color="#eeeeff"
              ></v-textarea>
          <v-btn type="submit" @click="my_submit" class="mr-4" >submit</v-btn>
        </v-form>
        </v-container>


    </div>

</template>

<script>

//import {mapState, mapGetters, mapActions} from 'vuex'
//import axios from 'axios'
import Vue from "vue";
import AxiosPlugin from "vue-axios-cors";

Vue.use(AxiosPlugin);

export default {
    name: "AddJson",

    data: () => ({
        d:{},
        json:"String-v-model",
        out: {content: ""},
      }),
    //props: {json:String},


      methods: {
        my_submit: function () {
            const options = {
                url: 'http://172.23.0.1:5000/list',
                method: 'POST',
                AccessControlAllowOrigin: "*",
            }
            options
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