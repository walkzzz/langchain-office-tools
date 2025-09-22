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

async def test_tools():
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
                print(f"初始化结果: {result}")
                
                # 获取会话ID
                session_id = get_session_id()
                print(f"会话ID: {session_id}")
                
                # 列出工具
                print("获取工具列表...")
                tools_result = await session.list_tools()
                tools = tools_result.tools  # 获取工具列表
                print(f"可用工具数量: {len(tools)}")
                
                # 测试调用一个简单的工具 - list_files_in_directory
                print("\n测试调用 list_files_in_directory 工具...")
                import os
                current_dir = os.getcwd()
                print(f"当前目录: {current_dir}")
                
                # 调用工具
                result = await session.call_tool(
                    name="list_files_in_directory",
                    arguments={
                        "directory": current_dir
                    }
                )
                
                print(f"工具调用结果类型: {type(result)}")
                print(f"工具调用结果: {result}")
                
                # 检查返回内容
                if hasattr(result, 'content'):
                    content = result.content
                    print(f"返回内容类型: {type(content)}")
                    if isinstance(content, list):
                        print(f"目录中的文件数量: {len(content)}")
                        print("前5个文件:")
                        for item in content[:5]:
                            print(f"  - {item}")
                    elif isinstance(content, str):
                        print(f"返回内容: {content}")
                    else:
                        print(f"返回内容: {content}")
                else:
                    print("工具调用完成，但没有返回内容")
                    
    except Exception as e:
        print(f"工具测试出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_tools())