import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def test_llm_manager():
    print("Testing LLMManager...")
    
    # 测试默认初始化
    print("1. Testing default initialization...")
    llm = LLMManager()
    print(f"   Provider: {llm.provider}")
    print(f"   Model: {llm.model}")
    
    # 测试指定提供商和模型初始化
    print("2. Testing specific initialization...")
    llm = LLMManager(provider="openai", model="gpt-4o-mini")
    print(f"   Provider: {llm.provider}")
    print(f"   Model: {llm.model}")
    
    # 测试获取可用提供商
    print("3. Testing get_available_providers...")
    providers = llm.get_available_providers()
    print(f"   Providers: {providers}")
    
    # 测试获取可用模型
    print("4. Testing get_available_models...")
    openai_models = llm.get_available_models("openai")
    print(f"   OpenAI models: {openai_models}")
    
    qwen_models = llm.get_available_models("qwen")
    print(f"   Qwen models: {qwen_models}")
    
    # 测试更新提供商
    print("5. Testing update_provider...")
    original_provider = llm.provider
    llm.update_provider("qwen")
    print(f"   Updated provider: {llm.provider}")
    llm.update_provider(original_provider)
    print(f"   Restored provider: {llm.provider}")
    
    # 测试更新模型
    print("6. Testing update_model...")
    original_model = llm.model
    llm.update_model("gpt-4o")
    print(f"   Updated model: {llm.model}")
    llm.update_model(original_model)
    print(f"   Restored model: {llm.model}")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_llm_manager()