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
import AptitudeTestResult from '../views/AptitudeTestResult.vue'
import AptitudeTest0 from '../views/AptitudeTest0.vue'
import AptitudeTest1 from '../views/AptitudeTest1.vue'
import AptitudeTest2 from '../views/AptitudeTest2.vue'
import AptitudeTest3 from '../views/AptitudeTest3.vue'
import AptitudeTest4 from '../views/AptitudeTest4.vue'
import AptitudeTest5 from '../views/AptitudeTest5.vue'
import AptitudeTest6 from '../views/AptitudeTest6.vue'
import { name } from 'normalize-range'

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
  { path: '/aptitudeTestResult', name: 'AptitudeTestResult', component:AptitudeTestResult},
  { path: '/aptitudeTest0', name: 'AptitudeTest0', component:AptitudeTest0},
  { path: '/aptitudeTest1', name: 'AptitudeTest1', component:AptitudeTest1},
  { path: '/aptitudeTest2', name: 'AptitudeTest2', component:AptitudeTest2},
  { path: '/aptitudeTest3', name: 'AptitudeTest3', component:AptitudeTest3},
  { path: '/aptitudeTest4', name: 'AptitudeTest4', component:AptitudeTest4},
  { path: '/aptitudeTest5', name: 'AptitudeTest5', component:AptitudeTest5},
  { path: '/aptitudeTest6', name: 'AptitudeTest6', component:AptitudeTest6},
  { path: '/InsideIsland', name: 'InsideIsland', component: () => import('../views/InsideIsland.vue') //訪問頁面時才載入 
  },
  {path: '/goal',name: 'Goal',component: () => import('../views/Goal.vue')},
  {path: '/insideRenting', name: 'InsideRenting', component: () => import('../views/InsideRenting.vue') //訪問頁面時才載入
  },
  {path: '/insideScholarship', name:'InsideScholarship', component: () => import('../views/InsideScholarship.vue')}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
