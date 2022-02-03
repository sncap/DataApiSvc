import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import Menu from "@/components/Menu.vue"
import dataSource from '../views/DataSource.vue'
import DataService from '../views/DataService.vue'
import DSC from '../views/DSC.vue'

Vue.use(VueRouter)

  const routes: Array<RouteConfig> = [
    {
      path: '/',
      name: 'Home',
      component: DSC
    },
    {
      path: '/',
      name: 'Menu',
      component: Menu
    },
    {
      path: '/ds',
      name: 'ds',
      component: dataSource
    },
    {
      path: '/dsvc',
      name: 'dsvc',
      component: DataService
    },
    {
      path: '/dsc',
      name: 'dsc',
      component: DSC
    },
    {
      path: '/about',
      name: 'About',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
