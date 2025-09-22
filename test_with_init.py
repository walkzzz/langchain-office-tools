import json
import urllib.request
import urllib.error
import urllib.parse

def initialize_session():
    """初始化会话并返回会话ID"""
    try:
        # 发送初始化请求到/mcp端点
        request_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "capabilities": {
                    "tools": {}
                }
            }
        }
        
        request_json = json.dumps(request_data).encode('utf-8')
        
        # 创建请求对象
        req = urllib.request.Request(
            "http://localhost:8001/mcp",
            data=request_json,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream"
            }
        )
        
        # 发送请求并获取响应
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print("Initialization response status:", response.status)
            print("Initialization response headers:", dict(response.headers))
            print("Initialization response body:", response_data)
            
            # 从响应头中获取会话ID
            session_id = response.headers.get('mcp-session-id')
            print("Session ID from headers:", session_id)
            return session_id
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error during initialization: {e.code} - {e.reason}")
        print("Response headers:", dict(e.headers))
        try:
            error_body = e.read().decode('utf-8')
            print("Error body:", error_body)
        except:
            print("Could not read error body")
        return None
    except Exception as e:
        print(f"Error during initialization: {type(e).__name__}: {e}")
        return None

def list_tools(session_id):
    """使用会话ID列出工具"""
    if not session_id:
        print("No session ID provided")
        return
        
    try:
        # 构造JSON-RPC请求
        request_data = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
        
        # 发送请求
        request_json = json.dumps(request_data).encode('utf-8')
        
        # 创建请求对象
        req = urllib.request.Request(
            "http://localhost:8001/mcp",
            data=request_json,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "Mcp-Session-Id": session_id
            }
        )
        
        # 发送请求并获取响应
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print("\nList tools response status:", response.status)
            print("List tools response headers:", dict(response.headers))
            print("List tools response body:", response_data)
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error during tools/list: {e.code} - {e.reason}")
        print("Response headers:", dict(e.headers))
        try:
            error_body = e.read().decode('utf-8')
            print("Error body:", error_body)
        except:
            print("Could not read error body")
    except Exception as e:
        print(f"Error during tools/list: {type(e).__name__}: {e}")

def main():
    print("Initializing session...")
    session_id = initialize_session()
    
    if session_id:
        print(f"\nUsing session ID: {session_id}")
        print("Listing tools...")
        list_tools(session_id)
    else:
        print("Failed to initialize session")

if __name__ == "__main__":
    main()