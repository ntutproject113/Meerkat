<script setup>
    import { ref } from 'vue'
    import Menu from '../components/Menu.vue';
    import { useScoreStore } from '../stores/score'
    import { useRouter } from 'vue-router'

    const store = useScoreStore()
    const router = useRouter()

    const options = [
        { key: 'R', text: '工藝實作、創客課、工程實驗類' },
        { key: 'A', text: '設計思考、視覺設計、插畫創作課' },
        { key: 'E', text: '簡報溝通、創業模擬、行銷策略課' },
        { key: 'S', text: '輔導技巧、心理學、助人技巧課程' },
        { key: 'I', text: '研究法、資料分析、統計推論課' },
        { key: 'C', text: '行政流程、報表工具、實務管理課' }
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
        router.push('/aptitudeTest6')
    }

    function resetOrder() {
        clickOrder.value = Array(options.length).fill(null)
        currentOrder.value = 0
    }
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest6" v-slot="{ navigate }">
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
                新學期開始了，
                <br>狐獴小學的同學們迎來了一個特別的機會——可以自由選修一門自己真正感興趣的課程。
                <br>小狐獴小樂選擇了手工藝課，想親手製作小禮物；
                <br>小狸貓小彤則選了天文學，期待探索星空的奧秘。
                <div class="Q5">
                    <br>這是一個關於依照興趣做選擇的題目。假如你是狐獴小學的學生，你會選擇什麼課呢？
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
    .Q5{
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