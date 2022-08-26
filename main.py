from typing import Optional

from fastapi import FastAPI
import json
from test import get_json_data
app = FastAPI()


# defining a decorator 
def hello_decorator(func): 
    
    # inner1 is a Wrapper function in  
    # which the argument is called 
        
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
    
        # calling the actual function now 
        # inside the wrapper function. 
        data = func() 
    
        print("This is after function execution") 
        return data
            
    return inner1 


@app.get("/")
def read_root():
    return {"Hello": "World, It's Dedar"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test/data")
@hello_decorator
def test_data():
    return get_json_data()


