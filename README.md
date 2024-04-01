# DroneBoxExpress-FE_Angular-BE_Django-Example

Angular Project Example - for testing purposes only

The project is currently being developed and it’s not in its finished state

Current Status: Functionality Completed on 90%\
Front-End Completed on 80%

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

API Access Points [Development Environment]:

* Login = POST - http://127.0.0.1:8000/api-token-aut
* Register = POST - http://127.0.0.1:8000/register
* User Details = GET - http://127.0.0.1:8000/get-details
* User Update = PUT - http://127.0.0.1:8000/update/int:pk/
* User Delete = DELETE - http://127.0.0.1:8000/delete/int:pk/
* List Orders = GET - http://127.0.0.1:8000/customer/orders
* Create Order = POST - http://127.0.0.1:8000/customer/orders/
* Order Details = GET - http://127.0.0.1:8000/customer/orders/int:pk
* Order Update = PUT - http://127.0.0.1:8000/customer/orders/int:pk/
* Order Delete = DELETE - http://127.0.0.1:8000/customer/orders/int:pk/
* List News Articles = GET - http://127.0.0.1:8000/staff/news
* Create News Article = POST - http://127.0.0.1:8000/staff/addNews/
* News Article Details = GET - http://127.0.0.1:8000/staff/news/int:pk
* News Article Update = PUT - http://127.0.0.1:8000/staff/news/int:pk/
* News Article Delete = DELETE - http://127.0.0.1:8000/staff/news/int:pk/
* List Airports = GET - http://127.0.0.1:8000/staff/airports
* Create Airport = POST - http://127.0.0.1:8000/staff/airports/
* Airport Details = GET - http://127.0.0.1:8000/staff/airports/int:pk
* Airport Update = PUT - http://127.0.0.1:8000/staff/airports/int:pk/
* Airporte Delete = DELETE - http://127.0.0.1:8000/staff/airports/int:pk/
* List Routes = GET - http://127.0.0.1:8000/staff/routes
* Create Routes = POST - http://127.0.0.1:8000/staff/routes/
* Route Details = GET - http://127.0.0.1:8000/staff/routes/int:pk
* Route Update = PUT - http://127.0.0.1:8000/staff/routes/int:pk/
* Route Delete = DELETE - http://127.0.0.1:8000/staff/routes/int:pk/
