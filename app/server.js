const express = require('express');
const bodyParser = require('body-parser');
const handlers = require('./lib/handlers');
const app = express();
const {postUser,loginUser} = require('./model/userModel')

app.use(bodyParser.urlencoded({
  extended: true
}));

app.use(express.json())

app.use(bodyParser.json());

PORT = 3000;

app.use(express.static(__dirname + '/public'))

app.get('/', (req, res) => {
  handlers.index((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});

app.get('/create-user', (req, res) => {
  handlers.createUser((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});

app.get('/login-user', (req, res) => {
  handlers.loginPage((statusCode,finalOutput) => {
    res.status(statusCode).send(finalOutput);
  });
});


app.post('/user-created',postUser);

app.post('/user-loggedin',loginUser);



app.listen(PORT, () => {
  console.log('App is listening on Port:',PORT);
});

