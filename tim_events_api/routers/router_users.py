from fastapi import APIRouter, Depends, HTTPException, status
from ..crud.users import *
from ..schemas import schema_users
from ..dependencies import get_db, ACCESS_TOKEN_EXPIRE_MINUTES
from ..schemas.schema_token import Token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["users"])


@router.post("/token", response_model=Token)
def login_for_access_token(db: Session= Depends(get_db),
                           form_data: OAuth2PasswordRequestForm = Depends()
                           ):
        user = authenticate_user(db=db, 
                                 username=form_data.username, 
                                 password=form_data.password
                                 )
        if not user:
                raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail= "Invalid Email or Password",
                        headers= {"WWW-Authenticate": "Bearer"}
                )
        expire_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        data = {"sub": form_data.username}
        access_token = create_access_token(data=data,
                                           expire_timdelta=expire_time
                                           )
        return Token(access_token=access_token, token_type="bearer")
        


@router.post("/users/", response_model=schema_users.User)
def create_user(user: schema_users.UserCreate, db: Session=Depends(get_db)):
        db_user_email = get_user_by_email(db=db, email=user.email)
        db_user_username = get_user_by_username(db=db, username=user.username)
        if db_user_email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="User with this Email Exists"
                                    )
        
        if db_user_username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="User with that Username already exists"
                                    )
        return add_user(db=db, user=user)


@router.get("/users/me/", response_model=schema_users.User)
def get_user_me(current_user: schema_users.User = Depends(get_current_user)):
        return current_user


@router.get("/users/{user_id}/", response_model=schema_users.User)
def read_user(
        user_id: int,
        db: Session=Depends(get_db),
        current_user: schema_users.User = Depends(get_current_user)
        ):
        if user_id != current_user.id:
                if not current_user.is_admin:
                    raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Cannot See the specified user, you are not an admin"
                        )
        user = get_user(user_id=current_user.id, db=db)
        if not user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="user does not exist")
        return user


@router.put("/users/me/", response_model=schema_users.User)
def update_user(
        user: schema_users.UserUpdate,
        db: Session=Depends(get_db),
        current_user: schema_users.User = Depends(get_current_user)
        ):
        db_user = get_user(user_id=current_user.id, db=db)
        if not db_user:
                raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                          detail="user does not exist"
                          )
        updated_user = edit_user(user=user, user_id=current_user.id, db=db)
        return updated_user


@router.delete("/users/me/")
def delete_user(
                db: Session=Depends(get_db),
                current_user: schema_users.User = Depends(get_current_user)
                ):
        return remove_user(user_id=current_user.id, db=db)
