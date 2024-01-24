
<template>
  <div>
    <b-button-group class="langInput">
      <b-button
        v-for="key in displayedLangList"
        :key="key"
        :class="{ 'selected': selectedLanguage === key }"
        @click="selectLanguage(key)"
      >
        {{ languageDictionary[key] }}
      </b-button>
    </b-button-group>
    <div class="optionArrow iconButton" @click="toggleLanguageGrid">
      <b-icon-caret-up-fill v-if="showLanguageGrid"></b-icon-caret-up-fill>
      <b-icon-caret-down-fill v-else></b-icon-caret-down-fill>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    displayedLangList: Array,
    selectedLanguage: String,
    languageDictionary: Object,
    showLanguageGrid: Boolean,
  },
  methods: {
    selectLanguage(language) {
      this.$emit("selectLanguage", language);
    },
    toggleLanguageGrid() {
      this.$emit("toggleLanguageGrid");
    },
  },
};
</script>

<style scoped>

</style>
