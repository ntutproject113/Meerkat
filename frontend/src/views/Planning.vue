<script setup>
import {ref} from 'vue';

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

</script>

<template>
    <!--地球-->
    <div>
        <img :src="imgSrc" alt="成就" class="earth"
        :class="{ 'earth-hover': isHover }"
        @mouseenter="onMouseEnter" @mouseleave="onMouseLeave">
    </div>
    <!--ToDoList-->
    <div>
        <img src="../assets/images/plan/Todolist.png" alt="ToDoList" class="todo">

        <ul>
            <li>第一項</li>
            <li>第二項</li>
            <li>第三項</li>
        </ul>
    </div>
    <!--目標牌-->
    <div>
        <img src="../assets/images/plan/goal.png" alt="目標" class="goal">
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
    height:300px;
    width:400px;
}
.todo{
    position: absolute;
    left: 350px;
    top: 60px;
    height: 130px;
    width: 350px;
}
ul{
    position: absolute;
    left: 350px;
    top: 200px;
    color:white;

}
 li{
  list-style: none;
  background: url('../assets/images/plan/checkbox.png') no-repeat left center;
  background-size: 40px 40px;
  display: flex;
  align-items: center;
  padding-left: 48px;
  height: 60px;
  font-size:24px;
   
}
</style>

<style>
html,body{
    min-height: 100vh; 
    background-color: #210E59; 
}
</style>