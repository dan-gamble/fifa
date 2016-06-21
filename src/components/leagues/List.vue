<template>
  <div class="leagues-list">
    <item v-for="league in leagues" :league="league"></item>
  </div>
</template>

<script type="text/babel">
  import Item from './ListItem.vue'
  import { modelListVue } from '../../utils/views'

  export default modelListVue('league', { Item })
</script>
