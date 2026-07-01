from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models.user import User
from app.core.config import settings


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    authorization: str = None,
):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
        )

    try:
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            raise Exception()

        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )

        user_id = payload.get("sub")

    except (JWTError, Exception):
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user