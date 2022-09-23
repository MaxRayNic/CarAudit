from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from configurations import settings

db_uri_format = 'postgresql://{user}:{password}@{host}/{db_name}'

db_uri = db_uri_format.format(**settings.POSTGRES_CRED)

engine = create_engine(db_uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

