# FastMCP 智能体平台

基于 Python 3.12，集成 FastAPI 与 FastMCP 的智能体平台项目骨架。

## 技术栈
- Python 3.12
- FastAPI
- FastMCP
- Uvicorn
- Pytest

## 目录结构
```
app/
  main.py
  api/v1.py
  core/config.py
  mcp/agent.py
tests/test_main.py
pyproject.toml
.env
README.md
```

## 快速开始
1. 安装依赖：
   ```bash
   pip install -r requirements.txt  # 或使用 Poetry/PDM
   ```
2. uvicorn启动服务：
   ```bash
   uvicorn app.main:app --reload
   ```
3. python启动服务：
   ```bash
   python3 run.py
   ```
4. 运行测试：
   ```bash
   pytest
   ```
---


