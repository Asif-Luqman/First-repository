from fastapi import APIRouter, Depends
from app.dependencies import get_account_service

router = APIRouter(prefix= "/account", tags= ["Account"])