import { leagues } from './components/leagues/components'
import { nations } from './components/nations/components'

export function configRouter (router) {
  router.map({
    '/nations': {
      component: nations.Index,
      subRoutes: {
        '/': {
          name: 'nations',
          component: nations.List
        },
        '/:slug': {
          name: 'nation',
          component: nations.Detail
        }
      }
    },

    '/leagues': {
      component: leagues.Index,
      subRoutes: {
        '/': {
          name: 'leagues',
          component: leagues.List
        },
        '/:slug': {
          name: 'league',
          component: leagues.Detail
        }
      }
    }
  })
}

