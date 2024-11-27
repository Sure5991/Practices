# Flask App Routing

from flask import Flask, render_template , request, redirect,url_for

# create simple flash application
app = Flask(__name__)

#GET method

@app.route('/',methods = ['GET'])
def welcome():
    return redirect(url_for('form'))

@app.route('/instruction',methods = ['GET'])
def instruction():
    return 'This calculator is used for two number. This can perform addition and subtraction. First blank is first number and second entry is second no'

# variable rule

@app.route('/result/<float:res>')
def result(res):
    return render_template('result.html',result=res)

# POST method

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        first = float(request.form['first'])
        second = float(request.form['second'])
        operation = (request.form['operation'])
        submit = (request.form['status'])
        if operation == "add":
            result = first + second
        elif operation == "sub":
            result = first - second
        elif operation == "mul":
            result = first * second  
        if submit == "same_page":
            return render_template('form.html',result = result)
        elif submit == "diff_page":
            return redirect(url_for('result',res = result))
        
if __name__ =="__main__":
    app.run(debug= True)