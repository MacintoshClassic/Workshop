<!DOCTYPE html>
<html>
<body>

<header>
  <h1>Car dealership project</h1>
  <p><b>Description:</b></p>
  <p>The web application for convenient management of the workshop orders.</p>
  <p>The application is created for the workshop staff. To make order appear in the system we insert the information to the database via UI or directly to the database using SQL. In the data, we have information about the clients, cars, mechanics, and actual repair orders (it includes car's issue, order price, mechanic’s name, and beginning/finishing dates). We also can add client and car to the system automatically if it has not been added before and change the order’s data if it has not been completed initially.</p>
  <p>Once the home page is opened, we can see the option to add all of this data via the user’s interface. To complete it, we just click the button “Add client” --> input his name and telephone number --> the system automatically generates the client id number. The same operation is possible with the car, where we click the “Add car” button --> insert the car registration number, model, and year --> the system will generate the car id number as well. The option of adding the order is the same, we click on the “Add order” button --> insert all of the information about the client and his car that I mentioned above. If a client or car doesn’t exist it’s not a problem because the system adds absent information to the database and order gets created.</p>
  <p>By means of this application, we can manage existing order(s). For example, we can assign the mechanic to the existing order where he initially has not been added. The same thing we may do with the finishing date in order to track the order’s finishing date. We also may check a particular client’s order information by inputting his id. The option of checking all the orders is also possible, we just need to clickin on the “Order list” button and all the orders will show up.</p>
  <p></p>
  <b>Languages and technologies I used:</b>
  <ul>
    <li>Python</li>
    <li>SQL (MariaDB)</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>Bootstrap</li>
    <li>Django</li>
    <li>Django REST framework</li>
    <li>Git</li>
   </ul>
  <p><b>P.S.</b> Database First approach has been used in this project. I mostly worked on the backend, this is why the user’s interface looks pretty simple.</p>
</header>

</body>
</html>
