from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

'''
In FastAPI, your main.py acts as the "blueprint" for your API. You define your data structures (the Pydantic models) first, and then you use them in your path operations (the functions) later in the same file.
'''
# 1. Define your Data Model
class Item(BaseModel):
    text: str
    is_done: bool = False
    
# 2. Create the FastAPI instance
app = FastAPI()

# 3. Your existing Root block
@app.get("/")
async def root():
    return {"message": "hello world"}

# 4. A new block using your Item model

# create endpoints to manage our list.
items = []
# POST: Create an item (Expects JSON payload)
@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return items
    #return {"message": f"Received: {item.text}", "status": item.is_done}
'''POST is the method used when you want to send data to a server to create something new.
Decorator: @app.post("/items") tells FastAPI to listen specifically for POST requests at the /items URL. If you try to visit this URL in your browser normally, you’ll get an error! Why? Because browsers perform GET requests by default when you type a URL. You need a tool (like FastAPI's /docs) to send a POST.
Think of POST endpoint as the "Create" button of your web application. While a GET request asks the server for data, a POST request sends data to the server—usually to save it in a database.
In FastAPI, this is handled seamlessly using Pydantic models to define what that data should look like.
To handle a POST request, you need two things:
    A Data Model: A class that defines the structure of the incoming data.
    The Route Decorator: Using @app.post().

Under the Hood when a client sends a request to your /items/ endpoint, FastAPI does the heavy lifting for you:
JSON Parsing: It reads the body of the request and converts the JSON into a Python dictionary.

With the built-in documentation you don't even need external tools like Postman to test this.
    Run your server: uvicorn main:app --reload
    Navigate to http://127.0.0.1:8000/docs
    Click on your POST method, hit "Try it out", and edit the JSON body.
    Hit Execute to see the server's response.
'''

# GET: Retrieve a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    return items[item_id]

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id >= len(items):
        # Return a 404 instead of crashing
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

''' save this file and execute on terminal 
>uvicorn main:app --reload
>Uvicorn running on http://127.0.0.1:8000
While FastAPI is the framework you use to write your code (the steering wheel, the seats, and the dashboard), 
Uvicorn is the actual server that handles the web requests coming from the internet and hands them to your Python code.

Why do you need it?

Python wasn't originally built to handle thousands of simultaneous web connections efficiently. To solve this, a standard called ASGI (Asynchronous Server Gateway Interface) was created.

Uvicorn is an ASGI server.
At url http://127.0.0.1:8000 I get json object
In web development, the single forward slash / is referred to as the Root Path. When you define decorator @app.get("/"), you are telling FastAPI: "Whenever someone visits the very base of my website (with no extra words in the URL), run the function directly below this."
{"message":"hello world"}'''