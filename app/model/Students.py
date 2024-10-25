from pydantic import BaseModel

class Students(BaseModel):
    firstName: str
    lastName: str
    fullName: str
    age: int
    dob: str
    address: str
    course: str
    fee: int
    collegeName: str
    rollNumber: str