from pydantic import BaseModel


class UsersBase(BaseModel):
      username: str


class UsersCreate(UsersBase):
      username: str
      email: str
      password: str
      phone:int
      address:str
      zipCode:int
      city:str
      


class User(UsersBase):
    id: int

    class Config:
        orm_mode = True

class UsersLoginSchema(BaseModel):
   
    email: str
    password: str
 
    class Config:
        orm_mode = True




class UserPaypalSchema(BaseModel):
    user_id: int
    orderId:str
    
    
    class Config:
        orm_mode = True

