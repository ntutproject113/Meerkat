<script setup>
    import { ref } from 'vue'
    import Menu from '../components/Menu.vue';
    import { useScoreStore } from '../stores/score'
    import { useRouter } from 'vue-router'
    
    const store = useScoreStore()
    const router = useRouter()

    const options = [
        { key: 'R', text: '動手做的實作營隊（木工、機器人、創客）' },
        { key: 'A', text: '藝術或創作營（繪畫、設計、攝影）' },
        { key: 'E', text: '商業營（簡報技巧、創業提案、行銷挑戰）' },
        { key: 'S', text: '志工營（陪伴孩童、與長輩互動）' },
        { key: 'I', text: '學術探索營（研究、模擬、調查設計）' },
        { key: 'C', text: '行政實習（資料整理、流程操作體驗）' }
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
        router.push('/aptitudeTest4')
    }

    function resetOrder() {
        clickOrder.value = Array(options.length).fill(null)
        currentOrder.value = 0
    }
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <RouterLink to = "/aptitudeTest4" v-slot="{ navigate }">
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
                寒暑假快到了，
                <br>狐獴小學的校園布告欄貼出一張海報：「快來報名課外活動，培養新興趣或提升自己！」
                <br>小狐獴小安想報名烹飪課，學習做出美味的點心；
                <br>而小狐獴小美想挑戰攝影，捕捉美麗的校園風景。
                <div class="Q3">
                    <br>這是一個關於寒暑假如何利用時間自我成長的題目。你會報名什麼課外活動呢？
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
    .Q3{
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