/* modal box */

let customMBox = document.getElementById("custom-modal-box");
let modalBoxContainer = document.getElementById("modal-box-container");
let modalImg = document.getElementById("modal-img");

let imgs = document.getElementsByClassName("art-pics");
for (var i = 0; i < imgs.length; i++) {
    imgs[i].addEventListener("click", function () {
        customMBox.style.display = "block";
        let curSrc = this.src;
        modalImg.src = this.src;
    });
}
modalBoxContainer.addEventListener("click", function () {
    customMBox.style.display = "none";
});

/* selection artwork homepage */
var aa = document.querySelector("#aa");
var bb = document.querySelector("#bb");
var cc = document.querySelector("#cc");


var dA = document.querySelector("#directory-A");
var dB = document.querySelector("#directory-B");
var dC = document.querySelector("#directory-C");

window.addEventListener("load", function () {
    aa.style.borderBottom = "2px solid black";

});
aa.addEventListener("click", function () {
    aa.style.borderBottom = "2px solid black";
    bb.style.borderBottom = "none";
    cc.style.borderBottom = "none";

    dA.style.display = "block";
    dB.style.display = "none";
    dC.style.display = "none";

});

bb.addEventListener("click", function () {
    aa.style.borderBottom = "none";
    bb.style.borderBottom = "2px solid black";
    cc.style.borderBottom = "none";

    dA.style.display = "none";
    dB.style.display = "block";
    dC.style.display = "none";

});

cc.addEventListener("click", function () {
    aa.style.borderBottom = "none";
    bb.style.borderBottom = "none";
    cc.style.borderBottom = "2px solid black";

    dA.style.display = "none";
    dB.style.display = "none";
    dC.style.display = "block";

});
