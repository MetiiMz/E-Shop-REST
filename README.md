# E-Shop REST API

A Django-based RESTful API for an e-commerce platform, featuring user authentication, product management, shopping cart, and order processing functionalities.

## Features

* **User Authentication:**

  * JWT-based authentication using `djangorestframework-simplejwt`.
  * Custom user model with fields: `full_name`, `email`, `phone_number`.

* **Product Management:**

  * CRUD operations for products and categories.
  * Support for subcategories.

* **Shopping Cart:**

  * Session-based cart management.
  * Add, remove, and view cart items.

* **Order Processing:**

  * Create orders from cart items.
  * View order history.

* **API Documentation:**

  * Integrated with Swagger using `drf-spectacular`.
