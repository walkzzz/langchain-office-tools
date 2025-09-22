from src.core.llm import LLMManager

# 创建LLMManager实例
llm = LLMManager(provider='modelscope', model='qwen2.5-coder-32b-instruct')

# 打印API密钥（注意：在生产环境中不要这样做）
print(f"Provider: {llm.provider}")
print(f"Model: {llm.model}")
print(f"Base URL: {llm.client.base_url}")
print(f"API Key: {llm.client.api_key}")