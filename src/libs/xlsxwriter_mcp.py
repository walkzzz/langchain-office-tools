"""
xlsxwriter库的MCP服务器配置
提供Excel电子表格创建和处理功能
"""

import os
from pathlib import Path
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
import xlsxwriter

# 初始化MCP服务器
mcp = FastMCP("XlsxWriterTools")


@mcp.tool()
def create_excel_workbook(data: List[List[Any]], filename: str, sheet_name: str = "Sheet1", save_path: str = "./") -> Dict[str, Any]:
    """
    创建Excel工作簿
    
    Args:
        data: 表格数据（二维列表）
        filename: 文件名（不含扩展名）
        sheet_name: 工作表名称
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.xlsx")
        
        # 创建工作簿和工作表
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet(sheet_name)
        
        # 写入数据
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                worksheet.write(row_idx, col_idx, cell_data)
                
        # 关闭工作簿
        workbook.close()
        
        return {
            "success": True,
            "message": f"Excel工作簿已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建Excel工作簿失败: {str(e)}"
        }


@mcp.tool()
def create_formatted_excel(data: List[List[Any]], filename: str, formatting: Dict[str, Any], save_path: str = "./") -> Dict[str, Any]:
    """
    创建带格式的Excel文件
    
    Args:
        data: 表格数据（二维列表）
        filename: 文件名（不含扩展名）
        formatting: 格式配置字典
        save_path: 保存路径
        
    Returns:
        操作结果
    """
    try:
        # 确保保存路径存在
        Path(save_path).mkdir(parents=True, exist_ok=True)
        
        # 创建文件路径
        file_path = os.path.join(save_path, f"{filename}.xlsx")
        
        # 创建工作簿
        workbook = xlsxwriter.Workbook(file_path)
        
        # 创建格式
        header_format = workbook.add_format(formatting.get("header", {}))
        cell_format = workbook.add_format(formatting.get("cell", {}))
        
        # 创建工作表
        worksheet = workbook.add_worksheet(formatting.get("sheet_name", "Sheet1"))
        
        # 写入数据
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                if row_idx == 0 and formatting.get("header_row", False):
                    worksheet.write(row_idx, col_idx, cell_data, header_format)
                else:
                    worksheet.write(row_idx, col_idx, cell_data, cell_format)
                    
        # 设置列宽
        column_widths = formatting.get("column_widths", [])
        for col_idx, width in enumerate(column_widths):
            worksheet.set_column(col_idx, col_idx, width)
            
        # 关闭工作簿
        workbook.close()
        
        return {
            "success": True,
            "message": f"格式化Excel文件已创建: {file_path}",
            "file_path": file_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"创建格式化Excel文件失败: {str(e)}"
        }


@mcp.tool()
def add_chart_to_excel(filename: str, chart_data: Dict[str, Any], save_path: str = "./") -> Dict[str, Any]:
    """
    向现有Excel文件添加图表
    
    Args:
        filename: 文件名（不含扩展名）
        chart_data: 图表数据配置
        save_path: 文件所在路径
        
    Returns:
        操作结果
    """
    try:
        file_path = os.path.join(save_path, f"{filename}.xlsx")
        
        if not os.path.exists(file_path):
            return {
                "success": False,
                "message": f"Excel文件不存在: {file_path}"
            }
            
        # 打开现有工作簿
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()
        
        # 创建图表
        chart_type = chart_data.get("type", "column")
        chart = workbook.add_chart({'type': chart_type})
        
        # 配置图表数据系列
        for series in chart_data.get("series", []):
            chart.add_series(series)
            
        # 设置图表标题和轴标签
        chart.set_title({'name': chart_data.get('title', '')})
        chart.set_x_axis({'name': chart_data.get('x_axis', '')})
        chart.set_y_axis({'name': chart_data.get('y_axis', '')})
        
        # 设置图表样式
        chart.set_style(chart_data.get('style', 1))
        
        # 插入图表到工作表
        position = chart_data.get('position', {'x_offset': 0, 'y_offset': 0})
        worksheet.insert_chart('E2', chart, position)
        
        # 关闭工作簿
        workbook.close()
        
        return {
            "success": True,
            "message": f"图表已添加到Excel文件: {file_path}"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"添加图表到Excel文件失败: {str(e)}"
        }


if __name__ == "__main__":
    import uvicorn
    print("启动XlsxWriter工具服务器...")
    uvicorn.run(mcp.streamable_http_app, host="127.0.0.1", port=8003)