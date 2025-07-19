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
        class="road w-full h-auto select-none"
        draggable="false"
        @dragstart.prevent
      />

      <!-- 路標：使用 Tailwind 絕對定位 + 響應式大小 -->
      <img
        src="../assets/images/plan/goal1.png"
        alt="短期目標"
        class=" goal-marker absolute z-20 "
        style="top: 50%; left: 50%; transform: translate(-50%, -50%)"
      />

      <img
        src="../assets/images/plan/goal2.png"
        alt="中期目標"
        class=" goal-marker absolute z-20 "
        style="top: 32%; left: 75%; transform: translate(-50%, -50%)"
      />

      <img
        src="../assets/images/plan/goal3.png"
        alt="最終目標"
        class=" goal-marker absolute z-20 "
        style="top: 90%; left: 20%; transform: translate(-50%, -50%)"
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
  height: 100vh;
  overflow-y:auto;
  position: relative;
  background-color: #E1E1E1; 
  user-select: none; 
}
.image-wrapper{
  width:100%;
  height:1000px;
  position: relative;
  top: 0;
  left: 0;
  will-change: transform;
}

.road {
  width: 100%;
  height: 100%;
  object-fit: contain; /* 保持比例，覆蓋整個容器 */
  display: block;
}
.goal-marker {
  width: 5vw;
  max-width: 100px;
  min-width: 80px;
  height: auto;
}

</style>