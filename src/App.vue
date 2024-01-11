<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div class="container">
    <h1>Welcome to Tauri!</h1>

    <div class="row">
      <a href="https://tauri.app" target="_blank">
        <img src="./assets/tauri.svg" class="logo tauri" alt="Tauri logo" />
      </a>

          <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    </div>

    <p>Fill out the form below and click Greet to get a response from test.py</p>

    <div>
      <input v-model="name" type="text" placeholder="Enter your name" />
      <input v-model="arg1" type="text" placeholder="Enter argument 1" />
      <input v-model="arg2" type="text" placeholder="Enter argument 2" />
    </div>

    <button @click="greet">Greet</button>

    <div style="margin-top: 20px;">
      <div id="greetMsg">{{ greetingMsg }}</div>
      <div id="argMsg">{{ argumentsMsg }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      arg1: "",
      arg2: "",
      greetingMsg: "",
      argumentsMsg: "",
    };
  },
  methods: {
    async greet() {
      // Check if any input is empty
      if (!this.name || !this.arg1 || !this.arg2) {
        alert("Please fill in all the fields");
        return;
      }

      // Pass user-input values to Python script
      const args = [this.name, this.arg1, this.arg2];
      const command = window.__TAURI__.shell.Command.sidecar("bin/python/test", args);
      const output = await command.execute();
      const { stdout, stderr } = output;

      // Parse the JSON output
      const jsonOutput = JSON.parse(stdout);

      // Access individual pieces of information
      this.greetingMsg = jsonOutput.greeting;
      this.argumentsMsg = jsonOutput.arguments;
    },
  },
};
</script>

<style scoped>
/* Your styles here */
.logo.tauri:hover {
  filter: drop-shadow(0 0 2em #ffe21c);
}

input {
  margin: 20px;
  width: 500px;
}

button {
  margin: auto;
  width: 200px;
}
</style>
