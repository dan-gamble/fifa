<template>
  <div>
    <ul>
      <item v-for="(k, v) in nations" :item="v"></item>
    </ul>

    <div class="pagination">
      <button @click="getNextNations()" v-show="nextPage">Next</button>
      <button @click="getPrevNations()" v-show="prevPage">Prev</button>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import Item from './NationsItem.vue'

  export default {
    data () {
      return {
        prevPage: '',
        nextPage: '',
        nations: []
      }
    },

    components: {
      Item
    },

    ready () {
      this.$http.get('/api/nations/', function (data, status, request) {
        this.nextPage = data.next
        this.prevPage = data.previous
        this.nations = data.results
      })
    },

    methods: {
      getNextNations () {
        this.$http.get(this.nextPage, function (data, status, request) {
          this.nextPage = data.next
          this.prevPage = data.previous
          this.nations = data.results
        })
      },
      getPrevNations () {
        this.$http.get(this.prevPage, function (data, status, request) {
          this.nextPage = data.next
          this.prevPage = data.prev
          this.nations = data.results
        })
      }
    }
  }
</script>
