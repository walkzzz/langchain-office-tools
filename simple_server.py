"""
使用stdio传输协议的服务器启动脚本
"""

import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 导入必要的组件
from mcp.server.fastmcp import FastMCP

# 创建主MCP服务器
mcp = FastMCP("LangchainOfficeTools")

# 动态导入office_tools模块并注册其中的工具
try:
    # 直接导入office_tools中的函数
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
    
    # 注册工具函数
    mcp.add_tool(create_word_document)
    mcp.add_tool(create_excel_spreadsheet)
    mcp.add_tool(create_powerpoint_presentation)
    mcp.add_tool(list_files_in_directory)
    mcp.add_tool(read_file_content)
    mcp.add_tool(move_file)
    mcp.add_tool(delete_file)
    mcp.add_tool(compress_files)
    mcp.add_tool(extract_archive)
    
    print("成功导入并注册office_tools模块中的工具")
    print("注册的工具数量:", len(mcp._tool_manager._tools))
        
except ImportError as e:
    print(f"警告: 无法导入office_tools模块: {e}")
except Exception as e:
    print(f"错误: 导入office_tools模块时发生异常: {e}")
    import traceback
    traceback.print_exc()

def main():
    # 启动服务器
    print("启动Langchain Office Tools服务器...")
    print("服务器名称:", mcp.name)
    # 使用stdio传输协议运行
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()