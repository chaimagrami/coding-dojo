from flask import flask
app= Flask(import_name__name__)

app.route(rule='/')
def index():
    return render_template(template_name_or_list="index.html")


if __name__=="__main__":
    app.run(debug=True)