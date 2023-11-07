var btn = document.querySelector("#btnForRemove")

function Remove() {
    btn.remove()
}

var input=document.querySelector("#MyInput")
function ShowAlert() {
    alert("you are searching for " + input.value)
}

var num1 = document.querySelector("#num1")
var num2 = document.querySelector("#num2")
var num3 = document.querySelector("#num3")

function img1() {
    num1.innerText++
}
function img2() {
    num2.innerText++
}
function img3() {
    num3.innerText++
}