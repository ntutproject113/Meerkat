<script setup>
    import { ref } from 'vue'
    import Menu from '../components/Menu.vue';
    import { useScoreStore } from '../stores/score'
    import { useRouter } from 'vue-router'

    const store = useScoreStore()
    const router = useRouter()

    const options = [
        { key: 'R', text: '安排場地、架設設備、佈置教室' },
        { key: 'A', text: '拍攝、剪影片，設計活動紀錄冊' },
        { key: 'E', text: '負責流程總管、指揮整體節奏' },
        { key: 'S', text: '帶小隊、陪學員互動與照顧情緒' },
        { key: 'I', text: '設計前測與後測問卷、分析回饋資料' },
        { key: 'C', text: '整理物資、點名簽到、填寫報表' }
    ] .sort(() => Math.random() - 0.5)
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

    function calculateScore() {
        clickOrder.value.forEach((order, index) => {
            if (order !== null) {
            // 名次越前面，分數越高 (6 - order)
                let score = 6 - order
                store.addScore(options[index].key, score)
            }
        })
        console.log("目前分數，R", store.R,"A", store.A,"E", store.E,"S", store.S,"I", store.I,"C", store.C)
        router.push('/aptitudeTest5')
    }

    function resetOrder() {
        clickOrder.value = Array(options.length).fill(null)
        currentOrder.value = 0
    }
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest5" v-slot="{ navigate }">
            <img
                src="../assets/images/aptitude_test_result/arrow.png" 
                class="arrow" 
                @click="()=>{
                    calculateScore();
                    navigate({ query: { R: R.value, A: A.value, E: E.value, S: S.value, I: I.value, C: C.value } });
                }"
            >
        </RouterLink>
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
    }
    .Q4{
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