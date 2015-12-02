<template>
  <div>
    <header>
      {{ header }}
    </header>

    <p>
      <a v-link="{ name: 'nations:nations' }">Nations</a>
      <a v-link="{ path: '/bar' }">Go to Bar</a>
    </p>

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
