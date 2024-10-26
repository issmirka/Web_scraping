# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:22:33 2024

@author: pawe2
"""

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: LightGray;
}
</style>
    <title> Hi! Welcome to my first page ;)  </title>
    <link rel="stylesheet" href="/Content/Examples/Html/L12/styles.css">
</head>
<body>
    <h1> Nice  to meet you </h1>
    <p> Very nice... </p>
    <hr/>
    <p> <small> Always is a good time for a small piece of chocolate </small> </p>
    <hr/>
    <h2> Tell me something about yourself... </h2>
    <p> <i> Something more... </i> </p>
    <p style = 'color:blue'> What is your favourite chocolate? </p>
    
    <p> Here you can read more about my fave sweet <a href ="https://www.lindt.pl/sklep"> <button>  click here! </button> </a> </p>
    <img src= "https://th.bing.com/th/id/OIP.llzksYKJJSDTANY_abd68gHaEF?rs=1&pid=ImgDetMain" alt="Opis zdjęcia" width="400" height="300">
</style>
</body>
</html> 
"""

import os 
current_path = os.getcwd()
file_name = "star.html"
final_path = os.path.join(current_path, file_name)
with open (final_path, 'w') as file:
    file.write(html_content)


