#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ModelScope模型使用示例
展示如何使用ModelScope的模型进行聊天完成调用
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager


def main():
    """主函数"""
    print("=== ModelScope模型使用示例 ===")
    
    # 初始化ModelScope模型 (Qwen/Qwen3-Coder-30B-A3B-Instruct)
    llm = LLMManager(provider='modelscope', model='Qwen/Qwen3-Coder-30B-A3B-Instruct')
    
    # 显示当前使用的提供商和模型
    print(f"当前提供商: {llm.provider}")
    print(f"当前模型: {llm.model}")
    print()
    
    # 准备聊天消息
    messages = [
        {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
        {"role": "user", "content": "请介绍一下qwen3-72b-instruct模型的特点和优势。"}
    ]
    
    print("=== 聊天完成调用 ===")
    print("发送消息:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    print()
    
    try:
        # 调用聊天完成接口
        response = llm.chat_completion(messages)
        
        # 输出响应
        print("收到响应:")
        print(response.choices[0].message.content)
        print()
        
    except Exception as e:
        print(f"调用失败: {e}")
        print("请确保:")
        print("  1. 已正确配置modelscope的API密钥")
        print("  2. 网络连接正常")
        print()
    
    # 展示如何切换到其他模型
    print("=== 切换模型示例 ===")
    print("要切换到modelscope的其他模型，可以使用:")
    print("  llm.update_model('qwen2.5-coder-32b-instruct')")
    print()
    
    # 切换模型示例
    llm.update_model("qwen2.5-coder-32b-instruct")
    print(f"切换后模型: {llm.model}")
    
    # 显示支持的所有modelscope模型
    print("\n支持的所有modelscope模型:")
    modelscope_models = llm.get_available_models("modelscope")
    for model in modelscope_models:
        print(f"  - {model}")


if __name__ == "__main__":
    main()