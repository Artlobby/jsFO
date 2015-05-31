"use strict";

function ContextMenuState() {
	GameState.call(this);
}

ContextMenuState.prototype = new GameState();
ContextMenuState.prototype.constructor = ContextMenuState;


ContextMenuState.prototype.x = 0;
ContextMenuState.prototype.y = 0;
ContextMenuState.prototype.prevX = 0;
ContextMenuState.prototype.prevY = 0;
ContextMenuState.prototype.targetItem = 0;
ContextMenuState.prototype.menuItems = [];
ContextMenuState.prototype.activeItems = [];
ContextMenuState.prototype.objectIndex = 0;

ContextMenuState.prototype.init = function() {}

ContextMenuState.prototype.input = function(e) {
			
	switch(e.type) {
		case "mousemove":
			break;
		case "keydown":
			break;
		case "mousedown":
			break;
		case "mouseup":
			console.log(this.objectIndex);
			mainState.contextMenuAction(this.menuItems[this.targetItem].action, this.objectIndex );	// context menu action
			_mouse.x = this.prevX;	// reset to previous stored mouse location
			_mouse.y = this.prevY;
			main_closeContextMenu();
			
			break;

		case "click":
			break;
		case 'contextmenu':	// switch input modes on mouse2
			break;
	};				
			
			
}

ContextMenuState.prototype.update = function() {
	this.targetItem = Math.max(0,Math.min( ((_mouse.y - this.y)/10)|0, this.menuItems.length-1));	// context menu action
}

ContextMenuState.prototype.render = function() {	
	for(var c = 0; c < this.menuItems.length; c++) {
		_context.drawImage((c == this.targetItem) ? this.menuItems[c].hoverImg : this.menuItems[c].img, this.x, this.y+(40*c));
	}
	
	_context.drawImage(_assets["art/intrface/actarrow.frm"].frameInfo[0][0].img, this.prevX, this.prevY);
	
}