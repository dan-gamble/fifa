export function configRouter (router) {
  router.map({
    '/': {
      component: require('./views/Home.vue')
    }
//    '/nations/:page': {
//      name: 'nations:nations',
//      component: require('./components/Nation/Nations.vue'),
//      subRoutes: {
//        '/item/:nation': {
//          name: 'nations:nation',
//          component: require('./components/Nation/Nation.vue'),
//        }
//      }
//    },
//      subRoutes: {
//        '/': {
//          component: require('./components/Nation/Nations.vue')
//        },
//        '/tree': {
//          name: 'nations:nation',
//          component: {
//            component: {
//              template: '<div>Tree</div>'
//            }
//          }
//        }
//      }
//    }
  })
}
