export function updatePlayerPositions ({ dispatch }, data) {
  dispatch('UPDATE_PLAYER_POSITIONS', data)
}

export function updateSelectedFormation ({ dispatch }, event) {
  dispatch('UPDATE_SELECTED_FORMATION', event.target.value)
}

export function updatePlayer ({ dispatch }, data) {
  dispatch('UPDATE_PLAYER', data)
}

export function updatePlayerChemistry ({ dispatch }, data) {
  dispatch('UPDATE_PLAYER_CHEMISTRY', data)
}
