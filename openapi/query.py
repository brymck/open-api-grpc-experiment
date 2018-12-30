from greeter_client import ApiClient, Configuration, DefaultApi, Person

configuration = Configuration()
client = ApiClient(configuration)
api = DefaultApi(client)
greeting = api.greet(payload=Person(name='bryan'))
print(greeting.message)
