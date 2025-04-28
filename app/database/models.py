import datetime

from sqlalchemy import func, DateTime, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

BaseModel = declarative_base()


class DictConvertableMixin:
    def to_dict(self) -> dict:
        self_as_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue

            if isinstance(value, DictConvertableMixin):
                value = value.to_dict()

            self_as_dict[key] = value

        return self_as_dict


class Timestamps:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True
    )


class User(BaseModel, Timestamps, DictConvertableMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
