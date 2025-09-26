<script setup>
import Menu from '../components/Menu.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import collectedImg from '../assets/images/icon/collected.png'
import uncollectedImg from '../assets/images/icon/uncollected.png'
const jobs = ref([])
const loading = ref(false)
const error = ref(null)

// 篩選條件
const filters = ref({
  keyword: '實習',    // 預設關鍵字
  page: 1,            // 頁碼
  asc: 0,             // 降冪
  order: 12,          // 排序方式
  edu: 4,             // 學歷限制
  area: '6001000000', // 工作地區
  jobcat: ''          // 職務分類，可選
})

// 取得工作資料
const fetchJobs = async () => {
  loading.value = true
  try {
    const res = await axios.get('http://localhost:8000/jobs', {
      params: filters.value
    })
     jobs.value = res.data.jobs.map(job => ({
      ...job,
      isFavorite: false   // 預設沒收藏
    }))
  } catch (e) {
    error.value = '載入失敗：' + e.message
  } finally {
    loading.value = false
  }
}
// 抓取地區 / 職務 map
const loadMaps = async () => {
  const resAreas = await axios.get('http://localhost:8000/map/areas')
  const resJobcats = await axios.get('http://localhost:8000/map/jobcats')
  areas.value = resAreas.data
  jobcats.value = resJobcats.data
}

// 清除篩選條件
const resetFilters = () => {
  filters.value = {
    keyword: '',
    page: 1,
    asc: 0,
    order: 12,
    edu: '',
    area: '',
    jobcat: ''
  }
  fetchJobs()
}

// 初始化
onMounted(() => {
  loadMaps()
  fetchJobs()
})
//收藏功能
const favorites = ref([])
const toggleFavorite = (job) => {
  job.isFavorite = !job.isFavorite
}
</script>

<template>
     <img src="../assets/images/renting/background.png" class="bg-image" alt="背景">

        <div class="layout-container">
            <Menu class="page-menu" />

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
        <h1 class="title">推薦實習資訊</h1>
        <div v-if="loading">載入中...</div>
        <div v-if="error">{{ error }}</div>

       <div v-if="jobs.length">
        <div v-for="job in jobs" :key="job.jobNo">
          <!-- 每一張實習卡片 -->
          <div class="job-card">

            <div class="job-content">
              <h3 class="job-title">{{job.jobName}}</h3>

              <div class="job-info">
                <img src="../assets/images/icon/comp.png" class="icon" alt="公司" />
                {{ job.custName }} <!--公司名稱-->
              </div>

              <div class="job-info">
                <img src="../assets/images/icon/location.png" class="icon" alt="地點" />
                {{ job.jobAddrNoDesc}} <!--工作地點-->
              </div>

              <div class="job-info">
                <img src="../assets/images/icon/money.png" class="icon" alt="薪資" />
                {{ job.salaryLow }} 元以上
              </div>
            </div>
             <!-- 收藏按鈕 -->
              <div class="favorite-box" @click="toggleFavorite(job)">
                <img 
                  :src="job.isFavorite ? collectedImg : uncollectedImg"
                  class="favorite-btn"
                  alt="收藏按鈕"
                />
              </div>
            </div>

          <img
            v-if="index !== jobs.length - 1"
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

        <div class="filters">
         
          <select id="area">
            <option value="">選擇地區</option>
          </select>
          <select id="jobcat">
            <option value="">選擇職務</option>
          </select>
          <select id="edu">
            <option value="">不限學歷</option>
            <option value="2">高中以上</option>
            <option value="3">專科以上</option>
            <option value="4">大學以上</option>
          </select>
        </div>

        <!-- 按鈕 -->
        <div class="buttons">
          <button class="search" onclick="fetchJobs()">查詢</button>
          <button class="reset" onclick="resetFilters()">清除條件</button>
        </div>

        <!-- 結果 -->
        <div id="results" class="job-list"></div>

        
      </div>
      <img
        src="../assets/images/renting/meerkat_Intern.png"
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
  padding-top: 0;   
  overflow-y: auto;        
  display: flex;
  flex-direction: column;
  gap: 1rem;  
}
.title{
  font-size: 32px;
  font-weight: bold;
  color: #000000;
  margin:-10px auto;
  text-align: center;
}
.job-card {
  position: relative;
  display: flex;
  border: none;
  overflow: hidden;
  margin-bottom: -5px;
  margin-top:-15px;
}
.line {
  display: block;
  width:100%;
  max-width:800px;
  height:auto;
  margin:10px auto;
  object-fit: contain;
  pointer-events: none;
}
.job-content {
  padding: 12px;
  flex: 1;
}

.job-title {
  font-weight: bold;
  color: #3B852B;
  margin-bottom: 6px;
}

.job-info {
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
.favorite-box {
  flex: 0 0 50px;           
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.favorite-btn {
  width:70px;
  height:70px;
  cursor: pointer;
  transition: transform 0.1s;
}
.meerkat{
  position: fixed;
  bottom:0%;
  right: 0%;
  width: 300px;
  height: auto;
  z-index: 20;
}
.search-block{
  width: 20%;
  padding-right: 2rem;
  min-height:500px;
  position: relative;
}
    .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 20px;
    }
    .filters select,
    .filters input {
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 6px;
      min-width: 150px;
    }
    .buttons {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }
    .buttons button {
      padding: 8px 16px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
    }
    .buttons .search {
      background-color: #3B852B;
      color: white;
    }
    .buttons .search:hover {
      background-color: #78d663;
    }
    .buttons .reset {
      background-color: #bdc3c7;
      color: black;
    }
    .buttons .reset:hover {
      background-color: #95a5a6;
    }
    .job-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }


</style>
<style>
html, body {
  height: 100%;
  overflow: hidden; /* 讓整頁不滾動 */
}
</style>

