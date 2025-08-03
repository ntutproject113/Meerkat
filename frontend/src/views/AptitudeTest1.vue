<script setup>
    import { ref } from 'vue'
    import Menu from '../components/Menu.vue';
    
    const options = [
        { key: 'R', text: '組裝佈景、布置現場、搬桌椅' },
        { key: 'A', text: '設計海報、社群宣傳圖' },
        { key: 'E', text: '和贊助廠商聯絡、對外溝通' },
        { key: 'S', text: '招呼來賓、帶新朋友認識流程' },
        { key: 'I', text: '查找活動案例、設計問卷蒐集意見' },
        { key: 'C', text: '整理活動物資、記帳、製作進度追蹤表' }
    ] 
    //Array(陣列長度).fill(預設值)，[null, null, null, null, null, null]
    const clickOrder = ref(Array(options.length).fill(null))
    //curremtOrder控制我現在已經點擊第幾次了
    const currentOrder = ref(0)

    function handleClick(index) {
        //如果這個選項還沒被點過的話，就將該選項(用index表示)的值紀錄成當下的currentOrder
        if (clickOrder.value[index] === null) {
            clickOrder.value[index] = currentOrder.value
            currentOrder.value++
        }
    }

    function resetOrder() {
        clickOrder.value = Array(options.length).fill(null)
        currentOrder.value = 0
    }
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest2">
            <img src="../assets/images/aptitude_test_result/arrow.png" class="arrow" >
        </RouterLink>
        <div class="question">
            <div class="word">
                在狐獴小學裡，每年最熱鬧的事情就是班上舉辦的「春季歡樂活動」了！
                <br>這一天，老師宣布：「這次的活動，我們採取自由分工，大家可以自由挑選自己想做的任務。」
                <br>狐狸小杰立刻興奮地舉手：「我想負責布置場地！」
                <br>小浣熊阿花則說：「我想帶領遊戲的規則講解！」
                <br>大家一邊討論，一邊決定自己的任務。
                <div class="Q1">
                    <br>這正是一個關於如何分工合作的題目，如果你是狐獴小學的學生，請依據你對這些任務的喜好排名？
                </div>
            </div>
        </div>
        <div class="reply">
            <span class="w1">排序</span>
            <span class="w2">選項</span>
            <div class="choice">
                <!--從 options 裡一個一個取出來，每一筆叫做 option，它的順序叫做 index-->
                <!--如果點擊div，就會觸發handleClick(index)這個函式-->
                <div
                    v-for="(option, index) in options"
                    :key="option.key"
                    class="option-item"
                    @click="handleClick(index)"
                >
                    <!--該標籤要for迴圈下，所以會跟著迴圈跑6次-->
                    <span>{{ option.text }}</span>
                    <!--如果clickOrder[index]不為空值，代表已經被點擊過了-->
                    <span v-if="clickOrder[index] !== null" class="answer">
                    <!--就會顯示這段文字(順序)-->
                    {{ clickOrder[index] + 1 }}
                </span>
                </div>
                <button class="reset-btn" @click="resetOrder">重置</button>
            </div>
        </div>    
    </div>
</template>

<style scoped>
    .page-wrapper{
        display: flex;
        justify-content: center;
        background-color: #47695B;
    }
    .question{
        display: flex;
        position: absolute;
        justify-content: center;
        top: 0;
        max-width: 770px;
        width: 100vw;
        height: 37vh;
    }
    .word{
        align-self: flex-end;
        margin-bottom: 2%;
        color: #ffffff;
    }
    .Q1{
        font-weight: bold;
    }
    .reply{
        display: flex;
        position: absolute;
        bottom: 0;
        max-width: 770px;
        width: 100vw;
        height: 60vh;
    }
    .answer{
        position: absolute;
        left: -10%;
    }
    .choice{
        position: absolute;
        left: 15%;
        max-width: 500.5px;
        width: 65vw;
        height: 52.7vh;
        color: #ffffff;
        padding-top: 30px;
        font-size: 20px;;
    }
    .option-item {
        display: flex;
        align-items: center;
        padding: 8px 12px;
        cursor: pointer;
        margin-bottom: 10px; /* 這裡調整間距，數字越大距離越大 */
        position: relative;
    }
    .w1{
        font-size: 20px;;
        position: absolute;
        left: 6.5%;
        color: #ffffff;
        font-weight: bold;
    }
    .w2{
        font-size: 20px;;
        position: absolute;
        left: 16.5%;
        color: #ffffff;
        font-weight: bold;
    }
    .arrow{
        z-index: 2;
        position: absolute;
        bottom: 5%;
        right: 5%;
        width: 100px;
    }
</style>