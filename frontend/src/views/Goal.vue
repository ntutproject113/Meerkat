<script setup>
import {ref,onBeforeUnmount} from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter();

function goBack() {
  router.back() 
}
</script>

<template>
  <div class="relative h-screen overflow-y-auto bg-gray-200">
  <!--回前頁的箭頭-->
    <img
        src="../assets/images/plan/arrow.png"
        class="back-arrow"
        alt="Back"
        @click="goBack"
    />
   <div class="viewport" >
    
    <div class="image-wrapper">

        <img src="../assets/images/plan/road.png" alt="目標路" class="road" draggable="false" @dragstart.prevent >

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
  position: absolute;
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

</style>