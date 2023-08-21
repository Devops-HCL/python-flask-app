# Simple Web Application

This is a simple web application using [Python Flask](http://flask.pocoo.org/). 
  
  Below are the steps required to get this working on a base linux system.
  
  - Install all required dependencies
  - Install and Configure Web Server
  - Start Web Server
   
## 1. Install all required dependencies
  
  Python and its dependencies

    apt-get install -y python python-setuptools python-dev build-essential python-pip python-mysqldb

   
## 2. Install and Configure Web Server

Install Python Flask dependency

    pip install flask
 

- Copy app.py or download it from source repository
- Configure database credentials and parameters 

## 3. Start Web Server

Start web server

    from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    name = input("NAME: ")
    sap_id = int(input("SAP_ID: "))
    return f"Hello, {name}! Welcome! Your sap id {sap_id}."

if __name__ == '__main__':
    app.run()

    
## 4. Test

Open a browser and go to URL

    http://<IP>:5000                          
 
