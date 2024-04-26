from graphene import ObjectType, String,Int,Float

class EmployeeObject(ObjectType):
    id = String()
    firstName = String()
    lastName = String()
    age = Int()
    email = String()
    phone = Float()
    sex = String()
    department = String()
    salary = Float()
    role = String()

    def __init__(self, id: str, firstName: str, lastName: str, age: int, email: str, phone: float, sex: str,
                 department: str, salary: float, role: str):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.email=email
        self.phone=phone
        self.sex=sex
        self.department=department
        self.salary=salary
        self.role=role

    def getEmployee(self):
        emp = {"id": self.id, "firstName": self.firstName, "lastName": self.lastName, "age": self.age, "email": self.email, "phone": self.phone,
                    "sex": self.sex, "department": self.department, "salary": self.salary, "role": self.role}
        return emp
