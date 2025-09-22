import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def main():
    print("=== Ollama 本地模型示例 ===")
    
    # 创建LLM管理器实例，指定使用Ollama
    llm = LLMManager(provider='ollama')
    
    # 显示当前提供商和模型
    print(f"当前提供商: {llm.provider}")
    print(f"当前模型: {llm.model}")
    
    # 显示Ollama支持的模型
    print("\nOllama支持的模型:")
    ollama_models = llm.get_available_models('ollama')
    for model in ollama_models:
        print(f"  - {model}")
    
    # 切换到特定模型
    print("\n=== 切换模型示例 ===")
    if ollama_models:
        # 切换到第一个可用的Ollama模型
        new_model = ollama_models[0]
        llm.update_model(new_model)
        print(f"已切换到模型: {llm.model}")
    
    # 演示聊天完成调用
    print("\n=== 聊天完成调用示例 ===")
    messages = [
        {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
        {"role": "user", "content": "你好，介绍一下你自己。"}
    ]
    
    print("发送消息:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    
    try:
        response = llm.chat_completion(messages)
        print("\n模型回复:")
        print(f"  {response}")
    except Exception as e:
        print(f"\n调用失败: {e}")
        print("请确保:")
        print("  1. Ollama 服务正在运行")
        print("  2. 指定的模型已下载")
        print("  3. Ollama API 端点正确 (默认为 http://localhost:11434/v1)")
    
    # 演示如何切换到其他Ollama模型
    print("\n=== 切换到其他Ollama模型 ===")
    for model in ollama_models:
        print(f"  - {model}")
    
    print("\n要切换到特定模型，可以使用:")
    print("  llm.update_model('模型名称')")
    
    print("\n=== 注意事项 ===")
    print("1. 使用Ollama时通常不需要API密钥")
    print("2. 确保Ollama服务正在运行 (ollama serve)")
    print("3. 确保所需模型已下载 (ollama pull 模型名称)")
    print("4. 默认API端点为 http://localhost:11434/v1")

if __name__ == "__main__":
    main()