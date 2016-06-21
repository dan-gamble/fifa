<template>
  <div class="nation">
    <a v-link="{ name: 'nation', params: { slug: nation.slug }}">{{ nation.name }}</a>
  </div>
</template>

<script type="text/babel">
  export default {
    props: ['nation']
  }
</script>
