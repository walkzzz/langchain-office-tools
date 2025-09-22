import sys
import os
import pytest

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.llm import LLMManager


def test_llm_manager_initialization():
    """测试LLMManager初始化"""
    # 测试默认初始化
    llm = LLMManager()
    assert llm.provider is not None
    assert llm.model is not None
    
    # 测试指定提供商和模型初始化
    llm = LLMManager(provider="openai", model="gpt-4o-mini")
    assert llm.provider == "openai"
    assert llm.model == "gpt-4o-mini"


def test_get_available_providers():
    """测试获取可用提供商"""
    llm = LLMManager()
    providers = llm.get_available_providers()
    assert isinstance(providers, list)
    assert len(providers) > 0
    assert "openai" in providers
    assert "qwen" in providers
    assert "deepseek" in providers


def test_get_available_models():
    """测试获取可用模型"""
    llm = LLMManager()
    
    # 测试获取openai模型
    openai_models = llm.get_available_models("openai")
    assert isinstance(openai_models, list)
    assert len(openai_models) > 0
    assert "gpt-4o-mini" in openai_models
    
    # 测试获取qwen模型
    qwen_models = llm.get_available_models("qwen")
    assert isinstance(qwen_models, list)
    assert len(qwen_models) > 0


def test_update_provider():
    """测试更新提供商"""
    llm = LLMManager()
    original_provider = llm.provider
    
    # 更新提供商
    llm.update_provider("qwen")
    assert llm.provider == "qwen"
    
    # 切换回原提供商
    llm.update_provider(original_provider)
    assert llm.provider == original_provider


def test_update_model():
    """测试更新模型"""
    llm = LLMManager()
    original_model = llm.model
    
    # 更新模型
    llm.update_model("gpt-4o")
    assert llm.model == "gpt-4o"
    
    # 切换回原模型
    llm.update_model(original_model)
    assert llm.model == original_model


if __name__ == "__main__":
    pytest.main([__file__])