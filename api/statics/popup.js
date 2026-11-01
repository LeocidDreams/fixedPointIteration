// reading current json File

function fetchingJsonFile(){
    fetch("./popup.js").then(
        (response)=>{
            if (response.ok){
                return response.json();
            }
        }).then(data=>console.log(data))
        .catch(error=>console.error("Failed to fetch data:",error));
    
}
let btn=document.getElementsByName('name');

btn.addEventListener("click",()=>{
    jsons=fetchingJsonFile();
    let div_=document.getElementById('result-expression');
    Array.from(jsons).forEach((json)=>{
            setTimeout(() => {
                   output= `
                    <div>
                        <label>adim: ${json['id']}</label>
                        <label>bagil hata: ${json['relativeError']}</label>
                        <label>basarili:${json['sucess']}</label>
                    </div>
                    `;
                    div_.appendChild(output);
                    
            }, 5000);   
    });
    

});