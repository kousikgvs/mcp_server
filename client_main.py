import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq


async def main():
    load_dotenv()

    config = {
        "mcpServers": {
            "zoophagous-red-squirrel": {
                "type": "streamable-http",
                "url": "https://zoophagous-red-squirrel.fastmcp.app/mcp"
            }
        }
    }

    client = MCPClient.from_dict(config)

    llm = ChatGroq(
        temperature=0,
        model_name="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    )

    agent = MCPAgent(llm=llm, client=client, verbose=True, max_steps=5)

    result = await agent.run("Give me 10 random strings using the generate_random_strings tool.")
    print(f"\nResult: {result}")


if __name__ == "__main__":
    asyncio.run(main())
