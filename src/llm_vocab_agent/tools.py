from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser

from llm_vocab_agent.llms import llm
from llm_vocab_agent.models import AdjektivList, AdverbList, SubstantivList, VerbList


@tool
async def get_verbs(n: int):
    """
    Возвращает n глаголов немецкого языка
    """

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} глаголов немецкого языка.
        Если глаголы имеют управление предлогом, тогда его нужно указать и объяснить что значит.

        Примеры:
        sich freuen - (über + Akk) - радоваться тому, что уже есть
        sich freuen - (auf + Akk) - радоваться чему-то в будущем
        arbeiten
        strahlen
        """
    )

    chain = prompt | llm.with_structured_output(VerbList) | StrOutputParser()

    result = await chain.ainvoke(input={"n": n})

    return str(result)


@tool
async def get_substantiv(n: int):
    """
    Возвращает n существительных немецкого языка
    """

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} существительных немецкого языка.
        """
    )

    chain = prompt | llm.with_structured_output(SubstantivList) | StrOutputParser()

    result = await chain.ainvoke(input={"n": n})

    return str(result)


@tool
async def get_adjektiv(n: int):
    """
    Возвращает n прилагательных немецкого языка
    """

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} прилагательных немецкого языка.
        """
    )

    chain = prompt | llm.with_structured_output(AdjektivList) | StrOutputParser()

    result = await chain.ainvoke(input={"n": n})

    return str(result)


@tool
async def get_adverb(n: int):
    """
    Возвращает n наречий немецкого языка
    """

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} наречий немецкого языка.
        """
    )

    chain = prompt | llm.with_structured_output(AdverbList) | StrOutputParser()

    result = await chain.ainvoke(input={"n": n})

    return str(result)


if __name__ == "__main__":
    import asyncio

    async def main():
        result = await get_adverb.ainvoke({"n": 3})

        print(result, end="\n\n")

    asyncio.run(main())
