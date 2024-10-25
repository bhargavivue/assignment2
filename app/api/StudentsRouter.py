from fastapi import FastAPI
from app.model.Students import Students

app=FastAPI()

@app.get("/students/{student_id}")
def getStudent(student_id: int):
    return {
        "first name":"jones",
         "last name":"smith",
          "fullname" :"jonessmith ",
           "age":25,
            "dob":"10/12/1988",
            "address":"hyderbad",
            "course":"cse",
            "fee":20000,
            "collegename":"rsn",
             "rollnumber":"102m503"
             }
@app.post("/students/")
def postStudent(input: Students):

    return {
        "first name":input.firstName,
         "last name":input.lastName,
          "fullname" :input.fullName,
           "age":input.age,
            "dob":input.dob,
            "address":input.address,
            "course":input.course,
            "fee" :input.fee,
            "collegename":input.collegename,
             "rollnumber":input.rollnumber,
             "Result": "Student posted with above detail"
             }