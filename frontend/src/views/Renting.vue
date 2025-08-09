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

  <div class="fullscreen-background"></div>

  <div class="layout-container">
    <Menu />

    <!-- 標題區 -->
    <header class="header">
      <div class="header-border">
        <img src="../assets/images/renting/word.png" alt="布告欄˙" class="word"/>
      </div>
    </header>

    <!-- 主內容 -->
    <div class="block">
    
      <!-- 左邊列表 -->

      <div class="data-block">
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
      <div class="search-block">
        <div class="search">
          <input class="search-input" type="text" placeholder="搜尋…" />
          <img src="../assets/images/renting/search.png" class="icon" alt="搜尋圖示" />
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
.fullscreen-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-image: url('../assets/images/renting/background.png');
  background-size: cover;     
  background-position: center;  
  background-repeat: no-repeat; 
  z-index: -1;                 
}
.layout-container {
  position: relative;           
  display: flex;                 
  flex-direction: column;       
  align-items: center;           
  justify-content: flex-start;   
  min-height: 100vh;              
  width: 90%;   
  height:100vh;               
  max-width: 72rem;              
  margin-left: auto;              
  margin-right: auto;
  padding-left: 1rem;             
  padding-right: 1rem;
  overflow: hidden;
}
.header {
  display: flex;                  
  align-items: center;             
  justify-content: space-between;  
  padding-left: 1.5rem;           
  padding-right: 1.5rem;
  padding-top: 0.5rem;               
  padding-bottom: 0.5rem;
  border-bottom: none;  
  width: 100%;     
}     
.header-border {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 1.5rem;
  width: 100%;
  background-image: url('../assets/images/renting/Header.png'); 
  background-repeat: no-repeat;
  background-position: bottom left;
  background-size: 100% auto;
}          
.word {
  width: 150px;
  height: auto;
  margin: 1% auto 1% auto;    
}
.block{
  display: flex;          
  flex: 1 1 0%;           
  width: 100%;            
  margin-top: 1rem; 
  height: calc(100vh - 100px); 
  overflow: hidden;      
}
.data-block {
  width: 70%;   
  height:100%;      
  padding-right: 1rem;    
  overflow-y: auto;        
  display: flex;
  flex-direction: column;
  gap: 1rem;   
}
.title{
  font-size: 32px;
  font-weight: bold;
  color: #000000;
  margin:0px auto;
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
  width:100%;
  max-width:800px;
  height:auto;
  margin:-70px auto;
  object-fit: contain;
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
  width: 20px;
  height: 20px;
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
.search-block{
  width: 30%;
  padding-left: 2rem;
  min-height:500px;
  background-image: url('../assets/images/renting/right.png'); 
  background-repeat: no-repeat;
  background-position: left top;  /* 對齊左上角 */
  background-size:40px 80%; 
  position: relative;
}
.search{
  display: flex;
  align-items: center;
  border: 3px solid black;
  border-radius: 9999px; 
  padding-left: 1rem;  
  padding-right: 1rem;
  padding-top: 0.5rem; 
  padding-bottom: 0.5rem;
  margin-bottom: 1rem; 
}
.search-input{
  flex: 1;
  outline: none;
  background-color: transparent; 
  border: none;
  font-size: 16px; 
}

</style>
<style>
html, body {
  height: 100%;
  overflow: hidden; /* 讓整頁不滾動 */
}
</style>
