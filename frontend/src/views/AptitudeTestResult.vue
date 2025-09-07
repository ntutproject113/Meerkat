<script setup>
    import Menu from '../components/Menu.vue';
    import { useScoreStore } from '../stores/score'

    const store = useScoreStore()
    
    //把分數整理成物件
    const scores = {
        R: store.R,
        A: store.A,
        E: store.E,
        S: store.S,
        I: store.I,
        C: store.C
    }

    // 轉成陣列並依分數排序，從大到小
    const sortedScores = Object.entries(scores)
        .sort(([, a], [, b]) => b - a) // 依 value 排序，b - a 表示從大到小

    // 取前三個
    const top3 = sortedScores.slice(0, 3).map(([key, value]) => ({ key, value }))

    console.log('前三大分數:', top3)
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="meerkatContainer">
            <img src="../assets/images/aptitude_test_result/AMeerkat.png" class="Ameerkat" v-if="top3[0].key === 'A'"/>
            <img src="../assets/images/aptitude_test_result/CMeerkat.png" class="Cmeerkat" v-if="top3[0].key === 'C'"/>
            <img src="../assets/images/aptitude_test_result/EMeerkat.png" class="Emeerkat" v-if="top3[0].key === 'E'"/>
            <img src="../assets/images/aptitude_test_result/IMeerkat.png" class="Imeerkat" v-if="top3[0].key === 'I'"/>
            <img src="../assets/images/aptitude_test_result/RMeerkat.png" class="Rmeerkat" v-if="top3[0].key === 'R'"/>
            <img src="../assets/images/aptitude_test_result/SMeerkat.png" class="Smeerkat" v-if="top3[0].key === 'S'"/>
        </div>
        <div class="resultTypeContainer">
            <div class="resultTypeContainer1">
                <img src="../assets/images/aptitude_test_result/A.png" class="A1" v-if="top3[0].key === 'A'"/>
                <img src="../assets/images/aptitude_test_result/C.png" class="C1" v-if="top3[0].key === 'C'"/>
                <img src="../assets/images/aptitude_test_result/E.png" class="E1" v-if="top3[0].key === 'E'"/>
                <img src="../assets/images/aptitude_test_result/I.png" class="I1" v-if="top3[0].key === 'I'"/>
                <img src="../assets/images/aptitude_test_result/R.png" class="R1" v-if="top3[0].key === 'R'"/>
                <img src="../assets/images/aptitude_test_result/S.png" class="S1" v-if="top3[0].key === 'S'"/>
            </div>
            <div class="resultTypeContainer2">
                <img src="../assets/images/aptitude_test_result/A.png" class="A2" v-if="top3[1].key === 'A'"/>
                <img src="../assets/images/aptitude_test_result/C.png" class="C2" v-if="top3[1].key === 'C'"/>
                <img src="../assets/images/aptitude_test_result/E.png" class="E2" v-if="top3[1].key === 'E'"/>
                <img src="../assets/images/aptitude_test_result/I.png" class="I2" v-if="top3[1].key === 'I'"/>
                <img src="../assets/images/aptitude_test_result/R.png" class="R2" v-if="top3[1].key === 'R'"/>
                <img src="../assets/images/aptitude_test_result/S.png" class="S2" v-if="top3[1].key === 'S'"/>
            </div>
            <div class="resultTypeContainer3">
                <img src="../assets/images/aptitude_test_result/A.png" class="A3" v-if="top3[2].key === 'A'"/>
                <img src="../assets/images/aptitude_test_result/C.png" class="C3" v-if="top3[2].key === 'C'"/>
                <img src="../assets/images/aptitude_test_result/E.png" class="E3" v-if="top3[2].key === 'E'"/>
                <img src="../assets/images/aptitude_test_result/I.png" class="I3" v-if="top3[2].key === 'I'"/>
                <img src="../assets/images/aptitude_test_result/R.png" class="R3" v-if="top3[2].key === 'R'"/>
                <img src="../assets/images/aptitude_test_result/S.png" class="S3" v-if="top3[2].key === 'S'"/>
            </div>
            <div class="resultWordContainer">
                <div class="word">
                    是「系統建築者」
                    <br>你看見世界的方式，與大多數人不同。 在混亂中，你尋找邏輯；在問題中，你設計解法。你不只是動手做事，更擅長用理性與架構，打造穩定的系統。當他人被困在錯綜複雜的問題裡，你早已開始規劃出口。
                    <br>你是天生的工程師。
                    <br>解決問題，是你給世界最強的魔法。
                </div>
                <div class="arrow">
                    <img src="../assets/images/aptitude_test_result/arrow.png" class="Arrow">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: #47695B;
        display: flex;
    }
    .meerkatContainer{
        display: flex;
        width: 40vw;
        height: 100vh;
    }
    .Ameerkat{
        max-width: 350px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-109%,-50%);
    } 
    .Cmeerkat{
        max-width: 415px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-100%,-50%);
    }
    .Emeerkat{
        max-width: 400px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-97%,-50%);
    }
    .Imeerkat{
        max-width: 440px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-90%,-50%);
    }
    .Rmeerkat{
        max-width: 300px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-110%,-50%);
    }
    .Smeerkat{
        max-width: 410px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-95%,-55%);
    }
    .resultTypeContainer{
        position: relative;
        width: 60vw;
        top:0%;
        right: 0;
    }
    .resultTypeContainer1{
        position: absolute;
        position: relative;
        top: 0;
        width: 150px;
        height: 40vh;
    }
    .A1, .C1, .E1, .I1, .R1, .S1{
        position: absolute;
        left: 0;
        bottom: 5%;
        width: 90%;
    }
    .resultTypeContainer2{
        position: absolute;
        top: 0;
        left: 0;
        transform: translateX(100%);
        width: 150px;
        height: 40vh;
    }
    .A2, .C2, .E2, .I2, .R2, .S2{
        position: absolute;
        left: 0;
        bottom: 5%;
        width: 90%;
    }
    .resultTypeContainer3{
        position: absolute;
        top: 0;
        left: 0;
        transform: translateX(200%);
        width: 150px;
        height: 40vh;
    }
    .A3, .C3, .E3, .I3, .R3, .S3{
        position: absolute;
        left: 0;
        bottom: 5%;
        width: 90%;
    }
    .resultWordContainer{
        position: absolute;
        position: relative;
        bottom: 0;
        width: 465PX;
        height: 60vh;
    }
    .word{
        position: absolute;
        top: 0;
        left: 0;
        width: 98%;
        height: 60%;
        font-size: 20px;
        color: #ffffff;
    }
    .arrow{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 40%;
    }
    .Arrow{
        position: absolute;
        top: 0;
        right: 5%;
        width: 25%;
    }
</style>