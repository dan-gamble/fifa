<style scoped>
  .counter {
    height: 200px;
    margin: 0 auto;
    max-width: 200px;

    line-height: 200px;
    text-align: center;

    border-radius: 4px;
    box-shadow: 0 0 10px #e2e2e2;
    cursor: pointer;

    transition: transform .3s, box-shadow .3s;
  }
  .counter:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.2);
  }
</style>

<template>
  <div class="counter" @click="handleClick">
    {{ count }}
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        count: this.$revue.getState().counter
      }
    },

    ready () {
      this.$subscribe('counter as count')
    },

    methods: {
      handleClick () {
        this.$revue.dispatch({type: 'INCREMENT'})
      }
    }
  }
</script>
