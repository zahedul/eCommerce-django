# ecom-store => Ecommerce System using Django

This is a ecommerce system built with Django. It allows users to browse, add, and order products online. It also has a recommendation system that suggests products based on user preferences and behavior.

## Features
- User authentication and registration
- Product listing and details
- Product listing and details
- Shopping cart and checkout
- Making orders
- Applying Coupon
- Product recommendation system using Surprise library
- Admin panel for managing products, categories, orders, and users

## Installation

To run this project locally, you need to have Python 3 and pip installed on your machine.

#### Navigate to the project directory:
```bash
cd eCommerce-django
```
#### Create and activate a virtual environment:

```shell
python -m venv venv
source venv/bin/activate
```

#### Install the required dependencies:

```shell
pip install -r requirements.txt
```

#### Apply the migrations to create the database tables:

```shell
python manage.py makemigration
python manage.py migrate
```

####  Create a superuser account to access the admin panel:

```shell
python manage.py createsuperuser
```

####  Run the development server:

```shell
python manage.py runserver
```

#### Others Details
```html
•  Open your browser and go to http://localhost:8000 to see the website.

Usage
•  To browse the products, go to http://localhost:8000/products.

•  To add a product to your cart, click on the "Add to Cart" button on the product page.

•  To view your cart, go to http://localhost:8000/cart.

•  To checkout and pay for your order, go to http://localhost:8000/checkout and enter your card details.

•  To see your order history, go to http://localhost:8000/orders.

•  To see the recommended products for you, go to http://localhost:8000/recommendations.

•  To access the admin panel, go to http://localhost:8000/et-admin and log in with your superuser credentials.

```

### License
This project is licensed under the MIT License - see the LICENSE file for details.
