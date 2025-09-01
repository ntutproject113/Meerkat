<script setup>
import Menu from '../components/Menu.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'

const loading = ref(false)
const error = ref(null)
const scholarships = ref([])
const count = ref(0)

// 篩選條件選項
const categories = ['急難救助', '才藝技藝', '資訊/研究計畫', '清寒助學']
const regions = ['北部', '中部', '南部', '東部', '全國']
const identities = ['低收入戶', '中低收入戶', '原住民', '身心障礙', '不拘']
const qualifications = ['清寒', '成績優良', '服務學習', '特殊境遇']
const sorts = [
  { value: '', label: '不排序' },
  { value: 'asc', label: '金額由小到大' },
  { value: 'desc', label: '金額由大到小' }
]

// 篩選條件狀態
const selectedCategory = ref('')
const selectedRegion = ref('')
const selectedIdentity = ref('')
const selectedQualification = ref('')
const selectedSort = ref('')

const getScholarships = async () => {
  loading.value = true
  try {
    const res = await axios.get('http://localhost:8000/scholarships', {
      params: {
        category: selectedCategory.value,
        region: selectedRegion.value,
        identity: selectedIdentity.value,
        qualification: selectedQualification.value,
        sort: selectedSort.value
      }
    })
    count.value = res.data.count
    scholarships.value = res.data.data
  } catch (error) {
    console.error('API 請求失敗', error)
    error.value = 'API 請求失敗：' + error.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  getScholarships()
})
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
        <h1 class="title">推薦獎學金資訊</h1>

        <div v-if="loading">載入中...</div>
          <div v-else-if="error">{{ error }}</div>
          <div v-else-if="scholarships.length">
            <div v-for="(item, index) in scholarships" :key="index">
              <div class="schol-card">
                <div class="schol-content">
                  <h3 class="schol-title">{{ item.ContentPlaceHolder1_divName }}</h3>
                  <div class="schol-info">
                    <img src="../assets/images/icon/comp.png" class="icon" alt="主辦單位" />
                    {{ item.institution || '未提供' }}
                  </div>
                   <div class="schol-info">
                    <img src="../assets/images/icon/money.png" class="icon" alt="金額" />
                    ${{ item.min_amount || '未提供' }} ~ ${{ item.max_amount || '未提供' }}元
                   </div>
                </div>
              </div>

        
          <img
            v-if="index !== scholarships.length - 1"
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
      
        <select v-model="selectedCategory">
            <option value="">全部類別</option>
            <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
          </select>

          <br/>
          <select v-model="selectedRegion">
            <option value="">全部地區</option>
            <option v-for="r in regions" :key="r" :value="r">{{ r }}</option>
          </select>

          <br/>
          <select v-model="selectedIdentity">
            <option value="">不限身分</option>
            <option v-for="i in identities" :key="i" :value="i">{{ i }}</option>
          </select>

          <br/>
          <select v-model="selectedQualification">
            <option value="">不限資格</option>
            <option v-for="q in qualifications" :key="q" :value="q">{{ q }}</option>
          </select>
          
          <br/>
          <select v-model="selectedSort">
            <option v-for="s in sorts" :key="s.value" :value="s.value">{{ s.label }}</option>
          </select>
         
          <br/>
          <button @click="getScholarships" class="btn">查詢</button>
        </div>
       
        
      </div>
      <img
        src=""
        alt="狐獴"
        class="meerkat"
      />
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
.schol-card {
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

.schol-content {
  padding: 12px;
  flex: 1;
}

.schol-title {
  font-weight: bold;
  color: #3B852B;
  margin-bottom: 6px;
}

.schol-info {
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
.search-block select {
  padding: 6px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
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
</style>
<style>
html, body {
  height: 100%;
  overflow: hidden; /* 讓整頁不滾動 */
}
</style>
