<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest4">
            <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow" >
        </RouterLink>
        <div class="question">
            <div class="word">
                寒暑假快到了，
                <br>狐獴小學的校園布告欄貼出一張海報：「快來報名課外活動，培養新興趣或提升自己！」
                <br>小狐獴小安想報名烹飪課，學習做出美味的點心；
                <br>而小狐獴小美想挑戰攝影，捕捉美麗的校園風景。
                <div class="Q3">
                    <br>這是一個關於寒暑假如何利用時間自我成長的題目。你會報名什麼課外活動呢？
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
    .Q3{
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