import urllib.request
import json

# 准备JSON-RPC请求数据
data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}

# 将数据转换为JSON并编码
json_data = json.dumps(data).encode('utf-8')

# 创建请求对象
req = urllib.request.Request('http://localhost:8001/mcp', data=json_data)
req.add_header('Content-Type', 'application/json')
req.add_header('Accept', 'application/json, text/event-stream')

try:
    # 发送请求
    response = urllib.request.urlopen(req)
    print('Status code:', response.getcode())
    print('Response headers:', dict(response.headers))
    print('Response:', response.read().decode('utf-8'))
except Exception as e:
    print('Error:', e)
    print('Error type:', type(e).__name__)
    # 如果可能，打印错误的响应内容
    if hasattr(e, 'read'):
        print('Error response:', e.read().decode('utf-8'))