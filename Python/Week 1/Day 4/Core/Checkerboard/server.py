from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)# Create a new instance of the Flask class called "app"


@app.route('/')
def index():
    return render_template('aaa.html',col=8,row=8,color_one="black",color_two="red")

@app.route('/hello')          # The "@" decorator associates this route with the function immediately following
def index_one():
    return render_template("aaa.html",row=8,col=4,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>')          # The "@" decorator associates this route with the function immediately following
def repeat(x,y):
    return render_template("aaa.html",row=x,col=y,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')          # The "@" decorator associates this route with the function immediately following
def col(x,y,color1,color2):
    return render_template("aaa.html",row=x,col=y,color_one=color1,color_two=color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=1339)    # Run the app in debug mode.

















