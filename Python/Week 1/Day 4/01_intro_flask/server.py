from flask import Flask, render_template
app = Flask(__name__)

# http://127.0.0.1:1337
@app.route('/')          
def hello_world():
    return 'Hello World!'  

# http://127.0.0.1:1337/hello
@app.route('/hello')
def hello():
     return "Hello From Server 🚀🚀🚀  "
 
# http://127.0.0.1:1337/hello/user
@app.route('/hello/user')
def say_hello():
    return "<h1>Hello James 😁😁😁</h1>"

# http://127.0.0.1:1337/hello/user/<username>
@app.route('/hello/user/<username>')
def say_hello_username(username):
    return f"<h1>Hello {username} 😁😁😁</h1>"

# http://127.0.0.1:1337/hello/user/<username>/<times>
@app.route('/hello/user/<username>/<int:times>')
def say_hello_username_n_times(username, times):
    return f"<h1>Hello {username} 😁😁😁</h1>" * times

# http://127.0.0.1:1337/user/<username>/<age>
@app.route('/hello/user/<username>/<int:age>')
def user_info(username, age):
    return f"<h1>USERNAME : {username} <br/> AGE : {age} </h1>"

# http://127.0.0.1:1337/index/jhon/54
@app.route('/index/<username>/<int:age>')
def index(username, age):
    users = [
        {'name':"John", 'age':'35'},
        {'name':"John", 'age':'35'},
        {'name':"John", 'age':'35'},
        {'name':"John", 'age':'35'},
        {'name':"John", 'age':'35'},
        {'name':"John", 'age':'35'}
    ]
    return render_template("index.html", user = username, number = age, users=users)



if __name__=="__main__":   
    app.run(debug=True, port=1337)    

