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
@app.route('/showDetails',methods=['POST','GET'])
def details():
    if request.method == 'POST':
        currentUsername = request.form['username']
        password = request.form['password']
        # logic to check data for user
        # if file present then display details else display error
        f = open('allUsers.txt','r')
        found = 0
        for line in f:
            userDetails = line.split('/')
            username = userDetails[0]
            userpassword = userDetails[1]
            # user = userDetails[2]
            if(username == currentUsername and password == userpassword):
                found = 1
        if found == 1 :
            return render_template('diplayDetails.html',userDetails = userDetails)
        else:
            return render_template('welcome.html',text = 'Please input correct usernanme or password')    
            


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


@app.route('/register',methods=['POST','GET'])
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
        # fnew=open(username+".txt",'a')
        # fnew.close()    
        # user=request.form['user']
        policy = request.form.getlist('policy[]')
        print(policy)
        policies = ','.join(policy)
        print(policies,"^^^^^^^^^^^^^^")
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
        # f=open(user+".txt",'a')
        f=open("allUsers.txt",'a')
        f.write(username+'/'+password+"/"+candidatename+"/"+fathername+"/"
        +mothername+"/"+email+"/"+mobno+"/"+gender+"/"+maritalstatus+"/"+day
        +"/"+month+"/"+year+"/"+location+"/"+policies)
        f.write("\n")
        f.close()
        # print(f,"^^^^^file content")
        # f1=open("allUsers.txt",'a')
        # f1.write(username+','+password+','+user)
        # f1.close()
        return render_template('registred.html',user=candidatename,accountType=accountType)
        



if __name__ == '__main__':
	app.run(debug=True)