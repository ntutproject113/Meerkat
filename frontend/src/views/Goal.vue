<script setup>
import {ref,onBeforeUnmount} from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter();

function goBack() {
  router.back() 
}
</script>

<template>
  
  <div class="relative min-h-screen overflow-hidden bg-gray-200">
    <!-- 回前頁的箭頭 -->
    <img
      src="../assets/images/plan/arrow.png"
      class="back-arrow absolute top-5 left-5 w-[25px] h-[25px] cursor-pointer z-10"
      alt="Back"
      @click="goBack"
    />
    <div class="viewport">
    <div class=" relative w-full " style="aspect-ratio:1440/855">
      <!-- 背景路圖 -->
      <img
        src="../assets/images/plan/road.png"
        alt="目標路"
        class="w-full h-full object-contain select-none"
        draggable="false"
        @dragstart.prevent
      />

      <!-- 路標：使用 Tailwind 絕對定位 + 響應式大小 -->
     <div class="target-container">
        <!-- 圖片 -->
        <img
          src="../assets/images/plan/goal1.png"
          alt="短期目標"
          class="goal-img"
        />
        <!-- 疊在圖片上的文字 -->
        <div class="target-text">
          短期目標
        </div>
      </div>

      <div class="target-container2">
        <img
          src="../assets/images/plan/goal1.png"
          alt="短期目標2"
          class="goal-img"
        />
        <div class="target-text">
          短期目標2
        </div>
      </div>

      <div class="target-container3">
        <img
          src="../assets/images/plan/goal1.png"
          alt="短期目標3"
          class="goal-img"
        />
        <div class="target-text">
          短期目標3
        </div>
      </div>

      <div class="target-container4">
        <img
          src="../assets/images/plan/goal2.png"
          alt="中期目標"
          class="goal-img2"
        />
        <div class="target-text2">
            中期目標
          </div>
      </div>

      <div class="target-container5">
        <img
          src="../assets/images/plan/goal2.png"
          alt="中期目標2"
          class="goal-img2"
        />
        <div class="target-text2">
            中期目標2
          </div>
      </div>

      <div class="target-container6">
        <img
          src="../assets/images/plan/goal3.png"
          alt="最終目標"
          class="goal-img2"
        />
        <div class="target-text2">
              最終目標
            </div>
      </div>
      </div>
    </div>
    </div>
 
</template>

<style scoped>
.back-arrow {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 25px;
  height:25px;
  cursor: pointer;
  z-index: 10;
}
.viewport {
  width: 100vw;
  min-height: 100vh;
  overflow-y:auto;
  position: relative;
  background-color: #E1E1E1; 
  user-select: none; 
}

.goal-marker {
  width: 5vw;
  max-width: 100px;
  min-width: 80px;
  height: auto;
}
.target-container {
  position: absolute;
  top: 8%;
  left: 20%;
  transform: translate(-50%, -50%);
}
.goal-img {
  width: 10vw;        
}
@media (min-width: 640px) {  /* sm */
  .goal-img {
    width: 100px;
  }
}

@media (min-width: 768px) {  /* md */
  .goal-img {
    width: 120px;
  }
}

@media (min-width: 1024px) { /* lg */
  .goal-img {
    width: 150px;
    }
}
.target-text {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
  font-weight: bold;
  color: rgb(255, 255, 255);
  white-space: nowrap;
  z-index:20;
}
.target-container2{
  position: absolute;
  top: 16%;
  left: 40%;
  transform: translate(-50%, -50%);
}
.target-container3{
  position: absolute;
  top: 14%;
  left: 60%;
  transform: translate(-50%, -50%);
}
.target-container4{
  position: absolute;
  top: 15%;
  left: 85%;
  transform: translate(-50%, -50%);
}
.goal-img2 {
  width: 14vw;        
}
.target-text2{
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
  font-weight: bold;
  color: rgb(0, 0, 0);
  white-space: nowrap;
  z-index:20;
}
.target-container5 {
  position: absolute;
  top: 50%;
  left: 15%;
  transform: translate(-50%, -50%);
}
.target-container6{
  position: absolute;
  top: 75%;
  left: 90%;
  transform: translate(-50%, -50%);
}

</style>
