"""
zipfile库的MCP服务器配置
提供文件压缩和解压缩功能
"""

import os
import zipfile
from pathlib import Path
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP

# 初始化MCP服务器
mcp = FastMCP("ZipFileTools")


@mcp.tool()
def create_zip_archive(file_paths: List[str], zip_path: str) -> Dict[str, Any]:
    """
    创建ZIP压缩文件
    
    Args:
        file_paths: 要压缩的文件路径列表
        zip_path: 压缩文件保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存目录存在
        Path(os.path.dirname(zip_path)).mkdir(parents=True, exist_ok=True)
        
        # 创建压缩文件
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    # 添加文件到压缩包
                    arcname = os.path.basename(file_path)
                    zipf.write(file_path, arcname)
                else:
                    return {
                        "success": False,
                        "message": f"文件不存在: {file_path}"
                    }
                    
        return {
            "success": True,
            "message": f"ZIP压缩文件已创建: {zip_path}",
            "zip_path": zip_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建ZIP压缩文件失败: {str(e)}"
        }


@mcp.tool()
def extract_zip_archive(zip_path: str, extract_to: str = "./") -> Dict[str, Any]:
    """
    解压ZIP文件
    
    Args:
        zip_path: ZIP文件路径
        extract_to: 解压目录
        
    Returns:
        操作结果
    """
    try:
        if not os.path.exists(zip_path):
            return {
                "success": False,
                "message": f"ZIP文件不存在: {zip_path}"
            }
            
        # 确保解压目录存在
        Path(extract_to).mkdir(parents=True, exist_ok=True)
        
        # 解压缩
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_to)
            
        return {
            "success": True,
            "message": f"ZIP文件已解压到: {extract_to}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"解压ZIP文件失败: {str(e)}"
        }


@mcp.tool()
def list_zip_contents(zip_path: str) -> Dict[str, Any]:
    """
    列出ZIP文件内容
    
    Args:
        zip_path: ZIP文件路径
        
    Returns:
        ZIP文件内容列表
    """
    try:
        if not os.path.exists(zip_path):
            return {
                "success": False,
                "message": f"ZIP文件不存在: {zip_path}"
            }
            
        # 读取ZIP文件内容
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            file_list = zipf.namelist()
            file_info = []
            
            for file_name in file_list:
                info = zipf.getinfo(file_name)
                file_info.append({
                    "name": file_name,
                    "size": info.file_size,
                    "compressed_size": info.compress_size,
                    "date": f"{info.date_time[0]}-{info.date_time[1]:02d}-{info.date_time[2]:02d} "
                            f"{info.date_time[3]:02d}:{info.date_time[4]:02d}:{info.date_time[5]:02d}"
                })
                
        return {
            "success": True,
            "files": file_info,
            "count": len(file_info)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"列出ZIP文件内容失败: {str(e)}"
        }


@mcp.tool()
def add_files_to_zip(zip_path: str, file_paths: List[str]) -> Dict[str, Any]:
    """
    向现有ZIP文件添加文件
    
    Args:
        zip_path: ZIP文件路径
        file_paths: 要添加的文件路径列表
        
    Returns:
        操作结果
    """
    try:
        # 如果ZIP文件不存在，则创建新文件
        if not os.path.exists(zip_path):
            mode = 'w'
        else:
            mode = 'a'
            
        # 添加文件到ZIP
        with zipfile.ZipFile(zip_path, mode, zipfile.ZIP_DEFLATED) as zipf:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    # 添加文件到压缩包
                    arcname = os.path.basename(file_path)
                    zipf.write(file_path, arcname)
                else:
                    return {
                        "success": False,
                        "message": f"文件不存在: {file_path}"
                    }
                    
        return {
            "success": True,
            "message": f"文件已添加到ZIP文件: {zip_path}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"添加文件到ZIP失败: {str(e)}"
        }


@mcp.tool()
def extract_specific_files(zip_path: str, file_names: List[str], extract_to: str = "./") -> Dict[str, Any]:
    """
    从ZIP文件中提取特定文件
    
    Args:
        zip_path: ZIP文件路径
        file_names: 要提取的文件名列表
        extract_to: 解压目录
        
    Returns:
        操作结果
    """
    try:
        if not os.path.exists(zip_path):
            return {
                "success": False,
                "message": f"ZIP文件不存在: {zip_path}"
            }
            
        # 确保解压目录存在
        Path(extract_to).mkdir(parents=True, exist_ok=True)
        
        # 提取特定文件
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            available_files = zipf.namelist()
            extracted_files = []
            
            for file_name in file_names:
                if file_name in available_files:
                    zipf.extract(file_name, extract_to)
                    extracted_files.append(file_name)
                else:
                    return {
                        "success": False,
                        "message": f"文件在ZIP中不存在: {file_name}"
                    }
                    
        return {
            "success": True,
            "message": f"已从ZIP文件提取 {len(extracted_files)} 个文件到: {extract_to}",
            "extracted_files": extracted_files
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"提取特定文件失败: {str(e)}"
        }


if __name__ == "__main__":
    import uvicorn
    print("启动ZipFile工具服务器...")
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8005)