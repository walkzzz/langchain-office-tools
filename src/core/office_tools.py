"""
日常办公软件操作API模块
提供对Word、Excel、PPT等办公软件的操作接口，并转换为MCP工具供大模型调用
"""

import os
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional
from mcp.server.fastmcp import FastMCP

# 初始化MCP服务器
mcp = FastMCP("OfficeTools")


@mcp.prompt(name="office_assistant")
def office_assistant_prompt():
    """办公工具助手提示词模板"""
    pass


@mcp.tool()
def create_word_document(content: str, filename: str, save_path: str = "./") -> Dict[str, Any]:
    """
    创建Word文档
    
    Args:
        content: 文档内容
        filename: 文件名（不含扩展名）
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.docx")
        
        # 这里应该调用实际的Word操作库（如python-docx）
        # 为简化示例，我们只是创建一个包含内容的JSON文件
        doc_data = {
            "content": content,
            "created_at": "2025-04-05",
            "format": "docx"
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(doc_data, f, ensure_ascii=False, indent=2)
            
        return {
            "success": True,
            "message": f"Word文档已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建Word文档失败: {str(e)}"
        }


@mcp.tool()
def create_excel_spreadsheet(data: List[List[Any]], filename: str, save_path: str = "./") -> Dict[str, Any]:
    """
    创建Excel电子表格
    
    Args:
        data: 表格数据（二维列表）
        filename: 文件名（不含扩展名）
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.xlsx")
        
        # 这里应该调用实际的Excel操作库（如openpyxl）
        # 为简化示例，我们只是创建一个包含数据的JSON文件
        spreadsheet_data = {
            "data": data,
            "created_at": "2025-04-05",
            "format": "xlsx"
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(spreadsheet_data, f, ensure_ascii=False, indent=2)
            
        return {
            "success": True,
            "message": f"Excel电子表格已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建Excel电子表格失败: {str(e)}"
        }


@mcp.tool()
def create_powerpoint_presentation(slides: List[Dict[str, Any]], filename: str, save_path: str = "./") -> Dict[str, Any]:
    """
    创建PowerPoint演示文稿
    
    Args:
        slides: 幻灯片数据列表，每个元素包含"title"和"content"键
        filename: 文件名（不含扩展名）
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.pptx")
        
        # 这里应该调用实际的PPT操作库（如python-pptx）
        # 为简化示例，我们只是创建一个包含幻灯片数据的JSON文件
        presentation_data = {
            "slides": slides,
            "created_at": "2025-04-05",
            "format": "pptx"
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(presentation_data, f, ensure_ascii=False, indent=2)
            
        return {
            "success": True,
            "message": f"PowerPoint演示文稿已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建PowerPoint演示文稿失败: {str(e)}"
        }


@mcp.tool()
def list_files_in_directory(directory: str = "./") -> Dict[str, Any]:
    """
    列出目录中的文件
    
    Args:
        directory: 目录路径
        
    Returns:
        文件列表
    """
    try:
        path = Path(directory)
        if not path.exists():
            return {
                "success": False,
                "message": f"目录不存在: {directory}"
            }
            
        files = []
        for item in path.iterdir():
            files.append({
                "name": item.name,
                "is_file": item.is_file(),
                "size": item.stat().st_size if item.is_file() else None,
                "modified": item.stat().st_mtime
            })
            
        return {
            "success": True,
            "files": files,
            "count": len(files)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"列出目录文件失败: {str(e)}"
        }


@mcp.tool()
def read_file_content(file_path: str) -> Dict[str, Any]:
    """
    读取文件内容
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件内容
    """
    try:
        if not os.path.exists(file_path):
            return {
                "success": False,
                "message": f"文件不存在: {file_path}"
            }
            
        # 获取文件扩展名
        _, ext = os.path.splitext(file_path)
        
        # 根据文件类型读取内容
        if ext.lower() in ['.txt', '.md', '.py', '.json']:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # 对于二进制文件，返回基本信息
            stat = os.stat(file_path)
            content = f"二进制文件 (大小: {stat.st_size} 字节)"
            
        return {
            "success": True,
            "content": content,
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"读取文件内容失败: {str(e)}"
        }


@mcp.tool()
def move_file(source_path: str, destination_path: str) -> Dict[str, Any]:
    """
    移动文件
    
    Args:
        source_path: 源文件路径
        destination_path: 目标文件路径
        
    Returns:
        操作结果
    """
    try:
        # 确保目标目录存在
        dest_dir = os.path.dirname(destination_path)
        if dest_dir:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)
            
        # 移动文件
        os.rename(source_path, destination_path)
        
        return {
            "success": True,
            "message": f"文件已移动: {source_path} -> {destination_path}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"移动文件失败: {str(e)}"
        }


@mcp.tool()
def delete_file(file_path: str) -> Dict[str, Any]:
    """
    删除文件
    
    Args:
        file_path: 文件路径
        
    Returns:
        操作结果
    """
    try:
        if not os.path.exists(file_path):
            return {
                "success": False,
                "message": f"文件不存在: {file_path}"
            }
            
        os.remove(file_path)
        
        return {
            "success": True,
            "message": f"文件已删除: {file_path}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"删除文件失败: {str(e)}"
        }


@mcp.tool()
def compress_files(file_paths: List[str], zip_path: str) -> Dict[str, Any]:
    """
    压缩文件
    
    Args:
        file_paths: 要压缩的文件路径列表
        zip_path: 压缩文件保存路径
        
    Returns:
        操作结果
    """
    try:
        import zipfile
        
        # 确保保存目录存在
        Path(os.path.dirname(zip_path)).mkdir(parents=True, exist_ok=True)
        
        # 创建压缩文件
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    # 添加文件到压缩包
                    zipf.write(file_path, os.path.basename(file_path))
                    
        return {
            "success": True,
            "message": f"文件已压缩: {zip_path}",
            "zip_path": zip_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"压缩文件失败: {str(e)}"
        }


@mcp.tool()
def extract_archive(archive_path: str, extract_to: str = "./") -> Dict[str, Any]:
    """
    解压缩文件
    
    Args:
        archive_path: 压缩文件路径
        extract_to: 解压目录
        
    Returns:
        操作结果
    """
    try:
        import zipfile
        
        if not os.path.exists(archive_path):
            return {
                "success": False,
                "message": f"压缩文件不存在: {archive_path}"
            }
            
        # 确保解压目录存在
        Path(extract_to).mkdir(parents=True, exist_ok=True)
        
        # 解压缩
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(extract_to)
            
        return {
            "success": True,
            "message": f"文件已解压到: {extract_to}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"解压缩文件失败: {str(e)}"
        }


@mcp.tool()
def create_task_list(tasks: List[Dict[str, Any]], filename: str, save_path: str = "./") -> Dict[str, Any]:
    """
    创建日常任务列表
    
    Args:
        tasks: 任务列表，每个任务包含"title"(标题), "description"(描述), "priority"(优先级), "due_date"(截止日期)等字段
        filename: 文件名（不含扩展名）
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.json")
        
        # 准备任务列表数据
        task_list_data = {
            "tasks": tasks,
            "created_at": "2025-04-05",
            "total_tasks": len(tasks),
            "pending_tasks": len([task for task in tasks if task.get("status", "pending") == "pending"])
        }
        
        # 保存到JSON文件
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(task_list_data, f, ensure_ascii=False, indent=2)
            
        return {
            "success": True,
            "message": f"任务列表已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建任务列表失败: {str(e)}"
        }


@mcp.tool()
def add_task_to_list(task_list_path: str, new_task: Dict[str, Any]) -> Dict[str, Any]:
    """
    向现有任务列表添加新任务
    
    Args:
        task_list_path: 任务列表文件路径
        new_task: 新任务信息，包含"title", "description", "priority", "due_date"等字段
        
    Returns:
        操作结果
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(task_list_path):
            return {
                "success": False,
                "message": f"任务列表文件不存在: {task_list_path}"
            }
            
        # 读取现有任务列表
        with open(task_list_path, "r", encoding="utf-8") as f:
            task_list_data = json.load(f)
            
        # 添加新任务
        task_list_data["tasks"].append(new_task)
        task_list_data["total_tasks"] = len(task_list_data["tasks"])
        task_list_data["pending_tasks"] = len([task for task in task_list_data["tasks"] if task.get("status", "pending") == "pending"])
        
        # 更新文件
        with open(task_list_path, "w", encoding="utf-8") as f:
            json.dump(task_list_data, f, ensure_ascii=False, indent=2)
            
        return {
            "success": True,
            "message": f"新任务已添加到: {task_list_path}",
            "total_tasks": task_list_data["total_tasks"]
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"添加任务失败: {str(e)}"
        }


@mcp.tool()
def get_task_list_summary(task_list_path: str) -> Dict[str, Any]:
    """
    获取任务列表摘要信息
    
    Args:
        task_list_path: 任务列表文件路径
        
    Returns:
        任务列表摘要
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(task_list_path):
            return {
                "success": False,
                "message": f"任务列表文件不存在: {task_list_path}"
            }
            
        # 读取任务列表
        with open(task_list_path, "r", encoding="utf-8") as f:
            task_list_data = json.load(f)
            
        # 统计信息
        tasks = task_list_data.get("tasks", [])
        total_tasks = len(tasks)
        
        # 按优先级统计
        priority_counts = {}
        for task in tasks:
            priority = task.get("priority", "medium")
            priority_counts[priority] = priority_counts.get(priority, 0) + 1
            
        # 按状态统计
        status_counts = {}
        for task in tasks:
            status = task.get("status", "pending")
            status_counts[status] = status_counts.get(status, 0) + 1
            
        return {
            "success": True,
            "summary": {
                "total_tasks": total_tasks,
                "pending_tasks": status_counts.get("pending", 0),
                "completed_tasks": status_counts.get("completed", 0),
                "priority_distribution": priority_counts,
                "created_at": task_list_data.get("created_at")
            }
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"获取任务列表摘要失败: {str(e)}"
        }


# 资源定义
@mcp.resource("file://documents")
def documents() -> List[str]:
    """列出文档目录中的文件"""
    docs_dir = Path.home() / "Documents"
    if docs_dir.exists():
        return [str(f) for f in docs_dir.iterdir() if f.is_file()]
    return []


@mcp.resource("file://desktop")
def desktop() -> List[str]:
    """列出桌面目录中的文件"""
    desktop_dir = Path.home() / "Desktop"
    if desktop_dir.exists():
        return [str(f) for f in desktop_dir.iterdir() if f.is_file()]
    return []


if __name__ == "__main__":
    # 测试代码
    print("Office Tools API 模块")
    print("提供日常办公软件操作接口")