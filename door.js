// --------------------------------
//scene id:  20170811064312816579
// --------------------------------

var d01 = object.find("d01");
var d02 = object.find("d02");
var ui = null;

// ----------------------------------
// set init door status to Dg/close
// Dc: open
// Dg: close
// ----------------------------------
d01.addProperty("device_id", "D01");
d01.addProperty("status", "Dg");
d02.addProperty("device_id", "D02");
d02.addProperty("status", "Dg");


function change_ui_image(ui) {
	var urlBase = "http://www.3dmomoda.com/mmdclient/script/examples/demos/";
	util.downloadTexture({
		"url": urlBase + "demo_panel_001.png",
		"success": function (tex) {
			ui.setImage("Button", tex);
		}
	});
}

function show_banner(obj, status_str) {
	var offsetY = obj.size.y;
	ui.setObject(obj, Vector3(0, offsetY, 0));
	ui.setText("Button/Text", status_str);
	change_ui_image(ui);
}

function fly_and_change(door, status) {
	// door status change to open
	if (status == 'Dc') {
		camera.flyTo({
			"eye": door.center + Vector3(1.5, 1.5, 5),
			"target": door.center,
			"time": 2.5,
			"complete": function () {
				door.setColorFlash(true, Color.red, 2.5);
				show_banner(door, door.getProperty("device_id") + " Opened");
				door.Open();
			}
		});
	}
	// door status change to close
	if (status == 'Dg') {
		camera.flyTo({
			"eye": door.center + Vector3(1.5, 1.5, 5),
			"target": door.center,
			"time": 1.5,
			"complete": function () {
				door.setColorFlash(false);
				show_banner(door, door.getProperty("device_id") + " Closed");
				door.Close();
			}
		});
	}
}

function change_door_status(door_id, status) {
	// status changed in door 01
	if (door_id == 'D01' && status != d01.getProperty('status')) {
		//print('change door' + door_id + ' status to ' + status + ' from ' + d01.getProperty('status'));
		d01.addProperty("status", status);
		fly_and_change(d01, status);
	}
	// status changed in door 01
	if (door_id == 'D02' && status != d02.getProperty('status')) {
		//print('change door' + door_id + ' status to ' + status + ' from ' + d02.getProperty('status'));
		d02.addProperty("status", status);
		fly_and_change(d02, status);
	}
}

// init banner
util.download({
	"url": "http://www.3dmomoda.com/mmdclient/script/examples/demos/outline_button.bundle",
	"success": function (res) {
		ui = gui.create(res);
		ui.setObject(null, null);
		ui.setScale(0.3, 0.3);
	}
});

gui.createButton("Open D01", Rect(40, 60, 70, 30), function () {
	camera.flyTo({
		"eye": d01.center + Vector3(1.5, 1.5, 5),
		"target": d01.center,
		"time": 2.5,
		"complete": function () {
			d01.setColorFlash(true, Color.red, 2.5);
			show_banner(d01, "D01 Opened");
			d01.Open();
			d01.addProperty("status", "Dc");
		}
	});

});

gui.createButton("Close D01", Rect(40, 100, 70, 30), function () {
	d01.setColorFlash(false);
	show_banner(d01, "D01 Closed");
	d01.Close();
	d01.addProperty("status", "Dg");
});

gui.createButton("Open D02", Rect(40, 140, 70, 30), function () {
	camera.flyTo({
		"eye": d02.center + Vector3(1.5, 1.5, 5),
		"target": d02.center,
		"time": 2.5,
		"complete": function () {
			d02.setColorFlash(true, Color.red, 2.5);
			show_banner(d02, "D02 Opened");
			d02.Open();
			d02.addProperty("status", "Dc");
		}
	});

});

gui.createButton("Close D02", Rect(40, 180, 70, 30), function () {
	d02.setColorFlash(false);
	show_banner(d02, "D02 Close");
	d02.Close();
	d02.addProperty("status", "Dg");
});

gui.createButton("Listen", Rect(40, 220, 60, 30), function () {
	util.setInterval(function () {
		util.download({
			"url": "http://uinnova.com:9009/doorstatus",
			"type": "text",
			"success": function (t) {
				t = string.trim(t);
				msgArray = string.split(t, ":");
				var door_id = msgArray[0];
				var status = msgArray[1];
				change_door_status(door_id, status);
			},
			"error": function (t) {
				print(t);
			}
		});
	}, 1500);
});

gui.createButton("Reset", Rect(40, 260, 60, 30), function () {
	camera.flyTo({
		"eye": Vector3(20, 40, -50),
		"target": Vector3(3, 4, 5),
		"time": 1,
		"complete": function () {
			ui.setObject(null, null);
		}
	});
});
