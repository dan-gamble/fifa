import Vue from 'vue'
import VueResource from 'vue-resource'

import Test from './Test.vue'

Vue.use(VueResource)

new Vue({
  el: '#player',
  components: {
    Test
  }
})
