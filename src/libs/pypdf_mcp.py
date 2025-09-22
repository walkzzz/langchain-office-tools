"""
pypdf库的MCP服务器配置
提供PDF文档处理功能
"""

import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from mcp.server.fastmcp import FastMCP
from pypdf import PdfReader, PdfWriter

# 初始化MCP服务器
mcp = FastMCP("PyPDFTools")


@mcp.tool()
def extract_pdf_text(pdf_path: str, page_numbers: Optional[List[int]] = None) -> Dict[str, Any]:
    """
    提取PDF文档文本内容
    
    Args:
        pdf_path: PDF文件路径
        page_numbers: 要提取的页面号列表（从1开始），如果为None则提取所有页面
        
    Returns:
        提取的文本内容
    """
    try:
        if not os.path.exists(pdf_path):
            return {
                "success": False,
                "message": f"PDF文件不存在: {pdf_path}"
            }
            
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        # 如果未指定页面，则提取所有页面
        if page_numbers is None:
            page_numbers = list(range(1, total_pages + 1))
            
        extracted_text = ""
        for page_num in page_numbers:
            if 1 <= page_num <= total_pages:
                page = reader.pages[page_num - 1]
                extracted_text += f"--- 第{page_num}页 ---\n"
                extracted_text += page.extract_text() + "\n\n"
            else:
                return {
                    "success": False,
                    "message": f"页面号 {page_num} 超出范围。PDF共有 {total_pages} 页。"
                }
                
        return {
            "success": True,
            "text": extracted_text,
            "total_pages": total_pages,
            "extracted_pages": len(page_numbers)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"提取PDF文本失败: {str(e)}"
        }


@mcp.tool()
def merge_pdfs(pdf_paths: List[str], output_path: str) -> Dict[str, Any]:
    """
    合并多个PDF文件
    
    Args:
        pdf_paths: PDF文件路径列表
        output_path: 输出文件路径
        
    Returns:
        操作结果
    """
    try:
        # 确保输出目录存在
        Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
        
        writer = PdfWriter()
        
        for pdf_path in pdf_paths:
            if not os.path.exists(pdf_path):
                return {
                    "success": False,
                    "message": f"PDF文件不存在: {pdf_path}"
                }
                
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                writer.add_page(page)
                
        # 保存合并后的PDF
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        return {
            "success": True,
            "message": f"PDF文件已合并: {output_path}",
            "output_path": output_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"合并PDF文件失败: {str(e)}"
        }


@mcp.tool()
def split_pdf(pdf_path: str, output_dir: str, page_ranges: List[Dict[str, int]]) -> Dict[str, Any]:
    """
    拆分PDF文件
    
    Args:
        pdf_path: PDF文件路径
        output_dir: 输出目录
        page_ranges: 页面范围列表，每个元素包含"start"和"end"键
        
    Returns:
        操作结果
    """
    try:
        if not os.path.exists(pdf_path):
            return {
                "success": False,
                "message": f"PDF文件不存在: {pdf_path}"
            }
            
        # 确保输出目录存在
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        output_files = []
        
        for i, page_range in enumerate(page_ranges):
            start_page = page_range.get("start", 1)
            end_page = page_range.get("end", total_pages)
            
            # 验证页面范围
            if start_page < 1 or end_page > total_pages or start_page > end_page:
                return {
                    "success": False,
                    "message": f"无效的页面范围: {start_page}-{end_page}。PDF共有 {total_pages} 页。"
                }
                
            writer = PdfWriter()
            
            # 添加指定范围的页面
            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])
                
            # 生成输出文件名
            output_filename = f"split_{i+1}_{os.path.basename(pdf_path)}"
            output_path = os.path.join(output_dir, output_filename)
            
            # 保存拆分后的PDF
            with open(output_path, "wb") as output_file:
                writer.write(output_file)
                
            output_files.append(output_path)
            
        return {
            "success": True,
            "message": f"PDF文件已拆分到目录: {output_dir}",
            "output_files": output_files
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"拆分PDF文件失败: {str(e)}"
        }


if __name__ == "__main__":
    import uvicorn
    print("启动PyPDF工具服务器...")
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8002)