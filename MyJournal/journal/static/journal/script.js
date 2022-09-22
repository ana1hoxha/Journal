import Journal from Journal.models
"""js e ka ne anene e kundert rradhen e importit , ndryshe nga """


fetch("https://type.fit/api/quotes")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var quote = data[Math.floor(Math.random() * 1000)].text
    document.querySelector("#quote").innerText = quote;
    console.log();
  });



document.querySelector("#submitButton").addEventListener("click",(event)=>{
  if(document.querySelector("#information").value.length != 0){
    textInfo = document.querySelector("#information").value;
    //here i should find how to run python shell inside of the javascript
    
  }
  
  else {
    return false;
  }
  
})



  
  