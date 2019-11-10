const express = require("express");
const app = express();
const PORT = process.env.PORT || 8080;
const path = require('path');
var randomCoordinates = require('random-coordinates');
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(express.urlencoded());
const csvdata = require('csvdata')

const { body,validationResult } = require('express-validator');
const { sanitizeBody } = require('express-validator');

var dataCounter = 0;
var data = [];
var archive = [];
var newData = false;
var restCounter = 0;

// lat, lng, date, time, address, description, cat
var parsed = [];

var masterData = csvdata.load('crimeTest.csv').then(
	function (data) {
		for (var i = 0; i < data.length; i++) {
			console.log(data[i]);
			var iterator = 0;

			var json = {};
			for (var key in data[i]) {
			    if (data[i].hasOwnProperty(key)) {           
			        // console.log(key, dat[i][key]);
			        if (iterator == 0) {
			        	json['lat'] = key;
			        }
			       	else if (iterator == 1) {
			        	json['lng'] = key;
			        }	else if (iterator == 2) {
			        	json['date'] = key + " Philadelphia";
			        }	else if (iterator == 3) {
			        	json['time'] = key;
			        }	else if (iterator == 4) {
			        	json['address'] = key;
			        }	else if (iterator == 5) {
			        	json['description'] = key;
			        }	else if (iterator == 6) {
			        	json['category'] = key;
			        }
			    }
			    iterator++;
			}
			// parsed.push(json1);
			parsed.push(json);
		}
		console.log(parsed);
	}
);


// set static folder 
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


// app data basic function
app.post('/post', function(req, res) {
	var sendFile = JSON.stringify(parsed);
	res.send(sendFile);
});


app.listen(PORT, ()=> console.log('Server Started'));
