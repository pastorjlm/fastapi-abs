import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return token
     
    


def signJWT(user_id: str,username:str,phone:int,address:str,city:str,subs:int) -> Dict[str,str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    response ={
        "access_token":token,
        "expires_in":time.time() + 600,
        "token_type":"Bearer",
        "id":user_id,
        "username":username,
        "phone":phone,
        "city":city,
        "address":address,
        "payment":subs
        }
    return token_response(response)



def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    