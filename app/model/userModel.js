const {connection} = require('../database/schema');

function postUser(req,res){
  const firstName = typeof(req.body.firstName) === 'string' && req.body.firstName.trim().length > 2 ? req.body.firstName.trim() : false;
  const lastName = typeof(req.body.lastName) === 'string' && req.body.lastName.trim().length > 2 ? req.body.lastName.trim() : false;
  const username = typeof(req.body.username) === 'string' && req.body.username.trim().length > 2 ? req.body.username.trim() : false;
  const password = typeof(req.body.password) === 'string' && req.body.password.trim().length > 4 ? req.body.password.trim() : false;
  const tosAgreement = req.body.tosAgreement ? req.body.tosAgreement : false;

  if(firstName && lastName && username && password && tosAgreement){
    console.log('Requests received...')
    const verifyUserusername = ` SELECT username FROM users.data WHERE username = '${username}' `
    connection.query(verifyUserusername,(err,result) => {
      if(err) res.send(err);
      if(result.length > 0) res.status(400).send(`User "${username}" Already Exists...`);
      else{
        if(result.length < 1){
          const insertUsers = `INSERT INTO users.data (firstname,lastname,username,password,tosAgreement) VALUES('${firstName}', '${lastName}', '${username}', '${password}', '${tosAgreement}')`;
          connection.query(insertUsers, (err,result,fields) => {
            if(err) res.send(err);
            if(result) res.status(201).json({
              Success: `User ${firstName.toUpperCase()} ${lastName.toUpperCase()} Added Successfully.`
            });
            if(fields) console.log(fields);
          });
          
        };
      };
      
    });
        

  }else{
    res.status(400).json({
      Error: 'Missing Required Parameter'
    });
  }    

}


function loginUser(req,res){
  const username = typeof(req.body.username) === 'string' && req.body.username.trim().length > 2 ? req.body.username.trim() : false;
  const password = typeof(req.body.password) === 'string' && req.body.password.trim().length > 4 ? req.body.password.trim() : false;

  if(username && password){
    console.log('Login Information Received');
    const verifyUser = ` SELECT password FROM users.data WHERE username = '${username}' `
    connection.query(verifyUser, (err,result) => {
      if(err) res.send(err);
      if(result.length < 1) res.send('username Not Found...');
      else{
        db_passwd = result[0].password;
        if(password === db_passwd){
          const showUserData = ` SELECT * FROM users.data WHERE username = '${username}' `
          connection.query(showUserData,(err,userData) => {
            if(err) res.status(500).send('Error: Cannot show User Information');
            if(userData){
              delete userData[0].password
              res.status(200).send(userData);
            };
          });
        }else{
          res.status(404).json({
            Error: 'Wrong user credentials...'
          })
        }
      };

    });

  }else{
    res.status(400).json({
      Error: 'Missing Required Parameter'
    });
  }
}

module.exports = {
  postUser,
  loginUser,
}