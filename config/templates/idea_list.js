function onlyNumber() 
{ 
	var str = 100;
	var Mynum = document.getElementById("inptext").value;
	Mynum =Mynum.replace(/[^0-9]/g,'');
	document.getElementById("inptext").value=Mynum;
	var plus = document.getElementById("inptext").value=Mynum;
	if (plus < str)
	{
		document.getElementById("inptext").value=100;
	}else if (plus > 300)
	{
		document.getElementById("inptext").value=300;
	}
} 
$(document).ready(function(){
	var inp =$("input").val();
	$(".up").on("click",function(){
		setTimeout(function(){
		if (inp == 300)
		{
			inp;
		}
		else{inp ++;}
		$("input").val(inp);
		},500);
	});
	$(".down").on("click",function(){
		setTimeout(function(){
		if (inp == 100)
		{
			inp;
		}
		else if(inp <= 300)
		{
			inp--;
		}
		$("input").val(inp);
		},500);
	});
});
