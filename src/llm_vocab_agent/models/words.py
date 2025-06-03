from typing import Optional

from pydantic import BaseModel

from .adjektivs import AdjektivList
from .adverbs import AdverbList
from .substantiv import SubstantivList
from .verb import VerbList


class DeutschWord(BaseModel):
    verbs: Optional[VerbList]
    substantivs: Optional[SubstantivList]
    adjektivs: Optional[AdjektivList]
    adverbs: Optional[AdverbList]
