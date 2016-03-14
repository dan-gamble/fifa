import positionChem from './utils/positionChem'
import positionLinks from './utils/positionLinks'
import positionMap from './utils/positionMap'

const state = {
  // Squad
  name: '',
  selectedFormation: '352',

  // Averages
  chem: 0,
  ovr: 0,
  pac: 0,
  sho: 0,
  pas: 0,
  dri: 0,
  def: 0,
  phy: 0,

  // Prices
  xbox: 0,
  playstation: 0,
  pc: 0,

  players: {
    0: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    1: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    2: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    3: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    4: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    5: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    6: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    7: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    8: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    9: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    },
    10: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: '',
      links: [],
      totalLinks: 0
    }
  }
}

const mutations = {
  'UPDATE_SELECTED_FORMATION' (state, val) {
    state.selectedFormation = val
  },

  'UPDATE_PLAYER' (state, data) {
    state.players[data.index].player = data.player
  },

  'UPDATE_PLAYER_CHEMISTRY' (state, data) {
    if (data.type === 'position') {
      const positionChemMap = `${state.players[data.index].position}:${data.player.position}`

      state.players[data.index].chemistry[data.type] = positionChem[positionChemMap]
    } else if (data.type === 'links') {
      let total = 0
      let totalLinks = 0

      for (const link of state.players[data.index].links) {
        if (state.players[link].player.hasOwnProperty('league') &&
            state.players[data.index].player.hasOwnProperty('league')) {
          totalLinks += 1
        }

        if (state.players[link].player.league &&
            state.players[data.index].player.league &&
            state.players[link].player.league.ea_id === state.players[data.index].player.league.ea_id) {
          total += ((1 / 3)) * 3
        }
      }

      console.log(total, totalLinks)
    }
  },

  'UPDATE_PLAYER_LINKS' (state, data) {
    const links = positionLinks[data.formation]

    for (const player in state.players) {
      state.players[player].links = links[player]
      state.players[player].totalLinks = links[player].length
    }
  },

  'UPDATE_PLAYER_POSITIONS' (state, data) {
    const positions = positionMap[data.formation]

    for (const player in state.players) {
      state.players[player].position = positions[player]
    }
  }
}

export default {
  state,
  mutations
}
