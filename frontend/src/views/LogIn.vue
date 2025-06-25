<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class = "page-wrapper">
        <Menu />
        <img src = "../assets/images/login/logInBoard.png" alt = "登入黑板" class = "logInBlackboard">
        <img src = "../assets/images/login/logInMeerkat.png" alt = "登入小獴" class = "logInMeerkat">
        <img src = "../assets/images/login/Account.png" alt = "帳號文字" class = "account">
        <img src = "../assets/images/login/password.png" alt = "密碼文字" class = "password">
        <img src = "../assets/images/login/inputbox.png" alt = "輸入框" class="inputbox1">
        <img src = "../assets/images/login/inputbox.png" alt = "輸入框" class="inputbox2">
    </div>
</template>

<style scoped>
    .page-wrapper {
        background-color: #dbdbdb;
        min-height: 100vh;
        width: 100%;
        position: relative;
    }
    .logInBlackboard{
        position: absolute;
        top: 15%;           /* 距離頂端 15% */
        left: 50%;           /* 水平中心 */
        transform: translateX(-40%);
        height: 50%;        /* 可按需求修改 */
        object-fit: contain;
        z-index: 1;
    }
    .logInMeerkat{
        position: absolute;
        bottom: 0%;           /* 距離頂端 15% */
        left: 50%;           /* 水平中心 */
        transform: translateX(-124%);
        height: 66%;        /* 可按需求修改 */
        object-fit: contain;
        z-index: 2;
    }
    .account{
        position: absolute;
        top: 30%;
        left: 50%;
        transform: translateX(-115%);
        height: 12%;
        object-fit: contain;
        z-index: 3;
    }
    .password{
        position: absolute;
        top: 41%;
        left: 50%;
        transform: translateX(-140%);
        height: 9%;
        object-fit: contain;
        z-index: 3;
    }
    .inputbox1{
        position: absolute;
        top: 20%;
        left: 50%;
        transform: translateX(-10%);
        height: 20%;
        object-fit: contain;
        z-index: 3;
    }
    .inputbox2{
        position: absolute;
        top: 30%;
        left: 50%;
        transform: translateX(-10%);
        height: 20%;
        object-fit: contain;
        z-index: 3;
    }
</style>

<style>
html, body {
  height: 100%;
  margin: 0;
}
</style>