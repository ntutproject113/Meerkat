<script setup>
import Menu from '../components/Menu.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import collectedImg from '../assets/images/icon/collected.png'
import uncollectedImg from '../assets/images/icon/uncollected.png'


const contests = ref([])      // 存比賽清單
const categoryMap = ref({})    //競賽卡片前的對應類別
const loading = ref(false)
const error = ref(null)


//收藏功能
const favorites = ref([])
const toggleFavorite = (index) => {
  favorites.value[index] = !favorites.value[index]
}

// 競賽資料 ---
const fetchContests = async () => {
  loading.value = true
  try {
    const res = await axios.get('http://localhost:8000/contests', {
      params: {
        page: filters.value.page,
        timeline: filters.value.timeline,
        location: filters.value.location,
        category: filters.value.category.join(',')  // 陣列轉字串
      }
    })
    contests.value = res.data.result
    favorites.value = contests.value.map(() => false) 
  } catch (e) {
    error.value = '載入失敗: ' + e.message
  } finally {
    loading.value = false
  }
}

// 取得分類資料（flat & map）
const fetchCategories = async () => {
  try {
    const flatRes = await axios.get('http://localhost:8000/categories', { params: { format: 'flat' } })
    categories.value = flatRes.data

    const mapRes = await axios.get('http://localhost:8000/categories', { params: { format: 'map' } })
    categoryMap.value = mapRes.data

  } catch (e) {
    console.error('載入分類失敗', e.message)
  }
}

// 取得名稱
function getCategoryNames(ids) {
  if (!Array.isArray(ids)) return []
  return ids.map(id => categoryMap.value[id]).filter(Boolean)
}



// 類別篩選相關
const categories = ref([])    // 存分類清單
const showCategoryModal = ref(false)
const filters = ref({ 
  page: 1, 
  timeline: 'notEnded', 
  location: 'taiwan', 
  category: [] 
})
const tempCategory = ref([])  
const selectedCategories = ref([])


const openCategoryModal = () => {
  tempCategory.value = [...filters.value.category]
  showCategoryModal.value = true
}
const closeCategoryModal = () => {
  showCategoryModal.value = false
}
const toggleCategory = (id) => {
  const idx = tempCategory.value.indexOf(id)
  if (idx > -1) {
    tempCategory.value.splice(idx, 1)
  } else {
    tempCategory.value.push(id)
  }
}
const confirmCategory = () => {
  filters.value.category = [...tempCategory.value]
  selectedCategories.value = [...tempCategory.value]
  closeCategoryModal()
}

