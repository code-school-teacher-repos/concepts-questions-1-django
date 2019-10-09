# Coding Concept questions for Django backend

### Start with the skeleton Django project provided. Do NOT create a new Django project using ```django-admin``` 

## Exercise 1: Endpoints/Routes/Redirects
You need to implement an endpoint ```user_check/``` that accepts a dynamic ```user_id``` (a number) as part of the endpoint URL. 

* If no number provided, or the number provided is negative (less than 0) your view should *redirect* the user to an HTML page that says ```Sorry Invalid User ID please try again!```

* If the user number is present and positive in the request, your view should display an HTML page that welcomes the user with a message that includes the user number provided in the request.

Sample Request:

```http://localhost:8000/user_check/2112/```

Sample Response in HTML:
```Welcome to the site User 2112!```


## Exercise 2: Endpoints/Routes/Templates
You need to implement an endpoint ```letter_kount``` that accepts a dynamic ```word_to_check``` (a string) as part of the endpoint URL. 

* If no string provided, respond with the message ```Please provide a string!```

* If a string is provided your view should determine which letter appears most frequently in the word and respond with a message that includes the word submitted and which letter appeared most often.


Sample Request:

```http://localhost:8000/letter_kount/momma```

Sample Response:

```'m' appears 3 times in the submitted word 'momma'```
