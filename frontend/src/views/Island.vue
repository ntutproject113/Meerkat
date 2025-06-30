<script setup>
    import { ref,reactive,onMounted } from 'vue';
    import { useRouter } from 'vue-router';

const router = useRouter()
const canvasSize = 5000 // 設定畫布超大尺寸
const stageRef = ref(null)

function goBack() {
  router.back() // ⬅️ 回到上一頁
}
function handleIslandClick(id) {
  // 跳轉到 InsideIsland.vue，並帶上 islandId
  router.push({ name: 'InsideIsland', query: { islandId: id } })
}

// 假裝這是後端傳來的資料
const imageDataFromServer = [
  { src: '../assets/images/plan/HTML.png', x: 2100, y: 2500 },
  { src: '../assets/images/plan/Java.png', x: 2800, y: 2400 },
  { src: '../assets/images/plan/finmgt.png', x: 2500, y: 2800 },
  { src: '../assets/images/plan/island2.png', x: 1800, y: 2000 },
  { src: '../assets/images/plan/island1.png', x: 3200, y: 3000 },
]



//初始畫布
const stageConfig = ref({
  width: window.innerWidth,
  height: window.innerHeight,
  draggable: true,
  // 初始位置設定為畫布中心
  x: -2500 + window.innerWidth / 2,
  y: -2500 + window.innerHeight / 2,
  //縮放比例1
  scale: { x: 0.9, y: 0.9},
})

let isDragging = false
let lastPos = { x: 0, y: 0 }

function handleMouseDown(e) {
  isDragging = true
  lastPos = {
    x: e.evt.clientX,
    y: e.evt.clientY
  }
}

//滑鼠拖移畫布
function handleMouseMove(e) {
 if (!isDragging) return
  const dx = e.evt.clientX - lastPos.x
  const dy = e.evt.clientY - lastPos.y

  let nextX = stageConfig.value.x + dx
  let nextY = stageConfig.value.y + dy

  // 限制拖動邊界（以畫布大小為基準）
  const minX = -(canvasSize - window.innerWidth)
  const minY = -(canvasSize - window.innerHeight)
  const maxX = 0
  const maxY = 0

  stageConfig.value.x = Math.max(minX, Math.min(maxX, nextX))
  stageConfig.value.y = Math.max(minY, Math.min(maxY, nextY))

  lastPos = {
    x: e.evt.clientX,
    y: e.evt.clientY,
  }
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
//放圖片
const imageItems = reactive([])

onMounted(() => {
  imageDataFromServer.forEach((item, index) => {
    const img = new Image()
    img.src = new URL(item.src, import.meta.url).href

    img.onload = () => {
      imageItems.push({
        id: index, // 唯一 ID
        x: item.x,
        y: item.y,
        width: 600,
        height: 400,
        image: img,
        draggable: true,
      })
    }
  })
})
//裝飾的小船
const decorations = ref([])

onMounted(() => {
  const list = [
    { src: '../assets/images/plan/boat.png', x: 1500, y: 1800, w: 300, h: 300 },
    { src: '../assets/images/plan/boat2.png', x: 3500, y: 2600, w: 200, h: 200 },
  ]

  list.forEach((item, index) => {
    const img = new Image()
    img.src = new URL(item.src, import.meta.url).href
    img.onload = () => {
      decorations.value.push({
        id: index,
        x: item.x,
        y: item.y,
        width: item.w,
        height: item.h,
        image: img,
      })
    }
  })
})

</script>

<template>
    <div>
      <!--回前頁的箭頭-->
       <img
            src="../assets/images/plan/arrow.png"
            class="back-arrow"
            alt="Back"
            @click="goBack"
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
                    width: canvasSize,
                    height: canvasSize,
                    fill: '#B2D1EA'
                }"
                />
            <v-image
            v-for="item in imageItems"
            :key="item.id"
            :config="{
              x: item.x,
              y: item.y,
              image: item.image,
              width: item.width,
              height: item.height,
              draggable: false
            }"
            @click="() => handleIslandClick(item.id)"
          />  
          <v-image
            v-for="item in decorations"
            :key="item.id"
            :config="{
                x: item.x,
                y: item.y,
                width: item.width,
                height: item.height,
                image: item.image,
                draggable: false
            }"
            /> 
             
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
  background-color: #B2D1EA;
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

</style>