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
pip-compile --generate-hashes --index-url=https://pypi.python.org/simple --output-file=requirements.txt requirements.in
```

To run the project:

```
uvicorn app:app --reload --port 8080
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

Easy to access endpoints: 
```
1. http://localhost:8080/
2. http://localhost:8080/docs
3. http://localhost:8080/health
4. http://localhost:8080/metrics
5. http://localhost:8080/api/fizzbuzz
6. http://localhost:8080/api/most_common
```


Questions:

What was your reasoning behind the tech stack used for this challenge?
```
    For this challenge I used FastAPI for backend and Javascript/JQuery for frontend. 
    FastAPI is fast web framework which in conjunction with uvloop and asyncio library allows efficient handling for requests and makes scalability of the app much easier.
    For frontend I decided to go with Javascript and JQuery with CSS templating due to its simplicity, but other frameworks like React or Angular would have also worked. 
    While JQuery might not be optimal for more complicated sites where handling of private data due to potential security leaks, in this scenario it works without any concerns. 
```

What piece of this challenge did you find the most challenging and why?
```
    While this application wasn't too hard to build out, some challenges I faced were around how robust the application would have to be and trying to make the frontend friendly enough and easy to operate.
```
How would you deploy this application for external users to use?
```
    1. To deploy this initially I would go with either Heroku or AWS. I like the fact that Heroku is pretty simple to use, maintain and cheap but if the application had scalability in mind I would choose AWS.
    2. Then I would create a container to host my application and make sure all of my dependencies are installed properly (Python/Javascript).
    3. After making sure that all dependencies are installed properly, I would either link a private github link hosting the code or use an FTP/SCP to copy everything to the container.
    4. We will need to make sure that any configuration files are properly protected/stored which we can use somthing like HashiCorp Vault cluster. After we have that we need to make sure that any environment variables are properly passed in which typically can be done via the web console/command line for Heroku/AWS.
    5. Next we want to make sure that the application starts properly which can be done via `uvicorn app:app --host 0.0.0.0 --port 8080` for the backend.
    6. If no errors pop up when booting it up, test the application via the web and api endpoints to make sure everything works as intended.
    7. Next we will need a domain name (which will need to purchased separately) and we'll need to configure it to point to the IP address from the provider where we deployed our application.
    8. We should also add an extra layer of security making sure the application is configured properly using HTTPS and potentially add some sort of external/internal authentication or authorazitaions (would mainly be useful for some of the metrics data exposed by /metrics).
    9. After all is deployed we will need to monitor the logs by either checking the /metrics endpoint or ssh into the container to see the type of requests being made. Might need to add extra exception handling and error logging and making sure that any security vulnerabilities are addressed properly.
    
```
After deploying your code, it seems to have gone viral as the most awesome app ever created in the history of time itself. How would you handle scaling and support your FizzBuzz app?

```
    While FastAPI and asyncio are sure ways to make ensure the application can handle traffic properly asyncronously we will need to address proper scaling on the server side.
    We can begin by adding more containers or vms in order to increase the resources being provided to each instance along with some sort of ratelimit being present.
    By increasing the resources to each instance we should also start to distribute the traffic across multiple instance.
    Another step to make sure reliability is provided is adding some sort of caching in order to reduce the load on the backend (in memory caching would be sufficient for an app like this), along with a CDN (content delivery network) by caching JavaScript and making sure they are served closer to the user making the request.
    When scaling having proper logs implemented is key, while I implemented prometheus logs and basic logging we would need to expand on that and include Grafana and Graylog as well (plenty of other options to chose from as well).
    API documentation updates would also be necessary to ensure that the users know how to properly use the endpoints and try to reduce the amount of spam requests being made. In addition to this we need some sort of integration for users to report bugs (previously I used Zendesk for this). 
```
