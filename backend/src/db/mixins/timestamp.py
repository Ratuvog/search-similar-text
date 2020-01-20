from sqlalchemy import Column, func, DateTime


class CreatedAt:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now()
    )


class UpdatedAt:
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now()
    )


class DeletedAt:
    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


class Timestamps(CreatedAt, UpdatedAt):
    pass


class SoftDelete(CreatedAt, UpdatedAt, DeletedAt):
    pass
