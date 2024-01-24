<template>
  <!-- <b-icon-gear-fill></b-icon-gear-fill> -->
  <div class="flex-space">
    <SliderBox :docSettingOn="docSettingOn" @toggleSlider="toggleSlider" />
    <div class="iconButton" id="settingsIcon" @click="showSettingsCard = true">
      <b-icon-gear-fill></b-icon-gear-fill>
    </div>
  </div>
  <div class="flex-space">
    <LanguageSelection
      class="lang-settings"
      :displayedLangList="displayedInputLangList"
      :selectedLanguage="selectedInputLanguage"
      :languageDictionary="inputLanguageDictionary"
      :showLanguageGrid="showInputLanguageGrid"
      @selectLanguage="selectInputLanguage"
      @toggleLanguageGrid="toggleRequestInputLanguageGrid"
    />
    <LanguageGrid
      :showGrid="showInputLanguageGrid"
      :languageList="inputLanguageKeys"
      :selectedLanguage="selectedInputLanguage"
      :languageDictionary="inputLanguageDictionary"
      @add-language="addToDisplayedInputLanguages"
    />
    <div class="iconButton swapLangBtn" @click="swapLanguages">
      <b-icon-arrow-left-right></b-icon-arrow-left-right>
    </div>
    <div class="lang-settings">
      <LanguageSelection
        :displayedLangList="displayedOutputLangList"
        :selectedLanguage="selectedOutputLanguage"
        :languageDictionary="outputLanguageDictionary"
        :showLanguageGrid="showOutputLanguageGrid"
        @selectLanguage="selectOutputLanguage"
        @toggleLanguageGrid="toggleRequestOutputLanguageGrid"
      />
      <LanguageGrid
        id="outputLangGrid"
        :showGrid="showOutputLanguageGrid"
        :languageList="outputLanguageKeys"
        :selectedLanguage="selectedOutputLanguage"
        :languageDictionary="outputLanguageDictionary"
        @add-language="addToDisplayedOutputLanguages"
      />
    </div>
  </div>
  <div id="text-input">
    <div>
      <b-form-textarea
        class="textarea"
        v-model="inputText"
        placeholder="Enter something..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>
    <div>
      <b-form-textarea
        class="textarea"
        id="outputtext"
        v-model="outputText"
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>
  </div>
  <div><b-button id="translate" @click="translate()">translate</b-button></div>
  <div>
    <SettingsCard
      v-if="showSettingsCard"
      class="settings-card"
      @close="showSettingsCard = !showSettingsCard"
    />
  </div>
</template>

<script>
import SettingsCard from "@/components/SettingsCard.vue";
import LanguageGrid from "./components/LanguageGrid.vue";
import LanguageSelection from "./components/LanguageSelection.vue";
import SliderBox from "./components/SliderBox.vue";

