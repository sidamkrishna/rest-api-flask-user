 Flask REST API - User Manager

This is a simple REST API built using **Flask**.  
It lets you do everything — GET, POST, PUT, DELETE users from memory.


 What It Does

 GET      `/users`            Get all users       GET      `/users/<id>`       Get single user       
 POST     `/users`            Add a new user      PUT      `/users/<id>`       Update user info     
 DELETE   `/users/<id>`       Delete a user          



 Compared to Django


| Setup          | Just 1 file (app.py), quick to start         | Many files (views.py, urls.py, etc.) |
| Structure      | You decide (no rules)                        | Strict structure                    |
| REST API       | You code it by hand                          | You use Django REST Framework       |
| Best for       | Learning, small apps, quick APIs             | Big apps, admin panels, serious stuff |
| Speed to build | 🔥 Super fast                                | 🧱 Takes time to set up              |


 How to Run
```bash
pip install flask
python app.py
