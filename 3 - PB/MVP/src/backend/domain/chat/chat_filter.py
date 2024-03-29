from dataclasses import dataclass

"""
ChatFilter: classe che rappresenta un filtro per la ricerca di chat
    Attributes:
        searchFilter (str): Il filtro di ricerca
"""
@dataclass
class ChatFilter:
    searchFilter: str