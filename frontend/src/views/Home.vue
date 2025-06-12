<script setup>

</script>

<template>
    <div>
        <div class = "half-view">
            <div class = "blackboardcontainer">
                <img src="../assets/首頁/blackboard.png" alt="黑板" class ="blackboard" />
            </div>
            <div class = "meerkatcontainer">
                <img src="../assets/首頁/meerkathalf.png" alt="小獴" class ="meerkathalf" />
            </div>
        </div>
        <div class = "full-view">
            <div class = "blackboardcontainer">
                <img src="../assets/首頁/blackboard.png" alt="黑板" class ="blackboard" />
            </div>
            <div class = "meerkatcontainer">
                <img src="../assets/首頁/meerkatfull.png" alt="小獴" class ="meerkatfull" />
            </div>
        </div>
    </div>
</template>

<style scoped>
    /* 桌機畫面（預設） */
    .half-view {
        display: block;
    }
    .full-view {
        display: none;
    }

    /* 黑板與獴獴的設定 */
    .blackboardcontainer {
        display: flex;
        justify-content: center; /* 水平置中 */
        height: auto;           /* 要有高度才能垂直置中 */
        z-index: 1;
    }
    .blackboard{
        width: 100%;
        height: auto;
        object-fit: contain;
        position: relative;
    }
    .meerkatcontainer{
        display: flex;
        justify-content: center; /* 水平置中 */
        height: auto;           /* 要有高度才能垂直置中 */
        z-index: 2;
        left: 50%;
    }
    .meerkathalf{
        width: 30%;
        height: auto;
        object-fit: contain;
        bottom:0;
        position: absolute;
    }
    .meerkatfull{
        width: 60%;
        height: auto;
        object-fit: contain;
        bottom: 0;
        position: absolute;
        transform: translatey(15%);
    }

    /* 小螢幕時切換為 mobile 畫面 */
    @media (max-width: 768px) {
        .half-view {
            display: none;
        }
        .full-view{
            display: block;
        }
    }
</style>

<style>
    html, body {
        margin: 0;
        padding: 0;
        background-color:#FFFCBE ;
        min-height: 100vh;
    }
</style>
