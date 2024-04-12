# backend
references
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page
https://medium.com/@devsumitg/how-to-connect-reactjs-django-framework-c5ba268cb8be
https://medium.com/@samradnus2001/how-to-secure-your-react-and-django-web-application-from-common-attack-cd6f31db0cf8
https://blog.stackademic.com/django-react-secure-authentication-using-http-only-cookie-ac718f0a2797


starting proj

## create a Virtual Environment (Optional but Recommended)
- python3 -m venv venv

## Activate the Virtual Environment

### On Windows
venv\Scripts\activate

### On macOS/Linux
source .venv/bin/activate

## follow these

pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver

go to /admin
add author
add b_post and copy uuid
add content block - select b_post,  select  image or text , if image upload image and caption , if text put only description

now we can view the post in http://127.0.0.1:8000/blogs/post/uuid/          note: (uuid is copied from b_post)

sorry : just testing purposes so routes r not well set

