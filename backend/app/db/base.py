from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    Every table in ShadowBoard inherits from this.
    """
    pass