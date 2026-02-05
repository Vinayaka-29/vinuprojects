# 🚀 QUICK START - 5 MINUTE SETUP

Fastest way to get your e-commerce shop running locally with admin account.

---

## ⚡ STEP-BY-STEP (Copy & Paste Commands)

### Step 1: Clone & Navigate

```bash
git clone https://github.com/Vinayaka-29/ecommerce-shop.git
cd ecommerce-shop/ecommerce-shop
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install & Setup

```bash
pip install -r requirements.txt
python manage.py migrate
```

### Step 4: Create Admin Account

```bash
python manage.py createsuperuser
```

When prompted:
```
Username: admin
Email: admin@example.com
Password: YourPassword123
Password (again): YourPassword123
```

### Step 5: Run Server

```bash
python manage.py runserver
```

**You should see:**
```
Starting development server at http://127.0.0.1:8000/
```

---

## 🌐 NOW OPEN IN BROWSER

| URL | Purpose |
|-----|----------|
| http://127.0.0.1:8000/ | 🏠 Homepage |
| http://127.0.0.1:8000/admin/ | 🔐 Admin Login |
| http://127.0.0.1:8000/checkout.html | 🛒 Place Order |
| http://127.0.0.1:8000/order-tracking/ | 📦 Track Order |

**Admin Credentials:**
- Username: `admin`
- Password: (whatever you entered in Step 4)

---

## 📋 YOUR FIRST TEST

### 1. Test the Website

1. Visit http://127.0.0.1:8000/
2. Click on products
3. Add items to cart
4. Go to Checkout
5. Fill in details and place order

### 2. View Order in Admin

1. Visit http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Click "Orders" in sidebar
4. See your order appear!
5. Click order to view full details

### 3. Track Order

1. Visit http://127.0.0.1:8000/order-tracking/
2. Enter the Order ID you just created
3. See order details and status

---

## 🎯 WHAT'S WORKING

✅ Product catalog
✅ Shopping cart (localStorage)
✅ Checkout form
✅ Order placement (/api/create-order/)
✅ Order storage in database
✅ Admin panel with order management
✅ Order tracking page
✅ Order status updates
✅ Customer delivery address
✅ Payment method tracking

---

## 🚨 COMMON ISSUES & FIXES

### "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

### "No module named django"
```bash
pip install -r requirements.txt
```

### "Database locked" error
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Can't login to admin
```bash
python manage.py changepassword admin
```

### Orders not showing in admin
- Restart server: Press Ctrl+C and run `python manage.py runserver` again
- Check migrations: `python manage.py migrate`

---

## 📚 DOCUMENTATION

For detailed setup & deployment info:
- **ADMIN_SETUP.md** - Complete setup with deployment options
- **DEPLOYMENT.md** - Production deployment guide
- **README.md** - Project overview

---

## 🔑 IMPORTANT

⚠️ **Change admin password after first login:**
1. Visit http://127.0.0.1:8000/admin/
2. Click username (top right)
3. Change password

⚠️ **Keep credentials secure:**
- Don't share admin password
- Use strong passwords in production
- Never commit credentials to GitHub

---

## 📊 DATABASE INFO

Your data is stored in: `db.sqlite3`

Tables created:
- auth_user (user accounts)
- products_product (products)
- products_category (categories)
- products_productreview (reviews)
- products_order (orders) ⭐ NEW!
- products_orderitem (order items) ⭐ NEW!

---

## ✅ CHECKLIST

- [ ] Cloned repository
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Migrations run
- [ ] Superuser created
- [ ] Server running
- [ ] Can access http://127.0.0.1:8000/
- [ ] Can login to http://127.0.0.1:8000/admin/
- [ ] Can see Orders in admin
- [ ] Placed test order
- [ ] Order visible in admin panel

---

## 🎉 NEXT STEPS

When ready to deploy live:
1. See **ADMIN_SETUP.md** PART 3 for deployment options
2. Choose platform (PythonAnywhere recommended)
3. Follow deployment steps
4. Create production admin account
5. Test live website

---

## 💬 NEED HELP?

**Common tasks:**

Restart server:
```bash
# Stop: Ctrl+C
# Start: python manage.py runserver
```

Reset everything:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

View all Django commands:
```bash
python manage.py help
```

---

**You're all set! Happy selling! 🛍️**
