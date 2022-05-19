

//pull the pathname from window location
const activePage = window.location.pathname;

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


var i = 0;
var txt = 'The site was established in 2022. The site is for people who love dogs.';
var speed=20;

function fun_text(){
    if (i < txt.length) {
        document.getElementById("text_open").innerHTML += txt.charAt(i);
        i++;
        setTimeout(fun_text, speed);
        }
  }

  var text1 ='Monthly cost on total dogs you rais is:'
  function message(){
    if(document.getElementById("FullName").value=="" && document.getElementById("email").value=="" ){
      window.alert("בבקשה תמלא את שדה השם והמייל");
    }
    if(document.getElementById("FullName").value!=="" && document.getElementById("email").value!=="" ){
      document.getElementById("ans").innerHTML=text1+document.getElementById("numDog").value*200;
      window.alert("תודה על שיתוף הפעולה , המסמך נשלח ");
     
    }
    if(document.getElementById("FullName").value!=="" && document.getElementById("email").value =="" ){
      window.alert("בבקשה מלא את המייל");
    }
    if(document.getElementById("FullName").value=="" && document.getElementById("email").value !=="" ){
      window.alert("בבקשה מלא את השם");
    }
   
    }
    