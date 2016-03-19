var browserSync = require('browser-sync')
var config      = require('../config')
var gulp        = require('gulp')

var browserSyncTask = function() {
  browserSync.init(config.tasks.browserSync)

  gulp.watch(['fifa/apps/*/jinja2/**/*.html', 'fifa/jinja2/**/*.html'], browserSync.reload)
}
gulp.task('browserSync', browserSyncTask)
module.exports = browserSyncTask
