# Live Server 本地测试指南

> 用于在本地测试嵌入 Dify 组件的简历 HTML

---

## 为什么需要 Live Server？

Dify 的 CSP（内容安全策略）配置只允许 HTTPS 页面嵌入，不允许 `file://` 本地文件直接访问。

使用 Live Server 可以在本地启动一个 HTTP 服务器，模拟 HTTPS 环境。

---

## 安装与使用

### 方法 1：VS Code 扩展（推荐）

#### 安装步骤

1. 打开 VS Code
2. 点击左侧扩展图标（或按 `Cmd+Shift+X`）
3. 搜索「Live Server」
4. 安装「Live Server」扩展（作者：Ritwick Dey）

#### 使用步骤

1. 在 VS Code 中打开简历 HTML 文件
2. 右键点击编辑区
3. 选择「Open with Live Server」
4. 浏览器自动打开 `http://127.0.0.1:5500/简历.html`
5. 测试 Dify 聊天组件

#### 停止服务

1. 点击 VS Code 右下角的「Port: 5500」
2. 选择「Stop Server」

---

### 方法 2：命令行（Python）

#### 使用 Python 3

```bash
# 进入简历所在目录
cd /path/to/resume/folder

# 启动 HTTP 服务器
python3 -m http.server 8000

# 访问 http://localhost:8000/简历.html
```

#### 使用 Python 2

```bash
python -m SimpleHTTPServer 8000
```

---

### 方法 3：命令行（Node.js）

#### 安装 http-server

```bash
npm install -g http-server
```

#### 使用

```bash
# 进入简历所在目录
cd /path/to/resume/folder

# 启动服务器
http-server -p 8000

# 访问 http://localhost:8000/简历.html
```

---

### 方法 4：命令行（PHP）

```bash
# 进入简历所在目录
cd /path/to/resume/folder

# 启动服务器
php -S localhost:8000

# 访问 http://localhost:8000/简历.html
```

---

## 常见问题

### Q1: Live Server 端口被占用

**错误信息**：
```
Error: listen EADDRINUSE: address already in use :::5500
```

**解决方案**：

**VS Code**：
1. 打开设置（`Cmd+,`）
2. 搜索「Live Server」
3. 找到「Live Server > Settings > Port」
4. 修改为其他端口（如 5501）

**命令行**：使用其他端口
```bash
python3 -m http.server 8001
```

---

### Q2: Dify 组件仍然无法加载

**可能原因**：
1. Dify 应用未正确发布
2. API Key 配置错误
3. 网络问题

**解决方案**：
1. 检查 Dify 应用状态
2. 在 Dify 中测试对话功能
3. 检查浏览器控制台错误信息

---

### Q3: 样式显示不正常

**可能原因**：
1. 相对路径问题
2. 文件编码问题

**解决方案**：
1. 确保所有文件在同一目录
2. 检查 CSS 文件是否正确链接
3. 确认文件编码为 UTF-8

---

## 调试技巧

### 打开浏览器控制台

1. 按 `F12` 或 `Cmd+Option+I`
2. 查看 Console 标签页的错误信息
3. 查看 Network 标签页的请求状态

### 检查 Dify 组件加载

在控制台中运行：
```javascript
// 检查 Dify 组件是否加载
console.log(document.querySelector('.dify-chat-container'));

// 检查是否有 CSP 错误
// 查看 Console 中的红色错误信息
```

---

## 快速启动脚本

创建 `start-server.sh`（macOS/Linux）：

```bash
#!/bin/bash
echo "启动简历服务器..."
python3 -m http.server 8000
echo "访问 http://localhost:8000"
```

创建 `start-server.bat`（Windows）：

```batch
@echo off
echo 启动简历服务器...
python -m http.server 8000
echo 访问 http://localhost:8000
pause
```

---

## 生产部署测试

在本地测试通过后，建议：

1. **部署到网络**（Vercel、GitHub Pages、Netlify）
2. **HTTPS 测试**：确保在 HTTPS 环境下正常工作
3. **多浏览器测试**：Chrome、Firefox、Safari
4. **移动端测试**：检查手机浏览器显示效果

---

## VS Code Live Server 配置建议

在 `.vscode/settings.json` 中添加：

```json
{
  "liveServer.settings.port": 5500,
  "liveServer.settings.root": "/workspace/resume",
  "liveServer.settings.CustomBrowser": "chrome",
  "liveServer.settings.host": "127.0.0.1",
  "liveServer.settings.NoBrowser": false
}
```
