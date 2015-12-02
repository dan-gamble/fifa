<template>
  <div class="tree">
    tree
    {{ msg }}
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        msg: 'Vue'
      }
    }
  }
</script>

<style scoped>
  .tree {
    background-color: red;
  }
</style>
