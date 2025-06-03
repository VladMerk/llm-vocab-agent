from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

from llm_vocab_agent.llms import llm
from llm_vocab_agent.models import DeutschWord
from llm_vocab_agent.tools import get_adjektiv, get_adverb, get_substantiv, get_verbs

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "Вы опытный преподаватель немецкого языка. "
                "Вам нужно по запросу вернуть слова немецкого языка. "
                "Используйте приложенные инструменты."
            ),
        ),
        ("user", "{input}"),
    ]
)

agent = create_react_agent(
    model=llm, tools=[get_adjektiv, get_verbs, get_substantiv, get_adverb], response_format=DeutschWord
)
agent_chain = prompt | agent


if __name__ == "__main__":
    import asyncio

    async def main():

        user_query = """Дайте 2 возратных глагола немецкого языка,
        3 существительных, 2 прилагательных и 3 наречия"""

        result = await agent_chain.ainvoke({"input": user_query})
        output = DeutschWord.model_validate(result["structured_response"])
        print("=" * 20, "Глаголы", "=" * 20)
        print(output.verbs)
        print("=" * 20, "Существительные", "=" * 20)
        print(output.substantivs)
        print("=" * 20, "Прилагательные", "=" * 20)
        print(output.adjektivs)
        print("=" * 20, "Наречия", "=" * 20)
        print(output.adverbs)

    asyncio.run(main())
