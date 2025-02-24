# wrts-forum-api
A wrapper for the studygo.com forum api.
This wrapper is used to log in, and do things in the studygo.com forum for asking questions.

**Current Functions**
- Get the last `n` questions (defaults to 20) `forum_get_all(range)`
- Get info about a question `forum_question_get(id)`
- Answer a question `forum_question_answer(id, answer)`
- Like an answer `forum_answer_like(id)`

## Setting up a client.
Make a client with the `Client` class, like this:
```python
client = Client(email, password)
```
That's it! You now have a client logged in.

## How the wrapper works
It simply makes requests to do certain things.

## Extra's:
- There are some examples in the `examples` folder.
- This will be a pip package soon
- I will port it to typescript soon (including npm)

This package is officialy made for educational purposes.
