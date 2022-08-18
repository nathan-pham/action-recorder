from __future__ import annotations
from typing import *
import json

DELIMITER = " ||| "

class Action:
    def __init__(self, type: str, data: Any):
        self.type = type
        self.data = data

    def __str__(self) -> str:
        return f"{self.type}{DELIMITER}{json.dumps(self.data)}"

    def __repr__(self) -> str:
        return str(self)

    def equals(self, action: Action):
        return str(action) == str(self)

    @classmethod
    def parse(cls, line: str) -> Action:
        type, data = line.split(DELIMITER)
        return cls(type, json.loads(data))