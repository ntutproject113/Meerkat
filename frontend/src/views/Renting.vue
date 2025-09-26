<script setup>
import Menu from '../components/Menu.vue'
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

// 綁定查詢參數（初始值與 API 預設一致）

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
        area_ids:  filters.value.area,
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

const showModal = ref(false)
//篩選
const filters = ref({
  city: [],   // 選中的縣市 cityNumber
  area: []    // 選中的區域 sid
})
const cities = ref([])
const areas = ref([])

// 已選項目
const selectedCities = ref([])
const selectedAreas = ref([])

// 暫存選擇（避免取消直接改到已選項目）
const tempCities = ref([])
const tempAreas = ref([])

const showLocationModal = ref(false)

const openLocationModal = () => {
  tempCities.value = [...filters.value.city]
  tempAreas.value = [...filters.value.area]
  showLocationModal.value = true
}
const closeLocationModal = () => {
  showLocationModal.value = false
}

// 切換選擇
const toggleCity = (id) => {
  if (tempCities.value.includes(id)) {
    tempCities.value = tempCities.value.filter(c => c !== id)
  } else {
    tempCities.value.push(id)
  }
}

const toggleArea = (id) => {
  if (id === '') {
    tempAreas.value = [''] // 不限選項，清除其他
    return
  }
  tempAreas.value = tempAreas.value.filter(a => a !== '') // 移除不限
  if (tempAreas.value.includes(id)) {
    tempAreas.value = tempAreas.value.filter(a => a !== id)
  } else {
    tempAreas.value.push(id)
  }
}

// 確認
const confirmLocation = () => {
  filters.value.city = [...tempCities.value]
  filters.value.area = [...tempAreas.value]
  selectedCities.value = [...tempCities.value]
  selectedAreas.value = [...tempAreas.value]
  closeLocationModal()
}
// 取得全部縣市
async function fetchCities() {
  const res = await axios.get('http://localhost:8000/areas/tree')
  cities.value = res.data
}

// 根據縣市取得該縣市的區域
async function fetchAreas(cityNumber) {
  if (!cityNumber) {
    areas.value = []
    return
  }
  const city = cities.value.find(c => c.cityNumber === cityNumber)
  areas.value = city ? city.areaList : []
}

// 當縣市變動時重新抓取區域
watch(() => filters.value.city, (newCity) => {
  fetchAreas(newCity)
})

onMounted(() => {
  fetchCities()
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
    
            <div class="form-block">
              <!-- 地區與區域篩選 -->
              <div class="filter-item">
                <button class="category-btn" @click="openLocationModal">地區篩選</button>
                
                <!-- 顯示已選取的區域 -->
                <div v-if="selectedAreas.length" class="selected-category-list">
                  <span v-for="id in selectedAreas" :key="id" class="selected-category-tag">
                    {{ allAreas.find(a => a.sid === id)?.areaName }}
                  </span>
                </div>

                <!-- Modal -->
                <div v-if="showLocationModal" class="modal-overlay" @click.self="closeLocationModal">
                  <div class="modal-content">
                    <h3>選擇地區與區域</h3>
                    
                    <!-- 顯示縣市與區域 -->
                    <div v-for="city in cities" :key="city.cityNumber" class="city-block">
                      <h4>{{ city.cityName }}</h4>
                      <div class="modal-category-list">
                        <label
                          v-for="area in city.areas"
                          :key="area.sid"
                          class="modal-category-item"
                          :class="{ selected: tempAreas.includes(area.sid) }"
                          @click="toggleArea(area.sid)"
                        >
                          {{ area.areaName }}
                        </label>
                        <!-- 加上不限 -->
                        <label
                          class="modal-category-item"
                          :class="{ selected: tempAreas.includes(`${city.cityNumber}-不限`) }"
                          @click="toggleArea(`${city.cityNumber}-不限`)"
                        >
                          不限
                        </label>
                      </div>
                    </div>

                    <!-- 按鈕 -->
                    <div class="modal-actions">
                      <button class="confirm-btn" @click="confirmLocation">確定</button>
                      <button class="cancel-btn" @click="closeLocationModal">取消</button>
                    </div>
                  </div>
                </div>
              </div>


        

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
  left: 50%;
  transform: translateX(-50%);
  width: 1000px;         
  height: 100vh;         
  object-fit: contain;
  pointer-events: none;
  z-index: 0;
}
.layout-container {
  position: relative;           
  display: flex;                 
  flex-direction: column;       
  align-items: center;           
  justify-content: flex-start;   
  min-height: 100vh;              
  width: 900px;                
  max-width: 100vw;              
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
  padding: 1rem 1rem;
  width: 100%;
  background-image: url('../assets/images/renting/Header.png'); 
  background-repeat: no-repeat;
  background-position: bottom center;
  background-size: 80% auto;
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
  margin-top: 0.5rem; 
  height: calc(100vh - 100px);       
}
.data-block {
  width: 60%;   
  height:400px;      
  padding-left: 5.7rem;    
  overflow-y: auto;        
  display: flex;
  flex-direction: column;
  gap: 1rem;  
}
/*相關租屋資訊的字*/
.title{ 
  font-size: 32px;
  font-weight: bold;
  color: #000000;
  margin:-8px auto;
  text-align: center;
}
.rent-card {
  position: relative;
  display: flex;
  border: none;
  overflow: hidden;
  margin-bottom: -5px;
  margin-top: -5px;
}
.image {
  width: 150px;
  height: 150px;   
  object-fit: cover;     
  display: block;
  border-bottom: 1px solid #ddd;
}

/* 分隔線 */
.line {
  display: block;
  width:100%;
  max-width:800px;
  height:auto;
  margin:20px auto;
  object-fit: contain;
  pointer-events: none;
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
  width: 20%;
  padding-right: 2rem;
  min-height:500px;
  position: relative;
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
  padding: 6px 8px;        
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
.filter-item {
  display: flex;
  flex-direction: column;
  min-width: 150px;
}
.filter-item label {
  font-size: 14px;
  margin-bottom: 4px;
}
.filter-item select,
.filter-item input {
  padding: 6px 8px;
  font-size: 14px;
  border: 1px solid #aaa;
  border-radius: 4px;
}

.filter-actions button {
  background-color: #3B852B; 
  color: white;
  padding: 8px 16px;        
  border-radius: 6px;        
  border: none;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}
.filter-actions button:hover {
  background-color: #78d663;
}

/* Modal 樣式 */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
}
.modal-content {
  background: #fff;
  padding: 24px 32px;
  border-radius: 12px;
  min-width: 260px;
  max-height: 80vh;
  overflow-y: auto;
}
.modal-category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin: 16px 0;
  }

.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.category-btn {
  padding: 8px 12px;
  background-color: #ffffff;
  color: #3B852B;
  border: solid 2px #3B852B;
  border-radius: 6px;
  cursor: pointer;
}

.selected-categories{
  margin-top: 8px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  font-size: 14px;
}
.modal-category-item{
  min-width: 80px;
  padding: 10px 18px;
  border: 2px solid #3B852B;
  border-radius: 8px;
  background: #fff;
  color: #3B852B;
  font-weight: bold;
  font-size: 15px;
  text-align: center;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border 0.2s;
  user-select: none;
}
.modal-category-item.selected {
  background: #3B852B;
  color: #fff;
  border: 2px solid #3B852B;
}
.confirm-btn{
  padding: 8px 12px;
  background-color: #3B852B;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.cancel-btn{
  padding: 8px 12px;
  background-color: #bababa;
  color: #000000;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}



</style>
<style>
html, body {
  height: 100%;
  margin: 0;

}

</style>
