# DroneBoxExpress-FE_Angular-BE_Django-Example

Angular Project Example - for testing purposes only

The project is currently being developed and it’s not in its finished state

Current Status: Functionality Completed on 0%\
Front-End Completed on 10%

The web project is of an imaginary company for delivering packages using drones and predetermined routes, the idea is that the web application has multiple functionalities and acts as both customer platform and staff platform. Depending on the user/profile type that is currently logged in, the web application either acts as a platform to add new airports, drones, routes and news articles or acts as a customer platform where information can be viewed and individual orders can be placed, modified and deleted. The web application notifies the user for changes to his/her orders status via email (currently in development). There are 3 user profile types in the application which are handled via custom user model and associated django signals. The front end is developed with Angular 16 while the backend is developed using Django 4.2.

User Profiles Types:
1. Admin
2. Staff
3. Customer

These are the following sections the Web application has:

* Home Section – Displaying recently added articles, news and events from the company staff, if a staff user is logged in it allows it to create new articles and modify and delete articles, he/she has created.

* Contacts and about us – Displaying company information

* Profile Section – Allows a logged user to view, edit and delete his/her profile

* Operations Section – Allows a user with a profile of "Staff" to make CRUD operation over the existing Airport, Drones, and Routes.

* Orders Section – Allows a user with a profile of "Customer" to generate, modify and delete orders. If user is "Staff" this section allows further functionality to adjust price ranges, view all orders and do CRUD operations over them.

Database Models:

* User Model
* News_Article Model
* Orders Model
* Route Model (incl. Airports, Prices, Distance)
* Airport Model
