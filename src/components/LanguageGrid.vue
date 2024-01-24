<template>
  <div v-if="showGrid" class="grid-container">
    <div
      v-for="language in languageList"
      :key="language"
      class="grid-item"
      :class="{ 'gridSelected': selectedLanguage === language }"
      @click="addToDisplayedLanguages(language)"
    >
      {{ languageDictionary[language] }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    showGrid: Boolean,
    languageList: Array,
    selectedLanguage: String,
    languageDictionary: Object,
  },
  methods: {
    addToDisplayedLanguages(language) {
      this.$emit("add-language", language);
    },
  },
};
</script>

<style scoped>
  .grid-container {
    position: absolute;
    width: 550px;
    background-color: white;
    padding:10px 20px 20px 20px;
    border-radius:5px;
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

  .grid-item:hover{
    background-color:rgb(233, 233, 233)
  }
</style>
