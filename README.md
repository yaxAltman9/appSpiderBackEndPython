### Python Flask 项目

#### 前置准备
1. **安装 Python:** 确保你已经安装了 Python 3.x。
2. **安装 pip:** 确保你已经安装了 pip。
3. **安装 MySQL:** 确保你已经安装了 MySQL，并创建了相应的数据库和表。
4. **配置数据库:** 根据你的数据库配置修改 `.env` 文件。

#### 启动项目
1. **克隆项目代码:** 将代码克隆到你的本地环境。
   ```sh
   git clone <your-repo-url>
   cd project-root
   ```
2. **创建虚拟环境:** 使用 `venv` 创建一个虚拟环境。
   ```sh
   python -m venv venv
   source venv/bin/activate  # 对于 Windows 系统使用 `venv\Scripts\activate`
   ```
3. **安装依赖:** 使用 pip 安装项目依赖。
   ```sh
   pip install -r requirements.txt
   ```
4. **运行项目:** 启动 Flask 应用程序。
   ```sh
   flask run
   ```

#### README.md
```markdown
# 项目名称

## 项目介绍
这个项目是一个基于 Python 和 Flask 的 Web 应用程序，用于管理和查询工作职位信息。它采用主流的 Flask 框架，并与 MySQL 数据库集成。

## 目录结构
```
project-root/
│
├── app/
│   ├── __init__.py
│   ├── controllers.py
│   ├── models.py
│   └── config.py
├── run.py
├── requirements.txt
└── .env
```

## 安装和运行

### 前置条件
- Python 3.x
- pip
- MySQL 数据库

### 步骤
1. 克隆项目代码:
   ```sh
   git clone <your-repo-url>
   cd project-root
   ```
2. 创建虚拟环境:
   ```sh
   python -m venv venv
   source venv/bin/activate  # 对于 Windows 系统使用 `venv\Scripts\activate`
   ```
3. 安装依赖:
   ```sh
   pip install -r requirements.txt
   ```
4. 配置数据库:
   创建 `.env` 文件并添加以下内容:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=0OKM0okm,
   DB_NAME=boss-spider
   ```
5. 运行项目:
   ```sh
   flask run
   ```

## 使用

### API 端点

- `GET /jobs/data` - 获取工作职位数据
  - 参数:
    - `searchTerm`: 查询关键词 (默认: `""`)
    - `page`: 页码 (默认: `1`)
    - `rowsPerPage`: 每页行数 (默认: `10`)
- `GET /jobs/check-db-connection` - 检查数据库连接

```

通过以上步骤，你可以分别启动 Java 和 Python 项目，并进行相应的测试和开发。如果有任何问题，请随时联系。