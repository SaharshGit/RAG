import numpy as np 
from pydantic import BaseModel
from dataclasses import dataclass

class DocumentPage(BaseModel):
    document_id :str
    document_name: str
    page_number: int
    text: str

class DocumentChunk(BaseModel):
    document_id: str
    document_name: str
    page_number: int
    chunk_id: str
    text: str

@dataclass
class IndexedChunk:
    chunk: DocumentChunk
    embedding: np.ndarray