from flask import Flask 
from hello import say_hello
app= Flask(_name_)

@app.route('/')
def home():
    return say_hello()

if _name=='main_':
    app.run(debug=True)