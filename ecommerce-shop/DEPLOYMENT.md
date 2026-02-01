# 🚀 Deployment Guide - E-Commerce Shop

## Quick Start: Get Your Working Website in 5 Minutes!

### Option 1: Deploy to Render.com (FREE & RECOMMENDED)

Render.com offers free hosting for Django apps. Follow these steps:

#### Step 1: Prepare Your Project
```bash
git clone https://github.com/Vinayaka-29/vinuprojects.git
cd vinuprojects/ecommerce-shop
```

#### Step 2: Add deployment files

Create `build.sh`:
```bash
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Create `render.yaml`:
```yaml
services:
  - type: web
    name: ecommerce-shop
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn shop.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
```

#### Step 3: Deploy
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Select `ecommerce-shop` folder
6. Click "Create Web Service"

**Your website will be live at**: `https://your-app-name.onrender.com`

---

### Option 2: Deploy to PythonAnywhere (FREE)

#### Step 1: Sign up
1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Create a free account

#### Step 2: Setup
1. Go to "Web" tab → "Add a new web app"
2. Choose "Manual configuration" → Python 3.10
3. In Bash console:

```bash
git clone https://github.com/Vinayaka-29/vinuprojects.git
cd vinuprojects/ecommerce-shop
mkvirtualenv ecommerce --python=/usr/bin/python3.10
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

#### Step 3: Configure WSGI
Edit `/var/www/yourusername_pythonany where_com_wsgi.py`:

```python
import sys
import os

path = '/home/yourusername/vinuprojects/ecommerce-shop'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Your website will be live at**: `https://yourusername.pythonanywhere.com`

---

### Option 3: Deploy to Railway.app (FREE)

#### Quick Deploy Button
1. Go to [Railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Add environment variables:
   - `SECRET_KEY` = (generate random string)
   - `DEBUG` = False

**Your website will be live at**: `https://your-app.railway.app`

---

### Option 4: Local Development

#### Quick Start
```bash
# Clone repository
git clone https://github.com/Vinayaka-29/vinuprojects.git
cd vinuprojects/ecommerce-shop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Load sample data (optional)
python manage.py loaddata sample_data.json

# Run server
python manage.py runserver
```

**Access locally at**: `http://localhost:8000`

---

## 📝 Complete Django Files Structure

For a fully working e-commerce website, you need:

### Backend Files:
- `shop/settings.py` - Django configuration
- `shop/urls.py` - URL routing
- `products/models.py` - Product models ✅ (Already added)
- `products/views.py` - Product views
- `products/admin.py` - Admin configuration
- `cart/models.py` - Shopping cart
- `cart/views.py` - Cart logic
- `orders/models.py` - Order management
- `orders/views.py` - Checkout process

### Frontend Files:
- `templates/base.html` - Base template
- `templates/products/list.html` - Product listing
- `templates/products/detail.html` - Product details
- `templates/cart/cart.html` - Shopping cart
- `templates/orders/checkout.html` - Checkout page
- `static/css/style.css` - Styles
- `static/js/cart.js` - Cart JavaScript

---

## 🎯 Recommended: Use Complete Django Template

For a production-ready e-commerce site, I recommend using:

1. **Django Oscar** - Complete e-commerce framework
   ```bash
   pip install django-oscar
   ```
   Demo: https://latest.oscarcommerce.com/

2. **Saleor** - Modern headless e-commerce
   ```bash
   git clone https://github.com/saleor/saleor.git
   ```
   Demo: https://demo.saleor.io/

3. **Django Shop** - Modular e-commerce
   ```bash
   pip install django-shop
   ```

---

## 🔧 Environment Variables

Create `.env` file:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 📦 Additional Requirements

Add to `requirements.txt` for deployment:
```
gunicorn==21.2.0
whitenoise==6.6.0
dj-database-url==2.1.0
python-dotenv==1.0.0
```

---

## 🌐 Live Demo Links

Once deployed, your e-commerce website will have:

- **Homepage**: `/` - Product listings
- **Product Detail**: `/products/<id>/` - Individual product
- **Cart**: `/cart/` - Shopping cart
- **Checkout**: `/checkout/` - Complete purchase
- **Admin Panel**: `/admin/` - Manage products
- **User Dashboard**: `/account/` - User profile

---

## ⚡ Quick Deploy Commands

### For Render.com:
```bash
# Add to requirements.txt
echo "gunicorn==21.2.0" >> requirements.txt
echo "whitenoise==6.6.0" >> requirements.txt

# Create Procfile
echo "web: gunicorn shop.wsgi" > Procfile

# Push to GitHub
git add .
git commit -m "Add deployment files"
git push
```

### For Heroku:
```bash
heroku create your-ecommerce-shop
heroku addons:create heroku-postgresql:mini
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 🎨 Customize Your Site

1. **Change colors**: Edit `static/css/style.css`
2. **Add logo**: Place in `static/images/logo.png`
3. **Update content**: Edit templates in `templates/`
4. **Add products**: Use Admin panel at `/admin/`

---

## 📞 Need Help?

- Django Documentation: https://docs.djangoproject.com/
- Deployment Guides: https://docs.djangoproject.com/en/5.0/howto/deployment/
- E-commerce Tutorials: https://www.youtube.com/results?search_query=django+ecommerce

---

## 🚀 Next Steps

1. Deploy to Render.com (easiest)
2. Add sample products via admin
3. Share your live website URL!
4. Add payment integration (Stripe/PayPal)
5. Customize design and features

**Your e-commerce website will be live and accessible via a public URL!** 🎉
