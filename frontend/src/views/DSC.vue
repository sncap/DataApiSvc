<template>
    <div>
        <data-source/>
        <br>
        <data-service/>
    </div>
</template>

<script>
import DataService from "./DataService";
import DataSource from "./DataSource";
    export default {
        name: "DSC",
        components: {
            DataSource,
            DataService
        }
    }
</script>

<style scoped>

</style>
