<template>
  <div>
    <input type="text" v-model="builder.name">
    <select v-model="builder.selectedFormation">
      <option v-for="(k, v) in formations | orderBy true"
              value="{{ v }}"
              :selected="builder.selectedFormation === v">{{ k }}</option>
    </select>

    <player v-for="player in builder.players" :player="player" :index="$index"></player>
  </div>
</template>

<script type="text/ecmascript-6">
  import Player from './Player.vue'

  import store from 'store'

  export default {
    components: {
      Player
    },

    ready () {
      store.dispatch({ type: 'UPDATE_POSITIONS', formation: this.builder.selectedFormation })
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
