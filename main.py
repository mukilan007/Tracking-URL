from flask import Flask, render_template, request
import requests

ash = Flask(__name__)  # create object with flask class and pass a variable using __name__ to flask constructor


@ash.route('/')  # API call and route for call particular URL ('/' URL for home page)
def home():  # view function
    return render_template("home.html")  # html page render using render_template


@ash.route('/helpline')
def help():
    return render_template('help.html')


@ash.route('/track', methods=['POST'])
def track():
    if request.method == 'POST':  # check request method was post or get received from client
        a = request.form['User_URL']  # form is a dictionary key+value , it store the value in 'a'
        res = requests.get(a)       # pass the URL which get from user
        redirect = res.history      # store history in redirect
        return render_template('track.html', s_url=res, redi=redirect)


if __name__ == '__main__':  # __name__ current module name and __main__ take it main program
    ash.run(debug=True)  # call run method to call application and debug mode for automatic save(looks live)
