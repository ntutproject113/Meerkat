<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="meerkatContainer">
            <img src="../assets/images/signin/graduated.png" class="meerkat" />
        </div>
        <div class="resultType">

        </div>
        <div class="resultWord">

        </div>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: #47695B;
        display: flex;
    }
    .meerkatContainer{
        display: flex;
        background-color: #ffffff;
        width: 40vw;
        height: 100vh;
    }
    .meerkat{
        width: 50vw;
        max-width: 478px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 45%;
        transform: translate(-100%,-50%);
    }
    .resultType{
        position: absolute;
        top: 0;
        right: 0;
        background-color: #dbdbdb;
        width: 60vw;
        height: 50vh;
    }
    .resultWord{
        position: absolute;
        bottom: 0;
        right: 0;
        background-color: #b0d0d0;
        width: 60vw;
        height: 50vh;
    }
    
</style>