# OpenAI配置指南

本文档详细说明了如何配置和使用OpenAI平台的API密钥。

## 获取API密钥

### 方法1：修改配置文件

在 `config/config.yaml` 文件中找到 `openai` 配置项，将其值替换为您的API密钥：

```yaml
api_keys:
  openai: "YOUR_OPENAI_API_KEY"  # 请替换为您的实际API密钥
```

### 方法2：设置环境变量

您也可以通过设置环境变量来配置API密钥：

```bash
export OPENAI_API_KEY="your_actual_api_key_here"
```

在Windows系统中使用：

```cmd
set OPENAI_API_KEY=your_actual_api_key_here
```

## 支持的模型

OpenAI平台支持以下模型：

- gpt-3.5-turbo
- gpt-3.5-turbo-instruct
- gpt-4
- gpt-4-turbo
- gpt-4o

## 测试配置

配置完成后，您可以运行以下命令测试配置是否正确：

```bash
python examples/llm_usage_example.py
```

如果配置正确，您将看到模型的响应输出。

## 配置验证

如果您已经正确配置了API密钥，运行示例代码时将看到类似以下的输出：

```
=== OpenAI平台示例 ===
提供商: openai
模型: gpt-3.5-turbo

模型响应:
[模型生成的内容]

=== 切换模型示例 ===
要切换到OpenAI的其他模型，可以使用:
  llm.update_model('gpt-4')

切换后模型: gpt-4

支持的所有OpenAI模型:
  - gpt-3.5-turbo
  - gpt-3.5-turbo-instruct
  - gpt-4
  - gpt-4-turbo
  - gpt-4o
```

如果遇到任何问题，请检查：

1. API密钥是否正确配置
2. 网络连接是否正常
3. API密钥是否有足够的权限