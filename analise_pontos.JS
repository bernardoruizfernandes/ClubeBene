const sqlite3 = require('sqlite3').verbose();
var express = require('express');
var cors = require('cors');
var app = express();

 app.use(cors());

// open a database connection
let db = new sqlite3.Database('./dadosbene.db', (err) => {
  if (err) {
    console.error(err.message);
  }
});

var usu = 'arieluz';

app.get('/pontos/', function(req, res){

  db.get("SELECT * FROM pontos WHERE usuario = ?", [usu], function(err, row) {

    if (row){
      res.send(row.pontos.toString());
    }

    else{
      console.log('sem pontos');
    }
    
  });
});


app.listen(4000, function(){
  console.log('localhost OK');
});

// close the database connection
//db.close((err) => {
//  if (err) {
//    return console.error(err.message);
//  }
//});

