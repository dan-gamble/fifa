<template>
  <div class="bld-Outer">
    <select v-model="formation">
      <option v-for="(k, v) in formations | orderBy -1" :value="v">
        {{ k }}
      </option>
    </select>

    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
    <player></player>
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
        formation: '3412'
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
