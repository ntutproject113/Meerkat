<script setup>
    import Menu from '../components/Menu.vue'
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import router from '../router'

    const name = ref('')
    const sex = ref('')
    const email = ref('')
    const phone = ref('')
    const school = ref('')
    const major = ref('')
    const grade = ref('')
    const interest = ref('')
    const skill = ref('')
    const plan = ref('')
    const username = ref('')     //儲存使用者帳號
    const password = ref('')  //儲存使用者密碼
    const showSetPrompt = ref(false)     //控制提示框是否出現

    function submit(){
        if( !name.value || !sex.value  || !email.value || !phone.value || !school.value || !major.value || !grade.value || !interest.value || !skill.value || !plan.value){
            alert('請完成所有表格')
            return
        }else{
            showSetPrompt.value = true   //顯示帳號密碼視窗
            console.log(name.value,sex.value,email.value,phone.value,school.value,major,grade.value,interest.value,skill.value,plan.value)
        }
    }
    function setAccountPassword(){
        if (!username.value || !password.value) {
        alert('請輸入帳號與密碼')
        return
        }
        router.push({ name: 'AptitudeTest' })
    }
</script>

<template>
    <div class = "page-wrapper">
        <Menu />
        <div class="graduatedMeerkatC">
            <img src="../assets/images/signin/graduated.png" class="graduatedMeerkat"/>
        </div>
        <!-- 基本資料表單 -->
        <form @submit.prevent="submit" class = "signinform">
            <div class="question">
                <div class="signInTitle">註冊</div>
                <div class="nameContainer">
                    <div class="name">01. 姓名：</div>
                    <input
                        v-model="name" 
                        type="text"
                        class = "inputname"
                        required
                    />
                </div>
                <div class="sexContainer">
                    <div class="sex">02. 性別：</div>
                    <label class="sexlabel male" :class="{ selected: sex === '男' }">   <!-- 點字就可以觸發input選取或輸入(連動的效果) -->
                        <input type="radio" v-model="sex" value="男" class="hiddenRadio" />男
                    </label>  <!-- class的條件切換 如果sex的值等於特定內容時就多加一個class -->
                    <div class="sp">/</div>
                    <label class="sexlabel female" :class="{ selected: sex === '女' }">
                        <input type="radio" v-model="sex" value="女" class="hiddenRadio" />女
                    </label>
                </div>
                <div class="emailContainer">
                    <div class="email">03. Email：</div>
                    <input
                        v-model="email" 
                        type="email"
                        class = "inputemail"
                        required
                    />
                </div>
                <div class="phoneContainer">
                    <div class="phone">04. 手機號碼：</div>
                    <input
                        v-model="phone" 
                        type="phone"
                        class = "inputphone"
                        required
                    />
                </div>
                <div class="schoolContainer">
                    <div class="school">05. 學校：</div>
                    <input
                        v-model="school" 
                        type="text"
                        class = "inputschool"
                        required
                    />
                </div>
                <div class="majorContainer">
                    <div class="major">06. 科系：</div>
                    <input
                        v-model="major" 
                        type="text"
                        class = "inputmajor"
                        required
                    />
                </div>
                <div class="gradeContainer">
                    <div class="grade">07. 年級：</div>
                    <input
                        v-model="grade" 
                        type="number"
                        class = "inputgrade"
                        required
                    />
                </div>
                <div class="interestContainer">
                    <div class="interest">08. 興趣：</div>
                    <input
                        v-model="interest" 
                        type="text"
                        class = "inputinterest"
                        required
                    />
                </div>
                <div class="skillContainer">
                    <div class="skill">09. 專長：</div>
                    <input
                        v-model="skill" 
                        type="text"
                        class = "inputskill"
                        required
                    />
                </div>
                <div class="planContainer">
                    <div class="plan">10. 目前對畢業後的規劃為？</div>
                    <label class="planlabel" :class="{ checked: plan === '升學' }">
                        <input type="radio" v-model="plan" value="升學" class="hiddenCheckbox"/>
                        <img src="../assets/images/signin/Checkbox.png" class="checkBox" />
                        <span class="custom-checkbox"></span>升學
                        <img src="../assets/images/signin/checked.png" class="checkedBox1" v-show="plan === '升學'" />
                    </label>
                    <label class="planlabel" :class="{ checked: plan === '就業' }">
                        <input type="radio" v-model="plan" value="就業" class="hiddenCheckbox"/>
                        <img src="../assets/images/signin/Checkbox.png" class="checkBox" />
                        <span class="custom-checkbox"></span>就業
                        <img src="../assets/images/signin/checked.png" class="checkedBox2" v-show="plan === '就業'"/>
                    </label>
                    <label class="planlabel" :class="{ checked: plan === '不清楚' }">
                        <input type="radio" v-model="plan" value="不清楚" class="hiddenCheckbox"/>
                        <img src="../assets/images/signin/Checkbox.png" class="checkBox" />
                        <span class="custom-checkbox"></span>不清楚
                        <img src="../assets/images/signin/checked.png" class="checkedBox3" v-show="plan === '不清楚'" />
                    </label>
                </div>
                <button type="submit" class="submitButton"></button>
            </div>
        </form>
        <!--<form class="account">
            <img src="../assets/images/login/Account.png"> 
        </form>-->
        <div class="background2" v-if="showSetPrompt">
            <img src="../assets/images/login/logInBoard.png" class="board"/>
            <img src="../assets/images/login/Account.png" class="account" />
            <img src="../assets/images/login/password.png" class="password" />
            <img src="../assets/images/login/inputbox.png" class="inputbox1" />
            <input 
                type="email"
                v-model="username"
                name="account"
                class="inputaccount" 
                placeholder="請輸入電子郵件"
            />
            <img src="../assets/images/login/inputbox.png" class="inputbox2" />
            <input 
                type="password" 
                v-model="password"
                name="password" 
                class="inputpassword"
                placeholder="請輸入您的登入密碼"
            />
            <img src="../assets/images/signin/Submit.png" class="signin" @click="setAccountPassword"/>
        </div>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: white;
        min-height: 100vh;
        width: 100%;
        position: relative;
        display: flex;
    }
    .paper{
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 800px;
        z-index: 1;
    }
    .signinform {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 700px;
        height: 1050px;
        display: flex;
        flex-direction: column;
        background: url(../assets/images/signin/Paper.png) no-repeat center top;
        background-size: contain;
        margin-top: 50px ;
    }
    .question{
        margin-top: 100px ;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        width: 425px;
        height: 850px;
        display: flex;
        flex-direction: column;
        gap: 28px;
    }
    .signInTitle{
        font-size: 2.3rem;
        z-index: 10;
        align-self:center;
    }
    .nameContainer, .emailContainer, .phoneContainer, .schoolContainer, .majorContainer, .gradeContainer, .interestContainer, .skillContainer{
        display: flex;
        font-size: 1.1rem;
        z-index: 10PX;
    }
    .inputname, .inputemail, .inputphone, .inputschool, .inputmajor, .inputgrade, .inputinterest, .inputskill{
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .sexContainer{
        display: flex;
        font-size: 1.1rem;
        z-index: 10PX;
        gap:15px;
    }
    .sp{
        position: relative;
        top: 15% ;
    }    
    .hiddenRadio {
        display: none; /* 隱藏 radio 圈圈 */
    }
    .sexlabel {
        cursor: pointer;
        padding: 4px 10px;
        border-radius: 100%;       
        border: 4px solid transparent; 
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 5px;
        height: 15px;
    }
    .sexlabel:hover {
        border-color: #e24f4f;
    }
    .sexlabel.selected {
        border-color: #b73131; /* 被選中時的背景色 */
    }
    .hiddenCheckbox{
        display: none;
    }
    .submitButton{
        background: url(../assets/images/signin/Submit.png)no-repeat center / contain;
        background-size: 120px;
        width: 90px;
        height: 65px;
        background-color: transparent;
        border: transparent;
        cursor: pointer;
        align-self:center;
    }
    .plan{
        display: flex;
        flex-direction: column;
    }
    .planlabel{
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        z-index: 13;
        margin-left: 25px;
        margin-top:15px;
        gap:5px ;
    }
    .checkBox{
        width: 22px;
    }
    .checkedBox1, .checkedBox2, .checkedBox3{
        width: 40px;
        position: relative;
        left:-19% ;
        margin-top: -5px;
    }
    .checkedBox3{
        left:-23.5% ;
    }
    .account{
        background: url(../assets/images/login/logInBoard.png) no-repeat;
        z-index: 5;
    }
    .graduatedMeerkat{
        position:relative;
        top: 45%;
        left: 50%;
        width: 650px;
        object-fit: cover;
        transform: rotate(-20deg);
    }
    .graduatedMeerkatC{
        position: relative;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 6;
        pointer-events: none; /* 圖片不擋點擊事件 */
    }
    .background2{
        position: fixed;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.6);
        z-index: 7;
        display: flex;
    }
    .board{
        position: fixed;
        width: 525px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 8;
    }
    .account{
        position: fixed;
        width: 200px;
        top: 50%;
        left: 50%;
        transform: translate(-120%, -75%);
        z-index: 9;
    }
    .password{
        position: fixed;
        width: 155px;
        top: 50%;
        left: 50%;
        transform: translate(-142%, -0%);
        z-index: 9;
    }
    .inputbox1{
        position: fixed;
        width: 250px;
        top: 50%;
        left: 50%;
        transform: translate(-24%, -110%);
        z-index: 9;
    }
    .inputbox2{
        position: fixed;
        width: 250px;
        top: 50%;
        left: 50%;
        transform: translate(-24%, 25%);
        z-index: 9;
    }
    .inputaccount{
        position: fixed;
        width: 200px;
        top: 50%;
        left: 50%;
        transform: translate(-20%, -223%);
        z-index: 10;
        font-size: 20px;
        color: #ffffff;
        background: none;
        border: none;
        outline: none;
    }
    .inputpassword{
        position: fixed;
        width: 200px;
        top: 50%;
        left: 50%;
        transform: translate(-20%, 157%);
        z-index: 10;
        font-size: 20px;
        background: none;
        border: none;
        outline: none;
        color: #ffffff;
    }
    .signin{
        position: fixed;
        width: 165px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, 82%);
        z-index: 11;
    }
    input::placeholder {
        color: #dbdbdb;            /* 淺灰色 */
        font-size: 18px;
    }
</style>