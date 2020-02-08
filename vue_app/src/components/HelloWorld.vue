<template>
  <div>

    <List id="lista" v-bind:jsons="jsons"></List>
  </div>
</template>

<script>

import axios from 'axios'
import List from "./List";

export default {
  name: 'HelloWorld',
  components: {List},
  jsons: [],
  data(){
    return{
      jsons: []
    }
  },

  created: function () {
    axios.get('http://localhost:5000/list')
    .then(res => this.jsons = res.data)
  },
  mounted() {
    axios.get('http://localhost:5000/list')
    .then(res => this.jsons = res.data)
    .catch(err => console.log(err))
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
