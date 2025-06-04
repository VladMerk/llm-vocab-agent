from enum import Enum

from pydantic import BaseModel, Field


class Gender(str, Enum):
    maskuline = "Maskuline"
    feminine = "Feminine"
    neuter = "Neuter"


class Substantiv(BaseModel):
    gender: Gender = Field(description="Род существительного")
    level: str = Field(description="Уровень слова, в списках которых он встречается впервые: A1, A2, B1, B2, C1, C2")
    word: str = Field(
        description="Существительное на немецком языке, единственного числа, именительного падежа, с артиклем. "
        "Например: das Haus"
    )
    translate: str = Field(description="Перевод существительного на русский язык")
    genetiv: str = Field(description="Форма существительного родительного падежа(Genetiv), например: des Hauses")
    plural: str = Field(description="Множественное число существительного с артиклем, например: die Häuser")
    example: list[str] = Field(
        default_factory=list, description="Примеры предложений с существительным и переводом на русский язык"
    )
    note: str = Field(
        default="",
        description=(
            "Только важные пояснения/нюансы употребления существительного. Если их нет, тогда верните пустую строку"
        ),
    )

    def __str__(self):
        examples = "\n\t".join(self.example)
        return (
            f"# {self.word} - {self.translate}, {self.genetiv}, {self.plural}"
            f"\n\t{self.gender.value}, {self.level}"
            f"\n\t{examples}\n\t{self.note}"

        )


class SubstantivList(BaseModel):
    substantiven: list[Substantiv]

    def __str__(self):
        return "\n".join(str(subs) for subs in self.substantiven)
