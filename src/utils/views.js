export function modelListVue (model, components) {
  return {
    components,

    data () {
      const data = {}
      data[`${model}s`] = []

      return data
    },

    created () {
      this.$http.get({ url: `/api/${model}s.json` }).then(res => {
        this[`${model}s`] = res.data.results
      })
    }
  }
}
