#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
提示词模板使用示例
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager

def main():
    # 初始化LLM管理器
    llm = LLMManager(provider="openai", model="gpt-4o-mini")
    
    print("=== 提示词模板功能演示 ===\n")
    
    # 1. 加载通用助手提示词模板
    print("1. 加载通用助手提示词模板:")
    try:
        general_template = llm.load_prompt_template("general_template")
        print(general_template)
    except FileNotFoundError as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")
    
    # 2. 渲染通用助手提示词模板
    print("2. 渲染通用助手提示词模板:")
    try:
        rendered_general = llm.render_prompt_template("general_template", question="什么是人工智能？")
        print(rendered_general)
    except (FileNotFoundError, ValueError) as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")
    
    # 3. 加载代码生成提示词模板
    print("3. 加载代码生成提示词模板:")
    try:
        code_template = llm.load_prompt_template("code_generation_template")
        print(code_template)
    except FileNotFoundError as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")
    
    # 4. 渲染代码生成提示词模板
    print("4. 渲染代码生成提示词模板:")
    try:
        rendered_code = llm.render_prompt_template(
            "code_generation_template", 
            requirement="编写一个Python函数，计算两个数的和"
        )
        print(rendered_code)
    except (FileNotFoundError, ValueError) as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")
    
    # 5. 加载文档总结提示词模板
    print("5. 加载文档总结提示词模板:")
    try:
        summary_template = llm.load_prompt_template("document_summary_template")
        print(summary_template)
    except FileNotFoundError as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")
    
    # 6. 渲染文档总结提示词模板
    print("6. 渲染文档总结提示词模板:")
    try:
        document_content = "人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。"
        rendered_summary = llm.render_prompt_template(
            "document_summary_template", 
            document_content=document_content
        )
        print(rendered_summary)
    except (FileNotFoundError, ValueError) as e:
        print(f"错误: {e}")
    print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()