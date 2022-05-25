#!/usr/bin/env python
# coding: utf-8

# A simple Flask App which takes radius, length, width as inputs and returns the total number of circles as output

#importing the required libraries
from flask import Flask, request, render_template
from code_directory.function_code import inscribe
#app=flask.Flask(__name__)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method=='POST':
        rad = float(request.form.get('radius-input'))
        len = int(request.form.get('length-input'))
        wid = int(request.form.get('width-input'))
        #calling the inscribe function
        data = inscribe(rad,len,wid)
        output = {'image':data[0],'table':data[1],'num':data[2]}
        inp = {'radius':rad,'length':len,'width':wid}

        return render_template('output_page.html',data=output,inp=inp)
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method=='POST':
        rad = float(request.form.get('radius-input'))
        len = int(request.form.get('length-input'))
        wid = int(request.form.get('width-input'))
        layout = str(request.form.get('layout-input'))
        print("layout: ", layout)
        #calling the inscribe function
        data = inscribe(rad,len,wid,layout)
        output = {'img': data[0]}
        inp = {'radius':rad,'length':len,'width':wid}
        elif layout.lower() == "n":
            print("Layout not required")
        else:
            print("Enter either y or n")

    #return render_template('index.html')

if __name__ == '__main__':
    app.run()





