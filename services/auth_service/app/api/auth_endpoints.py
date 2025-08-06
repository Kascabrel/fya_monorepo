from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    decode_refresh_token,
    SECRET_KEY,
    ALGORITHM,
)
from app.db import sessionLocal
from app.repository.user_repository import (
    authenticate_user,
    get_by_email,
    create_user,
)
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import (
    RefreshTokenRequest,
    RefreshTokenResponse,
    LoginResponse,
    TokenData,
)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    """Dependency to get DB session."""
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> UserOut:
    """
    Validates the current user's access token and retrieves the user.

    Args:
        token (str): JWT access token.
        db (Session): SQLAlchemy session.

    Returns:
        UserOut: User data if token is valid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(sub=email)
    except JWTError:
        raise credentials_exception

    user = get_by_email(db, email=token_data.sub)
    if user is None:
        raise credentials_exception

    return UserOut.model_validate(user)


@router.get("/home", tags=["Auth"])
def hello_world():
    """
    Simple tests route for API health check.
    """
    return {"hello": "Welcome to the home"}


@router.post("/register", response_model=UserOut, status_code=201, tags=["Auth"])
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    Args:
        user_create (UserCreate): Email and password.
        db (Session): DB session.

    Returns:
        UserOut: Newly created user.
    """
    user = get_by_email(db, email=str(user_create.email))
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user_create)
    return new_user


@router.post("/login", response_model=LoginResponse, tags=["Auth"])
def login(
        form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Authenticates a user and returns access + refresh tokens.

    Args:
        form_data (OAuth2PasswordRequestForm): username & password.
        db (Session): DB session.

    Returns:
        LoginResponse: Token and user data.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserOut.model_validate(user),
    )


@router.post("/refresh-token", response_model=RefreshTokenResponse, tags=["Auth"])
def refresh_token(request: RefreshTokenRequest):
    """
    Refreshes the access token using a valid refresh token.

    Args:
        request (RefreshTokenRequest): The refresh token payload.

    Returns:
        RefreshTokenResponse: New access token.
    """
    try:
        payload = decode_refresh_token(request.refresh_token)
        email = payload.sub
        if not email:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        # New access token based on the original user's email
        new_access_token = create_access_token(data={"sub": email})

        return RefreshTokenResponse(access_token=new_access_token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


@router.get("/me", response_model=UserOut, tags=["Auth"])
def get_me(current_user: UserOut = Depends(get_current_user)):
    """
    Retrieve the current authenticated user's profile.

    Args:
        current_user (UserOut): Injected by dependency from JWT token.

    Returns:
        UserOut: Current user info.
    """
    return current_user
