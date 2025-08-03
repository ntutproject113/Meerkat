<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTestResult">
            <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow" >
        </RouterLink>
        <div class="question">
            <div class="word">
                一天放學後，
                <br>同學們聚在一起聊天，大家開始討論：「你們覺得身邊的朋友最常稱讚你什麼能力或特質呢？」
                <br>小狐獴小欣說：「大家都說我很會傾聽，很能理解別人。」
                <br>小浣熊小峰則說：「我常被誇獎創意很豐富！」
                <div class="Q6">
                    <br>這是一個關於自我認知和同伴眼中你的優點的題目。你覺得朋友們最欣賞你的哪一點呢？
                </div>
            </div>
        </div>
        <div class="answer">
        </div>
        <div class="choice">
        </div>
    </div>
</template>

<style scoped>
    .page-wrapper{
        display: flex;
        background-color: #47695B;
    }
    .question{
        display: flex;
        position: absolute;
        justify-content: center;
        top: 0;
        width: 100vw;
        height: 45vh;
        background-color: #ffffff;
    }
    .word{
        align-self: flex-end;
        margin-bottom: 2%;
        
    }
    .Q6{
        font-weight: bold;
    }
    .answer{
        position: absolute;
        top: 45%;
        left: 0;
        width: 30vw;
        height: 55vh;
        background-color: #777777;
    }
    .choice{
        position: absolute;
        top: 45%;
        left: 30%;
        width: 70vw;
        height: 55vh;
        background-color: #333333;
    }
    .arrow{
        z-index: 2;
        position: absolute;
        bottom: 5%;
        right: 5%;
        width: 100px;
    }
</style>