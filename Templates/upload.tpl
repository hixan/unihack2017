<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8" />
<title>Upload</title>
<link rel="stylesheet" href="static/main.css">
</head>

<body>
  <div class="header">
    <H1 class="header-text"><a href="./home">Home</a></H1>
    <ul class="header-nav">
      <li class="nav-item active"><a href="./upload">Upload a file</a></li>
      <li class="nav-item"><a href="./index">Index</a></li>
      <li class="nav-item"><a href="./recipes">Recipes</a></li>
    </ul>
  </div>

  <div class="body">
    <form action="/uploading" method="post" enctype="multipart/form-data">
      <input type="file" name="data" />
      <input type="submit" value="Start upload" />
    </form>
  </div>
  

</body>

</html>
