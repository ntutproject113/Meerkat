<script setup>
    import Menu from '../components/Menu.vue';
    import { ref, nextTick } from 'vue'

    //userInput: 使用者輸入的文字
    const userInput = ref('')
    //messages: AI預設歡迎訊息
    const messages = ref([
        { type: 'ai', text: '您好，有什麼可以幫忙的嗎？', sender: 'meerkat' }
    ])

    //chatAreaRef: 聊天區域的參考，用於滾動功能
    const chatAreaRef = ref(null)

    function sendMessage(){
        //將使用者輸入的內容去除前後空白並存入content變數
        const content = userInput.value.trim();
        //如果使用者沒有輸入內容，就結束函式
        if (!content) return
        //將使用者輸入內容存進message陣列中，並標記為user
        messages.value.push({ type: 'user', text: content });
        //清空使用者輸入欄位
        userInput.value = '';
        //模擬AI回覆訊息
        setTimeout(() => {
            messages.value.push({ type: 'ai', text: '你說什麼，我看不到' });
            nextTick(() => {
                if (chatAreaRef.value) {
                chatAreaRef.value.scrollTop = chatAreaRef.value.scrollHeight;
                }
            });
        }, 1000);
        nextTick(() => {
            if (chatAreaRef.value) {
                chatAreaRef.value.scrollTop = chatAreaRef.value.scrollHeight;
            }
        });
    }
</script>

<template>
    <div class="page-wrapper">
        <Menu />
        <div class="backgroundcontainer">
            <div class="output">
                <div class="chatArea" ref="chatAreaRef">
                    <!--messages裡面會放很多條訊息，包含使用者輸入的type：user以及ai回覆的type：ai，將他用for迴圈的方是一個一個渲染出來-->
                    <!--給messages中每個被渲染出來的訊息兩個class，一個是統一的訊息風格，一個是針對不同type給予的不同樣式-->
                    <div v-for="(message, index) in messages" :key="index" :class="['chat-bubble',message.type]">
                        <img v-if="message.type === 'ai'" src="../assets/images/q&a/MeerkatAvatar.png" alt="AI頭像" class="avatar"/>
                        <span
                            class="bubble-text"
                            v-html="message.text.replace(/\n/g, '<br>')"
                        ></span>
                    </div>
                </div>
            </div>
            <div class="input">
                <img src="../assets/images/q&a/lines.png" alt="分隔線" class="line" />
                <!--用v-model綁定變數userInput，讓他們可以同步-->
                <!--按Enter後啟動函式-->
                <textarea
                    v-model="userInput"
                    @keyup.enter.exact="sendMessage"
                    placeholder="請輸入您的問題..."
                    class="chat-input"               
                    rows="1"
                ></textarea>
                <button @click="sendMessage" class="send-btn" aria-label="發送"></button>
            </div>    
        </div>
    </div>
</template>

<style scoped>
    .page-wrapper{
        background-color: white;
        min-height: 100vh;
        width: 100%;
        position: relative;
    }
    .backgroundcontainer{
        position: relative;
        max-width: 1100px;
        min-width: 550px;
        min-height: 550px;
        height: 100vh;
        background-image: url('../assets/images/q&a/background.png');
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
        margin: 0 auto;
    }
    .output{
        position: absolute;
        max-width: 1100px;
        width: 93%;
        height: 77vh;
        object-fit: contain;
        left: 50%;
        transform: translate(-50%);
        top: 3.7%;
    }
    .input{
        position: absolute;
        max-width: 1100px;
        width: 90%;
        height: 18vh;
        object-fit: contain;
        left: 50%;
        transform: translate(-50%);
        bottom: 2%;
        display: flex;
        align-items: center;
        z-index: 2;
    }
    .line{
        position: absolute;
        max-width: 112%;
        object-fit:contain;
        left: 50%;
        transform: translate(-50%);
        top: 0;
        z-index: 1;
    }
    .avatar{
        width: 55px;
        height: 55px;
        margin-right: 10px;
        z-index: 2;
    }
    .chatArea{
        position: absolute;
        max-width: 1000px;
        width: 88vw;
        height: 77vh;
        top: 0;
        left: 50%;
        transform: translate(-50%);
        z-index: 2;
        overflow-y: auto;
        padding-right: 8px;
    }
    .chat-bubble {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        margin-top: 8px;
    }
    /*使用者輸入呈現的文字內容靠右*/ 
    .chat-bubble.user {
        justify-content: flex-end;
    }
    /*AI回覆的文字內容靠左*/
    .chat-bubble.ai {
        justify-content: flex-start;
        flex-direction: row;
    }
    .bubble-text {
        background: #47695B;
        color: #fff;
        border-radius: 20px;
        padding: 10px 18px;
        max-width: 60%;
        word-break: break-all;
        margin: 0 10px;
    }
    .chat-bubble.user .bubble-text {
        background: #dbdbdb;
        color: #000;
    }
    .chat-input {
        /*輸入框會撐滿除了按鈕外的空間*/
        flex: 1;
        padding: 10px 16px;
        border-radius: 20px;
        border: 1px solid #ccc;
        font-size: 16px;
        margin-right: 12px;
        resize: none; /* 禁止拖曳改變大小 */
        line-height: 1.5;
        min-height: 40px;
        max-height: 100px;
        overflow-y: auto;
    }
    .send-btn {
        background-image: url('../assets/images/q&a/arrow-black.png');
        background-size: cover;
        cursor: pointer;
        width: 50px;
        height: 35px;
        border: none
    }
</style>