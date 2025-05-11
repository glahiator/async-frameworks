from typing import Optional, Union
from fastapi import APIRouter
import sys

# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.get("/")
async def root_handler():
    return {"version": "v1"}


@router.get("/info")
async def info_handler():
    return {"api": "v1", "python": sys.version_info}


@router.get("/filter")
async def filter_handler(param1, param2):
    return {"action": "filter", "param1": param1, "param2": param2}


@router.get("/filter_val")
async def filter_val_handler(
    param1: str,
    param2: Optional[int] = None,
) -> dict[str, Union[str, int]]:
    return {"action": "filter", "param1": param1, "param2": param2}
