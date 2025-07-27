<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="question">
            <div class="word">
                在狐獴小學裡，每年最熱鬧的事情就是班上舉辦的「春季歡樂活動」了！
                <br>這一天，老師宣布：「這次的活動，我們採取自由分工，大家可以自由挑選自己想做的任務。」
                <br>狐狸小杰立刻興奮地舉手：「我想負責布置場地！」
                <br>小浣熊阿花則說：「我想帶領遊戲的規則講解！」
                <br>大家一邊討論，一邊決定自己的任務。
                <div class="Q1">
                    <br>這正是一個關於如何分工合作的題目，你覺得，如果你是狐獴小學的學生，你會選擇哪個任務呢？
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
    .Q1{
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
</style>