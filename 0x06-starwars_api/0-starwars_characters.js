#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request({ url: url, strictSSL: false }, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  const charactersArray = JSON.parse(body).characters;

  function printCharacterName(index) {
    if (index >= charactersArray.length) {
      return;
    }

    request({ url: charactersArray[index], strictSSL: false }, function (err, res, body) {
      if (err) {
        console.error(err);
        return;
      }

      console.log(JSON.parse(body).name);
      printCharacterName(index + 1);  // Recursively call the next character
    });
  }

  printCharacterName(0);  // Start with the first character
});
