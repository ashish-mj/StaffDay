from flask_graphql import GraphQLView
from graphene import Schema
from flask import Flask
from gql.query import Query
from gql.mutation import Mutation

app = Flask(__name__)

schema = Schema(query=Query,mutation=Mutation)

app.add_url_rule('/staffday',view_func=GraphQLView.as_view( 'staffday',schema=schema, graphiql=True))

if __name__ == '__main__':
	app.run(debug=True)