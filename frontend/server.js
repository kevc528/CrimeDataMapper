const express = require("express");
const app = express();
const PORT = process.env.PORT || 8080;
const path = require('path');
var randomCoordinates = require('random-coordinates');
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(express.urlencoded());

const { body,validationResult } = require('express-validator');
const { sanitizeBody } = require('express-validator');

var dataCounter = 0;
var data = [];
var archive = [];
var newData = false;
var restCounter = 0;


coords = [{status: "active", lat: 40.7127837,lng: -74.0059413, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 34.0522342, lng: -118.2436849, temp: 24, Sat: 1351, speed: 215}, 	
{status: "active", lat: 41.8781136, lng: -87.6297982, temp: 24, Sat: 1351, speed: 215}, 	
{status: "active", lat: 29.7604267, lng: -95.3698028, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 39.9525839, lng: -75.1652215, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 33.4483771, lng: -112.0740373, temp: 24, Sat: 1351, speed: 215},
{status: "active", lat: 29.4241219, lng: -98.4936282, temp: 24, Sat: 1351, speed: 215},
];

function hex2a(hexx) {
    var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

// set static folder 
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

/*
app.get('/login', function(req, res) {
	res.sendFile(path.join(__dirname, 'public', 'login.html'));
});

app.post('/login', function(req, res) {
	console.log(req.body);
	res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
*/

// app data basic function
app.post('/post', function(req, res) {
	if (dataCounter > 0) {
		var info = data.pop();
		archive.push(info);
		dataCounter--;
		console.log("SENDING");
		console.log(info);
		res.send(JSON.stringify(info));
	}
	else {
		console.log("PASSIVE");
		res.send(JSON.stringify({status: "passive"}));
	}
});


app.post('/test', function(req, res) {
	"Test Post"
	res.send(coords[Math.floor(Math.random() * 10)]);
});

// for the reset buttons
app.post('/reset', function(req, res) {
	console.log("Status Reset")
	dataCounter = 0;
	newData = false;
	data = [];
	archive = [];
	res.send(200);
});

app.post('/csv', function(req, res) {
	console.log("CSV Request Recieved");
	res.send(JSON.stringify(data));
});

app.post('/restore', function(req, res) {
	if (restCounter == archive.length) {
		restCounter = 0;
	}
	res.send(archive[restCounter]);
	restCounter++;
});

app.post('/data', function(req, res) {
	try {

	console.log(req.body);
	var hex2 = hex2a(req.body.data);

	var str = hex2.split(",");

	
	var latitude = parseFloat(str[0]);
	var longitude = parseFloat(str[1]);
	var alt = parseFloat(str[2]);
	var temperature = parseFloat(str[3]);
	var speedIndicator = parseFloat(str[4]);
	var satNum = req.body.IMEI;
	

	var obj = {status: "active", lat: latitude,lng: longitude, temp: temperature, Sat: alt, speed: speedIndicator};
	//{status: "active", code: str};
	// {status: "active", lat: latitude,lng: longitude, temp: temperature, Sat: satNum, speed: alt};
	console.log(obj.status);
	console.log(obj.lat);
	console.log(obj.lng);
	console.log(obj.temp);
	console.log(obj.Sat);
	console.log(obj.speed);

	data.push({status: "active", lat: latitude,lng: longitude, temp: temperature, Sat: alt, speed: speedIndicator});
	console.log((typeof({status: "active", lat: latitude,lng: longitude, temp: temperature, Sat: satNum, speed: alt})));

	dataCounter++;
	newData = true;
	res.send(200);
	} catch {
		res.send(200);
	}
});

// establish access
app.post('/access', function(req, res) {
	res.redirect('/');

/*
	var user = req.body.loginUsername;
	var pass = req.body.loginPassword;
	if (user == "ayang015@seas.upenn.edu" && pass == "bakken") {
		res.redirect('/');
	}
	else {
		res.redirect('/');
	}
	*/
});


app.listen(PORT, ()=> console.log('Server Started'));
