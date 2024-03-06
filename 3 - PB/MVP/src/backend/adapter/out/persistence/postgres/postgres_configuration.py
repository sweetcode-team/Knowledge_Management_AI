from typing import Dict
from dataclasses import dataclass

@dataclass
class PostgresConfiguration:
    vectorStore: Dict[str, str]
    embeddingModel: Dict[str, str]
    llmModel: Dict[str, str]
    documentStore: Dict[str, str]