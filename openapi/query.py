from greeter_client import ApiClient, Configuration, DefaultApi, Person

configuration = Configuration()
client = ApiClient(configuration)
api = DefaultApi(client)
me = Person(name='bryan')
greeting = api.greet(me)
print(greeting.message)
