<script setup>
import Menu from '../components/Menu.vue';
import { ref } from 'vue';
import meerkat from '../assets/images/home/meerkat.png'
import glassesMeerkat from '../assets/images/home/glassesmeerkat.png'
import rent1 from '../assets/images/home/rent1.png'
import rent2 from '../assets/images/home/rent2.png'

const isMeerkatHover = ref(false);  /* 定義一個變數叫 isHover，一開始是 false (還沒滑鼠滑過圖片)*/
const isRentHover = ref(false)
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class = "blackboardcontainer">
            <img src="../assets/images/home/blackboard.png" alt="黑板" class ="blackboard" />
            <div class = "meerkatcontainer">
                <img :src="isMeerkatHover ? glassesMeerkat: meerkat" 
                    alt="小獴" class ="meerkat"
                    @mouseenter="isMeerkatHover = true" 
                    @mouseleave="isMeerkatHover = false"
                />
            </div>
            <div class = "rentcontainer">
                <img :src="isRentHover? rent2: rent1"
                    alt="租屋" class ="rent"
                    @mouseenter="isRentHover = true" 
                    @mouseleave="isRentHover = false"/>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .page-wrapper {
    background-color: #FFFCBE;
    min-height: 100vh;
    height: 100%;
    width: 100%;
    }
    /* 黑板與獴獴的設定 */
    .blackboardcontainer {
        display: flex; /* 讓container中的內容可以更隨意地排列，原本div預設是垂直排列，img預設是水平排列 */
        justify-content: center; /* 水平置中 */
        height: auto;
        z-index: 1;  /* 數字越大越上層 */
        position: relative;  /* 讓position: absolute定位用的 */
    }
    .blackboard{
        width: 100%;  /* 寬度100%填滿父容器 */
        object-fit: contain;  /* 在contain中完整顯示(不裁切) */
    }
    .meerkatcontainer{
        display: flex;
        justify-content: center;
        width: 100vw;   /* 100% 視窗寬度 */
        height: 85vh;  /* 100% 視窗高度 */
        z-index: 2;
        position: absolute;
        left: 50%; transform: translateX(-50%);
        top: 15%
    }
    .meerkat{
        width: 50%;
        height: auto;
        object-fit: cover;
        object-position: center top;  /* 保留圖片上半部，底部被裁掉 */
        z-index: 2;
    }
    .rentcontainer{
        display: flex;
        justify-content: center;
        width: 35vw;   /* 100% 視窗寬度 */
        height: auto;  /* 100% 視窗高度 */
        z-index: 2;
        position: absolute;
        left: 22%;bottom: 25%;
        transform: translateX(-50%) ;
    }
    .rent{
        width: 50%;
        height: auto;
        object-fit: cover;
        object-position: center top;  /* 保留圖片上半部，底部被裁掉 */
        z-index: 2;
        transform:rotate(-10deg)
    }
    .rent:hover{
        content: url("../assets/images/home/rent2.png");
        transform: rotate(-15deg);
    }

    
    :global(html),
    :global(body) {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #FFFCBE; /* 可有可無，看是否要統一 */
    }
</style>


