import json
import asyncio
from mcp.client.streamable_http import streamablehttp_client

async def test_api_with_session():
    """使用session ID测试API"""
    try:
        # 使用streamablehttp_client获取session ID
        async with streamablehttp_client("http://localhost:8001/mcp") as (read, write, get_session_id):
            # 获取session ID
            session_id = get_session_id()
            print(f"Session ID: {session_id}")
            
            # 构造JSON-RPC请求
            request_data = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/list"
            }
            
            # 发送请求
            import httpx
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:8001/mcp",
                    json=request_data,
                    headers={
                        "Content-Type": "application/json",
                        "Accept": "application/json, text/event-stream",
                        "X-Session-ID": session_id  # 添加session ID到请求头
                    }
                )
                
                print("Response status:", response.status_code)
                print("Response headers:", dict(response.headers))
                print("Response body:", response.text)
                
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(test_api_with_session())