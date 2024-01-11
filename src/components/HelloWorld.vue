<template>
  <div class="tab-container">
    <div
      v-for="(tab, index) in tabs"
      :key="index"
      @click="selectTab(index)"
      :class="{ 'active-tab': selectedTab === index }"
      class="tab"
    >
      {{ tab }}
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const tabs = ref(['Tab 1', 'Tab 2', 'Tab 3']);
const selectedTab = ref(0);

const selectTab = (index) => {
  selectedTab.value = index;
};
</script>

<style scoped>
.tab-container {
  display: flex;
  border-bottom: 1px solid #ccc;
}

.tab {
  padding: 10px 20px;
  cursor: pointer;
  user-select: none;
  border: 1px solid #ccc;
  border-bottom: none;
  border-radius: 5px 5px 0 0;
  margin-right: 5px;
  background-color: #f0f0f0;
}

.tab:hover {
  background-color: #e0e0e0;
}

.active-tab {
  background-color: #fff;
  border-bottom: 1px solid #ccc;
}
</style>
