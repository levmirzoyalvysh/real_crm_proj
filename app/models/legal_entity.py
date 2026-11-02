from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

if TYPE_CHECKING:
    from app.models.company import Company

from app.models.base import Base
from app.models.base import UUIDPrimaryKeyMixin, TimestampMixin



class LegalEntity(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "legal_entities"

    company_id: Mapped[UUID] = mapped_column(ForeignKey('companies.id',ondelete='CASCADE'))

    name: Mapped[str] = mapped_column(String(100))

    company: Mapped["Company"] = relationship(back_populates="legal_entities")



    
