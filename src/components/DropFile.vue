<template>
  <div class="main">
    <div
      class="dropzone-container"
      @dragover="dragover"
      @dragleave="dragleave"
      @drop="drop"
    >
      <input
        type="file"
        multiple
        name="file"
        id="fileInput"
        class="hidden-input"
        @change="onChange"
        ref="file"
        accept=".pdf,.jpg,.jpeg,.png"
      />
      <div class="upload-container">
        <b-icon
          id="file-upload-icon"
          icon="file-earmark-arrow-up-fill"
        ></b-icon>
        <label for="fileInput" class="file-label">
          <div v-if="isDragging">Release to drop files here.</div>
          <div v-else>Drop files here or <u>click here</u> to upload.</div>
        </label>
      </div>
      <div class="preview-container mt-4" v-if="files.length">
        <div v-for="file in files" :key="file.name" class="preview-card">
          <div class="file-tag">{{ getFileType(file.name) }}</div>
          <p :title="file.name">
            {{ makeName(file.name) }}
          </p>
          <div class="del-file">
            <button
              type="button"
              @click="remove(files.indexOf(file))"
              title="Remove file"
            >
              <b>&times;</b>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <p>{{selectedOutputLanguage}}</p>
</template>

<script>
export default {
  props: {
    selectedInputLanguage: String,
    selectedOutputLanguage: String,
  },
  data() {
    return {
      isDragging: false,
      files: [],
    };
  },
  methods: {
    onChange() {
      const newFiles = [...this.$refs.file.files];
      const uniqueNewFiles = newFiles.filter(
        (newFile) =>
          !this.files.some((existingFile) => existingFile.name === newFile.name)
      );
      this.files = [...this.files, ...uniqueNewFiles];
    },

    generateThumbnail(file) {
      let fileSrc = URL.createObjectURL(file);
      setTimeout(() => {
        URL.revokeObjectURL(fileSrc);
      }, 1000);
      return fileSrc;
    },

    getFileType(name) {
      let fileType = name.split(".")[name.split(".").length - 1];
      return fileType.toUpperCase();
    },

    makeName(name) {
      if (name.length > 24) {
        return (
          name.split(".")[0].substring(0, 20) +
          "..." +
          name.split(".")[name.split(".").length - 1]
        );
      }
      return name;
    },

    remove(i) {
      this.files.splice(i, 1);
    },

    dragover(e) {
      e.preventDefault();
      this.isDragging = true;
    },

    dragleave() {
      this.isDragging = false;
    },

    drop(e) {
      e.preventDefault();
      this.$refs.file.files = e.dataTransfer.files;
      this.onChange();
      this.isDragging = false;
    },

    async translateDocuments() {
      if (this.files && this.files.length > 0) {
        const url = "http://127.0.0.1:5000/documentTranslate";

        // Create FormData object
        const formData = new FormData();
        formData.append("file", this.files[0]); // Assuming the first file in the list

        // Add other data to the FormData object
        formData.append("input_lang", this.selectedInputLanguage);
        formData.append("output_lang", this.selectedOutputLanguage);

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
          } else {
            console.error("Error:", response.statusText);
          }
        } catch (error) {
          console.error("Error:", error.message);
        }
      }
    },
  },
};
</script>

<style>
.preview-container {
  max-width: 600px;
  margin: auto;
}

.upload-container {
  min-width: 200px;
}

#file-upload-icon {
  width: 77px;
  height: 77px;
  color: rgb(185, 185, 185);
  margin-bottom: 20px;
}
.file-tag {
  margin: 5px 8px;
  background-color: blueviolet;
  padding: 5px;
  color: white;
  border-radius: 5px;
}

p {
  margin: 0px;
}

.del-file {
  margin-left: auto;
}

button {
  background-color: transparent;
  border: 0px solid grey;
  width: unset;
}

.main {
  flex-grow: 1;
  text-align: center;
  border: 1px solid rgb(210, 210, 210);
  border-radius: 7px;
  min-height: 250px;
}

.dropzone-container {
  padding: 2rem;
}

.hidden-input {
  opacity: 0;
  overflow: hidden;
  position: absolute;
  width: 1px;
  height: 1px;
}

.file-label {
  font-size: 20px;
  display: block;
  cursor: pointer;
}

.preview-card {
  display: flex;
  padding: 5px;
  width: 100%;
  border-radius: 10px;
  align-items: center;
  justify-content: center;
  margin-bottom: 5px;
  background-color: rgb(233, 233, 233);
}

@media (min-width: 1024px) {
  .preview-container {
    width: 50%;
    float: right;
    padding: 2rem;
    border-left: 1px solid rgb(206, 206, 206);
    min-width: 500px;
  }

  .upload-container {
    width: 50%;
    float: left;
    padding: 2rem;
    min-width: 500px;
  }

  .main {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .dropzone-container {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>