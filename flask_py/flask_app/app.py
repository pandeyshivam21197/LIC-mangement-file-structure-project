from flask import Flask , render_template , flash , redirect , url_for , session , request , logging 
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hall_ticket')
def hall():
    return render_template('hall.html')

@app.route('/registration',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        reg_number  = request.form['reg_number']
        location = request.form['location']

        f = open('students.txt','a+')
        f.write(username+' | '+reg_number+' | '+location+' \n ')
        
        
        f=open('students.txt','r')
        for line in f:
            data = line.split('|');
        return render_template('success.html',ram=data)
    return render_template('registration.html')



if __name__ == '__main__':
    app.run(debug=True)