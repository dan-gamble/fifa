import Vue from 'vue'
import Revue from 'revue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import store from './store'

// Get our routes config
import { configRouter } from './routes'

// Tell Vue to use Vue router
Vue.use(Revue)
Vue.use(VueRouter)
Vue.use(VueResource)

// Router setup
const router = new VueRouter({
  history: true,
  saveScrollPosition: true,
  hashbang: false,
  linkActiveClass: 'active'
})
router.mode = 'html5'

// Assign our routes
configRouter(router)

// Build our base Vue model
const App = Vue.extend(require('./App.vue'))

// Start the router
router.start(App, '#app')

window.router = router
