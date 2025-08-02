<script setup>
import Menu from '../components/Menu.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

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
</script>

<template>


  <div class="fixed top-0 left-0 w-screen h-screen bg-no-repeat bg-cover bg-center pointer-events-none -z-10"
    style="background-image: url('../assets/images/background.png');"></div>

  <div class="relative flex flex-col items-center justify-start min-h-screen w-full max-w-6xl mx-auto px-4">
    <Menu />

    <!-- 標題區 -->
    <header class="flex items-center justify-between px-6 py-4 border-b border-black w-full">
      <h1 class="text-xl font-bold">推薦租屋資訊</h1>
      <img src="../assets/images/renting/avatar.png" alt="使用者" class="w-10 h-10 rounded-full" />
    </header>

    <!-- 主內容 -->
    <div class="flex flex-1 w-full mt-4">
      <!-- 左邊列表 -->
      <div class="w-2/3 pr-4 space-y-4 overflow-y-auto">
        <div v-if="loading">載入中...</div>
        <div v-if="error" class="text-red-600">{{ error }}</div>
        
        <template v-if="rentList.length">
          <div
            v-for="(rent, index) in rentList"
            :key="index"
            class="rent-card"
          >
            <img :src="rent.image || '../assets/images/default-room.jpg'" alt="房屋照片" class="rent-image" />

            <div class="rent-content">
              <h3 class="rent-title">{{ rent.rentName }}</h3>

              <div class="rent-info">
                <img src="../assets/images/renting/name.png" class="icon" alt="房屋類型" />
                {{ rent.rentType }} ｜{{ rent.houseType}}
              </div>

              <div class="rent-info">
                <img src="../assets/images/renting/location.png" class="icon" alt="地址圖示" />
                {{ rent.rentAdress }}
              </div>

              <div class="rent-info">
                <img src="../assets/images/renting/transport.png" class="icon" alt="捷運圖示" />
                距{{ rent.transportation }} {{ rent.distance }}公尺
              </div>
            </div>

            <div class="rent-price-wrapper">
              <p class="rent-price">
                {{ rent.rentPrice.toLocaleString() }}
                <span class="price-unit">元/月</span>
              </p>
            </div>
          </div>
        </template>

        <div v-else-if="!loading">沒有資料</div>
      </div>

      <!-- 右邊篩選 -->
      <div class="w-1/3 pl-4 border-l border-black relative">
        <div class="flex items-center border border-black rounded-full px-4 py-2 mb-4">
          <input type="text" placeholder="搜尋…" class="flex-1 outline-none bg-transparent" />
          <span class="ml-2">🔍</span>
        </div>
        <div>
          <p class="font-bold mb-2">篩選條件</p>
          <ul class="space-y-3 text-sm font-medium">
            <li class="cursor-pointer hover:underline">地區 ⌄</li>
            <li class="cursor-pointer hover:underline">價格 ⌄</li>
            <li class="cursor-pointer hover:underline">類型 ⌄</li>
            <li class="cursor-pointer hover:underline">其他條件 ⌄</li>
          </ul>
        </div>
      </div>
      <img
        src="../assets/images/renting/meerkat_Rent.png"
        alt="狐獴"
        class="fixed bottom-0 right-4 w-10 md:w-16 h-auto z-20"
      />
    </div>
  </div>
</template>

<style scoped>
.rent-card {
  display: flex;
  border: 1px solid black;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  margin-bottom: 16px;
}

.rent-image {
  width: 144px;  
  height: 112px; 
  object-fit: cover;
}

.rent-content {
  padding: 12px;
  flex: 1;
}

.rent-title {
  font-weight: bold;
  color: #3B852B;
  margin-bottom: 6px;
}

.rent-info {
  display: flex;
  align-items: center;
  font-size: 14px;
  margin-top: 4px;
}

.icon {
  width: 16px;
  height: 16px;
  margin-right: 6px;
  object-fit: contain;
}

.rent-price-wrapper {
  display: flex;
  align-items: flex-end;
  padding-right: 16px;
  padding-bottom: 8px;
}

.rent-price {
  color: #f59e0b; /* 相當於 text-yellow-500 */
  font-weight: bold;
  font-size: 18px;
}

.price-unit {
  color: black;
  font-size: 14px;
  margin-left: 4px;
}

</style>
