from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import functools
from conf.config import MYSQL

engines = {}

for role, role_settings in MYSQL.items():
    role_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
                "?charset=utf8".format(**role_settings))
    engines[role] = create_engine(role_url,
                                  pool_size=10,
                                  max_overflow=-1,
                                  pool_recycle=1800)

from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=True, bind=engines['master']))


def using_bind(name):
    try:
        return scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engines[name]))
    except:
        raise KeyError


ModelBase = declarative_base()


def commit_decorator(DBSession):
    def _wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            session = DBSession()
            try:
                func(*args, **kwargs)
                session.commit()
            except:
                session.rollback()

        return wrapper

    return _wrapper


db_commit = commit_decorator(DBSession)
