from graphene import Mutation,Float,String,Field,ObjectType,Boolean,Int
from gql.type import EmployeeObject
from db.couchbase import dbClient
import os

class AddEmployee(Mutation):
    class Arguments:
        firstName = String(required=True)
        lastName = String(required=True)
        age = Int(required=True)
        email = String(required=True)
        phone = Float(required=True)
        sex = String(required=True)
        department = String(required=True)
        salary = Float(required=True)
        role = String(required=True)
    employee = Field(lambda : EmployeeObject)

    @staticmethod
    def mutate(root,info,firstName,lastName,age,email,phone,sex,department,salary,role):
        id = dbClient.get(os.getenv("EMP_ID_KEY"))
        dbClient.upsert(os.getenv("EMP_ID_KEY"), id.value + 1)
        id = "EMP" + str(id.value)
        emp = EmployeeObject(id,firstName,lastName,age,email,phone,sex,department,salary,role)
        dbClient.insert(id,emp.getEmployee())
        return AddEmployee(employee=emp)

class UpdateEmployee(Mutation):
    class Arguments:
        id = String(required=True)
        age = Int()
        email = String()
        phone = Float()
        department = String()
        salary = Float()
        role = String()
    employee = Field(lambda : EmployeeObject)

    @staticmethod
    def mutate(root,info,id,age,email,phone,department,salary,role):
        result = dbClient.get(id).value
        if age is not None:
            result["age"] = age
        if email is not None:
            result["email"] = email
        if phone is not None:
            result["phone"] = phone
        if department is not None:
            result["department"] = department
        if salary is not None:
            result["salary"] = salary
        if role is not None:
            result["role"] = role
        dbClient.upsert(id,result)

        return UpdateEmployee(employee=result)

class DeleteEmployee(Mutation):
    class Arguments:
        id = String(required=True)

    status = Boolean()

    @staticmethod
    def mutate(root,info,id):
        try:
            dbClient.remove(id)
        except:
            return DeleteEmployee(status=False)
        return DeleteEmployee(status=True)

class Mutation(ObjectType):
    add_employee = AddEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()