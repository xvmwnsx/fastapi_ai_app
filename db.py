from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(url="sqlite:///chat_requests.db")