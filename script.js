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


// Function when clicking the POSITIVE button
btnPositive.addEventListener("click", function (event) {
  //Prevent screen to refresh
  event.preventDefault()

  //update the variable with user response
  userResponse = 1;
    // Call the API to input the answer in the JSON file
    let apiURL = `http://localhost:5000/dataJSON/${userResponse}`;
    const requestOptions = {
      method: 'PUT'
    };
    fetch(apiURL, requestOptions)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response not ok')};
          return response.json()
      })
      .then(data => {
        console.log(data);
        // When the API call completes successfully, play the video
        const videoSrc = `https://www.youtube.com/embed/${videoID}${autoPlay}`;
        video.src = videoSrc;  
        })
      // Handle the error here, display an error message to the user
      .catch (error => {
        console.error(`There has been a problem with the fetch operation: `, error)});
    });


//Function when click the NEGATIVE button
