<template>
    <div class='search-wrapper' v-if='showSearch'>
      <div id='headlessui-dialog-panel' class='search-dialog relative mx-auto max-w-xl transform divide-y divide-gray-100 dark:divide-gray-800 overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black ring-opacity-5 transition-all'>
          <div class="label-container top-label">
            <VDropdown :theme="'info-dropdown-hover'">
              <i :class="team1icon"></i>
              <template #popper>
                {{ team1 }}
              </template>
            </VDropdown>
            <VDropdown :theme="'info-dropdown-hover'">
              <i :class="team2icon"></i>
              <template #popper>
                {{ team2 }}
              </template>
            </VDropdown>
          </div>
          <div class='relative' v-on-clickaway='hideSearch'>
              <input
              ref='searchInput'
              v-model='searchTerm'
              @input='onInput'
              aria-expanded='false'
              aria-autocomplete='list'
              id='headlessui-combobox-input'
              role='combobox'
              type='text'
              tabindex='0'
              class='h-12 w-full border-0 bg-transparent dark:bg-gray-700 pl-11 pr-9 text-gray-900 dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-200 focus:ring-0 sm:text-sm'
              placeholder='Search...'>
          </div>
          <div v-show='showDropdown' v-on-clickaway='closeDropdown' class='dropdown absolute z-20 mt-1 w-full bg-white rounded-md shadow-lg'>
              <div v-for='item in searchResults' :key='item' class='px-4 py-2 hover:bg-gray-200 cursor-pointer' @click='playerClicked(item)'>
                  {{ item }}
              </div>
          </div>
      </div>
    </div>
</template>

<script>
import { mixin as clickaway } from 'vue-clickaway'
import { debounce } from 'lodash'
import { EventBus } from '~/event-bus.js'

export default {
  name: 'game-grid',
  mixins: [clickaway],
  data () {
    return {
      teams: '',
      team1: '',
      team2: '',
      team1icon: '',
      team2icon: '',
      searchTerm: '',
      showDropdown: false,
      searchResults: [],
      showSearch: false,
      loading: false,
      cancelTokenSource: null
    }
  },
  created () {
    EventBus.$on('show-search', () => {
      this.teams = this.$store.state.grid
      switch (this.$store.state.selectedGridLocation) {
        case 's00':
          this.team1icon = this.teams[0][0][0]
          this.team1 = this.teams[0][0][1]
          this.team2icon = this.teams[1][0][0]
          this.team2 = this.teams[1][0][1]
          break
        case 's01':
          this.team1 = this.teams[0][1][1]
          this.team2 = this.teams[1][0][1]
          this.team1icon = this.teams[0][1][0]
          this.team2icon = this.teams[1][0][0]
          break
        case 's02':
          this.team1 = this.teams[0][2][1]
          this.team2 = this.teams[1][0][1]
          this.team1icon = this.teams[0][2][0]
          this.team2icon = this.teams[1][0][0]
          break
        case 's10':
          this.team1 = this.teams[0][0][1]
          this.team2 = this.teams[1][1][1]
          this.team1icon = this.teams[0][0][0]
          this.team2icon = this.teams[1][1][0]
          break
        case 's11':
          this.team1 = this.teams[0][1][1]
          this.team2 = this.teams[1][1][1]
          this.team1icon = this.teams[0][1][0]
          this.team2icon = this.teams[1][1][0]
          break
        case 's12':
          this.team1 = this.teams[0][2][1]
          this.team2 = this.teams[1][1][1]
          this.team1icon = this.teams[0][2][0]
          this.team2icon = this.teams[1][1][0]
          break
        case 's20':
          this.team1 = this.teams[0][0][1]
          this.team2 = this.teams[1][2][1]
          this.team1icon = this.teams[0][0][0]
          this.team2icon = this.teams[1][2][0]
          break
        case 's21':
          this.team1 = this.teams[0][1][1]
          this.team2 = this.teams[1][2][1]
          this.team1icon = this.teams[0][1][0]
          this.team2icon = this.teams[1][2][0]
          break
        case 's22':
          this.team1 = this.teams[0][2][1]
          this.team2 = this.teams[1][2][1]
          this.team1icon = this.teams[0][2][0]
          this.team2icon = this.teams[1][2][0]
          break
      }
      this.showSearch = true
      this.$nextTick(() => {
        this.$refs.searchInput.focus()
      })
    })
    this.debouncedSearch = debounce(this.search, 30)
  },
  methods: {
    onInput () {
      this.debouncedSearch()
    },
    async search () {
      if (this.cancelTokenSource) {
        this.cancelTokenSource.cancel('Cancelling previous request')
      }
      this.cancelTokenSource = this.$axios.CancelToken.source()
      this.loading = true
      this.searchResults = ['Loading...']
      this.showDropdown = true
      try {
        const data = await this.$axios.get('/search_players?name=' + this.searchTerm, {
          cancelToken: this.cancelTokenSource.token
        })
        this.searchResults = data.data
      } catch (error) {
        if (this.$axios.isCancel(error)) {
          console.log('Request cancelled', error.message)
        } else {
          console.error(error)
        }
      } finally {
        this.loading = false
      }
    },
    closeDropdown () {
      this.showDropdown = false
    },
    hideSearch () {
      this.showSearch = false
      this.searchTerm = ''
      this.$store.commit('clearAllOnExit')
    },
    playerClicked (player) {
      this.$store.commit('setSelectedPlayerEasy', player)
      EventBus.$emit('player-selected')
    }
  }
}
</script>

