(function(){
	var Dojoobject={
		click: function(onclick){
			document.getElementById('clickbutton').addEventListener('click',onclick);
		},

		hover: function(hoverIn, hoverOut){
			document.getElementById('hoverbutton').addEventListener('mouseover',hoverIn);
			document.getElementById('hoverbutton').addEventListener('mouseout',hoverOut);
		}
	}

	var $Dojo=function $Dojo(buttonID){
		return Dojoobject;
	};

	window.$Dojo = $Dojo;
})();

$Dojo("#clickbutton").click(function(){ console.log("The button was clicked!"); alert('The button was click!') });

$Dojo("#hoverbutton").hover(function(){ console.log(" Hover on button!") }, function(){ console.log("Hover off!") });
