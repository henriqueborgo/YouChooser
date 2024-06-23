"use strict";

//Elements
const btnPositive = document.querySelector(".positive-button");
const btnNegative = document.querySelector(".negative-button");
const video = document.querySelector("#video");
const form = document.querySelector("form");
let videoID = "i9164jc-j_M";
let userResponse = 0;
const autoPlay = "?autoplay=1";

//Prevent the page to refress when clicking button
//Prevenet default (post/get method) behavior
form.addEventListener("submit", function (event) {
  event.preventDefault;
});

//Function when click the POSITIVE button
btnPositive.addEventListener("click", function () {
  userResponse = 1;
  const videoSrc = `https://www.youtube.com/embed/${videoID}${autoPlay}`;
  video.src = videoSrc;
});

//Function when click the NEGATIVE button
