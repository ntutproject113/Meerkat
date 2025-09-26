<script setup>
import Menu from '../components/Menu.vue'
</script>
<template>
     <img src="../assets/images/renting/background.png" class="bg-image" alt="背景">

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
            <h1 class="title">實習資訊</h1>
            <h2 class="rent-title">大安區精美小豪宅</h2>
            <div>類型：獨立套房</div>
            <div>租金：NT$12,000/月</div>  
            <div>地址：台北市大安區和平東路三段</div>
            <div>聯絡方式：0912-345-678</div>
            <div>交通：捷運大安站 步行時間：4分鐘</div>
            

        </div>
        <div class="detail-info">
          <h3>詳細資訊</h3>
          <div class="row">
            <span>開伙：</span>
            <span>✅</span>
          </div>
          <div class="row">
            <span>陽台：</span>
            <span>✅</span>
          </div>
          <div class="row">
            <span>洗衣機：</span>
            <span>✅</span>
          </div>
           <div class="row">
            <span>網路：</span>
            <span>❎</span>
          </div>
          <div class="row">
            <span>對外窗：</span>
            <span>❎</span>
          </div>
           <div class="row">
            <span>租期：</span>
            <span>一年</span>
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
  width: 60%;   
  height:400px;      
  padding-left: 5.7rem;    
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
.title{ 
  font-size: 32px;
  font-weight: bold;
  color: #000000;
  margin:-8px auto;
  text-align: center;
}
.rent-title {
  font-weight: bold;
  color: #3B852B;
  margin-bottom: 6px;
}
.detail-info {
  font-size: 16px;
}
.row {
  display: flex;
  justify-content: space-between; /* 左右分散 */
  padding: 4px 0;
}
.row span:first-child {
  font-weight: bold;
}
</style>