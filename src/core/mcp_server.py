import sys
import os
import importlib.util

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_path = os.path.join(project_root, 'src', 'core')
config_path = os.path.join(project_root, 'config')

# 添加项目根目录、src目录、core目录和config目录到sys.path
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'src'))
sys.path.insert(0, core_path)
sys.path.insert(0, config_path)

print(f"项目根目录: {project_root}")
print(f"Core路径: {core_path}")
print(f"Config路径: {config_path}")
print(f"当前sys.path: {sys.path}")

try:
    # 使用importlib动态导入office_tools模块
    office_tools_path = os.path.join(core_path, 'office_tools.py')
    print(f"尝试导入: {office_tools_path}")
    
    spec = importlib.util.spec_from_file_location("office_tools", office_tools_path)
    office_tools = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(office_tools)
    print("成功导入office_tools模块")
except Exception as e:
    print(f"导入office_tools模块时发生异常: {e}")
    raise

# 初始化MCP服务器
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import Prompt
mcp = FastMCP("LangchainOfficeTools")

# 注册工具
try:
    # 获取office_tools模块中的所有工具函数
    tool_functions = [
        office_tools.create_word_document,
        office_tools.create_excel_spreadsheet,
        office_tools.create_powerpoint_presentation,
        office_tools.list_files_in_directory,
        office_tools.read_file_content,
        office_tools.move_file,
        office_tools.delete_file,
        office_tools.compress_files,
        office_tools.extract_archive,
        office_tools.create_task_list,
        office_tools.add_task_to_list,
        office_tools.get_task_list_summary
    ]
    
    # 注册所有工具
    for tool_func in tool_functions:
        mcp.add_tool(tool_func)
        print(f"已注册工具: {tool_func.__name__}")
        
    print("所有工具注册完成")
except Exception as e:
    print(f"注册工具时发生异常: {e}")
    raise

# 注册Prompt
try:
    # 创建Prompt对象
    prompt = Prompt(
        name="office_assistant",
        description="办公助手提示词模板",
        fn=office_tools.office_assistant_prompt
    )
    mcp.add_prompt(prompt)
    print("已注册Prompt: office_assistant")
except Exception as e:
    print(f"注册Prompt时发生异常: {e}")
    raise

print("启动Langchain Office Tools服务器...")
print(f"服务器名称: {mcp.name}")
print(f"服务器地址: http://127.0.0.1:8001")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8001)

    