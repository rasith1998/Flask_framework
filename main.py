from flask import Flask, render_template,request

app = Flask(__name__)


# @app.route("/hello/<name>")#if we give name shoud add into the function
# @app.route("/hello/<int:name>")#if we want integer value
@app.route("/hello")
def first():
    # return "<h1>Welcome to Rasith %s</h1>"%name #String =%s
    # return "<h1>Welcome to Rasith %d</h1>" % name #Integer =%d
    #return (render_template('home.html'))
    #return (render_template('home.html',name=names))
    return (render_template('home.html'))

@app.route("/second",methods=['post']) # methods
def second():
    username=request.form["username"]#key value from html
    #return "Welcome to Data Analyst"
    #return (render_template('second.html'))
    return "username is "+ username


if __name__ == '__main__':
    app.run(debug=True)
