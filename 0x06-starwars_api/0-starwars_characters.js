#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// API endpoint for the Star Wars API
const endpoint = 'https://swapi-api.hbtn.io/api';

// Get the movie ID from the command-line arguments
const filmId = process.argv[2];

// Make a request to the API to retrieve movie details
request(`${endpoint}/films/${filmId}/`, async function (error, response, body) {
  if (error) return console.log(error);

  // Parse the API response to extract character URLs
  const characters = JSON.parse(body).characters;

  // Iterate through each character URL and retrieve details
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      // Make a request to the character URL
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          // Parse the character details response and print the character name
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
