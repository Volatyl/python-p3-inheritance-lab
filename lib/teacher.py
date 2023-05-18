#!/usr/bin/env python

from user import User

import random


class Teacher(User):

    knowledge = ['Sth']

    def teach(self):
        for i in self.knowledge:
            return i
