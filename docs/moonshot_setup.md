# Moonshot AI配置指南

本文档详细说明了如何配置和使用Moonshot AI平台的API密钥。

## 获取API密钥

### 方法1：修改配置文件

在 `config/config.yaml` 文件中找到 `moonshot` 配置项，将其值替换为您的API密钥：

```yaml
api_keys:
  moonshot: "YOUR_MOONSHOT_API_KEY"  # 请替换为您的实际API密钥
```

### 方法2：设置环境变量

您也可以通过设置环境变量来配置API密钥：

```bash
export MOONSHOT_API_KEY="your_actual_api_key_here"
```

在Windows系统中使用：

```cmd
set MOONSHOT_API_KEY=your_actual_api_key_here
```

## 支持的模型

Moonshot AI平台支持以下模型：

- moonshot-v1-8k
- moonshot-v1-32k
- moonshot-v1-128k

## 测试配置

配置完成后，您可以运行以下命令测试配置是否正确：

```bash
python examples/moonshot_example.py
```

如果配置正确，您将看到模型的响应输出。

## 配置验证

如果您已经正确配置了API密钥，运行示例代码时将看到类似以下的输出：

```
=== Moonshot AI平台示例 ===
提供商: moonshot
模型: moonshot-v1-8k

模型响应:
[模型生成的内容]

=== 切换模型示例 ===
要切换到Moonshot AI的其他模型，可以使用:
  llm.update_model('moonshot-v1-32k')

切换后模型: moonshot-v1-32k

支持的所有Moonshot AI模型:
  - moonshot-v1-8k
  - moonshot-v1-32k
  - moonshot-v1-128k
```

如果遇到任何问题，请检查：

1. API密钥是否正确配置
2. 网络连接是否正常
3. API密钥是否有足够的权限