<template>
  <div class="tree">
    <h1>Hello</h1>

    <div>
      <a v-link="{ path: '/' }">Home</a>
      <a v-link="{ name: 'leagues' }">Leagues</a>
      <a v-link="{ name: 'nations' }">Nations</a>
    </div>

    <router-view></router-view>
  </div>
</template>

<script>
  export default {}
</script>

<style type="text/css" rel="stylesheet/scss">
</style>
