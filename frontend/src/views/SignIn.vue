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

    function submit(){
        if( !name.value || !sex.value  || !email.value || !phone.value || !school.value || !major.value || !grade.value || !interest.value || !skill.value || !plan.value){
            alert('請完成所有表格')
            return
        }else{
            router.push({ name: 'Home'})
            console.log(name.value,sex.value,email.value,phone.value,school.value,major,grade.value,interest.value,skill.value,plan.value)
        }
    }
</script>

<template>
    <div class = "page-wrapper">
        <Menu />
        <img src = "../assets/images/signin/Paper.png" alt="註冊紙張" class="paper"/>
        <div class="signInTitle">註冊</div>
        <form @submit.prevent="submit" class = "signinform">
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
                <div class="sp">/</div>
                <label class="sexlabel male" :class="{ selected: sex === '男' }">   <!-- 點字就可以觸發input選取或輸入(連動的效果) -->
                    <input type="radio" v-model="sex" value="男" class="hiddenRadio" />男
                </label>  <!-- class的條件切換 如果sex的值等於特定內容時就多加一個class -->
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
                <label class="planlabel study" :class="{ checked: plan === '升學' }">
                    <input type="radio" v-model="plan" value="升學" class="hiddenCheckbox"/>
                    <span class="custom-checkbox"></span>升學
                </label>
                <label class="planlabel work" :class="{ checked: plan === '就業' }">
                    <input type="radio" v-model="plan" value="就業" class="hiddenCheckbox"/>
                    <span class="custom-checkbox"></span>就業
                </label>
                <label class="planlabel unknow" :class="{ checked: plan === '不清楚' }">
                    <input type="radio" v-model="plan" value="不清楚" class="hiddenCheckbox"/>
                    <span class="custom-checkbox"></span>不清楚
                </label>
            </div>
            <button type="submit" class="submitButton"></button>
        </form>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: white;
        min-height: 100vh;
        width: 100%;
        position: absolute;
    }
    .paper{
        position: relative;
        left: 50%;
        transform: translateX(-50%);
        width: 800px;
        z-index: 1;
    }
    .signInTitle{
        position: absolute;   
        top: 15%;             
        left: 50%;            
        transform: translateX(-50%);
        font-size: 2.3rem;
        z-index: 10;
    }
    .name{
        position: absolute;   
        top: 22%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .sex{
        position: absolute;   
        top: 26%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .sp{
        position: absolute;   
        top: 26.3%;             
        left: 50%;            
        transform: translateX(-1400%);
        font-size: 1.3rem;
        z-index: 10; 
    }
    .email{
        position: absolute;   
        top: 30%;             
        left: 50%;            
        transform: translateX(-245%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .phone{
        position: absolute;   
        top: 34%;             
        left: 50%;            
        transform: translateX(-185%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .school{
        position: absolute;   
        top: 38%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .major{
        position: absolute;   
        top: 42%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .grade{
        position: absolute;   
        top: 46%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .interest{
        position: absolute;   
        top: 50%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .skill{
        position: absolute;   
        top: 54%;             
        left: 50%;            
        transform: translateX(-265%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .plan{
        position: absolute;   
        top: 58%;             
        left: 50%;            
        transform: translateX(-95%);
        font-size: 1.1rem;
        z-index: 10;
    }
    .submitButton{
        background: url(../assets/images/signin/Submit.png)no-repeat center / contain;
        background-size: 120px;
        z-index: 11;
        position: absolute;
        top: 77%;
        left: 50%;
        transform: translateX(-50%);
        width: 90px;
        height: 65px;
        background-color: transparent;
        border: transparent;
        cursor: pointer;
    }
    .inputname{
        position: absolute;
        z-index: 12;
        top: 22%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputemail{
        position: absolute;
        z-index: 12;
        top: 30%;
        left: 50%;
        transform: translateX(-55%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputphone{
        position: absolute;
        z-index: 12;
        top: 34%;
        left: 50%;
        transform: translateX(-42%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputschool{
        position: absolute;
        z-index: 12;
        top: 38%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputmajor{
        position: absolute;
        z-index: 12;
        top: 42%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputgrade{
        position: absolute;
        z-index: 12;
        top: 46%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputinterest{
        position: absolute;
        z-index: 12;
        top: 50%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .inputskill{
        position: absolute;
        z-index: 12;
        top: 54%;
        left: 50%;
        transform: translateX(-57%);
        border: none;
        border-bottom: 1.75px solid #000000;
        background-color: transparent;
        outline: none;
        font-size: 18px;
    }
    .hiddenRadio {
        display: none; /* 隱藏 radio 圈圈 */
    }
    .sexlabel {
        position: absolute;
        top: 25.7%;
        font-size: 1.1rem;
        cursor: pointer;
        z-index: 11;
        padding: 4px 10px;
        border-radius: 100%;        /* 讓邊框變圓形 */
        border: 5px solid transparent; /* 預設邊框透明 */
        display: inline-flex;      /* 讓文字跟邊框合在一起 */
        transition: background-color 0.3s;
        align-items: center;
        justify-content: center;
        width: 5px;               /* 你想要的圈大小 */
        height: 15px;
    }
    .sexlabel.male {
        left: 50%;  /* 你想放哪裡自己調整 */
        transform: translateX(-355%);
    }
    .sexlabel.female {
        left: 50%;  /* 右邊一點 */
        transform: translateX(-175%);
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
    .custom-checkbox {
        display: inline-block;
        width: 45px;
        height: 45px;
        background-image: url('../assets/images/signin/checkbox.png');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        flex-shrink: 0;
}
    .planlabel{
        position: absolute;
        left: 50%;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: 10px;
        z-index: 13;
    }
    .planlabel.study{
        top: 62.5%;
        transform: translateX(-180%);
    }
    .planlabel.work{
        top: 67%;
        transform: translateX(-180%);
    }
    .planlabel.unknow{
        top: 71.5%;
        transform: translateX(-151%);
    }
    .planlabel.checked .custom-checkbox {
        background-image: url('../assets/images/signin/checked.png');
        background-size: 38px 35px;
        transform: translateX(-10%);
        transform: translateY(-12.5%);
    }
</style>