from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    name = input("NAME: ")
    sap_id = int(input("SAP_ID: "))
    return f"Hello, {name}! Welcome to HCL Technologies,Your sap id {sap_id}."

if __name__ == '__main__':
    app.run()
