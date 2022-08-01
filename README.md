# SDEV_220_Final_Project_Group7 Documentation
Summer 2022 SDEV 220 Final Project Group 7

Created by:
Kira Buck, Jaecob Dobler, Melissa Haney

# Getting Started
Open our Homepage at _____
Login or create an account
Now depending on your account status you have different authorization to different parts of the website. All users are able to view the products at the endpoint /products/detail/(product #)

# Users
On launch of the application all users are directed to login or create an account. 

Customer: Customer clients are users who do not have admin control.
Employee: Employee clients are users who have access to the dashboard and products.
Admin: Admin clients are users who have complete access to modify and manipulate the products and users.
 
# Applications

arthaus:
 This application houses the main django files including settings.py and manage.py
 
products:
 This application includes the models, views, and urls of the products for the database. 
 
users:
 This applications includes user/customer information.
 
 
# Templates / Html & Bootstrap
 ## partials:
 
  nav.html: this document adds the nav bar to the top of the Base.html
  
 products:
 
  detail.html: this document is used when the client goes to the endpoint /products/detail/<#>
  
 user:
 
  login.html: this document structures the login form.
  
  logout.html: this document tells django to logout the user.
  
  profile_update.html: this document allows users to update their profile.
  
  profile.html: this document shows a users profile.
  
  register.html: this document allows users to register a new user.
  
 Base.html: this document is the base template for the server all other documents extend this one.
 
 home.html: this is the homepage of the site.


# Libraries/Dependencies
1.) Django 4.0.6
2.) pytz 2022.1
 
