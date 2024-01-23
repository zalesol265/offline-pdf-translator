<template>
  <!-- <b-icon-gear-fill></b-icon-gear-fill> -->
  <div>
    <div id="sliderBox">
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
    </div>
  </div>
  <div>
    <div class="iconButton" id="settingsIcon" @click="showSettingsCard = true">
      <b-icon-gear-fill></b-icon-gear-fill>
    </div>
  </div>
  <div>
    <b-button-group class="langInput">
      <b-button
        v-for="(key) in displayedInputLangList"
        :key="key"
        :class="{ 'selected': selectedInputLanguage === key }"
        @click="selectInputLanguage(key)"
      >
        {{ inputLanguageDictionary[key] }}
      </b-button>
    </b-button-group>
    <div class="optionArrow iconButton" @click="toggleRequestInputLanguageGrid">
      <b-icon-caret-up-fill v-if="showInputLanguageGrid"></b-icon-caret-up-fill>
      <b-icon-caret-down-fill v-else></b-icon-caret-down-fill>
    </div>
    <div class="iconButton swapLangBtn" @click="swapLanguages">
      <b-icon-arrow-left-right></b-icon-arrow-left-right>
    </div>
  </div>
  <div>
    <b-button-group class="langInput">
      <b-button
        v-for="(key) in displayedOutputLangList"
        :key="key"
        :class="{ 'selected': selectedOutputLanguage === key }"
        @click="selectOutputLanguage(key)"
      >
        {{ outputLanguageDictionary[key] }}
      </b-button>
    </b-button-group>
    <div class="optionArrow iconButton" @click="toggleRequestOutputLanguageGrid">
      <b-icon-caret-up-fill v-if="showOutputLanguageGrid"></b-icon-caret-up-fill>
      <b-icon-caret-down-fill v-else></b-icon-caret-down-fill>
    </div>
  </div>
  <div>
    <div v-if="showInputLanguageGrid" class="grid-container">
      <div
        v-for="(key) in inputLanguageKeys"
        :key="key"
        class="grid-item"
        :class="{ 'gridSelected': selectedInputLanguage === inputLanguageDictionary[key] }"
        @click="addToDisplayedInputLanguages(key)"
      >
        {{ inputLanguageDictionary[key] }}
      </div>
    </div>
    <b-form-textarea
      class="textarea"
      v-model="inputText"
      placeholder="Enter something..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
  </div>
  <div>
    <div v-if="showOutputLanguageGrid" class="grid-container">
      <div
        v-for="(key) in outputLanguageKeys"
        :key="key"
        class="grid-item"
        :class="{ 'gridSelected': selectedOutputLanguage === outputLanguageDictionary.key }"
        @click="addToDisplayedOutputLanguages(key)"
      >
        {{ outputLanguageDictionary[key] }}
      </div>
    </div>
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
    <div v-if="showSettingsCard" class="settings-card">
      <div class="card-content">
        <h2>Settings</h2>
        <p>This is the settings card</p>
        <p>ideas for settings</p>
        <ul>dark theme</ul>
        <ul>language option settings</ul>
        <ul>which translator to use</ul>
        <ul>in doc translation, what output? (file or text)</ul>

      </div>
      <div class="card-close" @click="showSettingsCard = false">
        <b-icon-x></b-icon-x>
      </div>
    </div>
  </div>

</template>

<script>

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

  methods: {
    async getLanguageList() {
      const url = 'http://127.0.0.1:5000/languages';


    },
    async translate() {
      // alert("Translating!");
      // const args = ['translate', this.inputText, "en", "es"];
      // const command = window.__TAURI__.shell.Command.sidecar("bin/python/test", args);
      // const output = await command.execute();
      // const { stdout, stderr } = output;
      // alert(stdout);
      // this.outputText = stdout;
      // // Parse the JSON output
      // const jsonOutput = JSON.parse(stdout);

      // // Access individual pieces of information
      // this.outputText = jsonOutput.greeting;

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
      [ this.selectedOutputLanguage, this.selectedInputLanguage ] = [ this.selectedInputLanguage, this.selectedOutputLanguage ];
      this.updateLangDisplayList(this.displayedOutputLangList, this.selectedOutputLanguage);
      this.updateLangDisplayList(this.displayedInputLangList, this.selectedInputLanguage);
      [ this.inputText, this.outputText ] = [ this.outputText, this.inputText ];
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

<style scoped>


#slider {
  transition: transform 0.3s ease-in-out;
}

.slider-open {
  transform: translateX(100%); /* Set your desired distance */
}
</style>

<style scoped>
/* Your styles here */
.logo.tauri:hover {
  filter: drop-shadow(0 0 2em #ffe21c);
}

select,
input,
textarea {
  margin: 10px;
  width: 500px;
}

button {
  margin: 10px;
  width: 200px;
}
</style>
