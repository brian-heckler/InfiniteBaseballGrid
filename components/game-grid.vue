<template>
  <div v-if="hardMode == false">
    <div :class="$style.grid">
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
          <VDropdown :theme="'info-dropdown'" v-if="teams[0][0][2]">
            <i :class="teams[0][0][0]"></i>
            <template #popper>
              {{ teams[0][0][2] }}
            </template>
          </VDropdown>
          <i v-else :class="teams[0][0][0]"></i>
          <div :class="$style['team-text']">{{ teams[0][0][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
          <VDropdown :theme="'info-dropdown'" v-if="teams[0][1][2]">
            <i :class="teams[0][1][0]"></i>
            <template #popper>
              {{ teams[0][1][2] }}
            </template>
          </VDropdown>
          <i v-else :class="teams[0][1][0]"></i>
          <div :class="$style['team-text']">{{ teams[0][1][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 0 && teams[0].length > 0" :class="[$style['label-container'], $style['top-label']]">
          <VDropdown :theme="'info-dropdown'" v-if="teams[0][2][2]">
            <i :class="teams[0][2][0]"></i>
            <template #popper>
              {{ teams[0][2][2] }}
            </template>
          </VDropdown>
          <i v-else :class="teams[0][2][0]"></i>
          <div :class="$style['team-text']">{{ teams[0][2][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div></div> <!-- Empty grid cell -->
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <VDropdown :theme="'info-dropdown-left'" v-if="teams[1][0][2]">
              <i :class="teams[1][0][0]"></i>
              <template #popper>
                {{ teams[1][0][2] }}
              </template>
            </VDropdown>
            <i v-else :class="teams[1][0][0]"></i>
            <div :class="$style['team-text']">{{ teams[1][0][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div v-if="gridStatus['s00'] != false" :class="[$style.imageContainer, $style['top-left']]">
          <div :class="$style.rarityScore">{{ gridStatus['s00'].rarity_score }}%</div>
          <img :src="gridStatus['s00'].picture" :class="$style['player-image']" :alt="gridStatus['s00'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s00'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s00')" :class="[$style['grid-item'], $style['top-left']]" :disabled="gameOver"></button>
        <div v-if="gridStatus['s01'] != false" :class="$style.imageContainer">
            <div :class="$style.rarityScore">{{ gridStatus['s01'].rarity_score }}%</div>
            <img :src="gridStatus['s01'].picture" :class="$style['player-image']" :alt="gridStatus['s01'].name + ' photo'">
            <div :class="$style.playerName">{{ gridStatus['s01'].name }}</div>
        </div>
        <button v-else @click="buttonClicked('s01')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s02'] != false" :class="[$style.imageContainer, $style['top-right']]">
          <div :class="$style.rarityScore">{{ gridStatus['s02'].rarity_score }}%</div>
          <img :src="gridStatus['s02'].picture" :class="$style['player-image']" :alt="gridStatus['s02'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s02'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s02')" :class="[$style['grid-item'], $style['top-right']]" :disabled="gameOver"></button>
        <div :class="$style['share-button-container']" @click="shareGrid" >
          <img src="~/static/share.png" alt="Share Logo" :class="$style['share-button']" />
        </div>
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <VDropdown :theme="'info-dropdown-left'" v-if="teams[1][1][2]">
              <i :class="teams[1][1][0]"></i>
              <template #popper>
                {{ teams[1][1][2] }}
              </template>
            </VDropdown>
            <i v-else :class="teams[1][1][0]"></i>
            <div :class="$style['team-text']">{{ teams[1][1][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div v-if="gridStatus['s10'] != false" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ gridStatus['s10'].rarity_score }}%</div>
          <img :src="gridStatus['s10'].picture" :class="$style['player-image']" :alt="gridStatus['s10'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s10'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s10')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s11'] != false" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ gridStatus['s11'].rarity_score }}%</div>
          <img :src="gridStatus['s11'].picture" :class="$style['player-image']" :alt="gridStatus['s11'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s11'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s11')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s12'] != false" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ gridStatus['s12'].rarity_score }}%</div>
          <img :src="gridStatus['s12'].picture" :class="$style['player-image']" :alt="gridStatus['s12'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s12'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s12')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="unlimitedMode == false">
            <div :class="$style['small-text']">GUESSES</div>
            <div :class="$style['large-text']">{{ guesses }}</div>
        </div>
        <div v-else>
          <div :class="$style['small-text']">GUESSES</div>
          <div :class="$style['large-text']">&infin;</div>
        </div>
        <div v-if="teams.length > 1 && teams[1].length > 0" :class="$style['label-container']">
            <VDropdown :theme="'info-dropdown-left'" v-if="teams[1][2][2]">
              <i :class="teams[1][2][0]"></i>
              <template #popper>
                {{ teams[1][2][2] }}
              </template>
            </VDropdown>
            <i v-else :class="teams[1][2][0]"></i>
            <div :class="$style['team-text']">{{ teams[1][2][1] }}</div>
        </div>
        <div v-else></div> <!-- Empty grid cell -->
        <div v-if="gridStatus['s20'] != false" :class="[$style.imageContainer, $style['bottom-left']]">
          <div :class="$style.rarityScore">{{ gridStatus['s20'].rarity_score }}%</div>
          <img :src="gridStatus['s20'].picture" :class="$style['player-image']" :alt="gridStatus['s20'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s20'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s20')" :class="[$style['grid-item'], $style['bottom-left']]" :disabled="gameOver"></button>
        <div v-if="gridStatus['s21'] != false" :class="$style.imageContainer">
          <div :class="$style.rarityScore">{{ gridStatus['s21'].rarity_score }}%</div>
          <img :src="gridStatus['s21'].picture" :class="$style['player-image']" :alt="gridStatus['s21'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s21'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s21')" :class="$style['grid-item']" :disabled="gameOver"></button>
        <div v-if="gridStatus['s22'] != false" :class="[$style.imageContainer, $style['bottom-right']]">
          <div :class="$style.rarityScore">{{ gridStatus['s22'].rarity_score }}%</div>
          <img :src="gridStatus['s22'].picture" :class="$style['player-image']" :alt="gridStatus['s22'].name + ' photo'">
          <div :class="$style.playerName">{{ gridStatus['s22'].name }}</div>
      </div>
        <button v-else @click="buttonClicked('s22')" :class="[$style['grid-item'], $style['bottom-right']]" :disabled="gameOver"></button>

        <div v-if="gameOver">
          <button :class="$style.newgame" @click="newGame()">New Grid</button>
          <button :class="$style.stats" @click="goToStats()">Stats</button>
        </div>
        <button v-else :class="$style.giveUp" @click="giveUp()">Give Up</button>
    </div>
    <div :class="$style.unlimitedMode">
      <button v-if="hardMode == false" @click="hardModegame()" :class="$style.hardModeButton">Hard Mode</button>
      <button v-if="unlimitedMode == false" @click="unlimitedMode = true" :class="$style.unlimitedModeButton">Unlimited Mode</button>
    </div>
  </div>
</template>

<style module>
    @media screen and (max-width: 768px) {
        .grid {
            width: 100% !important;
            margin-top: 20% !important;
        }

        .large-text {
            font-size: 40px !important;
        }

        .small-text {
            font-size: 20px !important;
        }

        .playerName {
            font-size: 14px !important;
        }

        .newgame {
            font-size: 20px !important;
        }

        .stats {
            font-size: 20px !important;
        }

        .giveUp {
            font-size: 20px !important;
            height: 100% !important;
        }

        .rarityScore {
            font-size: 14px !important;
        }

        .unlimitedMode {
            width: 50% !important;
        }
    }
    @media screen and (min-width: 768px) {
        .grid {
            width: 768px !important; /* Change to whatever constant size you prefer */
            margin: auto !important; /* Center the grid */
        }
        .large-text {
            font-size: 60px !important;
        }

        .small-text {
            font-size: 20px !important;
        }

        .playerName {
            font-size: 14px !important;
        }

        .newgame {
            font-size: 20px !important;
        }

        .stats {
            font-size: 20px !important;
        }

        .giveUp {
            font-size: 20px !important;
            height: 100% !important;
        }

        .rarityScore {
            font-size: 14px !important;
        }

        .unlimitedMode {
            width: 25% !important;
        }
    }

    @media screen and (min-width: 1768px) {
        .grid {
            width: 768px !important; /* Change to whatever constant size you prefer */
            margin: auto !important; /* Center the grid */
        }
        .large-text {
            font-size: 60px !important;
        }

        .small-text {
            font-size: 20px !important;
        }

        .playerName {
            font-size: 14px !important;
        }

        .newgame {
            font-size: 20px !important;
        }

        .stats {
            font-size: 20px !important;
        }

        .giveUp {
            font-size: 20px !important;
            height: 100% !important;
        }

        .rarityScore {
            font-size: 14px !important;
        }

        .unlimitedMode {
            width: 15% !important;
        }
    }

    .giveUp {
      grid-column: 5 5;
      width: 90%;
      height: 50%;
      border-radius: 15px;
      background-color: #f44336; /* You can adjust this color */
      color: white;
      font-family: 'Roboto', sans-serif;
      font-weight: 700;
      font-size: 20px;
      border: none;
      cursor: pointer;
      margin-left: 10px;
  }

    .giveUp:hover {
        background-color: #ff1a1a; /* Adjust as needed */
    }

    .unlimitedMode {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-left: auto;
      margin-right: auto;
      margin-top: 2%;
      width: 10%;
      height: 100%;
  }

    .unlimitedModeButton {
      width: 100%;
      height: 100%;
      border-radius: 15px;
      background-color: #00e600; /* You can adjust this color */
      color: white;
      font-family: 'Roboto', sans-serif;
      font-weight: 700;
      font-size: 20px;
      border: none;
      cursor: pointer;
      padding: 5%;
      max-width: 120px;
  }

  .unlimitedModeButton:hover {
        background-color: #009800; /* Adjust as needed */
  }

  .hardModeButton {
      width: 100%;
      height: 100%;
      border-radius: 15px;
      background-color: #790146; /* You can adjust this color */
      color: white;
      font-family: 'Roboto', sans-serif;
      font-weight: 700;
      font-size: 20px;
      border: none;
      cursor: pointer;
      margin-right: 10px;
      padding: 5%;
      max-width: 100px;
  }

  .hardModeButton:hover {
        background-color: #600137; /* Adjust as needed */
  }

    .share-button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 110%;
        height: 100%;
    }

    .share-button {
        width: 40%;
        height: 40%;
        object-fit: cover;
        cursor: pointer;
    }

    .grid {
        display: grid;
        width: 50%;
        grid-template-columns: repeat(5, 1fr);
        gap: 2px;
        margin: auto;
        overflow: hidden;
    }

    .newgame {
        grid-column: 5 5;
        width: 100%;
        height: 50%;
        border-radius: 15px;
        background-color: #00e600;
        color: white;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        font-size: 90%;
        border: none;
        cursor: pointer;
    }

    .stats {
      grid-column: 5 5;
      width: 100%;
      height: 50%;
      border-radius: 15px;
      background-color: green;
      color: white;
      font-family: 'Roboto', sans-serif;
      font-weight: 700;
      font-size: 90%;
      border: none;
      cursor: pointer;
  }

    .newgame:hover {
        background-color: green;
    }

    .stats:hover {
      background-color: #00cc00;
  }

    .label {
        grid-column: span 1;
        width: 50%;
        height: 50%;
        /* Add any additional styles for the labels here */
    }

    .imageContainer {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      background-color: #383842;
    }

    .label-container {
        display: flex;
        justify-content:center;
        align-items: center;
        flex-direction: column;
    }

    .playerName {
      position: relative; /* Absolute positioning */
      bottom: 0; /* Position it at the bottom */
      color: #fff; /* Choose color according to your preference */
      background: rgba(0,0,0,0.6); /* Add a dark background for the text to be visible */
      text-align: center; /* To center the text */
      font-family: 'Roboto', sans-serif;
      font-size: 12px;
      border-radius: 10px;
      width: auto;
      padding: 0px 5px;
      overflow: hidden;
      text-overflow: ellipsis;
      display: inline-block;
      max-width: 100px;
      max-height: 30px;
  }

    .top-label {
        width: 100%;
        height: 90%;
        padding-bottom: 50%;
    }

    .player-image {
        grid-column: span 1;
        width: 70%;
        object-fit: cover;
        /* Add any additional styles for the player images here */
    }

    .grid-item {
        aspect-ratio: 5 / 7;
        padding: 10%;
        border: none;
        background-color: #383842;
        /* Other styles... */
    }

    .top-left {
      border-top-left-radius: 20px;
    }

    .top-right {
      border-top-right-radius: 20px;
    }

    .bottom-left {
      border-bottom-left-radius: 20px;
    }

    .bottom-right {
      border-bottom-right-radius: 20px;
    }

    .grid-item:hover {
        background-color: #565666; /* adjust as needed */
    }

    .large-text {
        font-size: 350%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }

    .team-text {
        padding-top: 5%;
        font-size: 100%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }

    .small-text {
        padding-top: 25%;
        font-size: 70%; /* Adjust to your preference */
        color: white;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
    }

.rarityScore {
  color: white; /* Choose color according to your preference */
  background: rgba(0,0,0,0.6); /* Add a dark background for the text to be visible */
  width: 25%;
  text-align: center; /* To center the text */
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  align-self: last baseline;
  border-radius: 10px;
  padding: 2px 3px;
}
</style>

<style>
  .fade-leave-active {
    transition: all 2s;
  }
  .fade-enter-from, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
  }
  .v-popper--theme-info-dropdown .v-popper__inner {
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

  .v-popper--theme-info-dropdown .v-popper__arrow-outer {
    border-color: rgba(56, 56, 56, 0.7);
  }

  .v-popper--theme-info-dropdown .v-popper__arrow-inner {
    visibility: hidden;
  }
  .v-popper--theme-info-dropdown-left .v-popper__inner {
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

  .v-popper--theme-info-dropdown-left .v-popper__arrow-outer {
    border-color: rgba(56, 56, 56, 0.7);
  }

  .v-popper--theme-info-dropdown-left .v-popper__arrow-inner {
    visibility: hidden;
  }
</style>

<style src="../node_modules/mana-font/css/mana.min.css"></style>
<style src="../node_modules/keyrune/css/keyrune.min.css"></style>

<script>
import { EventBus } from '~/event-bus.js'

export default {
  name: 'game-grid',
  data () {
    return {
      teams: [],
      guesses: 9,
      unlimitedMode: false,
      hardMode: false,
      gameOver: false,
      isVisible: false,
      gridStatus: {
        s00: false,
        s01: false,
        s02: false,
        s10: false,
        s11: false,
        s12: false,
        s20: false,
        s21: false,
        s22: false
      }
    }
  },
  methods: {
    toggleVisibility () {
      this.isVisible = !this.isVisible
    },
    async buttonClicked (buttonID) {
      console.log('Button clicked. Emitting event...')
      await this.$store.commit('setSelectedGridLocation', buttonID)
      EventBus.$emit('show-search')
    },
    newGame () {
      parent.location.reload()
    },
    hardModegame () {
      this.isVisible = !this.isVisible
      EventBus.$emit('show-hardMode')
      this.hardMode = true
    },
    shareGrid () {
      EventBus.$emit('show-share-popup')
      console.log('emitted share popup')
    },
    goToStats () {
      EventBus.$emit('game-over')
    },
    giveUp () {
      this.gameOver = true
      EventBus.$emit('game-over')
      this.guesses = 0
    }
  },
  async created () {
    EventBus.$on('show-easyMode', () => {
      this.isVisible = !this.isVisible
      this.hardMode = false
    })
    let data = ''
    if (this.$route.query.id !== undefined) {
      data = await this.$axios.get(`/get_shared_grid?id=${this.$route.query.id}`)
      this.teams = data.data
    } else {
      data = await this.$axios.get('/get_new_grid')
      this.teams = data.data
    }
    this.$store.commit('setGrid', data.data)
    EventBus.$on('player-selected', async () => {
      const playerData = this.$store.state.selectedPlayerEasy
      const player = playerData.split('|')[0].trim()
      const start = ''
      const end = ''
      for (const keys in this.gridStatus) {
        if (this.gridStatus[keys] !== false) {
          if (this.gridStatus[keys].name === player) {
            return alert('Player already selected! Please choose another.')
          }
        }
      }
      let team1 = ''
      let team2 = ''
      let team3 = ''
      let location = ''
      switch (this.$store.state.selectedGridLocation) {
        case 's00':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][0][1]
          team3 = this.teams[2][1]
          location = 's00'
          break
        case 's01':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][0][1]
          team3 = this.teams[2][1]
          location = 's01'
          break
        case 's02':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][0][1]
          team3 = this.teams[2][1]
          location = 's02'
          break
        case 's10':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][1][1]
          team3 = this.teams[2][1]
          location = 's10'
          break
        case 's11':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][1][1]
          team3 = this.teams[2][1]
          location = 's11'
          break
        case 's12':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][1][1]
          team3 = this.teams[2][1]
          location = 's12'
          break
        case 's20':
          team1 = this.teams[0][0][1]
          team2 = this.teams[1][2][1]
          team3 = this.teams[2][1]
          location = 's20'
          break
        case 's21':
          team1 = this.teams[0][1][1]
          team2 = this.teams[1][2][1]
          team3 = this.teams[2][1]
          location = 's21'
          break
        case 's22':
          team1 = this.teams[0][2][1]
          team2 = this.teams[1][2][1]
          team3 = this.teams[2][1]
          location = 's22'
          break
      }
      const data = await this.$axios.get(`/validate_player?name=${player}&team1=${team1}&team2=${team2}&team3=${team3}&start=${start}&end=${end}&end=${end}&hardMode=${this.hardMode}`)
      if (Object.keys(data.data).length > 0) {
        this.gridStatus[location] = data.data
      }
      this.guesses--
      if (this.guesses === 0 && this.unlimitedMode === false) {
        this.gameOver = true
        EventBus.$emit('game-over')
      }
      if (this.gridStatus.s00 !== false && this.gridStatus.s01 !== false && this.gridStatus.s02 !== false && this.gridStatus.s10 !== false && this.gridStatus.s11 !== false && this.gridStatus.s12 !== false && this.gridStatus.s20 !== false && this.gridStatus.s21 !== false && this.gridStatus.s22 !== false && this.unlimitedMode === true) {
        this.gameOver = true
        EventBus.$emit('game-over')
      }
    })
  }
}
</script>
