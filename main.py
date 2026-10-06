from fastapi import FastAPI 
from  APP.API.Routes import route

app=FastAPI()
app.include_router(route)






