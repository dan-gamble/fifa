import Vue from 'vue'
import Revue from 'revue'
import {createStore} from 'redux'
import reducers from './reducers'

const reduxStore = createStore(reducers)

const store = new Revue(Vue, reduxStore)

export default store
