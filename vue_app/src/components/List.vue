<template>
    <div>
        <div v-bind:key="json.id" v-for="json in jsons">
            <List_el v-bind:json="json"></List_el>
        </div>
    </div>
</template>

<script>
import List_el from "./List_el";
    export default {
        name: "List",
        components: {List_el},

        props: ["jsons"]
    }
</script>

<style scoped>


</style>