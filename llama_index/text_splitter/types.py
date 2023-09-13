"""Text splitter implementations."""
from abc import ABC, abstractmethod
from typing import List, Union, Any

from llama_index.schema import BaseComponent


class TextSplitter(ABC, BaseComponent):
    class Config:
        arbitrary_types_allowed = True

    @abstractmethod
    def split_text(self, text: str) -> List[str]:
        ...


class MetadataAwareTextSplitter(TextSplitter):
    @abstractmethod
    def split_text_metadata_aware(self, text: str, metadata_str: str) -> List[str]:
        ...


# Splitter type could also be from llama_index.bridge.langchain.TextSplitter
SplitterType = Union[TextSplitter, Any]
