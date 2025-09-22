import requests
import os

# 获取API密钥
api_key = os.getenv("MODELSCOPE_API_KEY", "ms-ef353a1a-27c4-4dcc-9ecc-6e65741ac39f")

# 设置请求头
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
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")