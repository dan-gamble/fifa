import positionMap from './positionMap'

const defaultState = {
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

export default function builder (state = defaultState, action) {
  switch (action.type) {
    case 'UPDATE_PLAYER_PLAYER':
      const index = action.index
      const arr = Object.values(state.players)

      const newArr = [
        ...arr.slice(0, index),
        Object.assign({}, arr[index], {
          player: action.player
        }),
        ...arr.slice(index + 1)
      ]

      const obj = {}
      for (let i = 0; i < newArr.length; i++) {
        obj[i] = newArr[i]
      }

      return Object.assign({}, state, {
        players: obj
      })

    case 'UPDATE_POSITIONS':
      const positions = positionMap[action.formation]

      return Object.assign({}, state, updatePositions(state, positions))

    default:
      return state
  }
}

function updatePositions (state, positions) {
  return {
    players: {
      0: {
        ...state.players[0],
        position: positions[0]
      },
      1: {
        ...state.players[1],
        position: positions[1]
      },
      2: {
        ...state.players[2],
        position: positions[2]
      },
      3: {
        ...state.players[3],
        position: positions[3]
      },
      4: {
        ...state.players[4],
        position: positions[4]
      },
      5: {
        ...state.players[5],
        position: positions[5]
      },
      6: {
        ...state.players[6],
        position: positions[6]
      },
      7: {
        ...state.players[7],
        position: positions[7]
      },
      8: {
        ...state.players[8],
        position: positions[8]
      },
      9: {
        ...state.players[9],
        position: positions[9]
      },
      10: {
        ...state.players[10],
        position: positions[10]
      }
    }
  }
}
