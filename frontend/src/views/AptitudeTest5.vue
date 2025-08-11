<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest6">
            <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow" >
        </RouterLink>
        <div class="question">
            <div class="word">
                新學期開始了，
                <br>狐獴小學的同學們迎來了一個特別的機會——可以自由選修一門自己真正感興趣的課程。
                <br>小狐獴小樂選擇了手工藝課，想親手製作小禮物；
                <br>小狸貓小彤則選了天文學，期待探索星空的奧秘。
                <div class="Q5">
                    <br>這是一個關於依照興趣做選擇的題目。假如你是狐獴小學的學生，你會選擇什麼課呢？
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
    .Q5{
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