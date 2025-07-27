<script setup>
import Menu from '../components/Menu.vue'
import { ref } from 'vue'


// 後端傳入的資料格式（開發中可先放假資料）
const rentList = ref([
  {
    title: '中山區精選套房',
    type: '獨立套房',
    floor: '6F/7F',
    address: '中山區雙城街19巷',
    distance: '距中山國中站 320公尺',
    price: 10000,
    image: '../assets/images/renting/house1.jpg',
  }
])
</script>

<template>
  <div class="w-screen h-screen bg-white font-sans relative overflow-hidden">
    <Menu />
    <!-- Header -->
    <header class="flex items-center justify-between px-6 py-4 border-b border-black">
      <div class="flex justify-center items-center">
        <img src="../assets/images/renting/word.png" alt="佈告欄" class="inline-block mr-2" />
      </div>
      <div class="w-10 h-10 rounded-full overflow-hidden">
        
      </div>
    </header>

    <div class="flex">
      <!-- Left: 房屋清單 -->
      <div class="w-2/3 p-6">
        <h2 class="text-2xl font-bold mb-6">推薦租屋資訊</h2>

        <div v-for="(item, index) in rentList" :key="index" class="mb-6 border-b border-black pb-4 flex">
          <img :src="item.image" alt="房屋圖片" class="w-32 h-24 object-cover rounded-md mr-4" />
          <div class="flex-1">
            <h3 class="text-green-600 font-semibold">{{ item.title }}</h3>
            <p class="text-sm">{{ item.type }} | {{ item.floor }}</p>
            <p class="text-sm text-gray-600">{{ item.address }}</p>
            <p class="text-sm text-gray-600">{{ item.distance }}</p>
          </div>
          <div class="text-yellow-500 text-xl font-bold self-end whitespace-nowrap">
            {{ item.price }} 元/月
          </div>
        </div>
      </div>

      <!-- Right: 篩選條件 -->
      <div class="w-1/3 p-6 border-l border-black relative">
        <div class="flex items-center border border-black rounded-full px-4 py-1 mb-4">
          <input type="text" placeholder="搜尋…" class="flex-1 outline-none" />
          <span class="ml-2">🔍</span>
        </div>

        <div>
          <p class="font-bold mb-2">篩選條件</p>
          <ul class="space-y-2">
            <li>地區 ⌄</li>
            <li>價格 ⌄</li>
            <li>類型 ⌄</li>
            <li>其他條件 ⌄</li>
          </ul>
        </div>

        <!-- 插圖角色 -->
        <img src="../assets/images/renting/meerkat_Rent.png" alt="角色" class="absolute bottom-0 right-4 w-32" />
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
