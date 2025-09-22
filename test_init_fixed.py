import requests
import json

# 服务器地址
BASE_URL = "http://localhost:8000"

# 初始化请求
def initialize_session():
    print("Initializing session...")
    
    # 正确的initialize参数格式
    init_data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    
    response = requests.post(f"{BASE_URL}/mcp", json=init_data, headers=headers, stream=True)
    
    print(f"Initialization response status: {response.status_code}")
    print(f"Initialization response headers: {dict(response.headers)}")
    
    # 读取响应内容
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(f"Initialization response body: {decoded_line}")
            if decoded_line.startswith("data: "):
                json_data = json.loads(decoded_line[6:])
                if "result" in json_data and "sessionId" in json_data["result"]:
                    return json_data["result"]["sessionId"]
    
    # 如果没有在流中找到sessionId，尝试从响应头获取
    session_id = response.headers.get("mcp-session-id")
    print(f"Session ID from headers: {session_id}")
    return session_id

# 列出工具
def list_tools(session_id):
    print(f"\nUsing session ID: {session_id}")
    print("Listing tools...")
    
    tools_data = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Mcp-Session-Id": session_id
    }
    
    response = requests.post(f"{BASE_URL}/mcp", json=tools_data, headers=headers, stream=True)
    
    print(f"List tools response status: {response.status_code}")
    print(f"List tools response headers: {dict(response.headers)}")
    
    # 读取响应内容
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(f"List tools response body: {decoded_line}")

if __name__ == "__main__":
    session_id = initialize_session()
    if session_id:
        list_tools(session_id)