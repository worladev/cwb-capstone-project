from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello CWB Members</h1>'


if __name__ == '__main__':
    app.run(debug=True)

#Enoch push to the right branch, Make a pull request, Add class in their own file,
#Push changes, Emma makes a pull request.