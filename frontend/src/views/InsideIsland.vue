<script setup>
//要加上串API
import { ref,onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const stageRef = ref(null);
const backgroundImage = ref(null);
const pyramidImage = ref(null);

// 背景圖片資訊
const imageWidth = 1440;
const imageHeight = 1024;
const repeatCountX = 6;
const repeatCountY = 5;
const canvasSize = {
  width: imageWidth * repeatCountX,
  height: imageHeight * repeatCountY
};
const repeatedImages = ref([]);
//新增的金字塔
const revealedPyramid = ref([]);

onMounted(() => {
  const img = new Image();
  img.src = new URL('../assets/images/plan/insideIsland.png', import.meta.url).href;
  img.onload = () => {
    backgroundImage.value = img;
    //背景圖
    const temp = [];
    for (let y = 0; y < repeatCountY; y++) {
      for (let x = 0; x < repeatCountX; x++) {
        temp.push({
          x: x * imageWidth,
          y: y * imageHeight
        });
      }
    }
    repeatedImages.value = temp;
  };
    //金字塔圖片
    const pyImg = new Image();
    pyImg.src = new URL('../assets/images/plan/pyramid.png', import.meta.url).href;
    pyImg.onload = () => {
        pyramidImage.value = pyImg;
    };
    });

//回報進度
function reportProgress(){
    if(!pyramidImage.value) return;
     // 基本邏輯：橫向排列
    const count = revealedPyramid.value.length;
    const margin = 100; // 圖與圖的間距
    const x = count * (300 + margin); // 假設每座金字塔寬 300px
    const y = canvasSize.height / 2 - 150; // 置中偏上

    revealedPyramid.value.push({ x, y });
}


//回前頁箭頭
function goBack() {
  router.back()
  }

  //初始畫布
const stageConfig = ref({
  width: window.innerWidth,
  height: window.innerHeight,
  draggable: true,
  // 初始位置設定為畫布中心
  x: -canvasSize.width / 2 + window.innerWidth / 2,
  y: -canvasSize.height / 2 + window.innerHeight / 2,
  //縮放比例1
  scale: { x: 0.9, y: 0.9},
})

let isDragging = false
let lastPos = { x: 0, y: 0 }

function handleMouseDown(e) {
  isDragging = true
  lastPos = {x: e.evt.clientX,y: e.evt.clientY}
}

//滑鼠拖移畫布
function handleMouseMove(e) {
 if (!isDragging) return
  const dx = e.evt.clientX - lastPos.x
  const dy = e.evt.clientY - lastPos.y

  let nextX = stageConfig.value.x + dx
  let nextY = stageConfig.value.y + dy

  // 限制拖動邊界（以畫布大小為基準）
  const minX = -(canvasSize.width - window.innerWidth)
  const minY = -(canvasSize.height - window.innerHeight)
  const maxX = 0
  const maxY = 0

  stageConfig.value.x = Math.max(minX, Math.min(maxX, nextX))
  stageConfig.value.y = Math.max(minY, Math.min(maxY, nextY))

  lastPos = {x: e.evt.clientX,y: e.evt.clientY,}
}

function handleMouseUp() {
  isDragging = false
}

//滾輪縮放功能
function handleWheel(e) {
  e.evt.preventDefault()
  const scaleBy = 1.05
  const stage = stageRef.value.getNode()
  const oldScale = stage.scaleX()
  const pointer = stage.getPointerPosition()

  const mousePointTo = {
    x: (pointer.x - stage.x()) / oldScale,
    y: (pointer.y - stage.y()) / oldScale,
  }
  // 限制縮放範圍
  let newScale = e.evt.deltaY > 0 ? oldScale / scaleBy : oldScale * scaleBy
  newScale = Math.max(0.2, Math.min(2, newScale)) // 限制縮放在 0.2 ~ 2 之間

  stage.scale({ x: newScale, y: newScale })

  const newPos = {
    x: pointer.x - mousePointTo.x * newScale,
    y: pointer.y - mousePointTo.y * newScale,
  }

  stage.position(newPos)
  stage.batchDraw()
}
</script>

<template>
    <div class="page-wrapper">
        <img
            src="../assets/images/plan/arrow.png"
            class="back-arrow"
            alt="Back"
            @click="goBack"
        />

           <button class="report-btn" @click="reportProgress">
                回報進度 ➕
            </button>

        <div class="infinite-canvas-wrapper">
            <!--v-stage是整個畫部的框框-->
            <v-stage
                :config="stageConfig"
                @wheel="handleWheel"
                @mousedown="handleMouseDown"
                @mousemove="handleMouseMove"
                @mouseup="handleMouseUp"
                ref="stageRef"
            >
            <v-layer>
                <v-rect
                    :config="{
                    x: 0,
                    y: 0,
                    width: canvasSize.width,
                    height: canvasSize.height,
                    fill: '#EBC973'
                    }"
                />
                </v-layer>

                <v-layer>
                <template v-if="backgroundImage">
                    <v-image
                    v-for="(item, index) in repeatedImages"
                    :key="'bg-' + index"
                    :config="{
                        x: item.x,
                        y: item.y,
                        image: backgroundImage,
                        width: imageWidth,
                        height: imageHeight
                    }"
                    />
                </template>
                </v-layer>

                <v-layer>
                <template v-if="pyramidImage">
                    <v-image
                    v-for="(item, index) in revealedPyramid"
                    :key="'pyramid-' + index"
                    :config="{
                        x: item.x,
                        y: item.y,
                        image: pyramidImage,
                        width: 300,
                        height: 300
                    }"
                    />
                </template>
                </v-layer>


            </v-stage>
        </div>
     </div>
</template>

<style scoped>
.infinite-canvas-wrapper {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: #EBC973;
}
.back-arrow {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 25px;
  height:25px;
  cursor: pointer;
  z-index: 10;
}
.report-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  padding: 8px 12px;
  font-size: 16px;
  background-color: #fff5c1;
  border: none;
  border-radius: 8px;
  z-index: 10;
  cursor: pointer;
}


</style>
