<template>
  <div class="tree">
    {{ test }}

    <div v-for="item in items">
      {{ item.slug }}
    </div>

    <input type="text" v-model="query" debounce="200">
  </div>
</template>

<script>
  export default {
    data () {
      return {
        test: 'Hey',
        query: '',
        items: []
      }
    },

    watch: {
      'query' (val) {
        this.$http.get('/api/nations/', { name: val }).then((res) => {
          this.items = res.data.results
        })
      }
    },

    methods: {
      searchMe () {
        this.$http.get('/api/nations/', { name: this.query }).then((res) => {
          this.items = res.data.results
        })
      }
    },

    ready () {
      this.$http.get('/api/nations/', { name: this.query }).then((res) => {
        this.items = res.data.results
      })
    }
  }
</script>
