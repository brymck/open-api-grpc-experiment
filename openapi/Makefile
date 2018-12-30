BREW_PREFIX = $(shell brew --prefix)

all: deps install

clean:
	rm -rf client

deps:
	brew install swagger-codegen@2

install:
	pip install --editable server/
	{ python -c 'import greeter_server as gs; gs.app.run()' & }; \
	    pid=$$!; \
	    sleep 1s; \
	    curl --header 'Content-Type: application/json' localhost:5000/schema > openapi/swagger.json; \
	    kill $$pid
	rm -rf generated
	$(BREW_PREFIX)/opt/swagger-codegen@2/bin/swagger-codegen generate --input-spec swagger.json --lang python --config config.json --output client
	pip install --editable client/

serve:
	python -c 'import greeter_server as gs; gs.app.run()'

query:
	python openapi/query.py

.PHONY: all clean deps install serve query
