<template>
  <div class="read">
    <h2>Read only todos</h2>

    <button @click="handleSubscribe">Subscribe</button>
    <button @click="handleUnsubscribe">Unsubscribe</button>

    <ul class="todos" v-if="todos && todos.length > 0">
      <li class="todo" :class="{del: todo.done}" v-for="todo in todos" track-by="$index" v-text="todo.text"></li>
    </ul>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: ['todos'],

    ready () {
      this.handleSubscribe()
    },

    methods: {
      handleUnsubscribe () {
        this.$unsubscribe()
      },
      handleSubscribe () {
        this.$subscribe('todos')
      }
    }
  }
</script>
