import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def main():
    # 创建LLM管理器实例
    llm = LLMManager()
    
    # 显示支持的模型提供商
    print("支持的模型提供商:")
    for provider in llm.get_available_providers():
        print(f"  - {provider}")
    
    # 显示各提供商支持的模型
    print("\n各提供商支持的模型:")
    for provider in llm.get_available_providers():
        models = llm.get_available_models(provider)
        print(f"  {provider}: {', '.join(models)}")
    
    # 演示如何配置API密钥
    print("\nAPI密钥配置方式:")
    print("1. 通过参数传递:")
    print("   llm = LLMManager(provider='openai', api_key='your-api-key')")
    
    print("\n2. 通过配置文件 (config/config.yaml):")
    print("   model_configs:")
    print("     openai:")
    print("       api_key: 'your-api-key'")
    
    print("\n3. 通过环境变量:")
    print("   export OPENAI_API_KEY='your-api-key'")
    
    print("\n4. 对于Ollama本地模型，通常不需要API密钥:")
    print("   llm = LLMManager(provider='ollama')")
    
    print("\n注意: 要实际调用模型API, 您需要:")
    print("  1. 获取相应模型提供商的API密钥")
    print("  2. 通过上述任一方式配置密钥")
    print("  3. 调用 llm.chat_completion(messages) 方法")

if __name__ == "__main__":
    main()