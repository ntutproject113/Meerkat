import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Planning from '../views/Planning.vue'

const routes = [
  { path: '/Home', name: 'Home', component: Home },
  { path: '/', name: 'Planning', component: Planning }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
