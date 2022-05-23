document.addEventListener("DOMContentLoaded", function() {
    var p = document.getElementById('q');
    var btn = document.getElementById('submit');
    var answer = document.getElementById('question');
    btn.onclick = function(){        
        var xhr = new XMLHttpRequest();

        xhr.open("POST", "https://turing.wotanutt.repl.co/newquestion", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var json = JSON.parse(xhr.responseText);
                console.log(xhr.responseText);
                console.log(xhr.status);
            }
        };
        var data = JSON.stringify({"answer": answer.value});
        xhr.send(data);
      const A = document.getElementById("response-A");
      const B = document.getElementById("response-B");
      A.remove();
      B.remove();
    };
})