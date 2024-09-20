#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    return console.error(err);
  }

  if (res.statusCode !== 200) {
    return console.error(`Error: ${res.statusCode}`);
  }

  const charactersArray = JSON.parse(body).characters;
  charactersArray.forEach((character) => {
    request(character, (err, res, body) => {
      if (err) {
        return console.error(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
