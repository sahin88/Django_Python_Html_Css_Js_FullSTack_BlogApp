# Django_Python_Html_Css_Js_FullSTack_BlogApp

## Features

- Django 3.1.7

- Html, Css, Js

## Appview

<img src="https://github.com/sahin88/Django_Python_Html_Css_Js_FullSTack_BlogApp/blob/main/blog_app_one.png"  width="400px" height="400px">.

<img src="https://github.com/sahin88/Django_Python_Html_Css_Js_FullSTack_BlogApp/blob/main/blog_app_two.png"  width="400px" height="400px">.

<img src="https://github.com/sahin88/Django_Python_Html_Css_Js_FullSTack_BlogApp/blob/main/blog_app_three.png"  width="400px" height="400px">.

## Getting Started

First clone the repository from Github and switch to the new directory:

```
$ git clone https://github.com/Django_Python_Html_Css_Js_FullSTack_BlogApp
$ cd Django_Python_Html_Css_Js_FullSTack_BlogApp

```

Create virtualenviroment by running following command.

```
$ python3 -m venv venv

```

Activate the virtualenv for your project.

```
$ source venv/bin/activate

```

Install project dependencies:

```
$ pip install -r requirements.txt

```

or

```
$ sudo -u postgres psql

```

after that, run respectively following commands

```
# CREATE USER name;
```

```
# CREATE DATABASE fileupload OWNER name;
```

Finally Update your settings.py and enter your password and username

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fileupload',
        'USER': '****',
        'PASSWORD': '*****',
        'HOST': 'localhost'
    }
}

```

Then simply apply the makemigrations

```
$ python manage.py makemigrations

```

After making migrations successfully, run following command to create table

```
$ python manage.py migrate

```

Now,you can start the Django development server

```
$ python manage.py runserver

```

To generate superuser and reach the admin interface to costumize your app please run following command

```
$ python manage.py  createsuperuser

```

## Licence

MIT

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
