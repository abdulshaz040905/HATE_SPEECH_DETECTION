

async function predict(){

let text=document.getElementById("text").value

let response=await fetch("http://127.0.0.1:5000/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
text:text
})

})

let data=await response.json()

document.getElementById("result").innerText=data.prediction

}