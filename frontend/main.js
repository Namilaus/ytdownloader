// Elements
const container = document.getElementsByClassName("container")[0]
const input = document.getElementById("url")
const button = document.getElementById("download_button")
const option = document.getElementById("option")

function showLoading() {
    document.getElementById('loading-animation').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loading-animation').style.display = 'none';
}

function errorMsg(text){
    const errorMsg = document.createElement("p")
    errorMsg.classList.add("error")
    errorMsg.textContent = text
    errorMsg.style.display = "block"
    container.appendChild(errorMsg)
}

function removeErrorMsg(){
    errorMsgEl = document.getElementsByClassName("error")[0]
    if(errorMsgEl !== undefined){
        container.removeChild(errorMsgEl)
    }
}

function removeLinkFromContainer(){
    
        if(document.getElementsByClassName("result")[0]){
        const results = document.getElementsByClassName("result")
        for(let index = 0; index < results.length; index++){
            results[index].style.display = "none"
        }
    }

    return
}

function addLinktoContainer(url,title){
    const result = document.createElement("div")
    const resultUrl = document.createElement("p")
    const resultTitle = document.createElement("p")
    const span = document.createElement("span")
    const download_link = document.createElement("a")

    result.classList.add("result")
    resultTitle.textContent =  "Title: " + title
    resultUrl.textContent = "Download Link: "
    download_link.textContent = "Click Here"
    download_link.setAttribute("href",url)
    download_link.setAttribute("target","_blank")

    resultTitle.appendChild(span)
    result.appendChild(resultTitle)
    resultUrl.appendChild(download_link)
    result.appendChild(resultUrl)
    container.appendChild(result)

    result.style.display = "block"
}


button.addEventListener('click',(e)=>{
    
    removeErrorMsg()
    showLoading();
    e.preventDefault()
   
    if(input.value=== '' || option.value === ''){
        hideLoading()
        errorMsg("Either input is blank or option is not selected you may put the url or select one of them options please!")
        console.log(option.value)
        return
    }
    else if(input.value!=='' && option.value === 'download_video'){
    fetch('https://ytdownloader.atayi.net:8443/download_video',{
        method:'POST',
        mode:"cors",
        headers: {
            "Content-Type": "application/json",
        },
        body:JSON.stringify({url:input.value})
    })
        .then(response => { 
            
            if(response.status !== 200){
                removeErrorMsg()
                hideLoading()
                errorMsg("Something went wrong try again, Please make sure that you chose the right Option and type the right link in input")
                return
            }
            return response.json()} )
        .then((response)=>{
            removeLinkFromContainer()
            hideLoading()
            addLinktoContainer(response.url,response.title)
    })
    
}
    else if(input.value!=='' && option.value === 'download_playlist'){
        fetch('https://ytdownloader.atayi.net:8443/download_playlist',{
            method:'POST',
            mode:"cors",
            headers: {
                "Content-Type": "application/json",
            },
            body:JSON.stringify({url:input.value})
            })
            .then(response => { 
                if(response.status !== 200){
                    removeErrorMsg()
                    hideLoading()
                    errorMsg("Something went wrong try again, Please make sure that you chose the right Option and type the right link in input")
                    
                    return
                }
                return response.json() } )
            .then((response)=>{
                removeLinkFromContainer()
                hideLoading()
                const lengthOfPlaylist = response.titles.length
                for(let i = 0; i < lengthOfPlaylist; i++){
                    addLinktoContainer(response.urls[i],response.titles[i])
                }
            })
    }
    else if(input.value!=='' && option.value === 'download_playlist_from'){
        const startIndex  = parseInt(document.getElementById("startIndex").value)
        console.log(startIndex)
        fetch('https://ytdownloader.atayi.net:8443/download_playlist_specific',{
            method:'POST',
            mode:"cors",
            headers: {
                "Content-Type": "application/json",
            },
            body:JSON.stringify({url:input.value,startIndex:startIndex})
            })
            .then(response => { 
                if(response.status !== 200){
                    removeErrorMsg()
                    hideLoading()
                    errorMsg("Something went wrong try again, Please make sure that you chose the right Option and type the right link in input")
                    
                    return
                }
                return response.json()} )
            .then((response)=>{
                removeLinkFromContainer()
                hideLoading()
                const lengthOfPlaylist = response.titles.length
                for(let i = 0; i < lengthOfPlaylist; i++){
                    addLinktoContainer(response.urls[i],response.titles[i])
                }
            })
    }
})


