from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio

MODEL_NAME = 'gemma3:12b'
OLLAMA_HOST = '192.168.1.71:11434'
TASK_INTRUCTION_FILENAME = 'instruction.txt'


async def run(task):
    agent = Agent(
        task=task,
        llm=ChatOllama(model=MODEL_NAME, base_url=OLLAMA_HOST),
    )
    await agent.run() 

async def main():
    with open(TASK_INTRUCTION_FILENAME) as f:
        await run(f.read())

asyncio.run(main())