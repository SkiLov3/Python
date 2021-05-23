import requests
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from uuid import uuid4
bhr_users={ "5246": {"firstName":"Tom","lastName":"McTest","email":"tmctest@grove.co","dept":"Testing Center"}
         }
jc_users = {}
app = FastAPI()
class UserOut(BaseModel):
    email: EmailStr
    firstName: str
    lastName: str
class UserBHR(BaseModel):
    email: Optional[EmailStr]
    firstName: Optional[str]
    lastName: Optional[str]
#pull data from BHR datastore, store in var
@app.get("/bhr/{user_id}",response_model=UserOut)
def read_user(user_id: str):
    return bhr_users[user_id]
#Post request
#post data from get var dict to JC endpoint
@app.post("/jumpcloud/create")
def create_user(user_in: UserBHR):
    jc_users.update(user_in)
    return user_in

@app.get("/jumpcloud/get/{email}")
async def read_user(email: EmailStr):
    return jc_users[email]
#get from JC endpoint to verify the data storage
#r = requests.post(http://127.0.0.1:8000/jumpcloud/create, user_in = {jc_data})





