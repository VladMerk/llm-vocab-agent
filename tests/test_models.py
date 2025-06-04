from llm_vocab_agent.models import (
    Verb,
    VerbList,
    Substantiv,
    SubstantivList,
    Adjektiv,
    AdjektivList,
    Adverb,
    AdverbList,
)
from llm_vocab_agent.models.verb import VerbType, VerbAUX
from llm_vocab_agent.models.substantiv import Gender


def test_verb_list_str():
    verbs = [
        Verb(
            word="machen",
            translate="делать",
            level="A1",
            verb_type=VerbType.regelmassig,
            aux=VerbAUX.haben,
            presens_3st="macht",
            prateritum="machte",
            partizip_ii="hat gemacht",
            reaktion="",
            note=None,
        ),
        Verb(
            word="gehen",
            translate="идти",
            level="A1",
            verb_type=VerbType.unregelmassig,
            aux=VerbAUX.sein,
            presens_3st="geht",
            prateritum="ging",
            partizip_ii="ist gegangen",
            reaktion="",
            note=None,
        ),
    ]
    out = str(VerbList(verbs=verbs))
    assert "# machen" in out
    assert "# gehen" in out


def test_substantiv_list_str():
    subs = [
        Substantiv(
            gender=Gender.maskuline,
            level="A1",
            word="der Mann",
            translate="мужчина",
            genetiv="des Mannes",
            plural="die Männer",
            example=["der Mann kommt"],
            note="",
        )
    ]
    out = str(SubstantivList(substantiven=subs))
    assert "der Mann" in out


def test_adjektiv_list_str():
    adjs = [
        Adjektiv(word="klein", translate="маленький", examples=["ein kleines Haus"])
    ]
    out = str(AdjektivList(adjektivs=adjs))
    assert "klein - маленький" in out


def test_adverb_list_str():
    advs = [Adverb(word="schnell", translate="быстро", examples=["er rennt schnell"])]
    out = str(AdverbList(adverbs=advs))
    assert "schnell - быстро" in out
