fetch("https://type.fit/api/quotes")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var quote = data[Math.floor(Math.random() * 1000)].text
    console.log(quote)
    document.querySelector("#quote").innerText = quote;
  });



/* function confirmElimination(){
  var res = confirm("Do you want to delete this journal?");

  if (res){
    return true;
  } else{
    return false;
  }

} */

  
