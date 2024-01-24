<template>
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
</template>

<script>
export default {
  props: {
    docSettingOn: Boolean,
  },
  methods: {
    toggleSlider() {
      this.$emit("toggleSlider");
    },
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