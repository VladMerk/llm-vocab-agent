from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser

from llm_vocab_agent.llms import llm
from llm_vocab_agent.models.substantiv import SubstantivList
from llm_vocab_agent.models.verb import VerbList


@tool
async def get_verbs(n: int):
    """
    Возвращает n глаголов немецкого языка
    """
    parser = PydanticOutputParser(pydantic_object=VerbList)

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} глаголов немецкого языка.
        Если глаголы имеют управление предлогом, тогда его нужно указать и объяснить что значит.

        Верни список глаголов строго в формате JSON, где каждый элемент соответствует следующей структуре:
        {format_instructions}

        Примеры:
        sich freuen - (über + Akk) - радоваться тому, что уже есть
        sich freuen - (auf + Akk) - радоваться чему-то в будущем
        arbeiten
        strahlen
        """
    )

    chain = prompt | llm.with_structured_output(VerbList) | StrOutputParser()

    result = chain.invoke(input={"n": n, "format_instructions": parser.get_format_instructions()})

    return str(result)


@tool
async def get_substantiv(n: int):
    """
    Возвращает n существительных немецкого языка
    """
    # parser = PydanticOutputParser(pydantic_object=SubstantivList)

    prompt = ChatPromptTemplate.from_template(
        """Вы очень опытный преподаватель немецкого языка.
        Вам необходимо вернуть {n} существительных немецкого языка.

        """
    )

    chain = prompt | llm.with_structured_output(SubstantivList) | StrOutputParser()

    result = chain.invoke(input={"n": n})

    return str(result)


if __name__ == "__main__":
    import asyncio

    async def main():
        result = await get_substantiv.ainvoke({"n": 5})

        print(result)

    asyncio.run(main())
