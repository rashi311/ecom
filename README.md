# Project Summary
This is e-commerce website built with Django.This website displays products.Users can add and remove products to/from their cart while also specifying the quantity of each item.They can then enter their details like phone number,email and address to place their orders.


# installation
### 1.clone Repository & Install Packages

git clone https://github.com/rashi311/ecom.git

### 2.Setup Virtualenv

virtualenv myenv
source myenv/bin/activate

### 3.install dependencies

pip install -r requirements.txt

### 4.Databse migration

python manage.py makemigrations
python manage.py migrate

### 5.create a superuser
python manage.py createsuperuser

### 6.Start the developement server
python manage.py runserver

### 7.Open your web browser and navigate to:
http://127.0.0.1:8000/
