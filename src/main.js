import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

Vue.use(VueResource)
Vue.use(VueRouter)

import { configRouter } from './routes'
import App from './App'

/* eslint-disable no-new */
export const router = new VueRouter({
  history: true,
  saveScrollPosition: true
})
router.mode = 'html5'

configRouter(router)

router.start(App, '#app')
window.router = router
