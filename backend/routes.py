from fastapi import APIRouter

from backend.modules.calcul import square
from backend.schemas import Integer

router = APIRouter(prefix='/api')

@router.get('/')
async def hello_world():
    return {'message': 'Hello, world!'}

@router.get('/health')
async def heath():
    return {'message': 'The server is up and running!'}

@router.post('/calcul')
async def calcul(integer: Integer):
    result = square(integer.integer)
    return {'result': result}