document.addEventListener("DOMContentLoaded", () => {

    const toggleBtn = document.getElementById("chat-toggle");
    const chatWindow = document.getElementById("chat-window");
    const closeBtn = document.getElementById("close-chat");
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("message-input");
    const messages = document.getElementById("messages");
    const welcome = document.querySelector(".welcome-screen");
    const newChatBtn = document.getElementById("new-chat-btn");

    // ------------------------
    // Open / Close
    // ------------------------

    toggleBtn.onclick = () => {

        chatWindow.style.display = "flex";

        toggleBtn.style.display = "none";

        input.focus();

    };

    closeBtn.onclick = () => {

        chatWindow.style.display = "none";

        toggleBtn.style.display = "block";

    };

    // ------------------------
    // Scroll
    // ------------------------

    function scrollBottom() {

        messages.scrollTop = messages.scrollHeight;

        document.getElementById("chat-body").scrollTop =
            document.getElementById("chat-body").scrollHeight;

    }

    // ------------------------
    // User Bubble
    // ------------------------

    function addUserMessage(text) {

        const div = document.createElement("div");

        div.className = "user-message";

        div.innerHTML = text;

        messages.appendChild(div);

        scrollBottom();

    }

    // ------------------------
    // Bot Bubble
    // ------------------------

    function addBotMessage(text) {

        const div = document.createElement("div");

        div.className = "bot-message";

        div.innerHTML = text;

        messages.appendChild(div);

        scrollBottom();

    }

    // ------------------------
    // Typing Indicator
    // ------------------------

    function showTyping() {

        const div = document.createElement("div");

        div.className = "bot-message";

        div.id = "typing";

        div.innerHTML = `
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
        `;

        messages.appendChild(div);

        scrollBottom();

    }

    function removeTyping() {

        const typing = document.getElementById("typing");

        if (typing)
            typing.remove();

    }

    // ------------------------
    // Dummy AI Response
    // ------------------------

    async function sendToBackend(message){

    showTyping();

    const response = await fetch("/chatbot/send/",{

        method:"POST",

        headers:{

            "Content-Type":"application/json",

            "X-CSRFToken":getCookie("csrftoken")

        },

        body:JSON.stringify({

            message:message

        })

    });

    const data=await response.json();

    removeTyping();

    addBotMessage(data.response);

}

    // ------------------------
    // Send
    // ------------------------

    function sendMessage() {

        const text = input.value.trim();

        if (!text)
            return;

        if (welcome)
            welcome.style.display = "none";

        addUserMessage(text);

        input.value = "";

        sendToBackend(text);

    }

    sendBtn.onclick = sendMessage;

    // ------------------------
    // Enter Key
    // ------------------------

    input.addEventListener("keydown", function(e){

        if(e.key==="Enter" && !e.shiftKey){

            e.preventDefault();

            sendMessage();

        }

    });

    // ------------------------
    // Suggestion Chips
    // ------------------------

    document.querySelectorAll(".chip").forEach(chip=>{

        chip.onclick=()=>{

            input.value=chip.innerText;

            sendMessage();

        };

    });

    // ------------------------
    // New Chat
    // ------------------------

    newChatBtn.onclick=()=>{

        messages.innerHTML="";

        welcome.style.display="block";

        input.value="";

    };

});

function getCookie(name){

    let cookieValue=null;

    if(document.cookie && document.cookie!==""){

        const cookies=document.cookie.split(";");

        for(let cookie of cookies){

            cookie=cookie.trim();

            if(cookie.startsWith(name+"=")){

                cookieValue=decodeURIComponent(cookie.substring(name.length+1));

                break;

            }

        }

    }

    return cookieValue;

}