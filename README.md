# ISS Monitoring

<img src="./images/Map-Presentation.gif" alt="exemplo imagem">

> Add some filters, look at the current location and enjoy the view :)

<br/>


## 💻 Requirements

Before we start, please verify if you have:

* `Python 3` or more.
* A ` Windows ` machine.

<br/>
<br/>

## ⚙ Installing dependencies

````
os
sys
PyQt5
pandas
folium
geopy
tzwhere
datetime
pytz
base64
io
numpy
mpl_toolkits
matplotlib
````
> Do it easily just with ` pip install <dependence> ` for each one.

<br/>
<br/>
<br/>

## 🚀 Getting started

### Customization
Here are simple customizations for your viewer.

<br/><br/>


<div style="text-align:center">
  <h2>🎨 Map Themes</h2>
  <p>Click on the images below:</p>
</div>

<!-- The four columns -->
<div class="row">

  <div class="column">
  <img src="./images/Demo-Dark.png" style="width:100%" onclick="myFunction(this);" alt="Dark Earth - 'cartodbdark_matter'">
  </div>
  <div class="column">
    <img src="./images/Demo-White.png"  style="width:100%" onclick="myFunction(this);"
    alt="White Earth - 'cartodbpositron'">
  </div>
  <div class="column">
    <img src="./images/Demo-Vintage.png"  style="width:100%" onclick="myFunction(this);"
    alt="Vintage - 'stamenwatercolor'">

  </div>
  <div class="column">
    <img src="./images/Demo-Street.png"  style="width:100%" onclick="myFunction(this);"
    alt="Street Map - 'openstreetmap'">

  </div>
  <div class="column" >

  <img src="./images/Demo-Relief.png"  style="width:100%" onclick="myFunction(this);"
  alt="Earth Relief - 'stamenterrain'">

  </div>

</div>

<div class="container">
  <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>

  <img id="expandedImg" style="width:100%"/>

  <div id="imgtext"></div>
</div>
  
</div>


* You can also change the default zoom rate but, remember to fix the position (or the size) of the ISS image on the maker.

> Check this feature on the line 74.



<br/><br/>

## ✨ Extra
I really recommed the usage of the Live Browser here, it takes a better view of the map, so you can go for a next level with this:

<h3 align="center"> pyinstaller </h3>
<br/>

```
pip install pyinstaller
```

<h4 align="center"> Standalone Python EXE Executable - Tutorial</h4>
<h6 align="center">(Click on this image below)</h6>

<p align="center">
    <a href="https://www.youtube.com/watch?v=QWqxRchawZY">
    <img src="https://i.ytimg.com/an_webp/QWqxRchawZY/mqdefault_6s.webp?du=3000&sqp=CMDdkZQG&rs=AOn4CLDZxcAARgZqiFU5rlAz0WhsycO8Cw" 
    width="60%" ></a>
</p>
<p align="center">
  <a href="https://pyinstaller.org/en/stable/"><img src="https://avatars.githubusercontent.com/u/1215332?s=200&v=4" 
    width="30" />
    Docs
  </a>
</p>


> Make both python files executable with pyinstaller and run it in a simple way.


<br/><br/><br/><br/><br/><br/>

## 📫 Contribute

1. Fork this repo.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your code and: `git commit -m '<commit_message>'`
4. Send to the original branch: `git push origin ISS_Monitoring / main`
5. Make a pull request.














<!---CSS--->
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
}

/* The grid: Four equal columns that floats next to each other */
.column {
  float: left;
  width: 25%;
  padding: 10px;
}

/* Style the images inside the grid */
.column img {
  opacity: 0.8; 
  cursor: pointer; 
}

.column img:hover {
  opacity: 1;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* The expanding image container */
.container {
  position: relative;
  display: none;
}

/* Expanding image text */
#imgtext {
  position: absolute;
  bottom: 15px;
  left: 15px;
  color: white;
  font-size: 20px;
}

/* Closable button inside the expanded image */
.closebtn {
  position: absolute;
  top: 10px;
  right: 15px;
  color: white;
  font-size: 35px;
  cursor: pointer;
}
</style>
















<!--JS-->
<script>
function myFunction(imgs) {
  var expandImg = document.getElementById("expandedImg");
  var imgText = document.getElementById("imgtext");
  expandImg.src = imgs.src;
  imgText.innerHTML = imgs.alt;
  expandImg.parentElement.style.display = "block";
}
</script>