"""
markitdown库的MCP服务器配置
提供文档转换为Markdown格式的功能
"""

import os
from pathlib import Path
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown

# 初始化MCP服务器
mcp = FastMCP("MarkItDownTools")


@mcp.tool()
def convert_to_markdown(file_path: str, output_dir: str = "./") -> Dict[str, Any]:
    """
    将文档转换为Markdown格式
    
    Args:
        file_path: 输入文件路径
        output_dir: 输出目录
        
    Returns:
        转换结果
    """
    try:
        if not os.path.exists(file_path):
            return {
                "success": False,
                "message": f"文件不存在: {file_path}"
            }
            
        # 确保输出目录存在
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # 初始化MarkItDown转换器
        md = MarkItDown()
        
        # 执行转换
        result = md.convert(file_path)
        
        # 生成输出文件路径
        input_filename = Path(file_path).stem
        output_file_path = os.path.join(output_dir, f"{input_filename}.md")
        
        # 保存转换结果
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(result.text_content)
            
        return {
            "success": True,
            "message": f"文件已转换为Markdown: {output_file_path}",
            "output_path": output_file_path,
            "text_content": result.text_content[:500] + "..." if len(result.text_content) > 500 else result.text_content
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"转换文件为Markdown失败: {str(e)}"
        }


@mcp.tool()
def convert_multiple_to_markdown(file_paths: list, output_dir: str = "./") -> Dict[str, Any]:
    """
    批量将文档转换为Markdown格式
    
    Args:
        file_paths: 输入文件路径列表
        output_dir: 输出目录
        
    Returns:
        转换结果
    """
    try:
        # 确保输出目录存在
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # 初始化MarkItDown转换器
        md = MarkItDown()
        
        results = []
        failed_conversions = []
        
        for file_path in file_paths:
            if not os.path.exists(file_path):
                failed_conversions.append({
                    "file": file_path,
                    "error": "文件不存在"
                })
                continue
                
            try:
                # 执行转换
                result = md.convert(file_path)
                
                # 生成输出文件路径
                input_filename = Path(file_path).stem
                output_file_path = os.path.join(output_dir, f"{input_filename}.md")
                
                # 保存转换结果
                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                    
                results.append({
                    "input_file": file_path,
                    "output_file": output_file_path,
                    "status": "success"
                })
            except Exception as e:
                failed_conversions.append({
                    "file": file_path,
                    "error": str(e)
                })
                
        return {
            "success": True,
            "message": f"批量转换完成。成功: {len(results)}, 失败: {len(failed_conversions)}",
            "successful_conversions": results,
            "failed_conversions": failed_conversions
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"批量转换文件为Markdown失败: {str(e)}"
        }


@mcp.tool()
def get_supported_file_types() -> Dict[str, Any]:
    """
    获取支持的文件类型列表
    
    Returns:
        支持的文件类型列表
    """
    try:
        # 初始化MarkItDown转换器
        md = MarkItDown()
        
        # 获取支持的文件类型
        supported_types = md.supported_file_types
        
        return {
            "success": True,
            "supported_types": supported_types
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"获取支持的文件类型失败: {str(e)}"
        }


if __name__ == "__main__":
    import uvicorn
    print("启动MarkItDown工具服务器...")
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8004)