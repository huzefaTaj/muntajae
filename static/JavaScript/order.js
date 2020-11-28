 // var c=parseInt( document.getElementById('month').value)
 var name=document.getElementById('name').textContent
 sessionStorage.setItem("name",name)
 console.log(name)
 var price=parseInt(document.getElementById('price').textContent)
 sessionStorage.setItem("price",price)
 console.log(price)

 
 // calender
 function calender(){
 var a=parseInt( document.getElementById('month1').value);
 var b=parseInt( document.getElementById('day1').value);
 var c=parseInt( document.getElementById('year1').value);
 
 var x=parseInt( document.getElementById('month2').value);
 var y=parseInt( document.getElementById('day2').value);
 var z=parseInt( document.getElementById('year2').value);
 
 var date1 = new Date(a+"/"+b+"/"+c); 
 var date2 = new Date(x+"/"+y+"/"+z); 
 
 // To calculate the time difference of two dates 
 var Difference_In_Time = date2.getTime() - date1.getTime(); 
 
 // To calculate the no. of days between two dates 
 var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24); 
 
 // call=document.getElementById('cal').innerHTML=Difference_In_Days+1
  return(call=document.getElementById('cal').innerHTML=Difference_In_Days)
 
 // return(console.log(x))
 
 }
 calender
 