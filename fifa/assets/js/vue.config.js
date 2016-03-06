import Vue from 'vue'

import components from './components'
import store from 'store'

Vue.filter('toString', (val) => {
  return String(val)
})

Vue.config.debug = true

export default {
  components,

  data () {
    return {
      builder: this.$select('builder')
    }
  },

  methods: {
    test () {
      store.dispatch({ type: 'TEST' })
    }
  }
}