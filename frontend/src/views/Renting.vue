<script setup>
import Menu from '../components/Menu.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 綁定查詢參數（初始值與 API 預設一致）
const areaIds = ref('5-10-8-12-9-3-7-4-6-1-2-11')
const price = ref(15000)
const casetype = ref([])
const page = ref(1)
const fee = ref(true)

// 狀態與資料
const loading = ref(false)
const error = ref(null)
const rentList = ref([])
const totalCount = ref(0)

const fetchRents = async () => {
  loading.value = true
  error.value = null
  rentList.value = []
  try {
    const res = await axios.get('http://localhost:8000/rents', {
      params: {
        area_ids: areaIds.value,
        price: price.value,
        casetype: casetype.value,
        page: page.value,
        fee: fee.value
      }
    
    })
    totalCount.value = res.data.total_count
    rentList.value = res.data.result
  } catch (e) {
    error.value = '載入失敗: ' + (e.response?.data?.detail || e.message)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchRents()
})

const houseTypes = [
  { value: '0', label: '不限' },
  { value: '1', label: '整層住家' },
  { value: '2', label: '獨立套房' },
  { value: '3', label: '分租套房' },
  { value: '4', label: '雅房' },
]

</script>

<template>

  <img src="../assets/images/renting/background.png" class="bg-image" alt="背景">

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
        <div v-if="error">{{ error }}</div>
        
       <div v-if="rentList.length">
        <div v-for="(rent, index) in rentList" :key="index">
          <!-- 每一張租屋卡片 -->
          <div class="rent-card">
             <a :href="rent.rentHref" target="_blank">
                <img
                  v-if="rent.rentPictureHref"
                  :src="rent.rentPictureHref"
                  alt="房屋圖片"
                  class="image"
                />
              </a>
            <div class="rent-content">
              <h3 class="rent-title">{{ rent.rentName }}</h3>

              <div class="rent-info">
                <img src="../assets/images/icon/house.png" class="icon" alt="房屋類型" />
                {{ rent.rentType }} ｜{{ rent.houseType }}
              </div>

              <div class="rent-info">
                <img src="../assets/images/icon/location.png" class="icon" alt="地址圖示" />
                {{ rent.rentAddress }}
              </div>

              <div class="rent-info">
                <img src="../assets/images/icon/transport.png" class="icon" alt="捷運圖示" />
                <div v-for="(t, index) in rent.transportation" :key="index">
                    距{{ t.stationName }} {{ t.walkTime }}分鐘 </div>
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
          <input class="search-input" type="text" placeholder="輸入關鍵字…" />
          <img src="../assets/images/icon/search.png" class="icon" alt="搜尋圖示" />
        </div>
    <div class="form-block">
      <label>
        地區 :
        <input v-model="areaIds" class="input-field" />
      </label>
        <label for="price">價格上限：{{ price }} 元</label>
          <input 
            type="range" 
            id="price" 
            v-model="price" 
            min="5000" 
            max="50000" 
            step="1000" 
            class="range-slider"
          />
        <p>房型類別：</p>
        <div class="checkbox-group">
          <label v-for="type in houseTypes" :key="type.value">
            <input 
              type="checkbox" 
              :value="type.value" 
              v-model="casetype"
            /> {{ type.label }}
          </label>
        </div>
      <label>
        頁碼:
        <input v-model.number="page" type="number" class="mini-input" />
      </label>
      <label>
        包含管理費:<input type="checkbox" v-model="fee" />
      </label>
      
      <button @click="fetchRents" class="btn">
        查詢
      </button>
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
.bg-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  object-fit: fill;   /* 確保整張圖顯示 */
  pointer-events: none;
  z-index:0;
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
  height:92%;      
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
.image {
  width: 150px;
  height: 150px;   
  object-fit: cover;     
  display: block;
  border-bottom: 1px solid #ddd;
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
  padding-bottom: 4px;
}

.rent-price {
  color: #f59e0b; /* 相當於 text-yellow-500 */
  font-weight: bold;
  font-size: 24px;
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
  width: 250px;
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
  background-size:40px 75%; 
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
/* 篩選區 */
.form-block {
  margin-bottom: 16px;       
  display: flex;
  flex-direction: column;
  gap: 8px;               
}
.mini-input {
  width: 80px;
  padding: 4px 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
.input-field {
  border: 1px solid #ccc;
  padding: 4px 8px;         
  border-radius: 6px;         
  width: 256px;             
  font-size: 14px;
}
.range-slider {
  width: 80%;
  -webkit-appearance: none; /* 移除預設樣式 */
  appearance: none;
  height: 6px;
  background: #ccc;
  border-radius: 3px;
  outline: none;
}
.range-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: green; /* 綠色 */
  cursor: pointer;
  border: none;
}
p {
  margin-bottom: 2px; 
}
.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 1px;
  font-size: 14px;
}
.btn {
  background-color: #3B852B; 
  color: white;
  padding: 8px 16px;        
  border-radius: 6px;        
  border: none;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.btn:hover {
  background-color: #78d663;
}
input[type="checkbox"] {
  appearance: none; /* 移除預設樣式 */
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 16px;
  height: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  position: relative;
}

/* 勾選狀態 */
input[type="checkbox"]:checked {
  background-color: green;
}

input[type="checkbox"]:checked::after {
  content: "✔";
  color: white;
  font-size: 12px;
  position: absolute;
  top: -2px;
  left: 3px;
}



</style>
<style>
html, body {
  height: 100%;
  overflow: hidden; /* 讓整頁不滾動 */
}
</style>
