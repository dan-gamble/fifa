<template>
  <div class="nations-list">
    <item v-for="nation in nations" :nation="nation"></item>
  </div>
</template>

<script type="text/babel">
  import Item from './ListItem.vue'
  import { modelListVue } from '../../utils/views'

  export default modelListVue('nation', { Item })
</script>
