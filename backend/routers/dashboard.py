from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from security import get_current_user

from services.dashboard import get_user_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/user")
def user_dashboard(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    return get_user_dashboard(db, current_user.id)