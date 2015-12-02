<template>
  <li>
    <div><a v-link="{ name: 'nations:nation', params: { nation: item.slug }}">{{ item.name }} - {{ item.name_abbr }}</a></div>
    <img :src="item.image_sm">
    <img :src="item.image_md">
    <img :src="item.image_lg">
  </li>
</template>

<script type="text/ecmascript-6">
  export default {
    props: ['item']
  }
</script>
