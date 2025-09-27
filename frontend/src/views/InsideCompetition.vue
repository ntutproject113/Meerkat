<script setup>
import Menu from '../components/Menu.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
function goBack() {
  router.back() 
}
</script>
<template>
     <div>
        <img src="../assets/images/renting/background.png" class="bg-image" alt="背景">
        <img
              src="../assets/images/plan/arrow.png"
              class="back-arrow"
              alt="Back"
              @click="goBack"
          />
      </div>
  <div class="layout-container">
    <Menu />
    <header class="header">
      <div class="header-border">
        <img src="../assets/images/renting/word.png" alt="布告欄˙" class="word"/>
      </div>
    </header>

    <!-- 主內容 -->
    <div class="block">
        <div class="data-block">
      <!-- 左側：比賽資訊 -->
      <section class="card">
        <h2 class="contest-title">全國大專程式設計競賽</h2>
        <p class="info"><strong>比賽類型：</strong>程式設計 / 科技競賽</p>
        <p class="info"><strong>地區：</strong>全國</p>
        <p class="info"><strong>報名期間：</strong>2025/10/01 ~ 2025/11/15</p>
      
        <u>報名連結</u>

        <h3 class="section-title">比賽說明</h3>
        <div class="box">
          <p>
            本競賽旨在提升大專學生程式設計能力，促進跨校交流與團隊合作，
            初賽為線上測驗，決賽於台北舉辦，設有豐富獎金。
          </p>
        </div>
        <h3 class="section-title">相關簡章</h3>
        <div class="box">
          <u> 競賽完整簡章</u>
        </div>

        <h3 class="section-title">參賽資格</h3>
        <div class="box">
          <p>
            全國大專院校在學學生皆可組隊參加，每隊至多 3 人。
          </p>
        </div>
      </section>

      <!-- 右側：補充資訊 -->
      <div>
        <div class="side-card">
          <h3>主辦單位</h3>
          <p>教育部資訊及科技教育司</p>
        </div>

       
      </div>
    </div>
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
  width: 80%;   
  height:400px;      
  padding-left: 6rem;    
  overflow-y: auto;        
  display: flex;
  flex-direction: column;
  gap: 1rem;  
}

.card {
  background: #fff;
  padding:  0px 10px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.contest-title {
  font-size: 22px;
  font-weight: bold;
  color: #3b852b;
  margin-bottom: 10px;
}
.info {
  margin: 5px 0;
}
.section-title {
  font-weight: bold;
  margin: 15px 0 8px;
}
.box {
  background: #eee;
  padding: 15px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.6;
}

/* 右側 */
.side-card {
  background: #fff;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  margin-bottom: 20px;
  font-size: 14px;
  line-height: 1.6;
}
.side-card h3 {
  margin: 5px 0;
  font-size: 16px;
  font-weight: bold;
}
.date {
  font-size: 12px;
  color: #888;
  text-align: right;
}
.back-arrow {
  position: fixed;
  top: 0;
  left: 60%;
  transform: translate(-470px, 50px); /* 1000px/2 - 25px/2，根據 .bg-image 寬度調整 */
  width: 25px;
  height: 25px;
  cursor: pointer;
  z-index: 10;
}
</style>