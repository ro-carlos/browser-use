import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    agent = Agent(
        task="Open this form document and answer all of the questions, writing them on the form itself. Link: https://docs.google.com/forms/d/e/1FAIpQLSevIWqoeP_Z_GCKMeBr9v_OcOHvua-pFOcHchWUhfqoFLm6dA/viewform?usp=dialog",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
