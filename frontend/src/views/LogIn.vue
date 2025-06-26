<script setup>
    import Menu from '../components/Menu.vue';
    import { ref } from 'vue'
    import { useRouter } from 'vue-router';

    const username = ref('')  //用來儲存帳號的變數
    const password = ref('')  //用來儲存密碼的變數
    const router = useRouter();  

    function login(){
        if (!username.value || !password.value){
            alert('請輸入帳號和密碼')
            return
        }
        router.push({ name: 'Planning' })
        console.log('登入中...',username.value,password.value)
    }
</script>

<template>
    <div class = "page-wrapper">
        <Menu />
        <img src = "../assets/images/login/logInBoard.png" alt = "登入黑板" class = "logInBlackboard">
        <img src = "../assets/images/login/logInMeerkat.png" alt = "登入小獴" class = "logInMeerkat">
        <img src = "../assets/images/login/Account.png" alt = "帳號文字" class = "account">
        <img src = "../assets/images/login/password.png" alt = "密碼文字" class = "password">
        <RouterLink to = '/' class="guestlink">
            <img  src = "../assets/images/login/GuestWord.png" alt = "訪客按鈕" class = "guest">
        </RouterLink>
        <RouterLink to = "">
            <img src = "../assets/images/login/signUpWord.png" alt = "登入按鈕" class = "signIn">
        </RouterLink>
        <form @submit.prevent="login" class = "loginform">
            <div class="inputBox1Container">
                <input
                    v-model="username" 
                    type="text"
                    class = "inputaccount"
                    required
                />
            </div>
            <div class="inputBox2Container">
                <input
                    v-model="password"
                    type="password"
                    class = "inputpassword"
                    required
                />
            </div>
            <button type="submit" class="submitButton"></button>
        </form>
    </div>
</template>

<style scoped>
    .page-wrapper {
        background-color: #dbdbdb;
        min-height: 100vh;
        width: 100%;
        position: relative;
    }
    .logInBlackboard{
        position: absolute;
        top: 15%;           /* 距離頂端 15% */
        left: 50%;           /* 水平中心 */
        transform: translateX(-40%);
        height: 50%;        /* 可按需求修改 */
        object-fit: contain;
        z-index: 1;
    }
    .logInMeerkat{
        position: absolute;
        bottom: 0%;           /* 距離頂端 15% */
        left: 50%;           /* 水平中心 */
        transform: translateX(-124%);
        height: 66%;        /* 可按需求修改 */
        object-fit: contain;
        z-index: 2;
    }
    .account{
        position: absolute;
        top: 30%;
        left: 50%;
        transform: translateX(-115%);
        height: 12%;
        object-fit: contain;
        z-index: 3;
    }
    .password{
        position: absolute;
        top: 41%;
        left: 50%;
        transform: translateX(-140%);
        height: 9%;
        object-fit: contain;
        z-index: 3;
    }
    .logInWord{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translateX(-21%);
        height: 14%;
        object-fit: contain;
        z-index: 3;
    }
    .inputaccount{
        position: absolute;
        top: 9%;
        height: 35px;
        width: 175px;
        font-size: 18px;
        z-index: 5;
        padding-left: 15px;
        padding-right: 15px;
        background-color: transparent;
        border: transparent;
        outline: none;
        color:white;  

    }
    .inputpassword{
        position: absolute;
        top: 7.5%;
        height: 35px;
        width: 175px;
        font-size: 18px;
        z-index: 5;
        padding-left: 15px;
        padding-right: 15px;
        background-color: transparent;
        border: transparent;
        outline: none;
        color:white;  
    }
    .submitButton{
        background: url(../assets/images/login/logInWord.png)no-repeat center / contain;
        background-color: transparent;
        border: none;
        position: absolute;
        top:52%;
        left: 50%;
        transform: translateX(-20%);
        width:100px;
        height: 60px;
        z-index: 4;
        cursor: pointer;
    }
    .inputBox1Container{
        position: absolute;
        top: 32%;
        left: 50%;
        transform: translateX(-10%);
        height: 45px;
        width: 200px;
        background: url(../assets/images/login/inputbox.png)no-repeat center / contain;
        background-size: 200px 45px;
        z-index: 4;
    }
    .inputBox2Container{
        position: absolute;
        top: 42%;
        left: 50%;
        transform: translateX(-10%);
        height: 45px;
        width: 200px;
        background: url(../assets/images/login/inputbox.png)no-repeat center / contain;
        background-size: 200px 45px;
        z-index: 4;
    }
    .guest{
        position: absolute;
        width: 90px;
        top:65%;
        left:50%;
        transform: translateX(-145%);
        z-index: 4;
    }
    .signIn{
        position: absolute;
        width: 92px;
        top:64%;
        left:50%;
        transform: translateX(120%);
        z-index: 4;
    }
</style>

<style>
html, body {
  height: 100%;
  margin: 0;
}
</style>