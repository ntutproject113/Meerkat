<script setup>
//要加上串API
import { ref,onMounted } from 'vue';
import { useRouter,useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const stageRef = ref(null);
const backgroundImage = ref(null);
const pyramidImage = ref(null);
const islandId = route.query.islandId

// 背景圖片資訊
const imageWidth = 1440;
const imageHeight = 1024;
const repeatCountX = 7;
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

//中間立牌
const centralImage = ref(null);

onMounted(() => {
  const centerImg = new Image();
  centerImg.src = new URL('../assets/images/plan/insideGoal.png', import.meta.url).href;
  centerImg.onload = () => {
    centralImage.value = centerImg;
  };
});

//回報進度
function reportProgress() {
  if (!pyramidImage.value || !stageRef.value) return

  const stage = stageRef.value.getNode()
  const scale = stage.scaleX()

  // 中央目標牌的範圍
  const avoidX1 = 3150
  const avoidX2 = 4150
  const avoidY1 = 1950
  const avoidY2 = 2650

  // 隨機產生不會蓋到立牌的位置
  let x, y
  let tries = 0
  do {
    const minX = 2500
    const maxX = 3700
    const minY = 1600
    const maxY = 2400

    x = Math.floor(Math.random() * (maxX - minX + 1)) + minX
    y = Math.floor(Math.random() * (maxY - minY + 1)) + minY
    tries++
  } while (
    x + 500 > avoidX1 && x < avoidX2 && // 有重疊
    y + 500 > avoidY1 && y < avoidY2 && // 有重疊
    tries < 50 // 避免死循環
  )

  revealedPyramid.value.push({ x, y , content: reportText.value })

  //自動聚焦畫面到該金字塔
  const newX = window.innerWidth / 2 - x * scale
  const newY = window.innerHeight / 2 - y * scale
  stage.position({ x: newX, y: newY })
  stage.batchDraw()
}
  const hoveredPyramidIndex = ref(null)
  const tooltipPosition = ref({ x: 0, y: 0 })

function handlePyramidMouseEnter(item, index) {
  console.log('hover in', index)
  const stage = stageRef.value?.getNode()
  if (!stage) return

  const scale = stage.scaleX()
  hoveredPyramidIndex.value = index
  tooltipPosition.value = {
    x: (item.x + 450) * scale + stage.x(),
    y: item.y * scale + stage.y() - 40,
  }
}

function handlePyramidMouseLeave() {
  hoveredPyramidIndex.value = null
}


//進度回報
const showReportModal = ref(false)
const reportText = ref('') // 儲存使用者輸入的進度

function submitReport() {
  if (reportText.value.trim() === '') {
    alert('請填寫進度再提交！')
    return
  }

  // 觸發新增金字塔
  reportProgress()

  // 清空內容、關閉彈窗
  reportText.value = ''
  showReportModal.value = false
}


//回前頁箭頭
function goBack() {
  router.back()
  }
const goalX = 3150 + 1000 / 2 // 中央牌 X 中心點
const goalY = 1950 + 700 / 2  // 中央牌 Y 中心點
  //初始畫布
const stageConfig = ref({
  width: window.innerWidth,
  height: window.innerHeight,
  draggable: true,
  // 初始位置設定為目標牌的位置
  x: -goalX * 0.6 + window.innerWidth / 2,
  y: -goalY * 0.6 + window.innerHeight / 2,
  scale: { x: 0.6, y: 0.6},
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
      <div v-if="showReportModal" class="modal-overlay">
        <div class="modal-content">
          <h2>回報今日進度</h2>
          <textarea v-model="reportText" placeholder="寫下你今天學到的一點小知識吧..." />
          <div class="modal-actions">
            <button @click="submitReport" class="submit-btn">完成回報</button>
            <button @click="showReportModal = false" class="cancel-btn">取消</button>
          </div>
        </div>
      </div>

        <img
            src="../assets/images/plan/arrow.png"
            class="back-arrow"
            alt="Back"
            @click="goBack"
        />

           <img
              src="../assets/images/plan/reportMeerkat.png"
              class="report-btn"
              @click="showReportModal = true"
              alt="回報進度"
            />

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

                <v-layer><!--目標牌-->
                  <template v-if="centralImage">
                    <v-image
                      :config="{
                        x: 3150,
                        y: 1950,
                        width: 1000,
                        height: 700,
                        image: centralImage,
                        zIndex: 5
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
                        width: 900,
                        height: 900,
                        draggable: false,         // 這樣 Konva 才不會預設跳過事件
                        hitStrokeWidth: 0         // 強制產生 hit 區域（即便是透明區域）
                    }"
                    @mouseenter="() => handlePyramidMouseEnter(item, index)"
                    @mouseleave="handlePyramidMouseLeave"
                    />
                </template>
                </v-layer>
            </v-stage>
        </div>
      <div
        v-if="hoveredPyramidIndex !== null"
        class="tooltip"
        :style="{
          top: tooltipPosition.y + 'px',
          left: tooltipPosition.x + 'px'
        }"
      >
        {{ revealedPyramid[hoveredPyramidIndex]?.content }}
      </div>
     </div>
      
</template>

<style scoped>
.page-wrapper {
  overflow: hidden;
}
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
  bottom: 0;
  right: 40px;
  width: 250px; /* 可自行調整大小 */
  height: auto;
  cursor: pointer;
  z-index: 10;
}
.report-btn:hover {
  filter: brightness(1.15);
  transition: filter 0.2s ease;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明黑底 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
}

.modal-content {
  background: white;
  padding: 24px;
  border-radius: 16px;
  width: 400px;
  max-width: 90%;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.modal-content h2 {
  margin: 0;
}

.modal-content textarea {
  resize: none;
  height: 120px;
  font-size: 16px;
  padding: 8px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
.submit-btn{
  background-color: #c4651d;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.cancel-btn {
  background-color: #9e9e9e;
  color: white;
  border: none;
  padding:10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.tooltip {
  position: absolute;
  background: rgba(0, 0, 0, 0.75);
  color: white;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 14px;
  pointer-events: none;
  white-space: pre-wrap;
  max-width: 200px;
  z-index: 999;
}


</style>
