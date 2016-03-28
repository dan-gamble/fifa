<template>
  <div class="gbs-Outer">
    <input class="gbs-Input"
           type="text"
           placeholder="Search.."
           v-model="query"
           debounce="300">

    <div class="gbs-Results" v-show="results.length">
      <a class="gbs-Result" v-for="result in results" :href="result.cached_url">
        {{ result.common_name }}
      </a>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        query: '',
        results: []
      }
    },

    watch: {
      query (val) {
        if (val !== '') {
          this.$http.get('/api/players', { query: this.query }).then((res) => {
            this.results = res.data.results
          })
        } else if (val === '') {
          this.results = []
        }
      }
    }
  }
</script>
