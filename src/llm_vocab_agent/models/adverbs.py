from pydantic import BaseModel, Field


class Adverb(BaseModel):
    word: str = Field(description="Наречие на немецком языке")
    translate: str = Field(description="Перевод наречия на русский язык")
    examples: list[str] = Field(
        default_factory=list, description="Примеры предложений с наречиями, вместе с переводом на русский язык"
    )

    def __str__(self):
        examples = "\n# ".join(self.examples)
        return f"{self.word} - {self.translate}\n{examples}"


class AdverbList(BaseModel):
    adverbs: list[Adverb]

    def __str__(self):
        return "\n".join(str(adv) for adv in self.adverbs)
