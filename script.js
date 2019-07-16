var totalmin = 0; 
var cur = 0 ;
var state=0; 

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function timer(){
	totalmin = parseInt(getCookie("totalmin"));
	if(totalmin == "" || isNaN(totalmin)) totalmin=0;
	if(state == 0) return; 
	cur +=1;
	totalmin +=1;
	setCookie("totalmin", totalmin, 1000);
	update();
}

function update(){
	document.getElementById("total").innerHTML=parseInt(totalmin / 60 / 60); 
	document.getElementById("hour").innerHTML=parseInt(cur / 60 / 60); 
	var cm=parseInt((cur/60) % 60);
	if(cm < 10)	cm="0"+cm; 
	document.getElementById("minut").innerHTML=cm;
	var cs = parseInt(cur % 60);
	if(cs < 10)	cs="0"+cs;
	document.getElementById("second").innerHTML=cs;
}

function clicked(){
	var sstate="";
	if(state)	sstate="stop";
	else		sstate="start";
	state=1-state;
	document.getElementById("but").value = sstate;
}

function main(){
	setInterval(timer, 1000)
}
