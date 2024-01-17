#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models


class User(BaseModel):
    """This class defines a user by various attributes"""
    __table__ = 'users'
    email = ''
    password = ''
    first_name = ''
    last_name = ''
