from fastapi import APIRouter



from apis.version1.no_auth import route_sign_in
from apis.version1.no_auth import route_login
from apis.version1.payments import route_payments

api_router = APIRouter()

api_router.include_router(route_sign_in.router,prefix="/sign_in",tags=["sign_in"])
api_router.include_router(route_login.router,prefix="/login",tags=["login"])
api_router.include_router(route_payments.router,prefix="/payment",tags=["payments"])