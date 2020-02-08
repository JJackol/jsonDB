<template>
  <json-view class="my" :data="json.data" :rootKey="json.id.toString()" />
</template>

<script>


import { JSONView } from 'vue-json-component';
import Vue from 'vue'
export default Vue.extend({
  components: { 'json-view': JSONView },
  props:["json"]
});

</script>

<style scoped>

.my {
}

</style>