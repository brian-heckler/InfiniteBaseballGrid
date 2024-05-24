import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const createStore = () => {
  return new Vuex.Store({
    state: {
      selectedGridLocation: null,
      selectedGridLocationHard: null,
      selectedPlayerEasy: null,
      selectedPlayerHard: null,
      grid: null,
      gridhard: null
    },
    mutations: {
      setSelectedGridLocation (state, item) {
        state.selectedGridLocation = item
      },
      setSelectedGridLocationHard (state, item) {
        state.selectedGridLocationHard = item
      },
      setSelectedPlayerEasy (state, item) {
        state.selectedPlayerEasy = item
      },
      setSelectedPlayerHard (state, item) {
        state.selectedPlayerHard = item
      },
      clearAllOnExit (state) {
        state.selectedGridLocation = null
        state.selectedGridLocationHard = null
        state.selectedPlayerEasy = null
        state.selectedPlayerHard = null
      },
      setGrid (state, item) {
        state.grid = item
      },
      setGridHard (state, item) {
        state.gridhard = item
      }
    }
  })
}

export default createStore
