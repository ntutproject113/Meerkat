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

    function submit(){
        if( !name.value || !sex.value || !email.value || !phone.value || !school.value || !major.value || grade.value || interest.value || skill.value){
            alert('請完成所有表格')
            return
        }else{
            router.push({ name: 'Home'})
        }
    }
</script>

<template>
    <div class = "page-wrapper">
        <Menu />
        <img src = "../assets/images/signin/Paper.png" alt="註冊紙張" class="paper"/>
        <div class="signInTitle">註冊</div>
        <form>
            <div class="nameContainer">
                <div class="name">01. 姓名：__________</div>
            </div>
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
        transform: translateX(-130%);
        font-size: 1.1rem;
        z-index: 10;
    }
</style>