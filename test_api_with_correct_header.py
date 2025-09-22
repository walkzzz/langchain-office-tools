import json
import urllib.request
import urllib.error

def test_api_with_correct_header():
    """使用正确的头部名称测试API"""
    # 使用从服务器日志中获取的session ID
    session_id = "e1e4f751859d4b64ad24d64a3e4e20f7"
    
    try:
        # 构造JSON-RPC请求
        request_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
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
                "Mcp-Session-Id": session_id  # 使用正确的头部名称
            }
        )
        
        # 发送请求并获取响应
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print("Response status:", response.status)
            print("Response headers:", dict(response.headers))
            print("Response body:", response_data)
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print("Response headers:", dict(e.headers))
        try:
            error_body = e.read().decode('utf-8')
            print("Error body:", error_body)
        except:
            print("Could not read error body")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    test_api_with_correct_header()