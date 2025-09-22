import os
import yaml
from openai import OpenAI
from typing import List, Dict, Any, Optional


class LLMManager:
    """大语言模型管理类，支持多种模型提供商"""
    
    # 模型配置
    MODEL_CONFIGS = {
        "openai": {
            "base_url": "https://api.openai.com/v1",
            "models": ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]
        },
        "qwen": {
            "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "models": ["qwen-turbo", "qwen-plus", "qwen-max", "qwen2.5-coder-32b-instruct", "qwen3-72b-instruct"]
        },
        "deepseek": {
            "base_url": "https://api.deepseek.com/v1",
            "models": ["deepseek-chat", "deepseek-coder"]
        },
        "moonshot": {
            "base_url": "https://api.moonshot.cn/v1",
            "models": ["moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"]
        },
        "modelscope": {
            "base_url": "https://api-inference.modelscope.cn/v1",
            "models": ["Qwen/Qwen3-Coder-30B-A3B-Instruct", "Qwen/Qwen3-235B-A22B-Instruct-2507"]
        },
        "zhipu": {
            "base_url": "https://open.bigmodel.cn/api/paas/v4",
            "models": ["glm-4", "glm-4-plus", "glm-4-air", "glm-4-airx", "glm-4-long", "glm-4-flash", "glm-4v"]
        },
        "anthropic": {
            "base_url": "https://api.anthropic.com/v1",
            "models": ["claude-3-5-sonnet-20241022", "claude-3-5-haiku-20241022", "claude-3-opus-20240229"]
        },
        "ollama": {
            "base_url": "http://localhost:11434/v1",
            "models": ["qwen3:8b", "nomic-embed-text:latest", "gemma3:1b"]
        },
        "siliconflow": {
            "base_url": "https://api.siliconflow.cn/v1",
            "models": ["Qwen/Qwen2.5-72B-Instruct", "Qwen/Qwen2.5-32B-Instruct", "Qwen/Qwen2.5-14B-Instruct", 
                      "Qwen/Qwen2.5-7B-Instruct", "Qwen/Qwen2.5-3B-Instruct", "Qwen/Qwen2.5-1.5B-Instruct",
                      "Qwen/Qwen2.5-0.5B-Instruct", "Qwen/Qwen2-7B-Instruct", "Qwen/Qwen2-1.5B-Instruct",
                      "Qwen/Qwen1.5-7B-Chat", "Qwen/Qwen1.5-4B-Chat", "Qwen/Qwen1.5-1.8B-Chat",
                      "THUDM/glm-4-9b-chat", "THUDM/chatglm3-6b", "deepseek-ai/DeepSeek-V2.5",
                      "deepseek-ai/DeepSeek-Coder-V2-Instruct", "deepseek-ai/deepseek-llm-67b-chat",
                      "01-ai/Yi-1.5-34B-Chat", "01-ai/Yi-1.5-9B-Chat", "01-ai/Yi-1.5-6B-Chat",
                      "01-ai/Yi-34B-Chat", "mistralai/Mistral-7B-Instruct-v0.3", "mistralai/Mixtral-8x7B-Instruct-v0.1",
                      "meta-llama/Meta-Llama-3.1-8B-Instruct", "meta-llama/Meta-Llama-3.1-70B-Instruct",
                      "meta-llama/Meta-Llama-3.1-405B-Instruct", "meta-llama/Meta-Llama-3-8B-Instruct",
                      "meta-llama/Meta-Llama-3-70B-Instruct", "google/gemma-2-27b-it", "google/gemma-2-9b-it",
                      "google/gemma-7b-it"]
        }
    }

    def __init__(self, provider: str = None, model: str = None, api_key: Optional[str] = None):
        """
        初始化LLM管理器
        
        Args:
            provider: 模型提供商 ("openai", "qwen", "deepseek", "moonshot", "modelscope", "zhipu", "anthropic")
            model: 模型名称
            api_key: API密钥（可选，如果未提供将从配置文件或环境变量中获取）
        """
        # 加载配置
        self.config = self._load_config()
        
        # 如果未指定提供商和模型，则从配置文件中获取默认值
        if provider is None:
            provider = self.config.get("default_provider", "openai")
        if model is None:
            model = self.config.get("default_model", "gpt-4o-mini")
            
        self.provider = provider
        self.model = model
        self.client = self._create_client(api_key)
    
    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        config_path = os.path.join(os.path.dirname(__file__), "config", "config.yaml")
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        return {}
    
    def _get_api_key(self, api_key: Optional[str] = None) -> str:
        """获取API密钥"""
        # 优先使用传入的API密钥
        if api_key:
            return api_key
            
        # 从配置文件中获取
        if self.config and "api_keys" in self.config:
            api_keys = self.config["api_keys"]
            if self.provider in api_keys:
                key = api_keys[self.provider]
                if key and key != f"YOUR_{self.provider.upper()}_API_KEY":
                    return key
        
        # 从环境变量获取
        env_vars = {
            "openai": "OPENAI_API_KEY",
            "qwen": "DASHSCOPE_API_KEY",  # 通义千问使用DASHSCOPE_API_KEY
            "deepseek": "DEEPSEEK_API_KEY",
            "moonshot": "MOONSHOT_API_KEY",
            "modelscope": "MODELSCOPE_API_KEY",
            "zhipu": "ZHIPUAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "siliconflow": "SILICONFLOW_API_KEY"
        }
        
        if self.provider in env_vars:
            env_key = env_vars[self.provider]
            env_value = os.getenv(env_key)
            if env_value:
                return env_value
        
        # 默认值
        return "YOUR_API_KEY"
    
    def _create_client(self, api_key: Optional[str] = None) -> OpenAI:
        """创建OpenAI客户端"""
        if self.provider not in self.MODEL_CONFIGS:
            raise ValueError(f"不支持的模型提供商: {self.provider}")
        
        config = self.MODEL_CONFIGS[self.provider]
        return OpenAI(
            api_key=api_key or self._get_api_key(None),
            base_url=config["base_url"]
        )
    
    def update_provider(self, provider: str, api_key: Optional[str] = None):
        """
        更新模型提供商
        
        Args:
            provider: 新的模型提供商
            api_key: 新的API密钥，如果为None则使用当前密钥
        """
        self.provider = provider
        self.client = self._create_client(api_key)
    
    def update_model(self, model: str):
        """
        更新模型
        
        Args:
            model: 新的模型名称
        """
        self.model = model
    
    def chat_completion(self, messages: list, **kwargs) -> Dict[str, Any]:
        """
        调用聊天完成接口
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            模型响应
        """
        # 设置默认参数
        default_params = {
            "model": self.model,
            "messages": messages
        }
        
        # 合并参数
        params = {**default_params, **kwargs}
        
        # 调用API
        response = self.client.chat.completions.create(**params)
        return response
    
    def get_available_providers(self) -> list:
        """获取所有支持的模型提供商"""
        return list(self.MODEL_CONFIGS.keys())
    
    def get_available_models(self, provider: Optional[str] = None) -> list:
        """
        获取指定提供商支持的模型列表
        
        Args:
            provider: 模型提供商，如果为None则使用当前提供商
            
        Returns:
            模型列表
        """
        if provider is None:
            provider = self.provider
        
        if provider in self.MODEL_CONFIGS:
            return self.MODEL_CONFIGS[provider]["models"]
        else:
            return []
    
    def load_prompt_template(self, template_name: str) -> str:
        """
        加载提示词模板
        
        Args:
            template_name: 模板名称（不包含文件扩展名）
            
        Returns:
            模板内容
        """
        template_path = os.path.join(
            os.path.dirname(__file__), 
            "config", 
            "prompt_templates", 
            f"{template_name}.txt"
        )
        
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            raise FileNotFoundError(f"提示词模板 '{template_name}' 不存在")
    
    def render_prompt_template(self, template_name: str, **kwargs) -> str:
        """
        渲染提示词模板
        
        Args:
            template_name: 模板名称（不包含文件扩展名）
            **kwargs: 模板变量
            
        Returns:
            渲染后的提示词
        """
        template_content = self.load_prompt_template(template_name)
        
        # 简单的模板渲染（使用Python内置的str.format方法）
        try:
            return template_content.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"模板 '{template_name}' 缺少必要的变量: {e}")


# 使用示例
if __name__ == "__main__":
    # 初始化OpenAI
    llm = LLMManager(provider="openai", model="gpt-4o-mini")
    
    # 调用示例
    messages = [
        {"role": "system", "content": "你是一个 helpful assistant."},
        {"role": "user", "content": "你好，介绍一下你自己"}
    ]
    
    response = llm.chat_completion(messages)
    print(response.choices[0].message.content)