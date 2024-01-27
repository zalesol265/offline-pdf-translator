<template>
  <div class="preview-card">
    <div class="file-tag">{{ getFileType() }}</div>
    <p :title="key">
      {{ makeName() }}
    </p>
    <div class="del-file">
      <button
        type="button"
        @click="$emit('remove-file')"
        title="Remove file"
      >
        <b>&times;</b>
      </button>
    </div>
  </div>
  <p>{{triggerTranslation}}</p>
</template>

<script>


export default {
    props: {
        file: File,
        input_lang: String,
        output_lang: String,
        triggerTranslation: Boolean
    },
    data() {
        return {
        requestStatus: "not started",
        };
    },
    watch: {
        triggerTranslation(curVal) {
            alert("here");
            if (curVal) {
                alert("starting translation");
                this.translateDocument();
            }
        }
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
        this.requestStatus="in progress";
        const url = "http://127.0.0.1:5000/documentTranslate";

        // Create FormData object
        const formData = new FormData();
        formData.append("file", this.file); // Assuming the first file in the list

        // Add other data to the FormData object
        formData.append("input_lang", this.input_lang);
        formData.append("output_lang", this.output_lang);

        // Make a POST request to your backend endpoint
        try {
          const response = await fetch(url, {
            method: "POST",
            body: formData,
          });

          if (response.ok) {
            // Handle the response from the backend
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
