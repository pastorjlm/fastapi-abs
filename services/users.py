import email
from schemas.users import User, UsersCreate,UsersLoginSchema
from utils.app_exceptions import AppException
from sqlalchemy import exc
from services.main import AppService, AppCRUD
from models.users import Users
from utils.service_result import ServiceResult
from auth.auth_handler import signJWT

class UserService(AppService):
    def create_user(self, user: UsersCreate) -> ServiceResult:
        user_create = UserCRUD(self.db).create_user(user)
        if not user_create:
            return ServiceResult(AppException.UserCreate())
        return ServiceResult(user_create)

    def get_user(self, user_id: int) -> ServiceResult:
        user_get = UserCRUD(self.db).get_user(user_id)
        if not user_get:
            return ServiceResult(AppException.UserGet({"user_id": user_id}))
        
        return ServiceResult(user_get)

    def login(self, user:UsersLoginSchema) -> ServiceResult:
        user_get = UserCRUD(self.db).login(user)
        # if not user_get:
        #     return ServiceResult(AppException.UserGet({"user_id": user_id}))
        
        return ServiceResult(user_get)    


class UserCRUD(AppCRUD):
    def create_user(self, user: UsersCreate) -> Users:
        
        user_create = Users(
            username=user.username,
             email=user.email, 
             password=user.password,
             phone=user.phone,
             address=user.address,
             zipCode=user.zipCode,
             city=user.city)
        self.db.add(user_create)
        try:
         self.db.commit()
         self.db.refresh(user_create)
         return user_create
        except exc.SQLAlchemyError as err:
         return None

    def get_user(self, user_id: int) -> Users:
        user_get = self.db.query(Users).filter(Users.id == user_id).first()
        if user_get:
            return user_get
        return None

    def login(self, user: UsersLoginSchema) -> Users:
        result = self.db.query(Users).filter(Users.email == user.email).first()
        if result is None:
            return {"error":"No user found"}
        if user.email == result.email and user.password == result.password:
           return signJWT(result.id)
        return {"error": "Wrong login details!" }   
