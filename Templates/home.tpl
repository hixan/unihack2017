<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
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
          <a class="navbar-brand" href="#">Home</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="/about">about</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  <div class=upload-box>
    
    
    
    <form action="/uploading" method="post" enctype="multipart/form-data" style="position:center;">
      <div class="box">
        <input type="file" name="data" id="file-1" class="inputfile inputfile-1" multiple style="display: none;" />
        <label for="file-1"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="17" viewBox="0 0 20 17"><path d="M10 0l-5.2 4.9h3.3v5.1h3.8v-5.1h3.3l-5.2-4.9zm9.3 11.5l-3.2-2.1h-2l3.4 2.6h-3.5c-.1 0-.2.1-.2.1l-.8 2.3h-6l-.8-2.2c-.1-.1-.1-.2-.2-.2h-3.6l3.4-2.6h-2l-3.2 2.1c-.4.3-.7 1-.6 1.5l.6 3.1c.1.5.7.9 1.2.9h16.3c.6 0 1.1-.4 1.3-.9l.6-3.1c.1-.5-.2-1.2-.7-1.5z"/></svg> <span>Choose a file&hellip;</span></label>
        
      </div>
    </form>
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
