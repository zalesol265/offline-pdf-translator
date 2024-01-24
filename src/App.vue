<template>
  <!-- <b-icon-gear-fill></b-icon-gear-fill> -->
  <div>
    <!-- <div id="sliderBox">
      <div id="slider" :class="{ 'slider-open': docSettingOn }" @click="toggleSlider">
        <div style="line-height: 2">
          <b-icon-file-earmark v-if="docSettingOn"></b-icon-file-earmark>
          <b-icon-fonts v-else></b-icon-fonts>
          {{ docSettingOn ? "File" : "Text" }}
        </div>
      </div>
      <div>
        <b-icon-fonts></b-icon-fonts>
        Text
      </div>
      <div>
        <b-icon-file-earmark></b-icon-file-earmark>
        File
      </div>
    </div> -->
    <SliderBox :docSettingOn="docSettingOn" @toggleSlider="toggleSlider" />

  </div>
  <div>
    <div class="iconButton" id="settingsIcon" @click="showSettingsCard = true">
      <b-icon-gear-fill></b-icon-gear-fill>
    </div>
  </div>
  <div>
    <LanguageSelection
      :displayedLangList="displayedInputLangList"
      :selectedLanguage="selectedInputLanguage"
      :languageDictionary="inputLanguageDictionary"
      :showLanguageGrid="showInputLanguageGrid"
      @selectLanguage="selectInputLanguage"
      @toggleLanguageGrid="toggleRequestInputLanguageGrid"
    />
    <div class="iconButton swapLangBtn" @click="swapLanguages">
      <b-icon-arrow-left-right></b-icon-arrow-left-right>
    </div>
  </div>
  <div>
    <LanguageSelection
      :displayedLangList="displayedOutputLangList"
      :selectedLanguage="selectedOutputLanguage"
      :languageDictionary="outputLanguageDictionary"
      :showLanguageGrid="showOutputLanguageGrid"
      @selectLanguage="selectOutputLanguage"
      @toggleLanguageGrid="toggleRequestOutputLanguageGrid"
    />
  </div>
  <div>
    <LanguageGrid
      :showGrid="showInputLanguageGrid"
      :languageList="inputLanguageKeys"
      :selectedLanguage="selectedInputLanguage"
      :languageDictionary="inputLanguageDictionary"
      @add-language="addToDisplayedInputLanguages"
    />
    <b-form-textarea
      class="textarea"
      v-model="inputText"
      placeholder="Enter something..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
  </div>
  <div>
    <LanguageGrid
      :showGrid="showOutputLanguageGrid"
      :languageList="outputLanguageKeys"
      :selectedLanguage="selectedOutputLanguage"
      :languageDictionary="outputLanguageDictionary"
      @add-language="addToDisplayedOutputLanguages"
    />
    <b-form-textarea
      class="textarea"
      id="outputtext"
      v-model="outputText"
      rows="3"
      max-rows="6"
    ></b-form-textarea>
  </div>
  <div />
  <div><b-button id="translate"  @click="translate()">translate</b-button></div>
  <div>
    <SettingsCard v-if="showSettingsCard" class="settings-card" @close="showSettingsCard = !showSettingsCard"/>
  </div>
</template>

<script>

import SettingsCard from "@/components/SettingsCard.vue";
import LanguageGrid from './components/LanguageGrid.vue';
import LanguageSelection from './components/LanguageSelection.vue';
import SliderBox from './components/SliderBox.vue';

export default {
  data() {
    return {
      docSettingOn: false,
      showInputLanguageGrid: false,
      showOutputLanguageGrid: false,
      showSettingsCard: false,
      inputLanguageDictionary:{},
      outputLanguageDictionary:{},
      inputLanguageKeys:[],
      outputLanguageKeys:[],
      displayedInputLangList:[],
      displayedOutputLangList: [],
      selectedInputLanguage: "",
      selectedOutputLanguage: "",
      inputText: "",
      outputText: "",
      clicks:0,
      requestInputGrid:false,
      requestOutputGrid:false
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
      const url = 'http://127.0.0.1:5000/languages';


    },
    async translate() {
      const url = 'http://127.0.0.1:5000/translate';
      const data = {
        text: this.inputText,
        input_lang: this.selectedInputLanguage,
        output_lang: this.selectedOutputLanguage
      };

      const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
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
    toggleRequestInputLanguageGrid(){
      this.requestInputGrid = !this.requestInputGrid;
    },    
    toggleRequestOutputLanguageGrid(){
      this.requestOutputGrid = !this.requestOutputGrid;
    },
    swapLanguages(){
      if (this.inputLanguageKeys.includes(this.selectedOutputLanguage) && this.outputLanguageKeys.includes(this.selectedInputLanguage) ){
        [ this.selectedOutputLanguage, this.selectedInputLanguage ] = [ this.selectedInputLanguage, this.selectedOutputLanguage ];
        this.updateLangDisplayList(this.displayedOutputLangList, this.selectedOutputLanguage);
        this.updateLangDisplayList(this.displayedInputLangList, this.selectedInputLanguage);
        [ this.inputText, this.outputText ] = [ this.outputText, this.inputText ];
      } else {
        alert("One of the selected languages cannot be used as either the input or output language.")
      }
    },
    addToDisplayedInputLanguages(language) {
      this.updateLangDisplayList(this.displayedInputLangList, language)
      this.selectInputLanguage(language);
      // this.toggleInputLanguageGrid();
    },
    addToDisplayedOutputLanguages(language) {
      this.updateLangDisplayList(this.displayedOutputLangList, language)
      this.selectOutputLanguage(language);
      // this.toggleOutputLanguageGrid();
    },
    updateLangDisplayList(langList, lang){
      if (!langList.includes(lang)) {
        langList.unshift(lang);
        langList.pop();
      };
    },
        // Handle document click event
    handleDocumentClick(event) {
      this.clicks += 1;
      if(this.requestInputGrid){
        this.toggleInputLanguageGrid();
        this.toggleRequestInputLanguageGrid();
      } else if (this.showInputLanguageGrid) {
        this.toggleInputLanguageGrid();
      }

      if(this.requestOutputGrid){
        this.toggleOutputLanguageGrid();
        this.toggleRequestOutputLanguageGrid();
      } else if (this.showOutputLanguageGrid) {
        this.toggleOutputLanguageGrid();
      }

    },
    setLanguageOptions(){
      fetch('http://127.0.0.1:5000/installed')
      .then(response => response.json())
      .then(data => {
        // data = json.dumps(data._getvalue());
        this.inputLanguageDictionary = data['input'];
        console.log(Object.keys(this.inputLanguageDictionary));
        this.outputLanguageDictionary = data['output'];
        this.inputLanguageKeys = JSON.parse(JSON.stringify(Object.keys(data['input'])));
        this.outputLanguageKeys = JSON.parse(JSON.stringify(Object.keys(data['output'])));
        this.displayedInputLangList = this.inputLanguageKeys;//.slice(2, 5);
        this.displayedOutputLangList = this.outputLanguageKeys.slice(2, 5);
        this.selectedInputLanguage = this.inputLanguageKeys[0];
        this.selectedOutputLanguage = this.outputLanguageKeys[3];
      })
      .catch(error => {
        console.error('Error fetching languages:', error);
      });
    }
  },

  mounted() {
    // Add a click event listener to the document
    document.addEventListener('click', this.handleDocumentClick);
    this.setLanguageOptions();
  },

  beforeUnmount() {
    // Remove the click event listener when the component is destroyed
    document.removeEventListener('click', this.handleDocumentClick);
  },

};
</script>
