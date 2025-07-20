<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <img src="../assets/images/aptitude_test/BG1.png" class="BG1">
        <img src="../assets/images/aptitude_test/BG2.png" class="BG2">
        <img src="../assets/images/aptitude_test/BG3.png" class="BG3">
        <div class="BG4container">
            <img src="../assets/images/aptitude_test/BG4.png" class="BG4">
        </div>
        <img src="../assets/images/aptitude_test/BG5.png" class="BG5">
        <img src="../assets/images/aptitude_test/aptitude_test.png" class="word">
        <img src="../assets/images/aptitude_test/Pass.png" class="pass">
        <RouterLink to = "/aptitudeTestResult">
            <img src="../assets/images/aptitude_test/start.png" class="start">
        </RouterLink>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: #47695b;
        min-height: 100vh;
        width: 100%;
        position: relative;
    }
    .BG1{
        width: 24%;
        position: absolute;
        top: -5%;
        left: -3%;
    }
    .BG2{
        width: 25%;
        position: absolute;
        top: -12%;
        left: 50%;
        transform: translateX(-50%);
    }
    .BG3{
        width: 20%;
        position: absolute;
        top: -3%;
        left: 100%;
        transform: translateX(-100%);
    }
    .BG4container{
        display: flex;
        width: 24%;
        position: absolute;
        top: 100%;
        left: -3%;
        transform: translateY(-100%);
    }
    .BG4{
        object-fit: cover;
        width: 100%;
    }
    .BG5{
        width: 25%;
        position: absolute;
        top: 100%;
        left: 100%;
        transform: translate(-100%,-100%);
    }
    .word{
        width: 45%;
        top: 50%;
        left: 50%;
        position: absolute;
        transform: translate(-50%,-53%);
    }
    .pass{
        width: 12%;
        top: 50%;
        left: 50%;
        position: absolute;
        transform: translate(-50%,420%);
    }
    .start{
        width: 15%;
        top: 50%;
        left: 50%;
        position: absolute;
        transform: translate(-50%,60%);
    }
</style>