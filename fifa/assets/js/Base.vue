<template>
  <div>
    <h1>{{ header }}</h1>

    <p>
      <a v-link="{ path: '/foo' }">Go to Foo</a>
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
    }
  }
</script>
