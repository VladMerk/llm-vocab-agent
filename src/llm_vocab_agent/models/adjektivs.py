from pydantic import BaseModel, Field


class Adjektiv(BaseModel):
    word: str = Field(description="Прилагательное на немецком языке")
    translate: str = Field(description="Перевод прилагательного на русский язык")
    examples: list[str] = Field(
        default_factory=list, description="Примеры словосочетаний с прилагательным, вместе с переводом на русский язык"
    )

    def __str__(self):
        examples = "\n# ".join(self.examples)
        return f"{self.word} - {self.translate}\n{examples}"


class AdjektivList(BaseModel):
    adjektivs: list[Adjektiv]

    def __str__(self):
        return "\n".join(str(adj) for adj in self.adjektivs)
