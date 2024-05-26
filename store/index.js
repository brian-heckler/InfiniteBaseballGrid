import Vue from 'vue'
import Vuex from 'vuex'
import FloatingVue from 'floating-vue'
import 'floating-vue/dist/style.css'

Vue.use(Vuex)
Vue.use(FloatingVue, {
  themes: {
    'info-dropdown': {
      $extend: 'dropdown',
      triggers: ['click', 'touch'],
      placement: 'top',
      delay: {
        show: 0,
        hide: 100
      }
      // Other options (see the 'Global options' section)
    },
    'info-dropdown-left': {
      $extend: 'dropdown',
      triggers: ['click', 'touch'],
      placement: 'left',
      delay: {
        show: 0,
        hide: 100
      }
      // Other options (see the 'Global options' section)
    },
    'info-dropdown-hover': {
      $extend: 'dropdown',
      triggers: ['hover', 'touch'],
      placement: 'top',
      delay: {
        show: 0,
        hide: 300
      }
      // Other options (see the 'Global options' section)
    }
  }
})

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
