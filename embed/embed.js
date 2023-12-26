var footerHTML = `<img src="https://rusk-games.pages.dev/images/logo.png" style = "height:3.4vh; margin-left: 10px"> <p style="margin-left: 15px;margin-top: 3vh; color: #ff894d; font-size: 1.2em">Find more games like this on <a href="https://rusk-games.pages.dev" style="color: skyblue"> https://rusk-games.pages.dev</a></p>`
const scriptElement = document.createElement("script");
scriptElement.src = "../js/custom.js";

document.body.appendChild(scriptElement);

if (
    window.location.href !== "https://rusk-games.pages.dev" &&
    window.location.href !== "https://rusk-games.rusk2016.repl.co"
) {
    // Create a footer with HTML from the variable 'footer' and set its height to 5vh
    const footer = document.createElement("footer");
    footer.innerHTML = footerHTML;
    footer.style.height = "6vh";
    footer.style.position = "fixed";
    footer.style.bottom = "0";
    footer.style.backgroundColor = '#404040';
    footer.style.width = "100%";
    footer.style.display = "flex";
    footer.style.alignItems = "center";
    
    document.body.appendChild(footer);

    $(document).ready(function () {$('#iframe').css({'height': '94vh'});})
}
