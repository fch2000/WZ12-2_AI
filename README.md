# 海上油田即时问答系统

一个基于DeepSeek API的智能聊天问答系统，集成AI聊天，智能PDF问答工具，AI搜索工具

---
## 🌟 特性

- 🖥️ **AI聊天助手**: 集成DeepSeek实现AI对话
- 📚 **智能PDF问答工具**: 基于RAG实现PDF文件问答
- 💬 **AI搜索工具**: 通过石油工业相关提示模板实现规范化搜索
- 💾 **记忆对话**: 存储历史消息，方便用户回顾
- 🌐 **Web界面**: 基于Streamlit的现代化交互界面
- 💬 **聊天体验**: 类ChatGPT的对话式问答体验
- 📱 **响应式设计**: 支持桌面和移动设备访问
---
## 🚀 本地部署

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

```
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="deepseek-chat", 
                   openai_api_key = "<此处替换成你的API密钥>",
                   openai_api_base = "https://api.deepseek.com/v1")
```

### 3. 获取DeepSeek API密钥

1. 访问 [DeepSeek平台](https://platform.deepseek.com/)
2. 注册并登录账户
3. 在API管理页面创建新的API密钥
4. 复制密钥并按上述方法配置

### 4. 运行系统

```bash
streamlit run main.py
```
---
## 📄 使用说明

### 1. **启动应用**:
   ```bash
   streamlit run streamlit_app.py
   ```
   
### 2. **功能特性**:
   - 🎨 **现代化界面**: 美观的Web界面，支持响应式设计
   - 💬 **聊天体验**: 类似ChatGPT的对话式交互
   - ⚙️ **即开即用**: 后台已配置好DeepSeek API密钥，无需用户输入即可对话
   - 📖 **专业搜索**: 搜索引擎已配置好石油工业和技术相关提示模板，实现精准搜索
   - 🗑️ **历史管理**: 支持清空聊天历史

### 3. **使用技巧**:
   - 使用侧边栏切换不同功能，获取API KEY和联系作者
   - AI聊天助手：与AI进行对话，通过侧边栏“开始新的对话”按钮清空历史对话
   - 智能PDF问答工具：上传PDF文件后，对文件内容提问，通过下拉框回顾历史问题，通过侧边栏“开始新的提问”按钮刷新回答
   - AI搜索工具：对与石油工业或技术相关问题搜索，文末可查看参考链接，通过侧边栏“开始新的提问”按钮刷新回答

### 示例问答

**问题**: 简述对压力变送器进行校验步骤

**答案**: 
概述：
在海上石油工程中，压力变送器的校验是确保生产安全和数据准确性的关键环节。校验需遵循行业标准（如API、ISO），通过对比标准压力源与变送器输出信号，验证其精度和稳定性。以下是详细的校验流程及注意事项。

1. 校验前准备：
1.1 工具与设备：
标准压力源：精度至少高于被校验变送器4倍（如0.025%级活塞式压力计）。
数字万用表/过程校验仪：用于测量电流（4-20mA）或电压信号。
压力模块/手操泵：提供稳定压力...
---
## 📁 项目结构

```
WZ12-2_AI/
├── pages/                    # 前端页面
│   ├──page0.py               # 首页前端代码
│   ├──page1.py               # 聊天页面前端代码
│   ├──page2.py               # 文本检索页面前端代码
│   └──page0.py               # 搜索引擎前端代码
├── main.py                   # Streamlit Web启动应用
├── requirements.txt          # 依赖列表
├── utils1.py                 # 聊天页面后端代码
├── utils2.py                 # 文本检索页面后端代码
└── utils3.py                 # 搜索引擎后端代码
```
---
## 🐛 故障排除

### 常见问题

1. **API密钥错误**
   ```
   错误: 401 Unauthorized
   解决: 检查API密钥是否正确设置
   ```

2. **依赖安装失败**
   ```bash
   # 升级pip
   python -m pip install --upgrade pip
   
   # 使用国内镜像
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
   ```
---
## 🙏 致谢

- [DeepSeek](https://www.deepseek.com/) - 提供强大的AI模型
- [Streamlit](https://streamlit.io/) - 易上手的网站框架
- [GitHub](https://github.com/) - 开源学习社区
- 涠洲12-2油田全体领导及同事支持