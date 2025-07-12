import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Planning from '../views/Planning.vue'
import Renting from '../views/Renting.vue'
import Intern from '../views/Intern.vue'
import Scholarships from '../views/Scholarships.vue'
import Competition from '../views/Competition.vue'
import Island from '../views/Island.vue'
import LogIn from '../views/LogIn.vue'
import SignIn from '../views/SignIn.vue'
import QA from '../views/Q&A.vue'
import AptitudeTest from '../views/AptitudeTest.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/planning', name: 'Planning', component: Planning },
  { path: '/renting', name: 'Renting', component: Renting },
  { path: '/intern', name: 'Intern', component: Intern },
  { path: '/scholarships', name: 'Scholarships', component: Scholarships },
  { path: '/competition', name: 'Competition', component: Competition },
  { path: '/island', name: 'Island', component: Island },
  { path: '/logIn', name: 'LogIn', component: LogIn},
  { path: '/signIn', name: 'SignIn', component: SignIn},
  { path: '/q&a', name: 'Q&A', component: QA},
  { path: '/aptitudeTest', name: 'AptitudeTest', component:AptitudeTest},
  {path: '/InsideIsland', name: 'InsideIsland', component: () => import('../views/InsideIsland.vue') //訪問頁面時才載入 
    },
    {path: '/goal',name: 'Goal',component: () => import('../views/Goal.vue')
}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
