from mcp.server.fastmcp import FastMCP
import asyncio

async def main():
    mcp = FastMCP('test')
    tools = await mcp.list_tools()
    print([t.name for t in tools])

if __name__ == "__main__":
    asyncio.run(main())