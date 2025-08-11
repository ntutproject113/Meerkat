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
      <img
        src="../assets/images/plan/goal1.png"
        alt="短期目標"
        class="absolute z-20 w-[10vw] sm:w-[100px] md:w-[120px] lg:w-[200px]"
        style="top: 8%; left: 20%; transform: translate(-50%, -50%)"
      />
      <img
        src="../assets/images/plan/goal1.png"
        alt="短期目標2"
        class="absolute z-20 w-[10vw] sm:w-[100px] md:w-[120px] lg:w-[200px]"
        style="top: 15%; left: 40%; transform: translate(-50%, -50%)"
      />
      <img
        src="../assets/images/plan/goal1.png"
        alt="短期目標3"
        class="absolute z-20 w-[10vw] sm:w-[100px] md:w-[120px] lg:w-[200px]"
        style="top: 15%; left: 65%; transform: translate(-50%, -50%)"
      />

      <img
        src="../assets/images/plan/goal2.png"
        alt="中期目標"
        class="absolute z-20 w-[14vw] sm:w-[120px] md:w-[150px] lg:w-[180px]"
        style="top: 10%; left: 85%; transform: translate(-50%, -50%)"
      />
      <img
        src="../assets/images/plan/goal2.png"
        alt="中期目標2"
        class="absolute z-20 w-[14vw] sm:w-[120px] md:w-[150px] lg:w-[180px]"
        style="top: 50%; left: 15%; transform: translate(-50%, -50%)"
      />

      <img
        src="../assets/images/plan/goal3.png"
        alt="最終目標"
        class="absolute z-20 w-[16vw] sm:w-[150px] md:w-[180px] lg:w-[220px]"
        style="top: 75%; left: 90%; transform: translate(-50%, -50%)"
      />
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

</style>
