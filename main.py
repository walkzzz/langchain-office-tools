# 导入必要的组件
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
 
# 初始化模型
model = ChatOpenAI(model="gpt-4o-mini")
 
# 创建提示词模板
system_template = "将以下内容从英语翻译成{language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template), 
    ("user", "{text}")
])
 
# 通过组合提示词和模型创建链
chain = prompt_template | model
 
# 使用链
result = chain.invoke({"language": "Italian", "text": "Hello, how are you?"})
print(result.content)
# 输出：Ciao, come stai?