 <template v-slot:default="props">

   <v-col class="colu mx-auto py-3 ">
      <v-row class="m_cell  pa-sm-2 " v-for="(item, i) in jsons"
            :key="i"
            cols="1"
             filled
            auto-grow
             pa2
          >
            <v-card class="elem">
              <v-card-title class="subheading font-weight-bold">{{ i }}</v-card-title>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item
                  v-for="(key, index) in item"
                  :key="index">
                  <v-list-item-content  :class="{ 'blue--text':0}">{{ index }}:</v-list-item-content>
                  <v-list-item-content  class="align-end" :class="{ 'blue--text':10  }">{{ key }}</v-list-item-content>
                </v-list-item>
              </v-list>

            </v-card>

        </v-row>
    </v-col>
 </template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: "List_el",
  props:{ jsons:{} },
});
</script>

<style scoped>

.colu {
  width: 50%;
  margin: auto;
  padding-top: 2px;
  padding-bot: 2px;
  background-color: dodgerblue;
  height: fit-content;
}

.elem{
  min-width: 200px;
  max-width: 80%;
  margin: auto;
  background-color: darkorange;
}
</style>