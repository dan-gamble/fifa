<template>
  <div class="gbs-Outer">
    <span class="gbs-Icon" @click="handleIconClick()"></span>

    <input class="gbs-Input"
           type="text"
           placeholder="Search.."
           debounce="300"
           transition="grow"
           v-model="query"
           v-show="show"
           v-el:input>

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
        show: false,
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
    },

    methods: {
      handleIconClick () {
        this.show = !this.show

        this.$nextTick(() => this.$els.input.focus())
      }
    }
  }
</script>
