from dataclasses import dataclass

"""
DocumentFilter: classe che rappresenta un filtro per la ricerca di documenti
    Attributes:
        searchFilter (str): Il filtro di ricerca
        
"""
@dataclass
class DocumentFilter:
    searchFilter: str