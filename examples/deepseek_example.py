#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek模型使用示例
展示如何使用DeepSeek模型进行对话
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager


def main():
    """主函数"""
    print("=== DeepSeek模型使用示例 ===")
    
    # 初始化LLM管理器，使用DeepSeek提供商
    llm = LLMManager(provider="deepseek", model="deepseek-chat")
    
    # 测试消息
    messages = [
        {"role": "system", "content": "你是一个 helpful assistant."},
        {"role": "user", "content": "请介绍一下DeepSeek模型的特点和优势"}
    ]
    
    try:
        # 调用模型
        print(f"正在使用模型: {llm.provider}/{llm.model}")
        response = llm.chat_completion(messages)
        
        # 输出结果
        print("\n模型响应:")
        print(response.choices[0].message.content)
        
        # 模型切换示例
        print("\n=== 切换模型示例 ===")
        print("要切换到deepseek的其他模型，可以使用:")
        print("  llm.update_model('deepseek-coder')")
        
        llm.update_model("deepseek-coder")
        print(f"\n切换后模型: {llm.model}")
        
        print("\n支持的所有deepseek模型:")
        models = llm.get_available_models("deepseek")
        for model in models:
            print(f"  - {model}")
            
    except Exception as e:
        print(f"调用模型时出错: {e}")


if __name__ == "__main__":
    main()