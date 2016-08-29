var path = require('path')

module.exports = [
  require('postcss-import')({
    glob: true
  }),
  require('postcss-sassy-mixins'),
  require('postcss-conditionals'),
  require('postcss-nested'),
  require('postcss-functions')({
    glob: path.join(__dirname, '../../fifa', 'assets', 'css', 'functions', '*.js')
  }),

  require('postcss-custom-properties'),
  require('postcss-custom-media'),
  require('postcss-media-minmax'),
  require('postcss-custom-selectors'),
  // Niceties
  require('postcss-assets')({
    basePath: 'fifa/assets/',
    loadPaths: ['img/'],
    baseUrl: '/static/'
  }),
  require('postcss-inline-svg')({
    path: 'fifa/assets/img/'
  }),
  require('postcss-brand-colors'),
  require('postcss-property-lookup'),
  require('postcss-lh')({
    rhythmUnit: 'vr'
  }),
  require('postcss-pxtorem'),
  require('postcss-will-change'),
  require('postcss-font-awesome'),
  require('postcss-round-subpixels'),
  require('postcss-calc'),
  require('postcss-hexrgba'),
  require('autoprefixer')({
    browsers: ['ie 11', 'last 2 versions']
  }),
];
