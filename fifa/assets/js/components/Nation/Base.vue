<template>
  <div>
    <a v-link="{ name: 'nations:nation', params: { nationId: 1 }}">Nation</a>

    <div>
      View

      <div class="tree">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        nations: ['A', 'B']
      }
    }
  }
</script>
