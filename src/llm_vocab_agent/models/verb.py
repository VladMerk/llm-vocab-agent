from enum import Enum

from pydantic import BaseModel, Field


class VerbType(str, Enum):
    regelmassig = "regelmässig"
    unregelmassig = "unregelmässig"


class VerbAUX(str, Enum):
    haben = "haben"
    sein = "sein"


class Verb(BaseModel):
    word: str = Field(
        description=(
            "Глагол на немецком языке. Если глагол возвратный, тогда добавлять в начало sich. Например: sich freuen"
        )
    )
    translate: str = Field(description="Перевод на русский язык.")
    level: str = Field(description="Уровни слов, в списках которых слово встречается впервые - A1, A2, B1, B2, C1, C2")
    verb_type: VerbType = Field(description="Правильный или неправильный глагол (regelmässig/unregelmässig)")
    aux: VerbAUX = Field(description="Вспомогательный глагол: haben/sein")
    presens_3st: str = Field(description="Форма 3го лица единственного числа настоящего времени")
    prateritum: str = Field(description="Präteritum 3го лица единственного числа")
    partizip_ii: str = Field(
        description="Partizip 2 3его лица единственного числа. Писать вместе со его вспомогательным глаголом. "
        "например, hat gesagt"
    )
    rektion: str | None = Field(
        default=None,
        description=(
            "Управление глагола предлогом. Описывать только одну форму управления, если у глагола их несколько. "
            "Форма ответа, например: (auf + Akk)."
            " Если управления нет, тогда возвращать пустую строку"
        ),
    )
    note: str | None = Field(
        default=None,
        description=("Только важные грамматические пометки об использовании слова. Пояснения давать на русском языке."),
    )

    def __str__(self):
        rektion = f" {self.rektion}" if self.rektion else ""
        note = f"\n## {self.note}" if self.note else ""
        return (
            f"# {self.word}{rektion} - {self.translate}"
            f" - {self.prateritum} - {self.partizip_ii}"
            f"{note}"
        )


class VerbList(BaseModel):
    verbs: list[Verb] = Field(description="Список глаголов")

    def __str__(self):
        return "\n\n".join(str(verb) for verb in self.verbs)
