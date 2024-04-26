from graphene import ObjectType,List,Field,String
from gql.type import EmployeeObject
from db.couchbase import dbClient

class Query(ObjectType):
    employeeList = List(EmployeeObject)
    employee = Field(EmployeeObject,id=String(required="True"))

    @staticmethod
    def resolve_employeeList(root,info):
        return list(dbClient.query("SELECT db_employee.* from db_employee  WHERE meta().id LIKE 'EMP1%'"))

    @staticmethod
    def resolve_employee(root,info,id):
        return dbClient.get(id).value


