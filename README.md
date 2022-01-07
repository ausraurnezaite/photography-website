# PERSONAL PHOTOGRAPHY WEBSITE 

#### Video Demo:  <https://youtu.be/U3ltpuaae28> 

#### Description: 

I’ve been photographing for many years. And now that I’ve gained some knowledge, I finally decided to create a website portfolio of my photography. 

I’ve always liked minimalistic, not too cluttered or distracting websites, so wanted mine to look the same. 

The website consists of home page, contacts page and galleries with different types of photography – portraits and landscapes. 

Project was created using HTML, Python, JavaScript, CSS, Flask, Flask-mail, Bootstrap. 

##### HTML files/ pages 

There are four HTML files: index, portraits, landscapes, contacts. 

All of these were made using Bootstrap’s grid which I find very easy to position items throughout the page also allowing to adapt positioning to different screen-size devices. 

It is possible to get from any page on website to any other page as there is dropdown navigation menu. 

###### portraits.html, landscapes.html 

Considering the positioning of the photographs I chose Bootstrap’s grid over CSS grid as it allows adding new photographs in between if needed without changing positioning code for the other pictures. 

###### index.html 

Index.html is very minimalistic home page with only few buttons whose main purpose is to navigate to other pages. 

###### contacts.html 

Page contains contact information as well as links to social media pages. 

Added a couple icons from bootstrap.com and fontawesome.com. 

For the user's convenience there is a contact form which is made to send emails to my personal mail. 

Some JavaScript features were integrated in order to make contact form to appear/disappear by clicking a button rather than creating a separate page only for the form. 

 

##### CSS files 

There are two CSS files: styles.css and media.css. 

Styles.css is responsible for all the styling of the website. Media.css’ purpose is to adapt the view to the mobile devices with the smaller screens. 

##### app.py 

Application file was made using Python, Flask and Flask-mail. 

Route functions were used to go from page to page as well as rendering templates of html pages. 

App’s main purpose is to get the information from the contacts form and send an email. 

Flash message was used to inform the user that message has been sent. 

The email address and password that are provided for the mail configurations were created only for the use of this application. I am not worried too much about revealing it. I used os environment variable in the first place but changed into the way it is at the moment because is make it less complicated to run the application.