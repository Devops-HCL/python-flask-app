from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return f"Hello, {name}! You are {age} years old."

if __name__ == '__main__':
    app.run()