export default {
  data() {
    return {
      docSettingOn: false,
      showInputLanguageGrid: false,
      showOutputLanguageGrid: false,
      showSettingsCard: false,
      inputLanguageDictionary: {},
      outputLanguageDictionary: {},
      inputLanguageKeys: [],
      outputLanguageKeys: [],
      displayedInputLangList: [],
      displayedOutputLangList: [],
      selectedInputLanguage: "",
      selectedOutputLanguage: "",
      inputText: "",
      outputText: "",
      clicks: 0,
      requestInputGrid: false,
      requestOutputGrid: false,
      prevWindowWidth: null,
      topSelectedInputLangs: [],
      topSelectedOutputLangs: [],
    };
  },
  components: {
    SettingsCard,
    LanguageGrid,
    LanguageSelection,
    SliderBox,
  },
  methods: {
    async getLanguageList() {
      const url = "http://127.0.0.1:5000/languages";
    },
    async translate() {
      const url = "http://127.0.0.1:5000/translate";
      const data = {
        text: this.inputText,
        input_lang: this.selectedInputLanguage,
        output_lang: this.selectedOutputLanguage,
      };

      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      const responseData = await response.json();
      this.outputText = responseData;
    },
    toggleSlider() {
      this.docSettingOn = !this.docSettingOn;
    },
    toggleInputLanguageGrid() {
      this.showInputLanguageGrid = !this.showInputLanguageGrid;
    },
    toggleOutputLanguageGrid() {
      this.showOutputLanguageGrid = !this.showOutputLanguageGrid;
    },
    selectInputLanguage(language) {
      this.selectedInputLanguage = language;
    },
    selectOutputLanguage(language) {
      this.selectedOutputLanguage = language;
    },
    toggleRequestInputLanguageGrid() {
      this.requestInputGrid = !this.requestInputGrid;
    },
    toggleRequestOutputLanguageGrid() {
      this.requestOutputGrid = !this.requestOutputGrid;
    },
    swapLanguages() {
      if (
        this.inputLanguageKeys.includes(this.selectedOutputLanguage) &&
        this.outputLanguageKeys.includes(this.selectedInputLanguage)
      ) {
        [this.selectedOutputLanguage, this.selectedInputLanguage] = [
          this.selectedInputLanguage,
          this.selectedOutputLanguage,
        ];
        this.updateLangDisplayList(
          this.displayedOutputLangList,
          this.selectedOutputLanguage,
          this.topSelectedOutputLangs
        );
        this.updateLangDisplayList(
          this.displayedInputLangList,
          this.selectedInputLanguage,
          this.topSelectedInputLangs
        );
        [this.inputText, this.outputText] = [this.outputText, this.inputText];
      } else {
        alert(
          "One of the selected languages cannot be used as either the input or output language."
        );
      }
    },
    addToDisplayedInputLanguages(language) {
      this.updateLangDisplayList(
        this.displayedInputLangList,
        language,
        this.topSelectedInputLangs
      );
      this.selectInputLanguage(language);
    },
    addToDisplayedOutputLanguages(language) {
      this.updateLangDisplayList(
        this.displayedOutputLangList,
        language,
        this.topSelectedOutputLangs
      );
      this.selectOutputLanguage(language);
    },
    updateLangDisplayList(displayedList, lang, topLangsList) {
      if (!displayedList.includes(lang)) {
        displayedList.unshift(lang);
        displayedList.pop();
      }

      if (window.innerWidth < 1024) {
        if (!topLangsList.includes(lang)) {
          topLangsList.unshift(lang);
          topLangsList.pop();
        }
      }
    },

    handleDocumentClick(event) {
      this.clicks += 1;
      if (this.requestInputGrid) {
        this.toggleInputLanguageGrid();
        this.toggleRequestInputLanguageGrid();
      } else if (this.showInputLanguageGrid) {
        this.toggleInputLanguageGrid();
      }

      if (this.requestOutputGrid) {
        this.toggleOutputLanguageGrid();
        this.toggleRequestOutputLanguageGrid();
      } else if (this.showOutputLanguageGrid) {
        this.toggleOutputLanguageGrid();
      }
    },
    setLanguageOptions() {
      fetch("http://127.0.0.1:5000/installed")
        .then((response) => response.json())
        .then((data) => {
          // Set list of available language keys, and provide dictionary to lookup names
          this.inputLanguageDictionary = data["input"];
          this.outputLanguageDictionary = data["output"];
          this.inputLanguageKeys = JSON.parse(
            JSON.stringify(Object.keys(data["input"]))
          );
          this.outputLanguageKeys = JSON.parse(
            JSON.stringify(Object.keys(data["output"]))
          );

          // Initialize language selection history and the default languages used for translation
          this.topSelectedInputLangs = this.inputLanguageKeys;
          this.topSelectedOutputLangs = this.outputLanguageKeys.slice(0, 3);
          this.selectedInputLanguage = this.inputLanguageKeys[0];
          this.selectedOutputLanguage = this.outputLanguageKeys[0];

          // Change how many options can be shown based on screen width (wide: 3 langs, narrow: 1 lang)
          if (window.innerWidth >= 1024) {
            this.displayedInputLangList = this.inputLanguageKeys;
            this.displayedOutputLangList = this.outputLanguageKeys.slice(0, 3);
          } else {
            this.displayedInputLangList = this.inputLanguageKeys.slice(0, 1);
            this.displayedOutputLangList = this.outputLanguageKeys.slice(0, 1);
          }
        })
        .catch((error) => {
          console.error("Error fetching languages:", error);
        });
    },
    changeDisplayedLanguageListLength() {
      if (this.prevWindowWidth < 1024 && window.innerWidth >= 1024) {
        this.displayedInputLangList = this.topSelectedInputLangs;
        this.displayedOutputLangList = this.topSelectedOutputLangs;
      } else if (this.prevWindowWidth >= 1024 && window.innerWidth < 1024) {
        this.displayedInputLangList = [this.selectedInputLanguage];
        this.displayedOutputLangList = [this.selectedOutputLanguage];
      }
      this.prevWindowWidth = window.innerWidth;
    },
  },

  mounted() {
    this.prevWindowWidth = window.innerWidth;
    document.addEventListener("click", this.handleDocumentClick);
    window.addEventListener("resize", this.changeDisplayedLanguageListLength);
    this.setLanguageOptions();
  },

  beforeUnmount() {
    document.removeEventListener("click", this.handleDocumentClick);
    window.removeEventListener(
      "resize",
      this.changeDisplayedLanguageListLength
    );
  },
};
</script>
