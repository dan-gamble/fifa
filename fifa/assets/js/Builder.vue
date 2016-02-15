<template>
  <div class="bld-Outer">
    <select v-model="formation">
      <option v-for="(k, v) in formations | orderBy -1" :value="v">
        {{ k }}
      </option>
    </select>

    <div class="players">
      <player index="1" :player="team.player1"></player>
      <player index="2" :player="team.player2"></player>
      <player index="3" :player="team.player3"></player>
      <player index="4" :player="team.player4"></player>
      <player index="5" :player="team.player5"></player>
      <player index="6" :player="team.player6"></player>
      <player index="7" :player="team.player7"></player>
      <player index="8" :player="team.player8"></player>
      <player index="9" :player="team.player9"></player>
      <player index="10" :player="team.player10"></player>
      <player index="11" :player="team.player11"></player>
    </div>

    <code>
      <pre>{{ $data | json }}</pre>
    </code>
  </div>
</template>

<script type="text/ecmascript-6">
  import Player from './Player.vue'

  export default {
    components: {
      Player
    },

    data () {
      return {
        test: 'Hey',
        query: '',
        items: [],
        formation: '3412',
        team: {
          player1: {},
          player2: {},
          player3: {},
          player4: {},
          player5: {},
          player6: {},
          player7: {},
          player8: {},
          player9: {},
          player10: {},
          player11: {}
        }
      }
    },

    props: {
      formations: {
        coerce (val) {
          return JSON.parse(val)
        }
      }
    },

    methods: {
      searchMe () {
        this.$http.get('/api/nations/', { name: val }).then((res) => {
          this.items = res.data.results
        })
      }
    },

    ready () {
      console.log(this.formations)
    }
  }
</script>
