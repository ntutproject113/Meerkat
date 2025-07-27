<script setup>
import Menu from '../components/Menu.vue'
import { ref,onMounted } from 'vue'
import axios from 'axios'


// 後端傳入的資料格式（
const rentList = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
  loading.value = true
  try {
    const res = await axios.get('http://localhost:8000/rents')
    rentList.value = res.data
  } catch (e) {
    error.value = '載入失敗: ' + e.message
  } finally {
    loading.value = false
  }
})
const bgImage = new URL('../assets/images/renting/background.png', import.meta.url).href
</script>

<template> 
  <div
  class="w-screen h-screen bg-center bg-no-repeat bg-[length:100%_100%] absolute top-0 left-0 bg-fixed -z-10"
  :style="{ backgroundImage: `url(${bgImage})` }">
    <Menu />
    <!-- 標頭 -->
    <header class="flex items-center justify-between px-6 py-4 border-b border-black">
      <div class="flex items-center">
        <img src="../assets/images/renting/word.png" alt="佈告欄" class="inline-block mr-2 w-6 h-auto" />
        <h1 class="text-lg font-bold">租屋佈告欄</h1>
      </div>
      <div class="w-10 h-10 rounded-full overflow-hidden">
        
      </div>
    </header>
    <div class="flex flex-1 overflow-hidden">
    <!--租屋資訊-->
    <div class="w-2/3 p-6 overflow-y-auto">
     <div v-if="loading">載入中...</div>
    <div v-if="error" style="color:red;">{{ error }}</div>

    <ul v-if="rentList.length">
      <li v-for="(rent, index) in rentList" :key="index">
        <strong>{{ rent.rentName }}</strong> 
        <div>{{ rent.rentType }} </div>
        <div>{{ rent.houseType }} </div>
        <div>價格：{{ rent.rentPrice }} 元</div>
      </li>
    </ul>

    <div v-else-if="!loading">沒有資料</div>
    </div>
    
      <!-- Right: 篩選 -->
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
         <!-- 狐獴-->
        <img
          src="../assets/images/renting/meerkat_Rent.png"
          alt="狐獴"
          class="absolute bottom-0 right-4 w-4 md:w-8 h-auto"
        />
        </div>
        </div>

    </div>
</template>

<style scoped>
</style>
