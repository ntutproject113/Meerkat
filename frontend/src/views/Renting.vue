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
      <img src="../assets/images/renting/word.png" alt="布告欄˙" class="word"/>
    
    </header>

    <!-- 主內容 -->
    <div class="flex flex-1 w-full mt-4">
    
      <!-- 左邊列表 -->

      <div class="w-2/3 pr-4 space-y-4 overflow-y-auto">
        <h1 class="title">推薦租屋資訊</h1>
        <div v-if="loading">載入中...</div>
        <div v-if="error" class="text-red-600">{{ error }}</div>
        
       <div v-if="rentList.length">
        <div v-for="(rent, index) in rentList" :key="index">
          <!-- 每一張租屋卡片 -->
          <div class="rent-card">
            <img :src="rent.image || '../assets/images/default-room.jpg'" alt="房屋照片" class="rent-image" />

            <div class="rent-content">
              <h3 class="rent-title">{{ rent.rentName }}</h3>

              <div class="rent-info">
                <img src="../assets/images/renting/name.png" class="icon" alt="房屋類型" />
                {{ rent.rentType }} ｜{{ rent.houseType }}
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

          <!-- ✅ 分隔線：不是最後一張時顯示 -->
          <img
            v-if="index !== rentList.length - 1"
            src="../assets/images/renting/line.png"
            alt="分隔線"
            class="line"
          />
        </div>
      </div>


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
        class="meerkat"
      />
    </div>
  </div>
</template>

<style scoped>
.word {
  width: 150px;
  height: auto;
  margin: 0 auto;
}
.title{
  font-size: 32px;
  font-weight: bold;
  color: #000000;
  margin-bottom: 16px;
  text-align: center;
}
.rent-card {
  position: relative;
  display: flex;
  border: none;
  overflow: hidden;
  margin-bottom: -5px;
  
}
.line {
  display: block;
  width:700px;
  height: 30%; /* 根據你的圖實際高度調整 */
  object-fit: contain;
  margin-left:auto;
  margin-right: auto;
  pointer-events: none;
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
.meerkat{
  position: fixed;
  bottom:0%;
  right: 2%;
  width: 350px;
  height: auto;
  z-index: 20;
}

</style>
