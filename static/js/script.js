console.log('scripts.js loaded');
function init(){
    document.querySelectorAll("pre>table>tbody>tr>th").forEach(
        (it)=>{
            it.innerHTML =it.textContent.split("_").map(x=>(x[0].toUpperCase()+x.slice(1))).join(" ")
        })

}