<template>
  <div class="flex-space">
    <SliderBox
      :docSettingOn="docSettingOn"
      @toggleSlider="docSettingOn = !docSettingOn"
    />
    <div class="iconButton" id="settingsIcon" @click="showSettingsCard = true">
      <b-icon-gear-fill></b-icon-gear-fill>
    </div>
  </div>
  <div class="flex-space">
    <LanguageSelection
      class="lang-settings"
      ref="inputLangsRef"
      @updateLanguage="updateInputLanguage"
    />
    <div class="iconButton swapLangBtn" @click="swapLanguages">
      <b-icon-arrow-left-right></b-icon-arrow-left-right>
    </div>
    <LanguageSelection
      class="lang-settings"
      ref="outputLangsRef"
      @updateLanguage="updateOutputLanguage"
    />
  </div>
  <DropFile
    v-if="docSettingOn"
    ref="dropFileRef"
    :input_lang="inputLanguage"
    :output_lang="outputLanguage"
  />
  
  <TextAreas
    v-else
    id="text-input"
    ref="textAreasRef"
    :input_lang="inputLanguage"
    :output_lang="outputLanguage"
  />
  <div><b-button id="translate" @click="translate()">translate</b-button></div>
  <SettingsCard
    v-if="showSettingsCard"
    class="settings-card"
    @close="showSettingsCard = !showSettingsCard"
  />
</template>

<script>
import SettingsCard from "@/components/SettingsCard.vue";
import LanguageSelection from "./components/LanguageSelection.vue";
import SliderBox from "./components/SliderBox.vue";
import DropFile from "./components/DropFile.vue";
import TextAreas from "./components/TextAreas.vue";

export default {
  data() {
    return {
      docSettingOn: false,
      showSettingsCard: false,
      clicks: 0,
      prevWindowWidth: null,
      inputLanguage: "",
      outputLanguage: ""
    };
  },
  components: {
    SettingsCard,
    LanguageSelection,
    SliderBox,
    DropFile,
    TextAreas,
  },
  methods: {
    async translate() {
      if (this.docSettingOn) {
        this.$refs.dropFileRef.translateDocuments();
      } else {
        this.$refs.textAreasRef.translateText();
      }
    },
    swapLanguages() {
      let output_lang = this.$refs.outputLangsRef.selectedLanguage;
      let input_lang = this.$refs.inputLangsRef.selectedLanguage;

      let output_options = this.$refs.outputLangsRef.languageKeys;
      let input_options = this.$refs.inputLangsRef.languageKeys;

      if (
        output_options.includes(input_lang) &&
        input_options.includes(output_lang)
      ) {
        this.$refs.inputLangsRef.selectLanguage(output_lang);
        this.$refs.outputLangsRef.selectLanguage(input_lang);
        this.$refs.textAreasRef.swapText();
      } else {
        alert(
          "One of the selected languages cannot be used as either the input or output language."
        );
      }
    },
    updateInputLanguage(language) {
      this.inputLanguage = language;
    },
    updateOutputLanguage(language) {
      this.outputLanguage = language;
    },
    handleDocumentClick(event) {
      this.clicks += 1;
      this.$refs.inputLangsRef.checkGridVisibility();
      this.$refs.outputLangsRef.checkGridVisibility();
    },
    setLanguageOptions() {
      fetch("http://127.0.0.1:5000/installed")
        .then((response) => response.json())
        .then((data) => {
          let inputLanguageDictionary = data["input"];
          let outputLanguageDictionary = data["output"];
          this.$refs.inputLangsRef.initializeLanguageSelection(inputLanguageDictionary);
          this.$refs.outputLangsRef.initializeLanguageSelection(outputLanguageDictionary);
        })
        .catch((error) => {
          console.error("Error fetching languages:", error);
        });
    },
    changeDisplayedLanguageListLength() {
      let curWindowWidth = window.innerWidth;
      this.$refs.inputLangsRef.adjustNumDisplayedLanguages(this.prevWindowWidth, curWindowWidth);
      this.$refs.outputLangsRef.adjustNumDisplayedLanguages(this.prevWindowWidth, curWindowWidth );
      this.prevWindowWidth = curWindowWidth;
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
    window.removeEventListener("resize", this.changeDisplayedLanguageListLength);
  },
};
</script>
