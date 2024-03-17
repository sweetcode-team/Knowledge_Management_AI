from dataclasses import dataclass
from datetime import datetime

"""
ChatInfo: classe che rappresenta le informazioni di una chat
    Attributes:
        title (str): Il titolo della chat
        timestamp (datetime): Il timestamp della chat
"""
@dataclass
class ChatInfo:
    title: str
    timestamp: datetime