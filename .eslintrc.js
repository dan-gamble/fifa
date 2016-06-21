module.exports = {
  root: true,
  extends: 'standard',
  ecmaFeatures: {
    modules: true,
  },
  env: {
    browser: true,
    es6: true
  },
  // required to lint *.vue files
  plugins: [
    'html'
  ],
  // add your custom rules here
  'rules': {
    'import/no-unresolved': 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0
  }
}
