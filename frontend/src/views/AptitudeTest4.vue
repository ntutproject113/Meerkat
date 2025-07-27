<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="question">
            <div class="word">
                暑假營隊開跑了，
                <br>老師對狐獴小學的營隊工作人員說：「大家可以挑選自己擅長或想挑戰的工作內容。」
                <br>小狐獴小強選擇負責帶隊，小貓咪小莉則決定嘗試設計海報。
                <br>雖然挑戰不少，但大家都在努力突破自己。
                <div class="Q4">
                    <br>這是一個關於發揮專長並勇於挑戰的題目。你會選擇什麼工作呢？
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
    .Q4{
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