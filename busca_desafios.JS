const sqlite3 = require('sqlite3').verbose();
var express = require('express');
var cors = require('cors');
var app = express();

app.use(cors());

// open a database connection
let db = new sqlite3.Database('./lanceumdesafio.db', (err) => {
  if (err) {
    console.error(err.message);
  }
});


app.get('/desafios', function(req,res){
  db.all("SELECT * FROM desafio ORDER BY usuario", function(err, row) {

    if (row){ res.send(row); };
      
  });
});

app.post('/votar/1', function(req, res){
  //registra o voto
  var usu = 'usua1';
  var vts = null;

  db.get("SELECT votos FROM desafio WHERE usuario = ?", [usu], function(err, row) {

    if (row){
      vts = row.votos +1;
      db.run("UPDATE desafio SET votos = ? WHERE usuario = ?", [vts, usu], function(err, row) {

        if (err){ console.log(err.message); };
      
        console.log('ATUALIZADO');
    
        db.all("SELECT * FROM desafio ORDER BY usuario", function(err, row) {
      
          if (row){ res.send(row); };
              
        });
      
      });

    }
  });
});

app.post('/votar/2', function(req, res){
  //registra o voto
  var usu = 'usua2';
  var vts = null;

  db.get("SELECT votos FROM desafio WHERE usuario = ?", [usu], function(err, row) {

    if (row){
      vts = row.votos +1;
      db.run("UPDATE desafio SET votos = ? WHERE usuario = ?", [vts, usu], function(err, row) {

        if (err){ console.log(err.message); };
      
        console.log('ATUALIZADO');
    
        db.all("SELECT * FROM desafio ORDER BY usuario", function(err, row) {
      
          if (row){ res.send(row); };
              
        });
      
      });

    }
  });
});

app.post('/votar/3', function(req, res){
  //registra o voto
  var usu = 'usua3';
  var vts = null;

  db.get("SELECT votos FROM desafio WHERE usuario = ?", [usu], function(err, row) {

    if (row){
      vts = row.votos +1;
      db.run("UPDATE desafio SET votos = ? WHERE usuario = ?", [vts, usu], function(err, row) {

        if (err){ console.log(err.message); };
      
        console.log('ATUALIZADO');
    
        db.all("SELECT * FROM desafio ORDER BY usuario", function(err, row) {
      
          if (row){ res.send(row); };
              
        });
      
      });

    }
  });
});

app.post('/votar/4', function(req, res){
  //registra o voto
  var usu = 'usua4';
  var vts = null;

  db.get("SELECT votos FROM desafio WHERE usuario = ?", [usu], function(err, row) {

    if (row){
      vts = row.votos +1;
      db.run("UPDATE desafio SET votos = ? WHERE usuario = ?", [vts, usu], function(err, row) {

        if (err){ console.log(err.message); };
      
        console.log('ATUALIZADO');
    
        db.all("SELECT * FROM desafio ORDER BY usuario", function(err, row) {
      
          if (row){ res.send(row); };
              
        });
      
      });

    }
  });
});


app.listen(4000, function(){
  
  console.log('localhost OK');
});

