import Vue from 'vue'
import VueResource from 'vue-resource'
import VueConfig from './vue.config'

Vue.use(VueResource)

new Vue(VueConfig).$mount('body')
