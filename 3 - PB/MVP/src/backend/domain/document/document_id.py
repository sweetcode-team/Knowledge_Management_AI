from dataclasses import dataclass

"""The unique identifier of a document."""
@dataclass
class DocumentId:
    id: str
    
    """
    Args:
        id (str): The unique identifier of the document.
    Returns:
        DocumentId: The DocumentId object.
    """
    def __hash__(self):
        return hash(self.id)

    """
    Args:
        other (Any): The object to compare.
    Returns:
        bool: True if the object is a DocumentId and has the same id, False otherwise.
    """
    def __eq__(self, other):
        return isinstance(other, DocumentId) and self.id == other.id