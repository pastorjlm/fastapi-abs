
from fastapi import FastAPI, Body, Depends,APIRouter,HTTPException
from sqlalchemy import insert
from services.users import UserService
from schemas.users import User, UsersCreate,UsersLoginSchema,UserPaypalSchema
from auth.auth_bearer import JWTBearer
from utils.service_result import handle_result
from auth.auth_handler import decodeJWT
from config.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/signup", response_model=User)
async def create_user(item: UsersCreate, db: get_db = Depends()):
    result = UserService(db).create_user(item)
    return handle_result(result)




@router.post("/login", tags=["user"])
async def user_login(user: UsersLoginSchema = Body(...),db: get_db = Depends()):
    result = UserService(db).login(user)
    
    return handle_result(result)


@router.post("/paypal", tags=["user"])
async def user_paypal(paypal: UserPaypalSchema = Body(...),db: get_db = Depends()):
    result = UserService(db).paypal(paypal)
    return handle_result(result)



@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: get_db = Depends()):
    result = UserService(db).get_user(user_id)
    return handle_result(result)
