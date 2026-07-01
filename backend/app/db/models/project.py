import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Project(Base):

    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    industry: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    company_stage: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    decision_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    owner = relationship("User")

    documents = relationship(
        "Document",
        back_populates="project",
        cascade="all, delete-orphan",
    )

    decisions = relationship(
        "Decision",
        back_populates="project",
        cascade="all, delete-orphan",
    )