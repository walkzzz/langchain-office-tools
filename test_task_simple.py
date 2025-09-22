import asyncio
import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from mcp.client.streamable_http import streamablehttp_client
    from mcp.client.session import ClientSession
    print("成功导入MCP客户端模块")
except ImportError as e:
    print(f"无法导入MCP客户端模块: {e}")
    print("请确保已安装mcp包")
    sys.exit(1)

async def test_task_tools():
    server_url = "http://localhost:8001/mcp"  # 使用服务器实际端口
    
    print(f"连接到服务器: {server_url}")
    
    try:
        async with streamablehttp_client(url=server_url) as (read, write, get_session_id):
            async with ClientSession(read, write) as session:
                print("连接成功!")
                
                # 初始化会话
                print("初始化会话...")
                result = await session.initialize()
                print("会话初始化完成")
                
                # 列出工具，查看是否包含新添加的任务管理工具
                print("获取工具列表...")
                tools_result = await session.list_tools()
                tools = tools_result.tools  # 获取工具列表
                
                # 查找任务管理相关的工具
                task_tools = [tool for tool in tools if 'task' in tool.name.lower()]
                print(f"找到 {len(task_tools)} 个任务相关工具:")
                for tool in task_tools:
                    print(f"- {tool.name}: {tool.description}")
                
                # 测试创建任务列表
                print("\n测试创建任务列表...")
                sample_tasks = [
                    {
                        "title": "完成项目报告",
                        "description": "完成季度项目进度报告",
                        "priority": "high",
                        "due_date": "2025-04-10",
                        "status": "pending"
                    },
                    {
                        "title": "准备会议材料",
                        "description": "为下周的团队会议准备演示材料",
                        "priority": "medium",
                        "due_date": "2025-04-08",
                        "status": "pending"
                    }
                ]
                
                # 调用创建任务列表工具
                result = await session.call_tool(
                    name="create_task_list",
                    arguments={
                        "tasks": sample_tasks,
                        "filename": "my_task_list",
                        "save_path": "./test_data"
                    }
                )
                
                print(f"创建任务列表结果: {result}")
                
                # 简单打印返回内容
                if hasattr(result, 'content'):
                    print(f"返回内容: {result.content}")
                    
    except Exception as e:
        print(f"任务工具测试出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_task_tools())