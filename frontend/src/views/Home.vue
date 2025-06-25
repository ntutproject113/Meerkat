<script setup>
import Menu from '../components/Menu.vue';
import { ref } from 'vue';
import meerkat from '../assets/images/home/meerkat.png'
import glassesMeerkat from '../assets/images/home/glassesmeerkat.png'

const isMeerkatHover = ref(false);  /* 定義一個變數叫 isHover，一開始是 false (還沒滑鼠滑過圖片)*/
const isRentHover = ref(false)
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class = "blackboardcontainer">
            <img src="../assets/images/home/blackboard.png" alt="黑板" class ="blackboard" />
            <img src="../assets/images/home/planning.png" alt="學涯規劃文字" class ="planning" />
            <img src="../assets/images/home/context1.png" alt="今日值日生文字" class ="context1" />
            <img src="../assets/images/home/context2.png" alt="小獴文字" class ="context2" />
            <div class = "meerkatcontainer">
                <img :src="isMeerkatHover ? glassesMeerkat: meerkat" 
                    alt="小獴" class ="meerkat"
                    @mouseenter="isMeerkatHover = true" 
                    @mouseleave="isMeerkatHover = false"
                />
            </div>
            <RouterLink to ="/renting" class = "rentcontainer">
                <img src="../assets/images/home/rent1.png" alt = "租屋1" class = "rent1"/>
                <img src="../assets/images/home/rent2.png" alt = "租屋2" class = "rent2"/>
                <img src="../assets/images/home/rent.png" alt = "租屋文字" class = "rent"/>
            </RouterLink>
            <RouterLink to = "/intern" class = "interncontainer">
                <img src="../assets/images/home/intern1.png" alt = "實習1" class = "intern1">
                <img src="../assets/images/home/intern2.png" alt = "實習2" class = "intern2">
                <img src="../assets/images/home/intern.png" alt = "實習文字" class = "intern">
            </RouterLink>
            <RouterLink to = "scholarships" class = "rewardcontainer">
                <img src="../assets/images/home/reward1.png" alt = "獎學金1" class = "reward1">
                <img src="../assets/images/home/reward2.png" alt = "獎學金2" class = "reward2">
                <img src="../assets/images/home/reward.png" alt = "獎學金文字" class = "reward">
            </RouterLink>
            <RouterLink to = "competition" class = "racecontainer">
                <img src="../assets/images/home/race1.png" alt = "比賽1" class = "race1">
                <img src="../assets/images/home/race2.png" alt = "比賽2" class = "race2">
                <img src="../assets/images/home/race.png" alt = "比賽文字" class = "race">
            </RouterLink>
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
        height: 74.7vh;  /* 100% 視窗高度 */
        z-index: 2;
        position: absolute;
        left: 50%; transform: translateX(-50%);
        top: 27%
    }
    .meerkat{
        width: 50%;
        height: auto;
        object-fit: cover;
        object-position: center top;  /* 保留圖片上半部，底部被裁掉 */
        z-index: 2;
    }
    /* 學涯規劃文字設定 */
    .planning{
        justify-content: center;
        object-fit: contain;
        width: 25vw;
        height: auto;
        z-index: 4;
        position: absolute;
        left: 50%; top: 8%;
        transform: translateX(-50%);
    }
    .context1{
        justify-content: center;
        object-fit: contain;
        width: 7vw;
        height: auto;
        z-index: 4;
        position: absolute;
        left: 88%; top: 10%;
        transform: translateX(-50%);
    }
    .context2{
        justify-content: center;
        object-fit: contain;
        width: 7vw;
        height: auto;
        z-index: 4;
        position: absolute;
        left: 88%; top: 51%;
        transform: translateX(-50%);
    }
    /* 租屋的設定 */
    .rentcontainer{
        display: flex;
        justify-content: center;
        width: 35vw;   /* 100% 視窗寬度 */
        height: auto;  /* 100% 視窗高度 */
        z-index: 3;
        position: absolute;
        left: 23%;bottom: 45%;
        transform: translateX(-50%) ;
    }
    .rent1{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(-10deg)
    }
    .rent2{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(0deg)
    }
    .rent {
        width: 40%;
        height: auto;
        object-fit: contain;
        z-index: 3;
        position: absolute;
        top: 0;
        left: 0;
        transform: translate(32%, -60%) rotate(-15deg);
    }
    .rent1 {
        opacity: 1;  /*表示元素的透明度*/
        z-index: 2;
    }
    .rent2,.rent {
        opacity: 0;
        z-index: 2;
    }
    .rentcontainer:hover .rent1{
        opacity: 0;
    }
    .rentcontainer:hover .rent{
        opacity: 1;
    }
    .rentcontainer:hover .rent2{
        opacity: 1;
    }

    /* 實習的設定 */
    .interncontainer{
        display: flex;
        width: 43vw;
        height: auto;
        z-index: 3;
        position: absolute;
        left: 42%;bottom: 76%;
        transform: translateX(-50%) ;
    }
    .intern1{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(13deg)
    }
    .intern2{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(0deg)
    }
    .intern{
        width: 38%;
        height: auto;
        object-fit: contain;
        z-index: 3;
        position: absolute;
        top: 0;
        left: 0;
        transform: translate(-45%, -55%) rotate(-20deg);
    }
    .intern1 {
        opacity: 1;  /*表示元素的透明度*/
        z-index: 2;
    }
    .intern2,.intern {
        opacity: 0;
        z-index: 2;
    }
    .interncontainer:hover .intern1{
        opacity: 0;
    }
    .interncontainer:hover .intern{
        opacity: 1;
    }
    .interncontainer:hover .intern2{
        opacity: 1;
    }

    /* 獎學金的設定 */
    .rewardcontainer{
        display: flex;
        width: 32vw;
        height: auto;
        z-index: 3;
        position: absolute;
        left: 79%;bottom: 76%;
        transform: translateX(-50%) ;
    }
    .reward1{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(0deg)
    }
    .reward2{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(0deg)
    }
    .reward{
        width: 40%;
        height: auto;
        object-fit: contain;
        z-index: 3;
        position: absolute;
        top: 0;
        left: 0;
        transform: translate(41%, -75%) rotate(15deg);
    }
    .reward1 {
        opacity: 1;  /*表示元素的透明度*/
        z-index: 2;
    }
    .reward2,.reward {
        opacity: 0;
        z-index: 2;
    }
    .rewardcontainer:hover .reward1{
        opacity: 0;
    }
    .rewardcontainer:hover .reward{
        opacity: 1;
    }
    .rewardcontainer:hover .reward2{
        opacity: 1;
    }

    /* 比賽的設定 */
    .racecontainer{
        display: flex;
        width: 30vw;
        height: auto;
        z-index: 3;
        position: absolute;
        left: 53%;bottom: 43%;
        transform: translateX(-50%) ;
        transform:rotate(270deg);
    }
    .race1{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(0deg)
    }
    .race2{
        position: absolute;
        width: 50%;
        height: auto;
        object-fit: cover;
        z-index: 3;
        transform:rotate(-10deg)
    }
    .race{
        width: 40%;
        height: auto;
        object-fit: contain;
        z-index: 3;
        position: absolute;
        top: 0;
        left: 0;
        transform: translate(80%, 70%) rotate(105deg);
    }
    .race1 {
        opacity: 1;  /*表示元素的透明度*/
        z-index: 2;
    }
    .race2,.race {
        opacity: 0;
        z-index: 2;
    }
    .racecontainer:hover .race1{
        opacity: 0;
    }
    .racecontainer:hover .race{
        opacity: 1;
    }
    .racecontainer:hover .race2{
        opacity: 1;
    }

    :global(html),
    :global(body) {
    margin: 0;
    padding: 0;
    height: 100%;
    
    }
</style>


