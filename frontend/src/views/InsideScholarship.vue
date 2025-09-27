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
          <!-- Left: Scholarship Info -->
          <section class="scholarship-card">
            <h2 class="scholarship-title">
              🎓 青年清寒助學金
            </h2>
            <p class="org">主辦單位：教育部</p>
            <p class="amount">💰 獎學金金額：每學期 20,000 元</p>

            <h3 class="section-title">獎學金類別</h3>
            <div class="scholarship-content">
              <p>清寒助學金</p>
            </div>

            <h3 class="section-title">身分別</h3>
            <div class="scholarship-content">
              <p>大專院校學生、研究所學生</p>
            </div>

            <h3 class="section-title">地區</h3>
            <div class="scholarship-content">
              <p>全國皆可申請</p>
            </div>

            <h3 class="section-title">申請資格</h3>
            <div class="scholarship-conditions">
              <ul>
                <li>設籍於中華民國，具學生身份。</li>
                <li>家庭年所得低於 100 萬。</li>
                <li>前一學期學業成績平均達 70 分以上。</li>
                <li>未同時領取其他政府補助性質獎助學金。</li>
              </ul>
            </div>
          </section>

          <!-- Right: Extra Info -->
          
            <div class="side-card">
              <h3>注意事項</h3>
              <p>
                申請需檢附戶籍謄本、財力證明及在學證明，
                請於期限內繳交，逾期恕不受理。
              </p>
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
.detail-block{
  width: 20%;
  padding-right: 2rem;
  min-height:500px;
  position: relative;
}
.scholarship-card {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.scholarship-title {
  font-size: 22px;
  font-weight: bold;
  color: #3b852B;
}
.org {
  margin: 5px 0;
  color: #555;
}
.amount {
  font-weight: bold;
  margin-bottom: 15px;
}
.section-title {
  font-weight: bold;
  margin: 15px 0 8px;
}
.scholarship-content,
.scholarship-conditions {
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