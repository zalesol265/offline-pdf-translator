
<template>
  <div>
    <b-button-group class="langInput">
      <b-button
        v-for="key in displayedLanguages"
        :key="key"
        :class="{ selected: selectedLanguage === key }"
        @click="selectLanguage(key)"
      >
        {{ languageDictionary[key] }}
      </b-button>
    </b-button-group>
    <div class="optionArrow iconButton" @click="toggleGrid">
      <b-icon-caret-up-fill v-if="showGrid"></b-icon-caret-up-fill>
      <b-icon-caret-down-fill v-else></b-icon-caret-down-fill>
    </div>
    <div v-if="showGrid" class="grid-container">
      <div
        v-for="language in languageKeys"
        :key="language"
        class="grid-item"
        :class="{ gridSelected: selectedLanguage === language }"
        @click="selectLanguage(language)"
      >
        {{ languageDictionary[language] }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showGrid: false,
      closeGridNextClick: false,
      displayedLanguages: [],
      languageKeys:[],
      topSelectedLangs:[],
      selectedLanguage:"",
      languageDictionary: {}
    };
  },

  methods: {

    initializeLanguageSelection(languageData) {
      this.languageDictionary = languageData;
      this.languageKeys = JSON.parse(JSON.stringify(Object.keys(languageData)));

      this.topSelectedLangs = this.languageKeys.slice(0, 3);
      this.selectedLanguage = this.languageKeys[0];
      this.$emit("updateLanguage", this.languageKeys[0]);

      // Change how many options can be shown based on screen width (wide: 3 langs, narrow: 1 lang)
      if (window.innerWidth >= 1024) {
        this.displayedLanguages = this.languageKeys.slice(0, 3);
      } else {
        this.displayedLanguages = this.languageKeys.slice(0, 1);
      }
    },
    updateDisplayedLanguages(lang) {
      if (!this.displayedLanguages.includes(lang)) {
        this.displayedLanguages.unshift(lang);
        this.displayedLanguages.pop();
      }

      if (window.innerWidth < 1024) {
        if (!this.topSelectedLangs.includes(lang)) {
          this.topSelectedLangs.unshift(lang);
          this.topSelectedLangs.pop();
        }
      }
    },
    selectLanguage(lang){
      this.updateDisplayedLanguages(lang);
      this.selectedLanguage = lang;
      this.$emit("updateLanguage", lang);
    },
    adjustNumDisplayedLanguages(prevWindowWidth, windowWidth) {
      if (prevWindowWidth < 1024 && windowWidth >= 1024) {
        this.displayedLanguages = this.topSelectedLangs;
      } else if (prevWindowWidth >= 1024 && windowWidth < 1024) {
        this.displayedLanguages = [this.selectedLanguage];
      }
    },
    checkGridVisibility(){
      if (this.closeGridNextClick) {
        this.showGrid = false;
        this.closeGridNextClick = false;
      } else if(this.showGrid){
        this.closeGridNextClick = true;
      }
    },
    toggleGrid() {
      this.showGrid = !this.showGrid;
    }
  },
};
</script>

<style scoped>

  .lang-settings{
    margin: auto;
  }

  .selected {
    color: blueviolet !important;
    margin: 0px !important;
    border-bottom: 3px solid blueviolet !important;
    border-radius: 0px !important;
  }

  .langInput {
    border-radius: 0px;
    margin: 5px;
    float: left;
    margin: 0px 0px 0px 8px !important;
  }

  .langInput > .btn {
    background-color: white;
    color: rgb(113, 113, 113);
    font-weight: 600;
    font-size: 14px;
    margin: 0px !important;
    border: 0px;
    border-radius: 0px !important;
    width: fit-content;
    padding: 8px 16px 14px 16px;
  }

  .langInput > .btn:hover {
    background-color: rgb(245, 239, 248);
    color: blueviolet;
    margin: 0px !important;
    border-radius: 0px !important;
  }

  .grid-container {
    position: absolute;
    width: 550px;
    background-color: white;
    padding: 10px 20px 20px 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 100;
    display: flex;
    flex-wrap: wrap;
    margin-top: 50px;
  }

  .grid-item {
    flex: 0 0 calc(33.33% - 10px);
    padding: 3px 3px 3px 20px;
    font-size: 15px;
    cursor: pointer;
  }

  .grid-item:hover {
    background-color: rgb(233, 233, 233);
  }

  .gridSelected {
    color: blueviolet !important;
    background-color: rgb(245, 239, 248);
  }
</style>
