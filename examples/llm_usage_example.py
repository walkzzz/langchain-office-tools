#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LLM使用示例
展示如何使用LLMManager类来管理不同的大语言模型
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os
from src.core.llm import LLMManager

def main():
    # 初始化LLM管理器
    llm = LLMManager()
    
    # 测试不同模型提供商
    providers = ["openai", "qwen", "deepseek", "modelscope"]
    
    # 消息示例
    messages = [
        {"role": "system", "content": "你是一个 helpful assistant."},
        {"role": "user", "content": "请用中文简要介绍Python编程语言的特点"}
    ]
    
    for provider in providers:
        try:
            print(f"\n--- 测试 {provider} ---")
            llm.update_provider(provider)
            
            # 可以为不同提供商设置不同的模型
            if provider == "qwen":
                llm.update_model("qwen-plus")
            elif provider == "deepseek":
                llm.update_model("deepseek-chat")
            elif provider == "modelscope":
                llm.update_model("qwen2.5-coder-32b-instruct")
            
            response = llm.chat_completion(messages)
            print(f"{provider} 回复: {response.choices[0].message.content}")
            
        except Exception as e:
            print(f"{provider} 调用失败: {str(e)}")
    
    # 展示支持的提供商和模型
    print("\n--- 支持的模型提供商 ---")
    for provider in llm.get_available_providers():
        print(f"- {provider}")
    
    print("\n--- 各提供商支持的模型 ---")
    for provider in llm.get_available_providers():
        models = llm.get_available_models(provider)
        print(f"{provider}: {', '.join(models)}")
        
    # 演示API密钥配置方式
    print("\n--- API密钥配置方式 ---")
    print("1. 通过参数传递:")
    print("   llm = LLMManager(provider='openai', api_key='your-api-key')")
    
    print("\n2. 通过配置文件 (config/config.yaml):")
    print("   model_configs:")
    print("     openai:")
    print("       api_key: 'your-api-key'")
    
    print("\n3. 通过环境变量:")
    print("   export OPENAI_API_KEY='your-api-key'")

if __name__ == "__main__":
    main()