<template>
  <div>
    <input type="text" v-model="builder.name">
    <select @input="updateSelectedFormation">
      <option v-for="(k, v) in formations | orderBy true"
              value="{{ v }}"
              :selected="builder.selectedFormation === v">{{ k }}</option>
    </select>

    <player v-for="player in builder.players" :player="player" :index="$index"></player>
  </div>
</template>

<script type="text/ecmascript-6">
  import Player from './Player.vue'
  import * as actions from './actions'

  export default {
    vuex: {
      actions,
      getters: {
        builder: (state) => state.builder
      }
    },

    components: {
      Player
    },

    ready () {
      this.updatePlayerPositions({ formation: this.builder.selectedFormation })
      this.updatePlayerLinks({ formation: this.builder.selectedFormation })
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
        this.updatePlayerPositions({ formation: val })
        this.updatePlayerLinks({ formation: val })
      }
    }
  }
</script>
