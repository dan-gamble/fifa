<template>
  <div class="player" @click="findPlayer()">
    Player

    <input type="text" v-model="term" v-show="show" debounce="200">

    <span v-if="!items.length">No results!</span>
    <div class="item" v-for="(k, v) in items">
      {{ v.first_name }} {{ v.last_name }} - {{ v.common_name }}
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
      findPlayer () {
        this.show = true
      }
    }
  }
</script>
