# GitHub 协作完整流程指南

本文档提供从项目仓库下载资料到协作更新的完整命令流程。

---

## 一、基础准备

### 1.1 克隆项目（首次操作）

```bash
# 克隆远程仓库到本地
git clone https://github.com/bucky1119/AI-Knowledge-Base.git

# 进入项目目录
cd AI-Knowledge-Base
```

### 1.2 配置 Git 用户信息

```bash
# 设置用户名和邮箱（只需配置一次）
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
```

---

## 二、日常协作流程

### 2.1 同步最新代码

```bash
# 确保在主分支
git checkout main

# 拉取最新代码
git fetch origin
git pull origin main
```

### 2.2 创建工作分支

```bash
# 创建新分支进行开发
git checkout -b feature/你的功能名称

# 或基于最新main创建
git checkout -b feature/你的功能名称 origin/main
```

### 2.3 查看和添加文件

```bash
# 查看当前状态
git status

# 添加单个文件
git add 文件名

# 添加所有文件
git add .

# 添加特定类型的文件
git add *.md        # 只添加markdown文件
git add src/       # 添加src目录下的文件
```

### 2.4 提交更改

```bash
# 提交并添加描述信息
git commit -m "提交描述：做了什么修改"

# 修改最后一次提交（如果描述写错了）
git commit --amend -m "正确的描述"
```

### 2.5 推送分支

```bash
# 首次推送（关联本地分支和远程分支）
git push -u origin feature/你的功能名称

# 后续推送
git push origin feature/你的功能名称
```

---

## 三、发起协作请求（Pull Request）

### 3.1 创建 PR 的完整流程

```bash
# 1. 确保代码已提交
git status

# 2. 推送分支到远程
git push -u origin feature/你的功能名称

# 3. 在浏览器中创建 Pull Request
# 访问: https://github.com/bucky1119/AI-Knowledge-Base/pull/new/feature/你的功能名称
```

### 3.2 同步远程更新

```bash
# 获取远程分支列表
git fetch origin

# 查看所有分支
git branch -a

# 切换到远程分支
git checkout -b 本地分支名 origin/远程分支名
```

---

## 四、常用辅助命令

### 4.1 分支管理

```bash
# 查看分支
git branch              # 本地分支
git branch -r           # 远程分支
git branch -a            # 所有分支

# 删除本地分支
git branch -d 分支名

# 删除远程分支
git push origin --delete 分支名
```

### 4.2 查看历史

```bash
# 查看提交历史
git log

# 查看简略历史
git log --oneline

# 查看某个文件的修改历史
git log 文件名

# 查看具体某次提交的内容
git show 提交ID
```

### 4.3 撤销操作

```bash
# 撤销未暂存的修改
git checkout -- 文件名

# 撤销已暂存但未提交的内容
git reset HEAD 文件名

# 撤销最后一次提交（保留修改）
git reset --soft HEAD~1

# 完全撤销最后一次提交（不保留修改）
git reset --hard HEAD~1
```

### 4.4 暂存工作

```bash
# 暂存当前工作
git stash

# 查看暂存列表
git stash list

# 恢复暂存的内容
git stash pop

# 删除暂存
git stash drop
```

---

## 五、协作最佳实践

### 5.1 每日工作流程

```bash
# 每天开始工作时
git checkout main
git pull origin main

# 创建新功能分支
git checkout -b feature/今日任务

# ... 进行开发工作 ...

# 提交并推送
git add .
git commit -m "完成XX��能"
git push -u origin feature/今日任务
```

### 5.2 分支命名规范

- `feature/功能名称` - 新功能开发
- `fix/问题描述` - Bug修复
- `docs/文档更新` - 文档更新
- `refactor/重构描述` - 代码重构

### 5.3 提交信息规范

```
feat: 添加新功能
fix: 修复问题
docs: 文档更新
style: 格式调整
refactor: 重构
test: 测试
```

---

## 六、常见问题解决

### 6.1 冲突解决

```bash
# 拉取时发生冲突
git pull origin main

# 手动解决冲突后
git add 解决冲突的文件
git commit -m "解决冲突"
git push
```

### 6.2 合并其他分支的修改

```bash
# 切换到要合并的分支
git checkout main

# 合并其他分支
git merge feature/其他分支

# 如果有冲突，手动解决后提交
```

### 6.3 更新fork的仓库

```bash
# 添加上游仓库
git remote add upstream https://github.com/bucky1119/AI-Knowledge-Base.git

# 获取上游更新
git fetch upstream

# 合并到主分支
git checkout main
git merge upstream/main
```

---

## 七、快速命令汇总

```bash
# 一键开始新任务
git checkout main && git pull origin main && git checkout -b feature/新任务

# 一键提交推送
git add . && git commit -m "描述" && git push -u origin feature/当前分支

# 查看当前状态
git status && git log --oneline -5
```

---

> 📝 **提示**: 建议在进行重要操作前先查看 `git status` 确认当前状态，避免误操作。