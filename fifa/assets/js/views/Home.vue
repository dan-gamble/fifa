<template>
  <write :todos="todos"></write>
  <read :todos="todos"></read>
</template>

<script type="text/ecmascript-6">
  import Write from '../components/Write.vue'
  import Read from '../components/Read.vue'

  export default {
    data () {
      return {
        todos: this.$revue.getState().todos
      }
    },

    components: {
      Write,
      Read
    }
  }
</script>
