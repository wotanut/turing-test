var intervalID = window.setInterval(myCallback, 500);

function myCallback() {
  // variables
  
  var xhr = new XMLHttpRequest();
  xhr.open("GET", 'https://turing.wotanutt.repl.co/whoresponded', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4)  { 

      // get the thing from the server
      var serverResponse = JSON.parse(xhr.responseText);
      console.log(serverResponse.column)
      console.log(serverResponse.AI)
      console.log(serverResponse.human)
      // get the two nodes

      if (serverResponse.human != null)
      {
        // need to make this dynamically change to B if it's B
        if (serverResponse.column == "A"){
          node = document.getElementById('A');
          var element = document.getElementById("response-A");

          //If it isn't "undefined" and it isn't "null", then it exists.
          if(typeof(element) != 'undefined' && element != null){
              // element exists so pass and do nothing
          } else{
            let insert = '<p id="response-A"> Respondant A: '  + serverResponse.human + '</p>'
            node.insertAdjacentHTML('afterend', insert);
          }
        }
        else{
          node = document.getElementById('B');
          var element = document.getElementById("response-B");

          //If it isn't "undefined" and it isn't "null", then it exists.
          if(typeof(element) != 'undefined' && element != null){
              // element exists so pass and do nothing
          } else{
            let insert = '<p id="response-B"> Respondant B: '  + serverResponse.human + '</p>'
            node.insertAdjacentHTML('afterend', insert);
          }
        }
      }
      // AI
      if (serverResponse.AI != null)
      {
        if (serverResponse.column == "A"){
          node = document.getElementById('B');
          var element = document.getElementById("response-B");

          //If it isn't "undefined" and it isn't "null", then it exists.
          if(typeof(element) != 'undefined' && element != null){
              // element exists so pass and do nothing
          } else{
            let insert = '<p id="response-B"> Respondant B: '  + serverResponse.AI + '</p>'
            node.insertAdjacentHTML('afterend', insert);
          }
        }
        else{
          node = document.getElementById('B');
          var element = document.getElementById("response-A");

          //If it isn't "undefined" and it isn't "null", then it exists.
          if(typeof(element) != 'undefined' && element != null){
              // element exists so pass and do nothing
          } else{
            let insert = '<p id="response-A"> Respondant A: '  + serverResponse.AI + '</p>'
            node.insertAdjacentHTML('afterend', insert);
          }
        }
      }
    }
  };
  xhr.send(null);
}
