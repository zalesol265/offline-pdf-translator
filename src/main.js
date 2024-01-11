import './assets/main.css'

// import Vue, { createApp } from '@vue/compat';
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// import App from './App.vue'


// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)

// createApp(App).mount('#app')

import Vue, { createApp } from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BootstrapVue, { BootstrapVueIcons } from 'bootstrap-vue'
import App from './App.vue'


Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons)
const app = createApp(App);
app.mount('#app');
