util.setInterval(function () {
	util.download({
		"url": "http://uinnova.com:9009/doorstatus",
		"type": "text",
		"success": function (t) {
			//print(t);
			t = string.trim(t)
				msgArray = string.split(t, ":");
			var door_id = msgArray[0];
			var status = msgArray[1];
			print(door_id + ':' + status);
		},
		"error": function (t) {
			print(t);
		}
	});
}, 1000);
