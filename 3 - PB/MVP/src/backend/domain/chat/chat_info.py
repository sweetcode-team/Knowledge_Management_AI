from dataclasses import dataclass
from datetime import datetime

@dataclass
class ChatInfo:
    title: str
    timestamp: datetime