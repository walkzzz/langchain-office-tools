# LangChain Office Tools

LangChain Office Tools 是一个集成了多种大语言模型的工具包，专为办公场景设计，支持多种模型提供商。

## 安装

```bash
# 方法1：使用pip安装（推荐）
pip install -r requirements.txt

# 方法2：使用uv安装（更快）
uv pip install -r requirements.txt

# 方法3：使用pyproject.toml安装
pip install -e .
```

## 配置

在 `config/config.yaml` 文件中配置您的API密钥：

```yaml
api_keys:
  openai: "YOUR_OPENAI_API_KEY"      # 请在OpenAI平台获取API密钥: https://platform.openai.com/api-keys
  qwen: "YOUR_QWEN_API_KEY"          # 请在阿里云百炼平台获取API密钥: https://help.aliyun.com/zh/bailian
  deepseek: "YOUR_DEEPSEEK_API_KEY"  # 请在DeepSeek平台获取API密钥: https://platform.deepseek.com/
  moonshot: "YOUR_MOONSHOT_API_KEY"  # 请在Moonshot平台获取API密钥: https://platform.moonshot.cn/console/api-keys
  modelscope: "YOUR_MODELSCOPE_API_KEY"  # 请在ModelScope平台获取API密钥: https://modelscope.cn/settings/api
  zhipu: "YOUR_ZHIPU_API_KEY"        # 请在智谱平台获取API密钥: https://bigmodel.cn/usercenter/apikeys
  anthropic: "YOUR_ANTHROPIC_API_KEY"  # 请在Anthropic平台获取API密钥: https://console.anthropic.com/settings/keys
  siliconflow: "YOUR_SILICONFLOW_API_KEY"  # 请在SiliconFlow平台获取API密钥: https://cloud.siliconflow.cn/account/ak
  ollama: "YOUR_OLLAMA_API_KEY"      # 本地模型，通常不需要API密钥
```

或者通过设置环境变量来配置API密钥：

```bash
# OpenAI API密钥
export OPENAI_API_KEY=your_actual_api_key_here

# 通义千问 API密钥
export DASHSCOPE_API_KEY=your_actual_api_key_here

# DeepSeek API密钥
export DEEPSEEK_API_KEY=your_actual_api_key_here

# Moonshot API密钥
export MOONSHOT_API_KEY=your_actual_api_key_here

# ModelScope API密钥
export MODELSCOPE_API_KEY=your_actual_api_key_here

# 智谱AI API密钥
export ZHIPUAI_API_KEY=your_actual_api_key_here

# Anthropic API密钥
export ANTHROPIC_API_KEY=your_actual_api_key_here

# SiliconFlow API密钥
export SILICONFLOW_API_KEY=your_actual_api_key_here

# Ollama 本地模型（通常不需要API密钥）
```

在Windows系统中使用：
```cmd
set OPENAI_API_KEY=your_actual_api_key_here
set DASHSCOPE_API_KEY=your_actual_api_key_here
set DEEPSEEK_API_KEY=your_actual_api_key_here
set MOONSHOT_API_KEY=your_actual_api_key_here
set MODELSCOPE_API_KEY=your_actual_api_key_here
set ZHIPUAI_API_KEY=your_actual_api_key_here
set ANTHROPIC_API_KEY=your_actual_api_key_here
set SILICONFLOW_API_KEY=your_actual_api_key_here
```

## 使用示例

```python
from src.core.llm import LLMManager

# 初始化LLM管理器
llm = LLMManager(
    provider="openai",
    model="gpt-3.5-turbo"
)

# 调用模型
messages = [
    {"role": "system", "content": "你是一个 helpful assistant."},
    {"role": "user", "content": "你好，介绍一下Python编程语言"}
]

response = llm.chat_completion(messages)
print(response.choices[0].message.content)
```

更多使用示例请查看 `examples/llm_usage_example.py` 文件。

## 支持的模型提供商

- OpenAI (GPT系列)
- 通义千问 (Qwen系列)
- DeepSeek (DeepSeek系列)
- Moonshot AI (Moonshot系列)
- ModelScope (Qwen系列)
- 智谱AI (GLM系列)
- Anthropic (Claude系列)
- SiliconFlow (多种开源模型)
- Ollama (本地模型)

## 项目结构

```
langchain-office-tools/
├── config/              # 配置文件目录
│   ├── config.yaml      # 模型配置文件
│   └── prompt_templates/ # 提示词模板目录
├── examples/            # 使用示例目录
│   ├── llm_usage_example.py
├── src/                # 源代码目录
│   ├── core/           # 核心模块
│   │   ├── llm.py      # 大语言模型管理器
│   │   └── mcp_server.py   # 服务端实现
│   ├── tests/          # 测试文件
│   └── utils/          # 工具模块
└── tests/              # 单元测试目录
```

