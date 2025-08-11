<script setup>
    import { ref } from 'vue'
    import Menu from '../components/Menu.vue';

    
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest3">
            <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow" >
        </RouterLink>
        <div class="question">
            <div class="word">
                期末快到了，
                <br>老師告訴狐獴小學的同學們：「這次小組要製作一份報告，大家可以自由選擇想負責的任務喔！」
                <br>狐獴小明想當資料搜集高手，斑尾猴小蓉則想負責美編設計。
                <br>大家開始熱烈討論分工，學習如何根據自己的興趣和專長來挑選任務。
                <div class="Q2">
                    <br>這正是一個關於團隊合作和自由選擇責任的題目。你會想挑哪一部分呢？
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
    .Q2{
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