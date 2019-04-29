"""Example models."""

from sqlalchemy import Column, Integer, text, DateTime, func, create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import MetaData
import os


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class PageView(Base):
    """Example model storing some data about page views."""

    __tablename__ = 'page_views'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, server_default=func.now(), nullable=False)
    data = Column(JSONB, server_default=text("'{}'"))

    def __repr__(self):
        """human-readable representation of an instance of this model."""
        return f'PageView#{self.id}'


def get_database_url():
    """Subj."""
    return os.environ.get(
        'DATABASE_URL',
        'postgresql://example:example@localhost:5432/example')


def setup(**kwargs):
    """Return database engine and a thread-local session factory."""
    engine = create_engine(
        get_database_url(),
        implicit_returning=False,
        **kwargs
    )

    Session = sessionmaker(bind=engine, autocommit=False, autoflush=True)
    return engine, scoped_session(Session)
