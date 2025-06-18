<script setup>
import Menu from '../components/Menu.vue';

</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class = "full-view">
            <div class = "blackboardcontainer">
                <img src="../assets/images/home/blackboard.png" alt="黑板" class ="blackboard" />
            </div>
            <div class = "meerkatcontainer">
                <img src="../assets/images/home/meerkatfull.png" alt="小獴" class ="meerkatfull" />
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
        height: auto;           /* 要有高度才能垂直置中 */
        z-index: 1;  /* 數字越大越上層 */
    }
    .blackboard{
        width: 100%;  /* 寬度100%填滿父容器 */
        height: auto;  /* 高度由原比例自動縮放 */
        object-fit: contain;  /* 在contain中完整顯示(不裁切) */
        position: relative;  /* 讓position: absolute定位用的 */
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
    .meerkatfull{
        width: 50%;
        height: auto;
        object-fit: cover;
        object-position: center top;  /* 保留圖片上半部，底部被裁掉 */
        z-index: 2;
    }

    
    :global(html),
    :global(body) {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #FFFCBE; /* 可有可無，看是否要統一 */
    }
</style>


