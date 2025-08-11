<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="word">
            在狐獴小學，大家經常有機會自由選擇自己想做的事。
            <br>無論是班上的活動、期末報告，還是寒暑假的課外活動，
            <br>都能讓同學們發現自己的興趣和能力。
            <br>接下來，讓我們看看這些有趣的故事吧！
        </div>
        <div class="image">
            <img src="../assets/images/aptitude_test0/school.png" class="school" />
        </div>
        <div class="meerkat">
            <img src="../assets/images/aptitude_test0/meerkat_head.png" class="meerkat_head" />
        </div>
        <RouterLink to = "/aptitudeTest1">
            <div class="Arrow">
                <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow">
            </div>
        </RouterLink>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: #B0C4DE;
    }
    .word{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 35vh;
        top: 0;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .image{
        display: flex;
        justify-content: center;
        width: 100vw;
        height: 70vh;
        position:absolute;
        bottom: 0;
    }
    .school{
        max-height: 100%;
    }
    .meerkat{
        position: absolute;
        width: 75px;
        height: 30vh;
        top: 0;
        left: 50%;
        transform: translateX(255%);
    }
    .meerkat_head{
        position: absolute;
        bottom: 0;
        width: 75px;
        transform: rotate(-20deg);
    }
    .Arrow{
        position: absolute;
        width: 75px;
        height: 45vh;
        top: 0;
        left: 50%;
        transform: translateX(335%);
    }
    .arrow{
        position: absolute;
        bottom: 0;
        right: 5%;
        width: 100px;
        object-fit: contain;
    }
</style>