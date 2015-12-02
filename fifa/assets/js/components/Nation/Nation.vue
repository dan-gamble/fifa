<template>
  <div>
    {{ nation.name }} - {{ nation.name_abbr }}
    <img :src="nation.image_sm">
    <img :src="nation.image_md">
    <img :src="nation.image_lg">
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        nation: {}
      }
    },

    ready () {
      const nation = this.$route.params.nation

      this.$http.get(`/api/nations/${nation}/`, function (data, status, request) {
        this.nation = data
      })
    }
  }
</script>
