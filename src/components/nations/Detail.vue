<template>
  <div class="nation">
    {{ nation.name }}
    {{ nation.cached_url }}

    total_players: {{ nation.total_players }}<br>
    total_bronze: {{ nation.total_bronze }}<br>
    total_silver: {{ nation.total_silver }}<br>
    total_gold: {{ nation.total_gold }}<br>
    total_informs: {{ nation.total_informs }}<br>
    total_special: {{ nation.total_special }}<br>

    <div class="players">
      <div class="player" v-for="player in players.results">
        {{ player.common_name }} ({{ player.overall_rating }})
      </div>

      <div class="pagination">
        <button type="button" @click="prevPage()" :disabled="players.links.previous">Prev</button>
        <button type="button">{{ players.pages.current }}</button>
        <button type="button" @click="paginate('next')" :disabled="loading">Next</button>
      </div>
    </div>
  </div>
</template>

<script type="text/babel">
  import { router } from '../../main'

  export default {
    data () {
      return {
        nation: {},
        players: [],
        loading: false
      }
    },

    created () {
      this.$http.get({ url: `/api/nations/${this.$route.params.slug}.json` }).then(res => {
        this.nation = res.data
      })

      const pageParam = this.$route.query.page ? `&page=${this.$route.query.page}` : ''
      const url = `/api/players/?nation=${this.$route.params.slug}${pageParam}`

      console.log(url)

      this.$http.get({ url }).then(res => {
        this.players = res.data
      })
    },

    computed: {
      nextPage () {
        return this.players.links.next.replace('8000', '8080')
      }
    },

    methods: {
      prevPage () {
        router.go({path: this.players.links.previous.replace('8000', '8080')})
      },
      paginate (direction) {
        if (this.loading) return

        const url = this.players.links[direction].replace('8000', '8080')

        this.loading = true
        this.$http.get({ url }).then(res => {
          this.players = res.data

          this.loading = false
        })
      }
    }
  }
</script>

<style type="text/css" rel="stylesheet/scss">
  button[disabled] {
    background-color: red;
  }
</style>
