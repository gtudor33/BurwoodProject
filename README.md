# fizz_buzz

This is an application with an endpoint to determine if a number is divisible by 3 then output is Fizz, if number is divisible by 5 then output is Buzz and if number is divisible by 15 then output is FizzBuzz. It also has another endpoint to display the 3 most common numbers submitted with their corresponding counts.

## Base project

The base project contains:

- fastapi setup with base endpoints (metrics, health and info)
- prometheus instrumentation and context managers

## Running the project

You will need to build the `requirements.txt` file. You need `pip-tools` for that:

```
pip install pip-tools
make requirements.txt
```

To run the project:

```
set -o allexport; source example.env; set +o allexport
python -m fizz-buzz
```

Optionally, you can pass the `--reload` flag for the server to automatically restart whenever a file changes.

You can confirm it is running by checking the base endpoints:

```
http://localhost:8080/health
http://localhost:8080/metrics
```

To run the tests:

```
python -m pytest
```

To start the project with docker-compose, just run:

```
docker-compose -p fizz-buzz up fizz-buzz
```


