import requests
import json

# ModelScope API密钥
api_key = "ms-ef353a1a-27c4-4dcc-9ecc-6e65741ac39f"

# 请求头
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ModelScope API端点
url = "https://api-inference.modelscope.cn/v1/models"

# 发送请求
try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        models = response.json()
        print("Available models:")
        for model in models.get('data', []):
            print(f"  - {model}")
    else:
        print(f"Error Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")