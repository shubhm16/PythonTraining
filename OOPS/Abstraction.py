# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:21:53 2025

@author: shubh
"""

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())