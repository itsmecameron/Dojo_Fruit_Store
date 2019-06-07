from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  
date_time = datetime.datetime.now()

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']

    strawberry_from_form = request.form['strawberry']
    blackberry_from_form = request.form['blackberry']
    raspberry_from_form = request.form['raspberry']
    apple_from_form = request.form['apple']

    count = int(request.form['strawberry']) + int(request.form['blackberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    

    print(f"Charging {first_name_from_form} {last_name_from_form} for {count} fruits")
    print(request.form)
    return render_template("checkout.html",first_name = first_name_from_form, last_name = last_name_from_form, student_id = student_id_from_form, strawberry = strawberry_from_form, blackberry = blackberry_from_form, raspberry = raspberry_from_form, apple = apple_from_form, count=count, date_time = date_time.strftime('%b %d %Y %H:%M:%S'))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    