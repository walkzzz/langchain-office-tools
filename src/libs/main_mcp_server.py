"""
主MCP服务器文件
整合所有库的MCP工具
"""

import sys
import os

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
libs_path = os.path.join(project_root, 'src', 'libs')

# 添加项目根目录和libs目录到sys.path
sys.path.insert(0, project_root)
sys.path.insert(0, libs_path)

print(f"项目根目录: {project_root}")
print(f"Libs路径: {libs_path}")

# 导入各个库的MCP模块
try:
    import pypdf_mcp
    print("成功导入pypdf_mcp模块")
except Exception as e:
    print(f"导入pypdf_mcp模块时发生异常: {e}")
    pypdf_mcp = None

try:
    import xlsxwriter_mcp
    print("成功导入xlsxwriter_mcp模块")
except Exception as e:
    print(f"导入xlsxwriter_mcp模块时发生异常: {e}")
    xlsxwriter_mcp = None

try:
    import markitdown_mcp
    print("成功导入markitdown_mcp模块")
except Exception as e:
    print(f"导入markitdown_mcp模块时发生异常: {e}")
    markitdown_mcp = None

try:
    import zipfile_mcp
    print("成功导入zipfile_mcp模块")
except Exception as e:
    print(f"导入zipfile_mcp模块时发生异常: {e}")
    zipfile_mcp = None

# 初始化主MCP服务器
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("OfficeLibsTools")

# 注册工具
try:
    # 注册pypdf工具
    if pypdf_mcp:
        pypdf_tools = [
            pypdf_mcp.extract_pdf_text,
            pypdf_mcp.merge_pdfs,
            pypdf_mcp.split_pdf
        ]
        for tool_func in pypdf_tools:
            mcp.add_tool(tool_func)
            print(f"已注册pypdf工具: {tool_func.__name__}")

    # 注册xlsxwriter工具
    if xlsxwriter_mcp:
        xlsxwriter_tools = [
            xlsxwriter_mcp.create_excel_workbook,
            xlsxwriter_mcp.create_formatted_excel,
            xlsxwriter_mcp.add_chart_to_excel
        ]
        for tool_func in xlsxwriter_tools:
            mcp.add_tool(tool_func)
            print(f"已注册xlsxwriter工具: {tool_func.__name__}")

    # 注册markitdown工具
    if markitdown_mcp:
        markitdown_tools = [
            markitdown_mcp.convert_to_markdown,
            markitdown_mcp.convert_multiple_to_markdown,
            markitdown_mcp.get_supported_file_types
        ]
        for tool_func in markitdown_tools:
            mcp.add_tool(tool_func)
            print(f"已注册markitdown工具: {tool_func.__name__}")

    # 注册zipfile工具
    if zipfile_mcp:
        zipfile_tools = [
            zipfile_mcp.create_zip_archive,
            zipfile_mcp.extract_zip_archive,
            zipfile_mcp.list_zip_contents,
            zipfile_mcp.add_files_to_zip,
            zipfile_mcp.extract_specific_files
        ]
        for tool_func in zipfile_tools:
            mcp.add_tool(tool_func)
            print(f"已注册zipfile工具: {tool_func.__name__}")

    print("所有工具注册完成")
except Exception as e:
    print(f"注册工具时发生异常: {e}")
    raise

print("启动Office Libraries Tools服务器...")
print(f"服务器名称: {mcp.name}")
print(f"服务器地址: http://127.0.0.1:8006")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8006)