## 开发

1. 安装开发依赖：
   ```bash
   # 方法1：使用pip安装（推荐）
   pip install -r dev-requirements.txt
   
   # 方法2：使用uv安装（更快）
   uv pip install -r dev-requirements.txt
   
   # 方法3：使用pyproject.toml安装开发依赖
   pip install -e .[dev]
   ```

2. 运行示例：
   ```bash
   python examples/llm_usage_example.py
   ```

3. 运行特定模型示例：
   ```bash
   python examples/deepseek_example.py
   ```

4. 运行测试：
   ```bash
   # 运行简单测试
   python simple_test.py
   
   # 或使用Makefile
   make test
   ```

5. 代码质量检查：
   ```bash
   # 格式化代码
   make format
   
   # 代码检查
   make lint
   
   # 类型检查
   make type-check
   
   # 安装pre-commit钩子
   make pre-commit-install
   ```

6. 使用Makefile简化开发任务：
   ```bash
   # 查看所有可用命令
   make help
   
   # 安装包
   make install
   
   # 清理构建文件
   make clean
   ```

7. 提示词模板功能：
   项目支持使用提示词模板来简化常见任务的提示词构建。
   
   加载和使用提示词模板的示例：
   ```python
   from src.core.llm import LLMManager
   
   # 初始化LLM管理器
   llm = LLMManager(provider="openai", model="gpt-4o-mini")
   
   # 加载提示词模板
   template_content = llm.load_prompt_template("general_template")
   
   # 渲染提示词模板
   rendered_prompt = llm.render_prompt_template("general_template", question="什么是人工智能？")
   ```
   
   可用的提示词模板：
   - `general_template`: 通用助手提示词模板
   - `code_generation_template`: 代码生成提示词模板
   - `document_summary_template`: 文档总结提示词模板
   
   更多使用示例请查看 `examples/prompt_template_example.py` 文件。

## 办公工具API

本项目提供了一套完整的办公工具API，支持日常办公软件操作并转换为MCP工具供大模型调用。

### 可用工具

- **文档处理工具**
  - Word文档创建和编辑
  - Excel电子表格创建和数据处理
  - PowerPoint演示文稿创建和格式化

- **文件管理工具**
  - 目录列表和文件浏览
  - 文件读取和内容提取
  - 文件移动和删除操作
  - 文件压缩和解压功能

- **文档转换工具**
  - PDF文本提取
  - Office文档转Markdown
  - 文件压缩和解压操作

### 启动服务

```bash
# 启动主MCP服务
python src/core/mcp_server.py

# 启动库专用MCP服务
python src/libs/main_mcp_server.py
```

### 使用示例

```python
# 客户端使用示例
from src.core.office_tools import (
    create_word_document,
    create_excel_spreadsheet,
    create_powerpoint_presentation,
    list_files_in_directory,
    read_file_content,
    move_file,
    delete_file,
    compress_files,
    extract_archive
)

# 创建Word文档
result = create_word_document(
    content="文档内容",
    filename="example",
    save_path="./output"
)
```

更多使用示例请查看 `examples/client_example.py` 文件。

## 库专用MCP服务器

本项目为每个办公库提供了独立的MCP服务器实现，以支持更细粒度的工具调用：

### 支持的库

1. **pypdf** - PDF处理库
   - 文本提取
   - PDF合并
   - PDF分割

2. **xlsxwriter** - Excel处理库
   - 创建Excel工作簿
   - 创建格式化Excel
   - 添加图表到Excel

3. **markitdown** - 文档转Markdown库
   - 单个文件转换
   - 批量文件转换
   - 获取支持的文件类型

4. **zipfile** - 压缩文件处理库
   - 创建ZIP压缩文件
   - 解压ZIP文件
   - 列出ZIP内容
   - 添加文件到ZIP
   - 提取特定文件

### 启动库专用服务器

每个库都有独立的MCP服务器实现，可以通过以下方式启动：

```bash
# 启动pypdf MCP服务器
python src/libs/pypdf_mcp.py

# 启动xlsxwriter MCP服务器
python src/libs/xlsxwriter_mcp.py

# 启动markitdown MCP服务器
python src/libs/markitdown_mcp.py

# 启动zipfile MCP服务器
python src/libs/zipfile_mcp.py

# 启动所有库的主MCP服务器
python src/libs/main_mcp_server.py
```

## 文档

有关各模型提供商的详细配置说明，请参阅 [docs](docs) 目录：

- [智谱AI配置指南](docs/zhipu_setup.md)
- [DeepSeek配置指南](docs/deepseek_setup.md)
- [OpenAI配置指南](docs/openai_setup.md)
- [通义千问配置指南](docs/qwen_setup.md)
- [Moonshot AI配置指南](docs/moonshot_setup.md)