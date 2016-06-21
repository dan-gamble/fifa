<template>
  <div class="league">
    {{ league.name }}
  </div>
</template>

<script type="text/babel">
  export default {
    data () {
      return {
        league: {}
      }
    },

    created () {
      this.$http.get({ url: `/api/leagues/${this.$route.params.slug}.json` }).then(res => {
        this.league = res.data
      })
    }
  }
</script>
