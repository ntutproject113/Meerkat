<script setup>
import {ref,reactive} from 'vue';
import { useRouter,useRoute } from 'vue-router';
import Menu from '../components/Menu.vue';
import { useTodoStore } from '../stores/todo'
import { storeToRefs } from 'pinia'
import { nextTick } from 'vue'


const router = useRouter()
const route = useRoute()

const goToIsland = () => {
  router.push({ name: 'Island' })
}
const goToRenting = () => {
  router.push({ name: 'Renting' })
}
 const goToIntern =() =>{
  router.push({name:'Intern'})
 }
 const goToCompetition =() =>{
  router.push({name:'Competition'})
 }
 const goToScholarship =() =>{
  router.push({name:'Scholarship'})
 }

 const islandId = route.query.islandId
//地球hover圖片
const normalImg = new URL('../assets/images/plan/地球.png', import.meta.url).href
const hoverImg = new URL('../assets/images/plan/地球轉.png', import.meta.url).href

// 建立圖片狀態
const imgSrc = ref(normalImg)
const isHover = ref(false)

const onMouseEnter = () => {
  imgSrc.value = hoverImg
  isHover.value = true
}
const onMouseLeave = () => {
  imgSrc.value = normalImg
  isHover.value = false
}
//todolist在todo.js
const todoStore = useTodoStore()
const { items } = storeToRefs(todoStore)

const handleCheck = (item) => {
  if (!item.checked) {
    item.checked = true;
    setTimeout(() =>{
    router.push({ name: 'InsideIsland', query: { islandId: item.islandId } })
  },300)
  } else {
    // 如果取消勾選，就只是更新狀態，不跳頁
    item.checked = false;
  }
};
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <!--地球-->
        <div>
            <img :src="imgSrc" alt="成就" class="earth"
            :class="{ 'earth-hover': isHover }"
            @mouseenter="onMouseEnter" @mouseleave="onMouseLeave"
            @click="goToIsland">
        </div>
        <!--ToDoList-->
        <div class="todolist">
            <img src="../assets/images/plan/Todolist.png" alt="ToDoList" class="todolist-img">
             <ul>
                <li v-for="(item, index) in items" :key="item.key">
                <label class="custom-checkbox" >
                    <input
                    type="checkbox"
                    :checked="item.checked" @change="handleCheck(item, index)" />
                    <span class="checkmark"></span>
                    {{ item.label }}
                </label>
                </li>
            </ul>
        </div>
      

        <!--目標牌-->
        <div>
            <img src="../assets/images/plan/goal.png" alt="目標" class="goal">
        </div>
        <!--為你推薦-->
        <div class="recommand">
            <img src="../assets/images/plan/rec_background.png" alt="背景" class="rec-background">
            <img src="../assets/images/plan/recommand_icon.png" alt="推薦圖示" class="recommand-icon">
            <p>
            <strong style="color: #703C05; font-size: 48px ; position: absolute; top: 70px; left: 160px;">為您推薦</strong>
            </p>
            <div class="grid-container">
                <div class="image-box" @click="goToRenting">
                    <img src="../assets/images/plan/rec_content.png" alt="租屋推薦" />
                    <div class="image-text">租屋</div>
                </div>
                <div class="image-box" @click="goToIntern">
                    <img src="../assets/images/plan/rec_content.png" alt="實習推薦" />
                    <div class="image-text">實習</div>
                </div>
                <div class="image-box" @click="goToCompetition">
                    <img src="../assets/images/plan/rec_content.png" alt="比賽推薦" />
                    <div class="image-text">比賽</div>
                </div>
                <div class="image-box" @click="goToScholarship">
                    <img src="../assets/images/plan/rec_content.png" alt="獎學金推薦" />
                    <div class="image-text">獎學金</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.earth {
  position: absolute;
  left: 0;
  top: 40px;
  height: 90vh;
  width: auto;
  max-height: 100vh;
  object-fit: contain;
  transition: all 0.3s ease;
}
.earth-hover {
  left: 0;
  top: 40px;
  height: 95vh;
  width: auto;
  max-height: 100vh;
}
.goal{
    position: absolute;
    right:10px;
    top: 0px;
    height:250px;
    width:400px;
}
.todolist{
    position: absolute;
    left: 350px;
    color:white;
}
.todolist-img{
    width: 250px;
    height: 180px;
    object-fit: contain;
}
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 12px;
}
.custom-checkbox {
  display: flex;
  align-items: center;
  position: relative;
  gap:2px;
  padding-left: 30px;
  cursor: pointer;
  user-select: none;
  font-size: 24px;
  
}

.custom-checkbox input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.custom-checkbox .checkmark {
  flex-shrink:0;
  height: 50px;
  width: 50px;
  background-image: url('../assets/images/plan/unchecked.png'); 
  background-size: contain;
  background-repeat: no-repeat;
  background-position:center;
}

.custom-checkbox input:checked ~ .checkmark {
  background-image: url('../assets/images/plan/checked.png');
}

.recommand{
    position:relative;
    left: 350px;
    top: 500px;
    width:800px;
    height: 800px;
    z-index: 1;
    
}
.rec-background{
    width: 800px;
    height: 800px;
    object-fit: cover;
    display:block;
    position: absolute;
    z-index:0;
}

.recommand-icon{
        position: absolute;
        top:60px;
        left:75px;
        width: 100px;
        height: 100px;
        object-fit: contain;
}
.rec-content{
    position: absolute;
    top: 500px;
    left: 100px;
    width: 600px;
    height: 500px;
    object-fit: contain;
    z-index: 2;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  width: fit-content;
  margin:0 auto;
  z-index:1;
  position: relative;
  padding-top: 160px;
  right:10px;
}

.image-box {
  position: relative;
  width: 300px; 
}

.image-box img {
  width: 320px;
  height:270px;
  display: block;
}

.image-text {
  position: absolute;
  top: 42px;
  left: 10px;
  width: 100%;
  text-align: center;
  font-weight: bold;
  padding: 5px 0px;
  font-size: 28px;
}


</style>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  background: #210E59; /* 保險起見，讓 body 也有底色 */
}

.page-wrapper {
  background-color: #210E59;
  min-height: 100vh;
  width: 100vw;
  position: relative;
  overflow-x: hidden;
}
</style>



