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
          <!-- Left: Job Info -->
          <section class="job-card">
            <h2 class="job-title">
              前端工程師 實習生（Vue3、Nuxt）
            </h2>
            <div class="company">異特資訊股份有限公司</div>
            <div>📍 台北市中正區</div>
            <div class="salary">💰 時薪 200 元</div>

            <h3 class="section-title">職務內容</h3>
            <div class="job-content">
              <ol>
                <li>設計出圖像豐富、高互動性、創意十足的前端網站，帶給用戶沉浸式的體驗。</li>
                <li>與後端工程師合作，將前端畫面與後端資料串接，打造穩定的產品功能。</li>
                <li>熟悉 Vue3、Nuxt 並在專案中能靈活應用，解決實際問題。</li>
                <li>能將 3D 與互動式動畫整合到網站，提升視覺效果，讓平台內容更具吸引力。</li>
              </ol>
            </div>

            <h3 class="section-title">職務需求</h3>
            <div class="job-requirements">
              <p>工作經歷：3年以上</p>
              <p>學歷要求：大專以上</p>
              <p>科系要求：資訊相關</p>
              <p>語文條件：英⽂ 700 分以上</p>
            </div>
          </section>

          <!-- Right: Company & Reviews -->
           <h2 class="section-title">公司介紹</h2>
            <div class="side-card">
              <h3>異特公司</h3>
              <p>
                我們秉持專業、效率並重的精神，提供客戶最佳解決方案，
                團隊重視成員的學習與成長，並鼓勵提出創新想法。
              </p>
            </div>

            <h2 class="section-title">心得</h2>
            <div class="side-card">
              <h3>後端工程師</h3>
              <p>我最近加入異特公司的後端團隊，團隊氛圍很好，學習到許多新技術。</p>
              <p class="date">2025.04.25</p>
            </div>

            <div class="side-card">
              <h3>前端工程師 實習生</h3>
              <p>
                這次在異特實習的經驗讓我受益良多，從基礎開始學起，逐漸能夠獨立完成小專案。
              </p>
              <p class="date">2025.06.25</p>
            </div>

            <div class="side-card">
              <h3>行銷企劃 實習生</h3>
              <p>
                在行銷實習期間，我不僅學到如何規劃專案，也更懂得團隊合作的重要性。
              </p>
              <p class="date">2025.06.30</p>
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
/* Job Info Card */
.job-card {
  background: #fff;
  padding:  0px 10px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.job-title {
  font-size: 22px;
  font-weight: bold;
  color: #3B852B;
}
.company {
  margin: 5px 0;
  color: #555;
}
.salary {
  font-weight: bold;
  margin-bottom: 15px;
}
.section-title {
  font-weight: bold;
  margin: 15px 0 8px;
}
.job-content,
.job-requirements {
  background: #eee;
  padding: 15px;
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.6;
}

/* Right Side Cards */
.side-card {
  background: #fff;
  padding:20px;
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