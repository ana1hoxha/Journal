
fetch("https://type.fit/api/quotes")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var quote = data[Math.floor(Math.random() * 1000)].text
    document.querySelector("#quote").innerText = quote;
    console.log();
  });



document.querySelector("#buttonSubmit").addEventListener("click",()=>{
    console.log("why the fuck")
})

  
  