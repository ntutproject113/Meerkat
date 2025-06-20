<script setup>
import { ref } from 'vue'


const canvasSize = 5000 // 設定畫布超大尺寸

const stageRef = ref(null)

//初始畫布
const stageConfig = ref({
  width: window.innerWidth,
  height: window.innerHeight,
  draggable: true,
  // 初始位置設定為畫布中心
  x: -2000,
  y: -2000,
  //縮放比例1
  scale: { x: 1, y: 1 },
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
  stageConfig.value.x += dx
  stageConfig.value.y += dy
  lastPos = {
    x: e.evt.clientX,
    y: e.evt.clientY
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

  const newScale = e.evt.deltaY > 0 ? oldScale / scaleBy : oldScale * scaleBy
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

        <!-- 可放任意元件或標記 -->
        <v-circle
          :config="{
            x: 2500,
            y: 2500,
            radius: 30,
            fill: 'red',
            draggable: true
          }"
        />
      </v-layer>
    </v-stage>
  </div>
</template>

<style scoped>
.infinite-canvas-wrapper {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background-color: #ccc;
}
</style>
