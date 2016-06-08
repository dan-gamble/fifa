export default {
  init (el) {
    this.el = el

    el.addEventListener('click', (e) => {
      e.preventDefault()

      if (el.getAttribute('aria-selected') === 'false') {
        el.setAttribute('aria-selected', 'true')
      } else {
        el.setAttribute('aria-selected', 'false')
      }
    })
  }
}
