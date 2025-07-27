<script setup>
    import Menu from '../components/Menu.vue';
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="meerkatContainer">
            <img src="../assets/images/signin/graduated.png" class="meerkat" />
        </div>
        <div class="resultTypeContainer">
            <div class="resultTypeContainer1">
                <img src="../assets/images/aptitude_test_result/A.png" class="A1" />
                <img src="../assets/images/aptitude_test_result/C.png" class="C1" />
                <img src="../assets/images/aptitude_test_result/E.png" class="E1" />
                <img src="../assets/images/aptitude_test_result/I.png" class="I1" />
                <img src="../assets/images/aptitude_test_result/R.png" class="R1" />
                <img src="../assets/images/aptitude_test_result/S.png" class="S1" />
            </div>
            <div class="resultTypeContainer2">
                <img src="../assets/images/aptitude_test_result/A.png" class="A2" />
                <img src="../assets/images/aptitude_test_result/C.png" class="C2" />
                <img src="../assets/images/aptitude_test_result/E.png" class="E2" />
                <img src="../assets/images/aptitude_test_result/I.png" class="I2" />
                <img src="../assets/images/aptitude_test_result/R.png" class="R2" />
                <img src="../assets/images/aptitude_test_result/S.png" class="S2" />
            </div>
            <div class="resultTypeContainer3">
                <img src="../assets/images/aptitude_test_result/A.png" class="A3" />
                <img src="../assets/images/aptitude_test_result/C.png" class="C3" />
                <img src="../assets/images/aptitude_test_result/E.png" class="E3" />
                <img src="../assets/images/aptitude_test_result/I.png" class="I3" />
                <img src="../assets/images/aptitude_test_result/R.png" class="R3" />
                <img src="../assets/images/aptitude_test_result/S.png" class="S3" />
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
    .meerkat{
        width: 50vw;
        max-width: 478px;
        object-fit: contain;
        position: absolute;
        top: 50%;
        left: 42.5%;
        transform: translate(-100%,-50%);
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
        display: none;
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
        display: none;
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
        display: none;
    }
    .A1, .C2, .E3{
        display: flex;
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