<style scoped>
@media screen and (max-width: 768px) {
  .search-dialog {
    width: 70% !important;
  }

  .search-dialog input {
    font-size: 14px !important;
    width: 95% !important;
  }
}

@media screen and (min-width: 768px) {
  .search-dialog {
    width: 60% !important;
  }

  .search-dialog input {
    font-size: 14px !important;
    width: 95% !important;
  }
}

@media screen and (min-width: 1200px) {
  .search-dialog {
    width: 40% !important;
  }

  .search-dialog input {
    font-size: 14px !important;
    width: 95% !important;
  }
}

.label-container {
    display: inline-flex;
    justify-content:center;
    align-items: center;
    flex-direction: row;
    gap: 5%;
}

.top-label {
        width: 100%;
        height: 100%;
        padding-bottom: 2%;
}

.team-text {
        padding-top: 0%;
        padding-left: 0%;
        font-size: 100%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
}

.search-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
}

.search-dialog {
  width: 60%;
  padding: 20px;
  background: #383842;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
  border-radius: 10px;
}

.search-icon {
  height: 20px;
  width: 20px;
  fill: #888;
}

.search-dialog input {
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  width: 98%;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.1);
}

.search-dialog .dropdown {
  margin-top: 10px;
  border-radius: 6px;
  box-shadow: 0px 3px 15px rgba(0,0,0,0.1);
  overflow: hidden; /* To follow the border-radius for children */
}

.search-dialog .dropdown div {
  padding: 10px;
  cursor: pointer;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  color: white;
}

.search-dialog .dropdown div:hover {
  background-color: #f6f6f6; /* Light hover effect */
  color: black;
}
</style>

<style>
.v-popper--theme-info-dropdown-hover .v-popper__inner {
  background: rgba(56, 56, 56, 0.7);
  color: #ffffff;
  padding: 10px;
  border: none;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.7);
  font-size: 14px;
  font-size: 100%; /* Adjust to your preference */
  color: white;
  text-align: center;
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  max-width: 250px;
}

.v-popper--theme-info-dropdown-hover .v-popper__arrow-outer {
  border-color: rgba(56, 56, 56, 0.7);
}

.v-popper--theme-info-dropdown-hover .v-popper__arrow-inner {
  visibility: hidden;
}
</style>
