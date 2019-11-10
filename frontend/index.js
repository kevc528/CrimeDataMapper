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
var newData = false;


coords = [{status: "active", lat: 40.7127837,lng: -74.0059413, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 34.0522342, lng: -118.2436849, temp: 24, Sat: 1351, speed: 215}, 	
{status: "active", lat: 41.8781136, lng: -87.6297982, temp: 24, Sat: 1351, speed: 215}, 	
{status: "active", lat: 29.7604267, lng: -95.3698028, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 39.9525839, lng: -75.1652215, temp: 24, Sat: 1351, speed: 215}, 
{status: "active", lat: 33.4483771, lng: -112.0740373, temp: 24, Sat: 1351, speed: 215},
{status: "active", lat: 29.4241219, lng: -98.4936282, temp: 24, Sat: 1351, speed: 215},
{status: "passive"},
{status: "passive"},
{status: "passive"},
];

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
	if (newData == true) {
		res.send(JSON.stringify(data[dataCounter]));
		dataCounter++;
		newData = false;
	}
	else {
		res.send(JSON.stringify({status: "passive"}));
	}
});

app.post('/test', function(req, res) {
	"Test Post"
	res.send(coords[Math.floor(Math.random() * 10)]);
});

// for the reset buttons
app.post('/reset', function(req, res) {
	dataCounter = 0;
	newData = false;
	data = [];
	res.send("Reset Complete")
});

app.post('/csv', function(req, res) {
	console.log("CSV Request Recieved");
	res.send(JSON.stringify(data));
});

app.post('/restore', function(req, res) {
	res.send(data);
});

app.post('/data', function(req, res) {
	data.push(req.body);
	newData = true;
	res.send(200);
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
