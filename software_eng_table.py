#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

"""This scripts creates a table called Software_engineer"""

engine = create_engine("sqllite:///sqllite.db")

Base = declarative_base()

"""Defining model""" 
class SE(Base):
   __tablename__ = 'software_engineer'
   id = column(Integer, primary_key=True, autoincrement=True)
   name = column(String(64), nullable=False)
   email = column(String(100), unique=True) 

"""create the tables"""
Base.metadata.create_all(engine)
