from fastapi import Request , Response ,Form, status
from fastapi import APIRouter as AR
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from pydantic_core import InitErrorDetails 
from APP.Schema.Struc import User

User_name=""
route=AR()
template=Jinja2Templates(directory="APP/Web_Pages")

@route.get("/",response_class=HTMLResponse)
async def root(request:Request) -> Response:
    return template.TemplateResponse(
        request=request,
        name="Login.html",
        context={"request":request}
    )

@route.post("/user-login",name="user-login",response_class=HTMLResponse)
async def login(request:Request,user:str=Form(...),password:str=Form(...)) -> Response:

    user_list={"deep@gmail.com":"Deep","yogesh@gmail.com":"yogesh"}
    user_password="deep"
    
    try:
        User(idd=user,Password=password)
        if user in user_list.keys() and password==user_password:
            global User_name
            User_name+=str(user_list.get(user))
            return template.TemplateResponse(
                request=request,
                name="Index.html",
                context={"request":request,"username":user_list.get(user)}
            )
        else:
            return template.TemplateResponse(request, "login.html", {"err": "Invalid ID or Password!"})


    except ValidationError as e:
        return HTMLResponse(content=f"<h4>Plese Enter Correct Data {e}</h4>",status_code=status.HTTP_406_NOT_ACCEPTABLE)


@route.get("/index",response_class=HTMLResponse)
def index(request:Request) -> Response:
    return template.TemplateResponse(
        request=request,
        name="Index.html",
        context={"request":request,"username":User_name}
    )

@route.get("/item",response_class=HTMLResponse)
def item(request:Request,item_id:int) -> Response:
    item_list={1:"coffee",2:"Tea",3:"choclate"}
    if item_id is None or item_id =="":
        con="<h4>There Is No Item Mention</h4>"
        return HTMLResponse(content=con)
    return template.TemplateResponse(
        request=request,
        name="itemlist.html",
        context={"request":request,"Itemname":item_list.get(item_id, "Not Found")}
    )

@route.get("/user",response_class=HTMLResponse)
async def user(request:Request ,username:str | None=None ) -> Response:
    if username is None or username=="":
        con="<h4>noo IUser Exist</h4>"
        return HTMLResponse(content=con)
    else:
        return template.TemplateResponse(
            name="User.html",
            request=request,
            context={"request":request,"username":username}
        )

@route.get("/form",name="form",response_class=HTMLResponse)
def form_ren(request:Request) -> Response:
    return template.TemplateResponse(
        request=request,
        name="form.html",
        context={"request":request}
    )

@route.post("/user-submit",name="form-submit",response_class=HTMLResponse)
async def submit(
    request:Request,
    id:str=Form(...),
    password: str= Form(...)
    ) -> Response:
    
    try:
        User(idd=id,Password=password)
        return template.TemplateResponse(
            name="User.html",
            request=request,
            context={"request":request,"username":id}
        )
    except ValidationError as e:
        return HTMLResponse(content= f"<h4>Plese Enter Correct Data {e}</h4>",status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
