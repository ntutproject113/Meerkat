import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import VueKonva from 'vue-konva'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import './assets/tailwind.css'

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate) 
app.use(pinia) 
app.use(router)
app.use(VueKonva)

app.mount('#app')






