<template>
  <div class="menu-container">
    <!-- 漢堡按鈕 -->
    <div class="menu-toggle" @click="toggleMenu">☰</div>

    <!-- 側邊選單 -->
    <div class="side-menu" :class="{ open: isOpen }">
      <router-link
        v-for="(item, index) in menuItems"
        :key="index"
        :to="item.link"
        class="menu-item"
        @click="closeMenu"
      >
        <img :src="item.img" :alt="item.name" class="menu-img" />
        <div class="menu-label">{{ item.name }}</div>
         <img src="../assets/images/menu/line.png" alt="divider" class="divider-img" />
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 展開選單
const isOpen = ref(false)
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

// 側邊欄選單資料
const menuItems = [
  { img: new URL('../assets/images/menu/home.png', import.meta.url).href, link:'/'},
  { img: new URL('../assets/images/menu/rent.png', import.meta.url).href },
  { img: new URL('../assets/images/menu/intern.png', import.meta.url).href },
  { img: new URL('../assets/images/menu/scholarship.png', import.meta.url).href },
  { img: new URL('../assets/images/menu/competition.png', import.meta.url).href },
  { img: new URL('../assets/images/menu/plan.png', import.meta.url).href ,link:'/planning' },
  { img: new URL('../assets/images/menu/login.png', import.meta.url).href }
]
</script>

<style scoped>
.menu-container {
  position: relative;
}

.menu-toggle {
  font-size: 32px;
  cursor: pointer;
  padding: 10px;
  z-index: 1001;
  position: fixed;
  top: 10px;
  left: 10px;
}

.side-menu {
  position: fixed;
  top: 0;
  left: -100%;
  width: 250px;
  height: 100vh;
  background-color: white;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.2);
  padding: 10px 10px;
  z-index: 1000;
  transition: left 0.3s ease-in-out;
  overflow-y: auto; 
  

  display: flex;
  flex-direction: column;
  justify-content: center; /* 垂直置中 */
  align-items: center; 
}

.side-menu.open {
  left: 0;
}

.menu-item {
  text-align: center; 
}

.menu-img {
  width: 40%;
  height: auto;
  margin-top:5px ;
  margin-bottom: 5px;
}

.menu-label {
  margin-top: 1px;
  font-size: 16px;
  font-family: 'Noto Serif TC', serif;
}
.divider-img {
  width: 70%;
  margin: -30px auto -30px;
  display: block;
  
}


</style>
