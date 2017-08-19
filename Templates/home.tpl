<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8" />
<title>Home</title>
<link rel="stylesheet" href="static/main.css">
<link rel="stylesheet" href="https://bootswatch.com/paper/bootstrap.css">

</head>

<body>
  <div>
    <H1 class="header-text"><a href="./home">Home</a></H1>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" onClick="onclickfunc()">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/home">Home</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="/about">about</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  
  <div class="body">
	<h2>Food in the Fridge</h2>
	<p> </p>
	<a><b>What is it?</b></a>
	<p>Do you have ingrediandts/food in your fridge or pantry 
	which you want to use to make yourself a decent meal? 
	Well now it's easy! Just take or upload a photo and within 
	a few secounds you'll have recipes in front of you. It also 
	lets you know if you are one or two ingrediants off so you can
	decide if you want to quickly duck down to the shops. </p>
	<a><b>The Crew</b></a>
	<p>Alex, Jacobus, Josh</p>
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg" 
		alt="food" style="width:100%;height:80%;">
	
	
  </div>
  <script>
    function onclickfunc(){
      if (document.getElementById("bs-example-navbar-collapse-1").style.display=="none"){
        document.getElementById("bs-example-navbar-collapse-1").style.display="initial"
      }else{
        document.getElementById("bs-example-navbar-collapse-1").style.display="none"
      }
    }
  </script>

</body>

</html>
