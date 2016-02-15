<template>
  <div class="player" @click="toggleModal()">
    <span v-if="player.common_name">{{ player.common_name }}</span>

    <div class="search" v-show="show">
      <input type="text" v-model="term" debounce="200" @click.stop>

      <span v-if="!items.length">No results!</span>
      <div class="item" v-for="(k, v) in items" @click.stop="setPlayer(v)">
        {{ v.first_name }} {{ v.last_name }} - {{ v.common_name }}
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        item: {},
        items: [],
        term: '',
        show: false
      }
    },

    props: ['index', 'player'],

    watch: {
      'term' (newVal, oldVal) {
        console.log(newVal, oldVal)
        if (newVal) {
          this.$http.get('/api/players/', { query: newVal }).then((res) => {
            this.items = res.data.results
          })
        }

        if (oldVal && this.items.length) {
          this.items = []
        }
      }
    },

    methods: {
      setPlayer(player) {
        this.$parent.$set(`team.player${this.index}`, player)
        this.show = false
      },

      toggleModal() {
        this.show = !this.show
        this.items = []
      }
    }
  }
</script>
