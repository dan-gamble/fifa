<template xmlns:v-el="http://www.w3.org/1999/xhtml">
  <div>
    Player {{ index + 1 }} position: {{ player.position }}
    <button @click="getResults(index)">Change player</button>
    <input type="text"
           v-model="query"
           v-show="showInput"
           debounce="200"
           v-el:input>
    <span v-if="player.player">{{ player.player.common_name }}</span>
    <span>Chem: {{ overallChemistry }}</span>
    <div>
      <div v-for="result in results">
        <div @click="updatePlayer(result, index)">
          {{ result.first_name }} {{ result.last_name }} - {{ result.common_name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import positionChem from './positionChem'
  import store from 'store'

  export default {
    data () {
      return {
        chemistry: {
          links: 0,
          position: 0,
          boost: 0
        },
        results: [],
        query: '',
        showInput: false
      }
    },

    props: ['index', 'player'],

    computed: {
      overallChemistry () {
        return Object.values(this.chemistry).reduce((prev, next) => {
          return prev + next
        }) || 0
      }
    },

    watch: {
      'player.player' (player) {
        if (player) {
          const positionChemMap = `${this.player.position}:${player.position}`
          this.chemistry.position = positionChem[positionChemMap]
        }
      },

      query (val) {
        if (val !== '') {
          this.$http.get('/api/players', { query: this.query }).then((res) => {
            this.results = res.data.results
          })
        }
      }
    },

    methods: {
      getResults () {
        this.showInput = true

        this.$nextTick(() => {
          this.$els.input.focus()
        })
      },

      updatePlayer (player, index) {
        // Current problem with this is it deletes the current instance and inserts a new one.
        // This kind of works in our current case but might cause problems in the future
        store.dispatch({ type: 'UPDATE_PLAYER_PLAYER', player, index })
        this.query = ''
        this.showInput = false
        this.results = []
      }
    }
  }
</script>
