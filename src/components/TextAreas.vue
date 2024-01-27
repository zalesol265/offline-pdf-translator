<template>
  <div>
    <div>
      <b-form-textarea
        class="textarea"
        v-model="inputText"
        placeholder="Enter something..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>
    <div>
      <b-form-textarea
        class="textarea"
        id="outputtext"
        v-model="outputText"
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        input_lang: String,
        output_lang: String,
    },
    data() {
        return {
            inputText: '',
            outputText: '',
            isDragging: false,
            files: [],
        };
    },
  methods: {

    async translateText() {

        const url = "http://127.0.0.1:5000/translate";
        const data = {
          text: this.inputText,
          input_lang: this.input_lang,
          output_lang: this.output_lang,
        };

        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
        const responseData = await response.json();
        this.outputText = responseData;
      
    },

    swapText(){
        [this.inputText, this.outputText] = [this.outputText, this.inputText];
    }
  }
};
</script>

<style>
.textarea{
  margin-bottom:5px;
  min-height:200px!important;
  overflow-y: auto!important;
}

.textarea:focus {
  border: 1px solid rgb(230, 230, 230);
  box-shadow: 0 0 2px rgb(166, 80, 181);
  outline: none;
}

#outputtext{
  background-color:#f3f3f3;
}


</style>