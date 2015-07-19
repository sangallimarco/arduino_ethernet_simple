var telnet = require('telnet')
 
telnet.createServer(function (client) {
 
  // listen for the actual data from the client 
  client.on('data', function (b) {
    console.log('Data received' + b);
    client.write(b + "\n");
  })
 
  client.write('connected to Telnet server!')
 
}).listen(23)