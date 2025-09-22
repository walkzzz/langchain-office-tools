# 智谱AI配置指南

本文档详细说明了如何配置和使用智谱AI平台的API密钥。

## 获取API密钥

### 方法1：修改配置文件

在 `config/config.yaml` 文件中找到 `zhipu` 配置项，将其值替换为您的API密钥：

```yaml
api_keys:
  zhipu: "YOUR_ZHIPU_API_KEY"  # 请替换为您的实际API密钥
```

### 方法2：设置环境变量

您也可以通过设置环境变量来配置API密钥：

```bash
export ZHIPUAI_API_KEY="your_actual_api_key_here"
```

在Windows系统中使用：

```cmd
set ZHIPUAI_API_KEY=your_actual_api_key_here
```

## 支持的模型

智谱AI平台支持以下模型：

- glm-4
- glm-4-plus
- glm-4-air
- glm-4-airx
- glm-4-long
- glm-4-flash
- glm-4v

## 测试配置

配置完成后，您可以运行以下命令测试配置是否正确：

```bash
python examples/zhipu_example.py
```

如果配置正确，您将看到模型的响应输出。

## 配置验证

如果您已经正确配置了API密钥，运行示例代码时将看到类似以下的输出：

```
=== 智谱平台示例 ===
提供商: zhipu
模型: glm-4

模型响应:
[模型生成的内容]

=== 切换模型示例 ===
要切换到zhipu的其他模型，可以使用:
  llm.update_model('glm-4-plus')

切换后模型: glm-4-plus

支持的所有智谱模型:
  - glm-4
  - glm-4-plus
  - glm-4-air
  - glm-4-airx
  - glm-4-long
  - glm-4-flash
  - glm-4v
```

如果遇到任何问题，请检查：

1. API密钥是否正确配置
2. 网络连接是否正常
3. API密钥是否有足够的权限
