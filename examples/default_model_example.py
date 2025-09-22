import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def main():
    print("=== 默认模型配置示例 ===")
    
    # 创建LLM管理器实例，不指定提供商和模型，使用配置文件中的默认值
    llm = LLMManager()
    
    # 显示当前提供商和模型
    print(f"当前默认提供商: {llm.provider}")
    print(f"当前默认模型: {llm.model}")
    
    # 演示聊天完成调用
    print("\n=== 聊天完成调用示例 ===")
    messages = [
        {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
        {"role": "user", "content": "请介绍一下月之暗面的moonshot模型的特点和优势。"}
    ]
    
    print("发送消息:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    
    try:
        response = llm.chat_completion(messages)
        print("\n模型回复:")
        print(f"  {response.choices[0].message.content}")
    except Exception as e:
        print(f"\n调用失败: {e}")
        print("请确保:")
        print("  1. 已正确配置moonshot的API密钥")
        print("  2. 网络连接正常")
    
    # 演示如何切换到其他提供商和模型
    print("\n=== 切换到其他提供商和模型 ===")
    print("要切换到特定提供商和模型，可以使用:")
    print("  llm = LLMManager(provider='提供商名称', model='模型名称')")
    
    print("\n支持的所有提供商:")
    for provider in llm.get_available_providers():
        print(f"  - {provider}")
        
    print("\n支持的所有模型 (以moonshot为例):")
    moonshot_models = llm.get_available_models('moonshot')
    for model in moonshot_models:
        print(f"  - {model}")

if __name__ == "__main__":
    main()