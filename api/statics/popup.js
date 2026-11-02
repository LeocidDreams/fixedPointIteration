// reading current json File

function fetchingJsonFile(){
    //requesting /api/iterations and response gives it json format(iterations)
    // fetch("./iteration.json").then(
    //     (response)=>{
    //         if (response.ok){
    //             return response.json();
    //         }
    //     }).then(data=>console.log(data))
    //     .catch(error=>console.error("Failed to fetch data:",error));

    fetch('/api/iterations').then(
        (response)=>{
            if (response.ok){
                return response;
            }
        }
    ).then((data)=>console.log(data))
    .catch((error)=>console.error("Failed to fetch data",error));
    
}
let btn=document.getElementsByName('name');

btn.addEventListener("click",()=>{
    jsons=fetchingJsonFile();
    
    let div_=document.getElementById("result-expression");
    Array.from(jsons).forEach((json)=>{
            // routing current json to /api/iterations/<int:string>
            step=json['step'];
            fetch("/api/iterations/${step}",{method:"GET",
                body:JSON.stringify(json),
            }).then(
                (response)=>{
                    if (response.ok){
                        return response.json();
                    }
                }
            ).catch((error)=>console.error("Failed to fetch data",error));
    });
});