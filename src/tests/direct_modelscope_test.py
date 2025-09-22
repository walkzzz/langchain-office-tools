import requests
import json

# ModelScope API密钥
api_key = "ms-ef353a1a-27c4-4dcc-9ecc-6e65741ac39f"

# 请求头
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 请求数据
data = {
    "model": "qwen2.5-coder-32b-instruct",
    "messages": [
        {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
        {"role": "user", "content": "请简单介绍一下你自己。"}
    ]
}

# ModelScope API端点
url = "https://api-inference.modelscope.cn/v1/chat/completions"

# 发送请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")