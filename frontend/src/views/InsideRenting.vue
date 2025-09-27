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
        <img src="../assets/images/renting/word.png" alt="租屋資訊" class="word"/>
      </div>
    </header>

    <!-- 主內容 -->
    <div class="block">
      <div class="data-block">
        <!-- Left: 租屋資訊 -->
        <section class="rent-card">
          <h2 class="rent-title">
            🏠 台北市中正區 溫馨小套房
          </h2>
          <p class="landlord">房東：王先生</p>
          <p class="landlord">聯絡方式：0912-345-678</p>
          <p>📍 距離台大醫院捷運站 5 分鐘</p>
          <p class="price">💰 租金：12,000 元/月</p>
          <u>看更多 </u>
          <h3 class="section-title">房屋特色</h3>
          <div class="rent-content">
            <ul>
              <li>室內 25 坪，採光佳，通風好</li>
              <li>家具齊全（床、衣櫃、冷氣、沙發）</li>
              <li>大樓有管理員，環境安全</li>
              <li>提供網路，租金含管理費</li>
            </ul>
          </div>

          <h3 class="section-title">租屋條件</h3>
          <div class="rent-conditions">
            <div class="row">
              <span>押金：</span>
              <span>2個月</span>
            </div>
             <div class="row">
              <span>最短租期：</span>
              <span>一年</span>
            </div>
             <div class="row">
              <span>開伙：</span>
              <span>❎</span>
            </div>
             <div class="row">
              <span>寵物：</span>
              <span>❎</span>
            </div>
            <div class="row">
              <span>洗衣機：</span>
              <span>✅</span>
            </div>
            <div class="row">
              <span>冰箱：</span>
              <span>✅</span>
            </div>
            <div class="row">
              <span>網路：</span>
              <span>✅</span>
            </div>
            <div class="row">
              <span>對外窗：</span>
              <span>✅</span>
            </div>

          </div>
        </section>
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
  padding: 0.5rem 1.5rem;
  width: 100%;     
}     
.header-border {
  display: flex;
  align-items: center;
  justify-content: center;
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
  margin: 1% auto;    
}
.block {
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

/* Left Rent Card */
.rent-card {
  background: #fff;
  padding:  0px 10px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.rent-title {
  font-size: 22px;
  font-weight: bold;
  color: #3B852B;
}
.landlord {
  margin: 5px 0;
  color: #555;
}
.price {
  font-weight: bold;
  margin-bottom: 15px;
}
.section-title {
  font-weight: bold;
  margin: 15px 0 8px;
}
.rent-content,
.rent-conditions {
  background: #eee;
  padding: 15px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.6;
}

/* Right Side Cards */
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
.row {
  display: flex;
  padding: 4px 0;
}
.row span:first-child {
  font-weight: bold;
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
