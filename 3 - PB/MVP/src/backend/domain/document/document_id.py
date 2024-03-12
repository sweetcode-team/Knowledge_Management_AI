from dataclasses import dataclass

"""The unique identifier of a document."""
@dataclass
class DocumentId:
    id: str
    
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, DocumentId) and self.id == other.id