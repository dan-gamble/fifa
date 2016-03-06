<template>
  <div>
    <input type="text" v-model="builder.name">
    <select v-model="builder.selectedFormation">
      <option v-for="(k, v) in formations | orderBy true"
              value="{{ v }}"
              :selected="builder.selectedFormation === v">{{ k }}</option>
    </select>

    <div>Player 1 position: {{ builder.players['1'].position }}</div>
    <div>Player 2 position: {{ builder.players['2'].position }}</div>
    <div>Player 3 position: {{ builder.players['3'].position }}</div>
    <div>Player 4 position: {{ builder.players['4'].position }}</div>
    <div>Player 5 position: {{ builder.players['5'].position }}</div>
    <div>Player 6 position: {{ builder.players['6'].position }}</div>
    <div>Player 7 position: {{ builder.players['7'].position }}</div>
    <div>Player 8 position: {{ builder.players['8'].position }}</div>
    <div>Player 9 position: {{ builder.players['9'].position }}</div>
    <div>Player 10 position: {{ builder.players['10'].position }}</div>
    <div>Player 11 position: {{ builder.players['11'].position }}</div>
  </div>
</template>

<script type="text/ecmascript-6">
  import store from 'store'

  export default {
    ready () {
      store.dispatch({type: 'UPDATE_POSITIONS', formation: this.builder.selectedFormation})
    },

    data () {
      return {
        builder: this.$select('builder')
      }
    },

    props: {
      formations: {
        coerce (val) {
          return JSON.parse(val)
        }
      }
    },

    watch: {
      'builder.selectedFormation' (val) {
        store.dispatch({type: 'UPDATE_POSITIONS', formation: val})
      }
    },

    methods: {
      test () {
        store.dispatch({type: 'TEST'})
      }
    }
  }
</script>
