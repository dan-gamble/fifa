import Vue from 'vue'
import VueResource from 'vue-resource'

import components from './components'
import store from './store'

Vue.use(VueResource)

Vue.filter('toString', (val) => {
  return String(val)
})

Vue.config.debug = true

export default {
  store,
  components
}
