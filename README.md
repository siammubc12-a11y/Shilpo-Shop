# ShilpoShop — Fair Trade Bangladesh

A simple Django e-commerce project for a fair trade social enterprise.

## Login Credentials

| Role     | Username | Password  |
|----------|----------|-----------|
| Admin    | admin    | admin123  |
| Customer | rahim    | user1234  |

## Quick Start

```bash
# Step 1: Install Django
pip install django pillow

# Step 2: Go into the project folder
cd shilposhop   (or wherever manage.py is)

# Step 3: Run migrations
python manage.py migrate

# Step 4: Add sample data (products, users, budget)
python manage.py seed_data

# Step 5: Start the server
python manage.py runserver

# Step 6: Open in browser
http://127.0.0.1:8000/
```

## Django Admin Panel

```
http://127.0.0.1:8000/admin/
Username: admin
Password: admin123
```

## Apps Included

| App           | Purpose                                   |
|---------------|-------------------------------------------|
| users_app     | Register, Login, Logout, Profile          |
| products_app  | Browse and manage products                |
| orders_app    | Place and view orders                     |
| payments_app  | Pay for orders                            |
| reviews_app   | Write product reviews                     |
| budget_app    | Admin-only financial records              |
| cart_app      | Add up to 2 products to cart + checkout  |

## Cart Rules

- Customers can add **up to 2 different products** to the cart at once.
- You can increase quantity of the same product by clicking "+ Cart" again.
- Checkout creates orders for all cart items and clears the cart.

## User vs Admin

| Feature          | Customer | Admin |
|------------------|----------|-------|
| Browse products  | Yes      | Yes   |
| Add to cart      | Yes      | No    |
| Place orders     | Yes      | No    |
| Add products     | No       | Yes   |
| Edit products    | No       | Yes   |
| Budget records   | No       | Yes   |
| Django admin     | No       | Yes   |
