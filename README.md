# Access Key Manager

This project is Key Manager Application built with Django framework . The app allows users (schools) to sign up, log in ,request for a key to activate their school's account and to know their status of their requested keys (i.e Active,Expired or Revoked). Adminstrators possess an additional privileges to manually revoke a key a pursed key and access an end point
## Features

- User authentication (signup, login, logout) with email verification
- Password reset functionality
- Unique Key for all users
- Details of Access Keys 
- Key Revoking (Admin)
- Endpoint Access


## Prerequisites

- Python 3.8+
- Django 4.2+
- pip (Python package installer)

## Usage

### User Authentication
1. **Sign Up:**
   
  Users sign up with an email address, username  and password. Email verification is required

3. **Log In:**
   
   Users log in with their registered email and password

4. **Password Reset:**
   
   Users can reset their password through their email addresses

### Key Accesess Management
- Logged in users can view their list of requested(purchased) Access keys.
- Logged in users have info on the status(Active,Expired,Revoked) of their requested(purchased) keys.
- Logged in users have info on the details(date procured,expiry date) of each access key they have.
- Logged in users can't request can for an active key if they have an existing active key.


  **Admin Functionalities**
- Admin can view all the details of a registered user (i.e Access key,username,status,procurement date,expiry date)
- Admin can manually revoke a key from a user
- Admin can access an endpiont of status code 200 or 404 depending on the availabilty of an active key for any user on the platform through the email search bar
    -status code 200 displays if user has an active key
    -status code 404 displays if email doesn't exists or user doesn't have an active key
## Deployed Link

Default Superuser details

-email : `josepharmoo415@gmail.com`

-password : `power448`

-link : https://jaarmoo.pythonanywhere.com

**Additional Info**: Website is not responsive.Best viewed on laptop or desktop screen


## Entity-Relationship Diagram of Database


![access-key-er-diagram](https://github.com/user-attachments/assets/1ddb10ea-f29e-4f57-87e7-f876eaf40063)




  
   
