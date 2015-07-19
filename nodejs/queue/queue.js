module.exports = function QueueManager (tasks, connection) {
	this.tasks = tasks;
	this.connection = connection;

	var self = this;

	this.next = function () {
		return this.tasks.shift();
	};

	this.exec = function () {
		var i = this.next();

		if (!i) {
			return this.terminate();
		}

		console.log('Sending command:', i);

		this.connection.exec("#>" + i.cmd, function (response){
			console.log('Data received', response);
			
		});

		// force new message
		setTimeout(function(){
				self.exec();
			}, i.t);

	};

	this.terminate = function () {
		console.log('Terminate');
		this.connection.destroy();
	}
};