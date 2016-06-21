<template>
  <div class="league">
    <a v-link="{ name: 'league', params: { slug: league.slug }}">{{ league.name }}</a>
  </div>
</template>

<script type="text/babel">
  export default {
    props: ['league']
  }
</script>
