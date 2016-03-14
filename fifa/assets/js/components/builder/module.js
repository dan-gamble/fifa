import positionChem from './utils/positionChem'
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
      position: ''
    },
    1: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    2: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    3: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    4: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    5: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    6: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    7: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    8: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    9: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    },
    10: {
      chemistry: {
        links: 0,
        position: 0,
        boost: 0
      },
      player: {},
      position: ''
    }
  }
}

const mutations = {
  'UPDATE_PLAYER_POSITIONS' (state, data) {
    const positions = positionMap[data.formation]

    for (const player in state.players) {
      state.players[player].position = positions[player]
    }
  },

  'UPDATE_SELECTED_FORMATION' (state, val) {
    state.selectedFormation = val
  },

  'UPDATE_PLAYER' (state, data) {
    state.players[data.index].player = data.player
  },

  'UPDATE_PLAYER_CHEMISTRY' (state, data) {
    const positionChemMap = `${state.players[data.index].position}:${data.player.position}`

    state.players[data.index].chemistry[data.type] = positionChem[positionChemMap]
  }
}

export default {
  state,
  mutations
}
