"use strict";

function MainLoadState() {
	GameState.call(this);
};

MainLoadState.prototype = new GameState();
MainLoadState.prototype.constructor = MainLoadState;
MainLoadState.prototype.backgroundImage = 0;

MainLoadState.prototype.loadPercentage = 0;

MainLoadState.prototype.init = function() {		// use arguments here to pass saved state data.

	this.backgroundImage = document.getElementById("MainLoadState_bg");

	let payloadSuccess = function(res) {
		console.log("MainLoadState: download complete - parsing loadData");
		asset_parseLoadData(res);
		contextMenuState.init.call(contextMenuState);		// init contextMenu items
		main_menu();
	}.bind(this);

	console.log("MainLoadState: loading remotely");
	loadJsonPayload("jsfdata/main.jsf")
		.then(payloadSuccess)
		.catch(payloadError);

};


MainLoadState.prototype.input = function(e) { }

MainLoadState.prototype.update = function() { }


MainLoadState.prototype.render = function() {
	_context.globalAlpha = 1;

	var fullWidth = ((_screenWidth/2)|0);
	var barWidth = fullWidth * this.loadPercentage;
	var barX = fullWidth - (fullWidth/2)|0;
	var barY = _screenHeight - 128;

	_context.drawImage(this.backgroundImage,0,0,1024,768,0,0,_screenWidth,_screenHeight);

	_context.beginPath();
	_context.moveTo(barX-6, barY-6);
	_context.lineTo((barX-6) + fullWidth + 12, barY-6);
	_context.lineTo((barX-6) + fullWidth + 12, barY-6+76);
	_context.lineTo(barX-6, barY-6+76);
	_context.lineTo(barX-6, barY-6);
	_context.closePath();
	_context.lineWidth = 4;
	_context.strokeStyle = "#afb1a7";
	_context.stroke();

	_context.fillStyle = "#afb1a7";
	_context.fillRect(barX,barY,barWidth,64);

	_context.globalAlpha = 1;

};
