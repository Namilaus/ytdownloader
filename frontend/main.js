// Elements
const container = document.getElementsByClassName("container")[0]
const input = document.getElementById("url")
const button = document.getElementById("download_button")
const option = document.getElementById("option")


function errorMsg(text){
    const errorMsg = document.createElement("p")
    errorMsg.classList.add("error")
    errorMsg.textContent = text
    errorMsg.style.display = "block"
    container.appendChild(errorMsg)
}

function addLinktoContainer(url,title){
    const result = document.createElement("div")
    const resultUrl = document.createElement("p")
    const resultTitle = document.createElement("p")
    result.classList.add("result")
    resultUrl.textContent = url
    resultTitle.textContent = title
    result.style.display = "block"
    result.appendChild(resultUrl)
    result.appendChild(resultTitle)
    container.appendChild(result)
}

function removeErrorMsg(){
    errorMsgEl = document.getElementsByClassName("error")[0]
    if(errorMsgEl !== undefined){
        container.removeChild(errorMsgEl)
    }
}

button.addEventListener('click',(e)=>{
    
    removeErrorMsg()
    
    e.preventDefault()
   
    if(input.value==='' || option.value ===''){
        errorMsg("Either input is blank or option is not selected you may put the url or select one of them options please!")
        console.log(option.value)
        return
    }
    else if(input.value!=='' && option.value === 'download_video'){
    fetch('http://127.0.0.1:8000/download_video',{
    method:'POST',
    mode:"cors",
    headers: {
        "Content-Type": "application/json",
    },
    body:JSON.stringify({url:input.value})
}).then(res => { 

    console.log(res)
    return res.json()}).then((resp)=>{
        addLinktoContainer(resp.url,resp.title)
    })
    }
})













// datas = {
//     url:'https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd'
// }

// fetch('http://127.0.0.1:8000/download_playlist',{
//     method:'POST',
//     mode:"cors",
//     headers: {
//         "Content-Type": "application/json",
//     },
//     body:JSON.stringify(datas)
// }).then(res => { 
//     console.log(res)
//     return res.json()}).then(resp=>console.log(resp))

