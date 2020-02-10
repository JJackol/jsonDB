<template>
    <div class="input" >
        <v-container fluid>


             <v-form ref="form" class="jsonstr" name="jsonstr" id="my_jsonstr">

                <v-textarea
                class="content"
                name="content"
                id = "content"
                filled
                label="Json input"
                auto-grow
                color="#ffffff"
                background-color="#eeeeff"
                v-model="json"
              ></v-textarea>
          <v-btn type="button" @click="my_submit" class="mr-4" >submit</v-btn>
        </v-form>
        </v-container>


    </div>

</template>

<script>

//import {mapState, mapGetters, mapActions} from 'vuex'
import axios from 'axios'
import Vue from "vue";
import AxiosPlugin from "vue-axios-cors";
//import VForm from "vuetify/lib/components/VForm/VForm";

Vue.use(AxiosPlugin);

export default {
    name: "AddJson",


    data: () => ({
        d:{},
        json:"String-v-model",
        content: "",
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
            axios.post('http://172.23.0.1:5000/list', {"content": this.json}  , options)
                .then( request => {
                    if(request.data['done'])
                        alert("JSON inserted into DB")
                    else
                        alert("bad input" )
                } )
                .catch((err) => {
                    alert(+ err.toString())
                })
            console.log(this.d)
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