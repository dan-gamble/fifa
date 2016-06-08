import Vue from 'vue'
import VueConfig from './vue.config'

// import barSelector from './utils/bar-selector'

new Vue(VueConfig).$mount('body')

document.addEventListener('DOMContentLoaded', () => {
  // barSelector.init(document.querySelector('.pg-Bar_Selector'))
})
