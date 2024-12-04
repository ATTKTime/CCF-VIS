import {createApp} from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './assets/reast.css'
import {createPinia} from 'pinia'
import persist from 'pinia-plugin-persistedstate'

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
app.use(pinia.use(persist))
app.use(ElementPlus)
app.mount('#app')
