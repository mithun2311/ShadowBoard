from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    TokenResponse,
)


from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(User).where(User.email == request.email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = User(
        id=uuid4(),
        full_name=request.full_name,
        email=request.email,
        hashed_password=hash_password(request.password),
    )

    db.add(user)

    await db.commit()

    await db.refresh(user)

    return RegisterResponse(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        message="User registered successfully",
    )


@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(
        subject=str(user.id),
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
    )