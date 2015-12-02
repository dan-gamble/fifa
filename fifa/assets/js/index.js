import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

// Get our routes config
import { configRouter } from './routes'

// Tell Vue to use Vue router
Vue.use(VueRouter)
Vue.use(VueResource)

// Router setup
const router = new VueRouter({
  history: true,
  saveScrollPosition: true,
  hashbang: false
})
router.mode = 'html5'

// Assign our routes
configRouter(router)

// Build our base Vue model
const App = Vue.extend(require('./App.vue'))

// Start the router
router.start(App, '#app')

window.router = router
