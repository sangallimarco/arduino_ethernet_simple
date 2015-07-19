var telnet = require('another-telnet-client'),
	queueFactory = require('./queue/queue'),
	connection = new telnet(),
	params = {
	  host: '192.168.1.46',
	  port: 23,
	  irs: '\n',
	  ors: '\n',
	  shellPrompt: null,
	  timeout: 15000,
	  // removeEcho: 4
	}

	;

/**
 * Init tasks
 * [onT description]
 * @type {Number}
 */
var onT = 300000,
	offT = 3000,
	tasks = [
		{cmd: 'D0', t: offT},
		{cmd: 'E0', t: offT},
		{cmd: 'F0', t: offT},
		{cmd: 'G0', t: offT},
		{cmd: 'H0', t: offT},

		{cmd: 'D1', t: onT},
		{cmd: 'D0', t: offT},
		{cmd: 'E1', t: onT},
		{cmd: 'E0', t: offT},
		{cmd: 'F1', t: onT},
		{cmd: 'F0', t: offT},
		{cmd: 'G1', t: onT},
		{cmd: 'G0', t: offT},
		{cmd: 'H1', t: onT},
		{cmd: 'H0', t: offT}

	],
	queue = null;


/**
 * Connect to client
 * @param  {queueFactory} prompt) {             queue [description]
 * @return {[type]}               [description]
 */
connection.on('connect', function(prompt) {
	console.log('Connected, sending commands');
	queue = new queueFactory(tasks, connection);
	queue.exec();
});
connection.on('timeout', function() {
  console.log('Timeout');
});
connection.on('close', function() {
  console.log('Closed');
});
connection.connect(params);

console.log('Running...');
