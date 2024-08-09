#!/usr/bin/node

const request = require('request');

const makeRequest = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      makeRequest(arr, i + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      makeRequest(chars, 0);
    }
  }
);
