<script>
import { useRouter} from 'vue-router';
</script>

<template>
    <div class="page-wrapper-road">
        <img src="../assets/images/plan/road.png" alt="目標路" class="road">

    </div>

</template>
<style coped>
.page-wrapper-road {
  background-color: #E1E1E1;
  min-height: 100vh;
  width: 100vw;
  overflow:hidden;
  position: relative;
  margin:0;
  padding:0;
}

.road {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 保持比例，覆蓋整個容器 */
  display: block;
}

</style>