from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pos_back_end.api.menu.menu_models import PostMenuCategoryRequestBody, PostMenuItemRequestBody
from pos_back_end.api.menu.menu_services import MenuServices
from pos_back_end.db.dependencies import get_db

router = APIRouter()

@router.get("/menu")
def get_menu(restaurant_id: int, db: Session = Depends(get_db)):
    return MenuServices.get_menu_categories(restaurant_id, db)


@router.post("/categories")
def post_menu_category(request: PostMenuCategoryRequestBody, db: Session = Depends(get_db)):

    new_menu_category = MenuServices.create_menu_category(request)

    db.add(new_menu_category)
    db.commit()


@router.post("/items")
def post_menu_item(request: PostMenuItemRequestBody, db: Session = Depends(get_db)):

    new_menu_item = MenuServices.create_menu_item(request)