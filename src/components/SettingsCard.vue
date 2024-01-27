<template>
  <div class="settings-card">
    <div class="card-content">
      <h2>Settings</h2>
      <p>This is the settings card</p>
      <p>ideas for settings</p>
      <ul>
        dark theme
      </ul>
      <ul>
        language option settings
      </ul>
      <ul>
        which translator to use
      </ul>
      <ul>
        in doc translation, what output? (file or text)
      </ul>
    </div>
    <div class="card-close" @click="closeSettingsCard">
      <b-icon-x></b-icon-x>
    </div>
  </div>
</template>

<script>
export default{
  methods: { 
    async getLanguageList() {
      const url = "http://127.0.0.1:5000/languages";
    },
    closeSettingsCard() {
      this.$emit("close");
    },
  },
}
</script>


<style scoped>
.settings-card {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black background */
  z-index: 200; /* Ensure it appears above other elements */
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  min-width: 600px;
  min-height: 700px;
}

.card-close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  color: #fff;
  font-size: 20px;
}

.settings-card {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black background */
  z-index: 200; /* Ensure it appears above other elements */
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>