from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods= ['GET','PUT','post'])


def flasktest():
    Student =	 [ {
       "name": "Ford",
       "age": "21",
  
         },
        {
         "name": "Ria",
          "age": "31",
 
         },

           {
         "name": "Dev",
         "age": "41",
 
        }

     ]
    age=None
    user_input = request.args.get('name')
    
    for i in Student:
        if i['name'] == user_input:
            age=i
            break
    return str(age)
  
    

   




@app.route('/kaveri')

def testKav():
    return "This is writtern by Kaveri Gojare"


if __name__ == '__main__':
    app.debug= True
    app.run(host='0.0.0.0',port= 5000)

