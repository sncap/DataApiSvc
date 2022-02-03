<template>
    <v-toolbar flat>
      <v-menu bottom left>
        <template v-slot:activator="{ on }" >
          <v-app-bar-nav-icon v-on="on"></v-app-bar-nav-icon>
        </template>
        <v-list>
          <v-list-item v-for="(item, i) in links" :key="i" :to="item.to" @click="menu = false">
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item>
        </v-list>

      </v-menu>

    </v-toolbar>
</template>

<script>
  export default {
    name: 'Menu',
    data() {
      return {
        links: [
          {
            to: '/ds',
            icon: 'mdi-table',
            text: 'Data Source'
          },
          {
            to: '/about',
            icon: '',
            text: 'About'
          },
        ],
      };
    },
    methods: {},

  };
</script>

<style lang="scss" scoped>
</style>
