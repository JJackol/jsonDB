<template v-slot:stat="props">


    <v-container class="stats mx-auto  my-auto py-md-5  grey lighten-5 pb-9"
    fill-height fluid>
<v-row
align="center"
justify="center">

    <v-col >
        <v-row
              no-gutters
        >

        <v-col
            no-gutters>
        <v-card
          class="pa-2"
          outlined
          tile
        >   Number of json files    </v-card>

        </v-col>
        <v-col
            no-gutters>
            <v-card
              class="pa-2"
              outlined
              tile
            >  {{ stat.nr_of_files }}    </v-card>

          </v-col>

        </v-row>

        <v-row
              no-gutters
        >

            <v-col
            no-gutters>
                <v-card
                  class="pa-2"
                  outlined
                  tile
                >   Number of json files   </v-card>

            </v-col>
            <v-col
            no-gutters>
                <v-card
                  class="pa-2"
                  outlined
                  tile
                > {{ stat.nr_values }}   </v-card>

            </v-col>
        </v-row>
    </v-col>


</v-row>
  </v-container>
</template>

<script>


    export default {
        name: "MyStats",
        props:{stat:{}},

    }
</script>

<style scoped>
    .stats{

        margin: fill;
    }

</style>