<template>
  <div class="container">
    <nav class="navbar navbar-light bg-faded">
      <a href="/" class="navbar-brand">Futmoz</a>

      <ul class="nav navbar-nav">
        <!--<li class="nav-item">
          <a class="nav-link" v-link="{ name: 'nations:nations' }">Nations</a>
        </li>

        <li class="nav-item">
          <a v-link="{ name: 'leagues:leagues' }">Leagues</a>
        </li>

        <li class="nav-item">
          <a v-link="{ name: 'clubs:clubs' }">Clubs</a>
        </li>

        <li class="nav-item">
          <a v-link="{ name: 'players:players' }">Players</a>
        </li> -->

        <form class="form-inline navbar-form pull-right">
          <input class="form-control" type="text" placeholder="search">
          <button class="btn btn-success-outline" type="submit">Search</button>
        </form>
      </ul>
    </nav>

    <router-view></router-view>

    <footer>
      {{ footer }}
    </footer>
  </div>
</template>

<script type="text/ecmascript-6">


  export default {
    data () {
      return {
        header: 'Header',
        footer: 'Footer'
      }
    },

    components: {
      // 'scf-header': Header
    }
  }
</script>
