"use strict";

//Read JSON file (currently only works in Google Chrome)
import videoInformation from "./videoInformation.json" with { type: "json" };

//Elements
const btnPositive = document.querySelector(".positive-button");
const btnNegative = document.querySelector(".negative-button");
const video = document.querySelector("#video");
const form = document.querySelector("form");

//Variables
let userResponse = 0;
const autoPlay = "?autoplay=1";
const videoID = videoInformation.id

//Start the page with the desired video
let videoSrc = `https://www.youtube.com/embed/${videoID}`;
video.src = videoSrc;

//Prevent the page to refress when clicking button
form.addEventListener("submit", function (event) {
  event.preventDefault;
});

//Function when click the POSITIVE button
btnPositive.addEventListener("click", function () {
  userResponse = 1;
  //Play the video
  videoSrc = `https://www.youtube.com/embed/${videoID}${autoPlay}`;
  video.src = videoSrc;
});

//Function when click the NEGATIVE button
