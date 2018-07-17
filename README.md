
# enBazarr API


By Adrianacmy

## Description

API for the first part of my trading app 

## Setup/Installation Requirements


Make sure your os already installed pip, python3.6, virtualenv <br/>

Run below commands in terminal:

```sh

 git clone https://github.com/Adrianacmy/capstone-API.git
 cd capstone-API
 virturalenv . -p python3.6
 source bin/activate
 cd src
 pip install requirements.txt
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser  #follow step by step to create the user
 python manage.py runserver
 
```

Login to admin with the superuser created above if it is necessary  

## Please check [here for how to use this API](#)

## User Stories

This is the API, please check user stories [in the UI repo](https://github.com/Adrianacmy/capstone-UI/tree/master)

## Known Bugs

## Technologies focused

- Dango2.0
- Django restful framework
- Django restful framework JWT

## Thanks

- https://min-api.cryptocompare.com/

## This software is licensed under the MIT license.

*Copyright (c) 2018 Adrianacmy*