"""
    Exception class for elaboration errors
"""
class ElaborationException(Exception):
    def __init__(self, message):
        self.message = message