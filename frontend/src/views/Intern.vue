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
    jobs.value = res.data.jobs
  } catch (e) {
    error.value = '載入失敗：' + e.message
  } finally {
    loading.value = false
  }
}

// 初始化時載入資料
onMounted(fetchJobs)

//收藏功能
const favorites = ref([])
const toggleFavorite = (index) => {
  favorites.value[index] = !favorites.value[index]
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
              <div class="favorite-box" @click="toggleFavorite(index)">
                <img 
                  :src="favorites[index] ? collectedImg : uncollectedImg"
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
        <div class="search">
          <input class="search-input" type="text" placeholder="搜尋…" />
          <img src="../assets/images/icon/search.png" class="icon" alt="搜尋圖示" />
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
        src=""
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
.job-card {
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