onMounted(async () => {
   fetchCategories()
   fetchContests()
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
        <h1 class="title">推薦比賽資訊</h1>
        <div v-if="loading">載入中...</div>
        <div v-if="error">{{ error }}</div>

          <!-- 每一張比賽卡片 -->
        <div v-if="contests && contests.length">
          <div 
            v-for="(item, index) in contests" 
            :key="item.id || index"
            class="contest-wrapper"
          >
            <!-- 每一張比賽卡片 -->
            <div class="contest-card">
              <!-- 類別 -->
               
              <div  class="category-box">
                <span class="category-text" 
                v-for="name in getCategoryNames(item.categoryIds)" 
                 :key="name"> {{ name }}</span>
              </div>

              <!-- 資訊 -->
              <div class="contest-content">
                <h3 class="contest-title">{{ item.cpName }}</h3>
                <div class="contest-info">
                  <img src="../assets/images/icon/date.png" class="icon" alt="日期圖示" />
                  結束時間：{{ item.cpEndTime }}
                </div>
                <div class="contest-info">
                  主辦單位: {{ item.cpOrganizer }}
                </div>
              </div>
              <!--好像不用寫在這裡
                  <div class="contest-info">
                   <div>總獎金: {{ item.cpPrizeTop }}</div>
                  </div>
                  <div class="contest-info">
                  <a :href="item.url" target="_blank" class="link">
                    查看詳情
                  </a>
                </div>
                -->

              <!-- 收藏按鈕 -->
              <div class="favorite-box" @click="toggleFavorite(index)">
                <img 
                  :src="favorites[index] ? collectedImg : uncollectedImg"
                  class="favorite-btn"
                  alt="收藏按鈕"
                />
              </div>
            </div>

            <!-- 分隔線（最後一張不要） -->
            <img
              v-if="index !== contests.length - 1"
              src="../assets/images/renting/line.png"
              alt="分隔線"
              class="line"
            />
          </div>
        </div>

        <!-- 沒有資料的顯示 -->
        <div v-else-if="!loading">沒有資料</div>
      </div>


      <!-- 右邊篩選 -->
      <div class="search-block">
        <div class="search">
          <input class="search-input" type="text" placeholder="搜尋…" />
          <img src="../assets/images/icon/search.png" class="icon" alt="搜尋圖示" />
        </div>
        <div class="filter-container">
          <!-- 時間 -->
          <div class="filter-item">
            <label for="timeline">時間：</label>
            <select id="timeline" v-model="filters.timeline">
              <option value="notEnded">尚未結束</option>
              <option value="ended">已結束</option>
              <option value="all">全部</option>
            </select>
          </div>

          <!-- 地點 -->
          <div class="filter-item">
            <label for="location">地點：</label>
            <select id="location" v-model="filters.location">
              <option value="taiwan">台灣</option>
              <option value="japan">日本</option>
              <option value="global">全球</option>
            </select>
          </div>

          <!-- 類別 -->

          <!-- 比賽類別按鈕 -->
         <div class="filter-item">
            <button class="category-btn" @click="openCategoryModal">比賽類別</button>
            
            <!-- 顯示已選取類別 -->
            <div v-if="selectedCategories.length" class="selected-category-list">
              <span v-for="id in selectedCategories" :key="id" class="selected-category-tag">
                {{ categories.find(c => c.id === id)?.name }}
              </span>
            </div>

            <div v-if="showCategoryModal" class="modal-overlay" @click.self="closeCategoryModal">
              <div class="modal-content">
                <h3>選擇比賽類別</h3>
                <div class="modal-category-list">
                  <label v-for="cat in categories" :key="cat.id"
                        class="modal-category-item"
                        :class="{ selected: tempCategory.includes(cat.id) }"
                        @click="toggleCategory(cat.id)">
                    {{ cat.name }}
                  </label>
                </div>
                <div class="modal-actions">
                  <button class="confirm-btn" @click="confirmCategory">確定</button>
                  <button class="cancel-btn" @click="closeCategoryModal">取消</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 查詢按鈕 -->
          <div class="filter-actions">
            <button @click="fetchContests">查詢</button>
          </div>
        </div>
      </div>
      <img src="" alt="狐獴" class="meerkat"/>
       
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
.contest-card {
  display: flex;
  border: none;
  overflow: hidden;
  align-items: center;
  padding: 12px 0;
  
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


.contest-content {
  padding: 0 12px;
  flex: 1;
 }

.contest-title {
  font-weight: bold;
  color: #3B852B;
  margin: 0;
}
.contest-info {
  font-size: 14px;
  margin-top: 4px 0 0;
}
.icon {
  width: 20px;
  height: 20px;
  margin-right: 6px;
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
.category-box {
  height: 60px;
  flex: 0 0 60px;
  background: #d9d9d9;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.category-text {
  color: #3B852B;
  font-weight: bold;
  font-size: 16px;
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
.filter-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
  border: none;
  margin-bottom: 10px;
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
.selected-category-list {
  margin-top: 10px;
}
.selected-category-tag {
  display: inline-block;
  background: #e7e7e7;
  color: #3B852B;
  padding: 4px 8px;
  border-radius: 12px;
  margin-right: 6px;
  font-size: 14px;
}


</style>

<style>
html, body {
  height: 100%;
  overflow: hidden; /* 讓整頁不滾動 */
}
</style>

