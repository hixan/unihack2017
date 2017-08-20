<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Results</title>
<link rel="stylesheet" href="https://bootswatch.com/paper/bootstrap.css">
<link rel="stylesheet" href="static/main.css">

</head>

<body>
  <div>
    <H1 class="header-text"><a href="./">Home</a></H1>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" onClick="onclickfunc()">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Home</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="/about">about</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  <div class=sidebar-float>
    <div>
      <form action="/upload" method="post" enctype="multipart/form-data" style="position:center;" id="form">
        <div class="box">
          <input type="file" name="upload" id="file" class="inputfile inputfile-1" multiple style="display: none;" />
          <label for="file"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="17" viewBox="0 0 20 17"><path d="M10 0l-5.2 4.9h3.3v5.1h3.8v-5.1h3.3l-5.2-4.9zm9.3 11.5l-3.2-2.1h-2l3.4 2.6h-3.5c-.1 0-.2.1-.2.1l-.8 2.3h-6l-.8-2.2c-.1-.1-.1-.2-.2-.2h-3.6l3.4-2.6h-2l-3.2 2.1c-.4.3-.7 1-.6 1.5l.6 3.1c.1.5.7.9 1.2.9h16.3c.6 0 1.1-.4 1.3-.9l.6-3.1c.1-.5-.2-1.2-.7-1.5z"/></svg> <span>Choose a file&hellip;</span></label>
        </div>
      </form>
    </div>
    <form action="/uploading" method="post">
      %for ingredient in ingredients:
        <input type="checkbox" name="ingredient" value={{ingredient}}> {{ingredient}}<br>
      %end
      <input type="submit" style="width:100px; text-align:center;" value="Submit">
    </form>
  </div>
  <div class="body">
    <p><heading>Recipes</heading><br />
    </p>
    <table class="ui-box">
      % for recipe in recipes:
        %print(recipe)
        <tr>
        <td class="recipe">
          <div class="recipe-text"><a href={{recipe[2]['link']}}>{{recipe[2]['title']}}<br/></a>
          <p>serves: {{recipe[2]['yield']}}</p>
          <p>ingredients you have: {{recipe[0]}}</p>
          <p>ingredients you don't have: {{recipe[1]}}</p></div>
          <img src={{recipe[2]['picLink']}} alt={{recipe[2]['title']}} align-content="right" style="width:80%; margin-left:20%; max-height:500px;float:right;" >
        </td>
        </tr>
      % end
    </div>
  </table>
  <script>
    function onclickfunc(){
      if (document.getElementById("bs-example-navbar-collapse-1").style.display=="none"){
        document.getElementById("bs-example-navbar-collapse-1").style.display="initial"
      }else{
        document.getElementById("bs-example-navbar-collapse-1").style.display="none"
      }
    }
    document.getElementById("file").onchange = function() {
      document.getElementById("form").submit();
    };
  </script>

</body>

</html>
