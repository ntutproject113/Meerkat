import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Planning from '../views/Planning.vue'
import Renting from '../views/Renting.vue'
import Intern from '../views/Intern.vue'
import Scholarships from '../views/Scholarships.vue'
import Competition from '../views/Competition.vue'


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/planning', name: 'Planning', component: Planning },
  { path: '/renting', name: 'Renting', component: Renting },
  { path: '/intern', name: 'Intern', component: Intern },
  { path: '/scholarships', name: 'Scholarships', component: Scholarships },
  { path: '/competition', name: 'Competition', component: Competition }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
