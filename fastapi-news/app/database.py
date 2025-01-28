import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables
# load_dotenv()
# host=os.getenv("DB_HOST")
# user=os.getenv("DB_USER")
# passwd=os.getenv("DB_PASS")
# database=os.getenv("DB_NAME")
# encoded_passwd = quote_plus(passwd)


# SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{passwd}@{host}/{database}"
# 
DATABASE_URL = "mysql+mysqlconnector://root:IamAshiq105435@localhost/news"

# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(DATABASE_URL)


# try:
#     connection = engine.connect()
#     print("Connected to the MySQL database!")
#     connection.close()
# except Exception as e:
#     print(f"An error occurred: {e}")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
