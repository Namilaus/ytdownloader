datas = {
    url:'https://www.youtube.com/watch?v=viukm2i-eYY&list=PLwXXfk5wsyAB0jtiodt1i6NB5rvv_ZiKd'
}

fetch('http://127.0.0.1:8000/download_playlist',{
    method:'POST',
    mode:"cors",
    headers: {
        "Content-Type": "application/json",
    },
    body:JSON.stringify(datas)
}).then(res => { 
    console.log(res)
    return res.json()}).then(resp=>console.log(resp))

