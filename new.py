from flask import Flask , render_template , request ,session
import json

app=Flask(__name__)

@app.route('/')
def hello():
    text=" "
    return render_template('welcome.html',text=text)

# when clicked on sign up
@app.route('/signIn')
def signIn():
    text=" "
    return render_template('login.html',text=text)

# authenticate user and display its details
@app.route('/showDetails')
def showDetails():
    if request.method == 'POST':
        currentUsername = request.form['username']
        password = request.form['password']
        # logic to check data for user
        # if file present then display details else display error
        f = open('allUsers.','r')
        for line in f:
            userAndPass = line.split(',')
            username = userAndPass[0]
            if(username == currentUser):
                return render_template('diplayDetails.html',)
            else:
                return render_template('welcome.html')



# ----------------------------------------------------------------------------------

@app.route('/signUp') #to download admit card for already signed up user
def signUp():
    return render_template('details.html')
    # text="no user exist,no marks card!"
    # if request.method == 'POST':
    #     username = request.form['username']
    #     f=open("new.txt",'r')
    #     flag='n'
    #     for line in f:
    #         l=line.split(",")
    #         if(l[0]==username):
    #             return render_template('markscard.html',user=username)
        
    #     return render_template('login.html',text=text)
    
@app.route('/about')    
def about():
    return render_template("about.html")

# @app.route('/saveDetails',methods=['POST','GET']) #to check if any other user with the same name is prsent or not
# def details():
#     if request.method == 'POST':
#         text='USERNAME ALREADY EXIST!!'
#         username = request.form['username']
#         password = request.form['password']
#         f=open("new.txt",'r')
#         flag='y'
#         for line in f:
#             l=line.split(",")
#             if(l[0]==username):
#                 flag='n'
#         f.close()
#         if(flag=='y'):
#             f1=open("new.txt",'a')
#             f1.write(username+","+password)
#             f1.write("\n")
#             f1.close()
#             fnew=open(username+".txt",'a')
#             fnew.close()    
#             return render_template('details.html',user=username)  
#         else:
#             return render_template('login.html',text=text)  


@app.route('/registered',methods=['POST','GET'])
def filedata():           
    if request.method == 'POST':
        # flag='n'
        # for line in f:
        #     l=line.split(",")
        #     if(l[0]==username):
        #         flag='y'
        #     f.close()
        #     if(flag=='n'):
        #         f1=open("allUsers.txt",'a')
        #         f1.write(username+","+password)
        #         f1.write("\n")
        #         f1.close()
        username = request.form['username']
        password = request.form['password']
        fnew=open(username+".txt",'a')
        fnew.close()    
        user=request.form['user']
        policies = request.form['policy']
        accountType = request.form['accountType']
        candidatename = request.form['candidatename']
        fathername= request.form['fathername']
        mothername = request.form['mothername']
        email = request.form['email']
        mobno = request.form['mobno']
        gender = request.form['gender']
        maritalstatus = request.form['maritalstatus']
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']
        location = request.form['location']
        f=open(user+".txt",'a')
        f.write(password+"/"+candidatename+"/"+fathername+"/"
        +mothername+"/"+email+"/"+mobno+"/"+gender+"/"+maritalstatus+"/"+day
        +"/"+month+"/"+year+"/"+location+"/"+policy)
        f=open("allUsers.txt",'a')
        f.write(username+','+password)
        return render_template('registred.html',user=user,accountType=accountType)




if __name__ == '__main__':
	app.run(debug=True)