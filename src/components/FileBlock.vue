<template>
  <div class="preview-card">
    <div class="file-tag">{{ getFileType() }}</div>
    <p :title="key">
      {{ makeName() }}
    </p>
    <div class="file-status">
      <button
        v-if="requestStatus == 'not started'"
        type="button"
        @click="$emit('remove-file')"
        title="Remove file"
      >
        <b>&times;</b>
      </button>
      <b-icon
        v-else-if="requestStatus == 'in progress'"
        icon="arrow-clockwise"
        class="spin"
      ></b-icon>
      <b-icon
        v-else-if="requestStatus == 'success'"
        icon="check2"
        class="success"
      ></b-icon>
      <b-icon v-else icon="dash-circle" class="error"></b-icon>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    file: File,
    input_lang: String,
    output_lang: String,
    triggerTranslation: Boolean,
  },
  data() {
    return {
      requestStatus: "not started",
    };
  },
  watch: {
    triggerTranslation(curVal) {
      if (curVal) {
        this.translateDocument();
      }
    },
  },

  methods: {
    makeName() {
      let name = this.file.name;
      if (name.length > 24) {
        return (
          name.split(".")[0].substring(0, 20) +
          "..." +
          name.split(".")[name.split(".").length - 1]
        );
      }
      return name;
    },

    getFileType() {
      let name = this.file.name;
      let fileType = name.split(".")[name.split(".").length - 1];
      return fileType.toUpperCase();
    },
    async translateDocument() {
      if (this.file) {
        this.requestStatus = "in progress";
        const url = "http://127.0.0.1:5000/documentTranslate";

        // Create FormData object
        const formData = new FormData();
        formData.append("file", this.file);
        formData.append("input_lang", this.input_lang);
        formData.append("output_lang", this.output_lang);

        try {
          const response = await fetch(url, {
            method: "POST",
            body: formData,
          });

          if (response.ok) {
            const data = await response.json();
            console.log(data);
            this.requestStatus = "success";
          } else {
            console.error("Error:", response.statusText);
            this.requestStatus = "fail";
          }
        } catch (error) {
          console.error("Error:", error.message);
          this.requestStatus = "fail";
        }
      }
    },
  },
};
</script>


<style scoped>
.file-status {
  margin-left: auto;
  margin-right: 10px;
}

svg {
  font-size: larger;
}

.success {
  color: green;
  font-size: x-large;
}

.error {
  color: red;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.spin {
  animation: spin 1.5s linear infinite;
}
</style>