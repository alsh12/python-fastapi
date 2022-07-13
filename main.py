import imp
from tokenize import String
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}


@app.get('/blog')
def blog(limit:int=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'list of {limit} published blogs'}
    else:
        return {'data':f'list of {limit} blogs'}

@app.get('/blog/unlisted')
def unlisted():
    return {'data':'unlisted blogs'}

@app.get('/blog/{id}')
def index(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def blogComents(id:int):
    return {'data':'comments for blog '+str(id)}