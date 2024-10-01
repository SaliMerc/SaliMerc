let humburg=document.getElementById("open");
let close=document.getElementById("close");
let links=document.getElementById("links");
humburg.addEventListener('click', () =>{
    links.style.display='block'
    close.style.display='block'
    humburg.style.display='none'
})
close.addEventListener('click', () =>{
    links.style.display='none'
    close.style.display='none'
    humburg.style.display='block'
})
let hero=document.querySelector(".h1")
hero.addEventListener('dbclick', () =>{
    hero.style.transform='scale(1.3)'
})