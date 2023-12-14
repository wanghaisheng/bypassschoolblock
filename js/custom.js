/*

Custom script

This file will not be overwritten by the updater

*/

// JavaScript code
window.onload = function() {
  $('iframe').not('.flash').attr('srcdoc', `
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body style="">
    <style>
      body{
        background-color: #8b460b; 
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      .loader{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
        margin-top: 13px;

      }
      @keyframes rotate {
        from {
          transform: rotate(0deg);
        }
        to {
          transform: rotate(360deg);
        }
      }

      svg {
        animation: rotate 2s linear infinite;
      }

    </style>
    <div class='center'>
    <img src="https://rusk-games.pages.dev/images/logo.png" alt="" width='360'>
    <div class="loader">
      <svg height="40" width="40" xmlns="http://www.w3.org/2000/svg">
        <path d="M 20 5 A 15 15 10 0 0 5 18" fill="transparent" stroke="#f48d41" stroke-width="3" stroke-linecap="round" />


      </svg>


    </div>
    </div>
  </body>
  </html>
  `)
    setTimeout(function() {
        $("iframe").removeAttr("srcdoc");

    }, 2000); // Hide the loading screen after 1 second
};

function search_animal() {
  let input = document.getElementById("searchbar").value;
  input = input.toLowerCase();
  let x = document.getElementsByClassName("animals");

  for (i = 0; i < x.length; i++) {
    if (!x[i].innerHTML.toLowerCase().includes(input)) {
      x[i].style.display = "none";
    } else {
      x[i].style.display = "block";
    }
  }
}