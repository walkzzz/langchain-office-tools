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
                
                # 获取会话ID
                session_id = get_session_id()
                print(f"会话ID: {session_id}")
                
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
                    },
                    {
                        "title": "回复客户邮件",
                        "description": "回复重要客户的技术咨询邮件",
                        "priority": "high",
                        "due_date": "2025-04-06",
                        "status": "completed"
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
                
                print(f"创建任务列表结果类型: {type(result)}")
                if hasattr(result, 'content'):
                    print(f"返回内容类型: {type(result.content)}")
                    print(f"返回内容: {result.content}")
                    
                    # 直接处理返回结果，不再使用json.loads
                    content_data = result.content
                    if isinstance(content_data, list) and len(content_data) > 0:
                        # 如果是列表，获取第一个元素
                        content_item = content_data[0]
                        # 如果是TextContent对象，获取其text属性
                        if hasattr(content_item, 'text'):
                            import json
                            try:
                                result_data = json.loads(content_item.text)
                            except:
                                result_data = {"message": str(content_item.text)}
                        else:
                            result_data = content_item if isinstance(content_item, dict) else {}
                    elif hasattr(content_data, 'text'):
                        # 如果是TextContent对象，获取其text属性
                        import json
                        try:
                            result_data = json.loads(content_data.text)
                        except:
                            result_data = {"message": str(content_data.text)}
                    elif isinstance(content_data, str):
                        # 如果是字符串，尝试解析JSON
                        import json
                        try:
                            result_data = json.loads(content_data)
                        except:
                            result_data = {"message": content_data}
                    else:
                        result_data = content_data if isinstance(content_data, dict) else {}
                    
                    # 检查是否成功创建
                    success = result_data.get("success", False) if isinstance(result_data, dict) else False
                    if success:
                        task_list_path = result_data.get("file_path")
                        print(f"任务列表创建成功，路径: {task_list_path}")
                        
                        # 测试获取任务列表摘要
                        print("\n测试获取任务列表摘要...")
                        summary_result = await session.call_tool(
                            name="get_task_list_summary",
                            arguments={
                                "task_list_path": task_list_path
                            }
                        )
                        
                        print(f"任务列表摘要结果类型: {type(summary_result)}")
                        if hasattr(summary_result, 'content'):
                            print(f"摘要内容类型: {type(summary_result.content)}")
                            content_data = summary_result.content
                            if isinstance(content_data, list) and len(content_data) > 0:
                                # 如果是列表，获取第一个元素
                                content_item = content_data[0]
                                # 如果是TextContent对象，获取其text属性
                                if hasattr(content_item, 'text'):
                                    print(f"摘要内容: {content_item.text}")
                                else:
                                    print(f"摘要内容: {content_item}")
                            elif hasattr(content_data, 'text'):
                                # 如果是TextContent对象，获取其text属性
                                print(f"摘要内容: {content_data.text}")
                            else:
                                print(f"摘要内容: {content_data}")
                        
                        # 测试添加新任务
                        print("\n测试添加新任务...")
                        new_task = {
                            "title": "安排团队建设活动",
                            "description": "组织本月的团队建设活动",
                            "priority": "low",
                            "due_date": "2025-04-15",
                            "status": "pending"
                        }
                        
                        add_result = await session.call_tool(
                            name="add_task_to_list",
                            arguments={
                                "task_list_path": task_list_path,
                                "new_task": new_task
                            }
                        )
                        
                        print(f"添加任务结果类型: {type(add_result)}")
                        if hasattr(add_result, 'content'):
                            print(f"添加任务内容类型: {type(add_result.content)}")
                            content_data = add_result.content
                            if isinstance(content_data, list) and len(content_data) > 0:
                                # 如果是列表，获取第一个元素
                                content_item = content_data[0]
                                # 如果是TextContent对象，获取其text属性
                                if hasattr(content_item, 'text'):
                                    print(f"添加任务内容: {content_item.text}")
                                else:
                                    print(f"添加任务内容: {content_item}")
                            elif hasattr(content_data, 'text'):
                                # 如果是TextContent对象，获取其text属性
                                print(f"添加任务内容: {content_data.text}")
                            else:
                                print(f"添加任务内容: {content_data}")
                    else:
                        message = "未知错误"
                        if isinstance(result_data, dict):
                            message = result_data.get('message', '未知错误')
                        elif hasattr(result_data, 'text'):
                            message = result_data.text
                        elif isinstance(result_data, str):
                            message = result_data
                        print(f"创建任务列表失败: {message}")
                else:
                    print("创建任务列表失败，没有返回有效内容")
                    
    except Exception as e:
        print(f"任务工具测试出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_task_tools())