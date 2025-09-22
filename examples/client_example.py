"""
Langchain Office Tools 客户端示例

展示如何使用日常办公软件操作API
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager
from src.core.office_tools import (
    create_word_document,
    create_excel_spreadsheet,
    create_powerpoint_presentation,
    list_files_in_directory,
    read_file_content,
    move_file,
    delete_file,
    compress_files,
    extract_archive
)


def example_word_document():
    """创建Word文档示例"""
    print("=== 创建Word文档示例 ===")
    result = create_word_document(
        content="这是一个示例文档内容。\n包含多行文本。",
        filename="example_document",
        save_path="./output"
    )
    print(f"结果: {result}\n")


def example_excel_spreadsheet():
    """创建Excel电子表格示例"""
    print("=== 创建Excel电子表格示例 ===")
    data = [
        ["姓名", "年龄", "城市"],
        ["张三", 25, "北京"],
        ["李四", 30, "上海"],
        ["王五", 28, "广州"]
    ]
    result = create_excel_spreadsheet(
        data=data,
        filename="example_spreadsheet",
        save_path="./output"
    )
    print(f"结果: {result}\n")


def example_powerpoint_presentation():
    """创建PowerPoint演示文稿示例"""
    print("=== 创建PowerPoint演示文稿示例 ===")
    slides = [
        {"title": "演示文稿标题", "content": "这是第一页的内容"},
        {"title": "第二页", "content": "这是第二页的内容\n包含多行文本"},
        {"title": "总结", "content": "这是最后一页的内容"}
    ]
    result = create_powerpoint_presentation(
        slides=slides,
        filename="example_presentation",
        save_path="./output"
    )
    print(f"结果: {result}\n")


def example_file_operations():
    """文件操作示例"""
    print("=== 文件操作示例 ===")
    
    # 列出当前目录的文件
    result = list_files_in_directory("./output")
    print(f"目录内容: {result}")
    
    # 读取文件内容
    if result["success"] and result["count"] > 0:
        # 假设第一个文件是JSON文件
        files = result["files"]
        json_files = [f for f in files if f["is_file"] and f["name"].endswith(".json")]
        if json_files:
            file_path = f"./output/{json_files[0]['name']}"
            content_result = read_file_content(file_path)
            print(f"文件内容: {content_result}")


def main():
    """主函数"""
    print("Langchain Office Tools 客户端示例")
    print("================================")
    
    # 创建输出目录
    import os
    os.makedirs("./output", exist_ok=True)
    
    # 运行各个示例
    example_word_document()
    example_excel_spreadsheet()
    example_powerpoint_presentation()
    example_file_operations()
    
    print("所有示例运行完成！")


if __name__ == "__main__":
    main()