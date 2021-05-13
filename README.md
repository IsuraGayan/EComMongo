<h1>Django E-Commerce Site with MYSQL Database</h1>

<p>This is an E-Commerce Web Site which has made using Django Framework (Python Web Framework).</p>

<p>Users can uses this site to order Spices they want. When User place an Order with the with the Billing Address, Site Admin will reciece an Email with Ordered Products and User's
Billing Address. Both Guest Users and Registered Users can use this site to fulfill their wants.</p>

<p>When User adds a Product to the Cart, a session with Key Name 'CART' will be intialzed. Then the added Products will appended to Session 'CART'. If User Placed the Order, the Email will send.
Also, if the User is an authenticated User, the Order will be saved to the Database.
</p>

<p><b>Required 3rd Party Libraries</b></p>
<ul>
<li>Django==3.0.5</li>
<li>djongo==1.3.4</li>
<li>Pillow==8.2.0</li>
<li>pymongo==3.11.4</li>
</ul>
