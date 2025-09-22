import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def main():
    print("=== 智谱平台模型使用示例 ===")
    
    # 初始化智谱平台的LLM实例
    # 支持的zhipu模型: ['glm-4', 'glm-4-plus', 'glm-4-air', 'glm-4-airx', 'glm-4-long', 'glm-4-flash', 'glm-4v']
    llm = LLMManager(provider='zhipu', model='glm-4')
    
    # 显示当前使用的提供商和模型
    print(f"当前提供商: {llm.provider}")
    print(f"当前模型: {llm.model}")
    print(f"API Base URL: {llm.client.base_url}")
    
    # 演示聊天完成调用
    print("\n=== 聊天完成调用 ===")
    messages = [
        {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
        {"role": "user", "content": "请介绍一下智谱清言的GLM模型系列的特点和优势。"}
    ]
    
    print("发送消息:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    
    try:
        response = llm.chat_completion(messages)
        print("\n收到响应:")
        print(f"  {response.choices[0].message.content}")
    except Exception as e:
        print(f"\n调用失败: {e}")
        print("请确保:")
        print("  1. 已正确配置zhipu的API密钥")
        print("  2. 网络连接正常")
    
    # 演示如何切换到其他模型
    print("\n=== 切换模型示例 ===")
    print("要切换到zhipu的其他模型，可以使用:")
    print("  llm.update_model('glm-4-plus')")
    
    llm.update_model('glm-4-plus')
    print(f"\n切换后模型: {llm.model}")
    
    print("\n支持的所有zhipu模型:")
    zhipu_models = llm.get_available_models('zhipu')
    for model in zhipu_models:
        print(f"  - {model}")

if __name__ == "__main__":
    main()