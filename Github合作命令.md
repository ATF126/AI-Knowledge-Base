# GitHub 协作完整流程指南

本文档提供从 fork 仓库、同步上游、更新内容，到提交 Pull Request 的完整命令流程。适合第一次参与协作的同学按步骤执行。

具体案例可以查看沈成同学提供的[案例](./GitHub合作案例/github-fork-upload-guide.md)

## 1. Fork 仓库

原仓库：https://github.com/bucky1119/AI-Knowledge-Base.git

先到原仓库页面点击 Fork，把项目复制到自己的 GitHub 账号下。后续所有修改都在自己的 Fork 仓库中完成。

## 2. 克隆到本地

把自己的 Fork 仓库克隆到本地电脑：

	git clone https://github.com/你的账号/仓库名.git
	cd 仓库名

如果仓库已经存在本地，也可以直接进入目录。

## 3. 配置上游仓库

为了后续同步原仓库的最新内容，给本地仓库添加 upstream 远程地址：

	git remote add upstream https://github.com/bucky1119/AI-Knowledge-Base.git
	git remote -v

执行后可以看到 origin 和 upstream 两个远程地址。

## 4. 新建分支

可以直接在main主分支修改，也可以创建新分支进行管理。

	git checkout -b feature/你的功能名

分支名建议清晰直接，例如：

	docs/add-contribution-guide

## 5. 更新内容

在分支里修改文件、补充内容或修复问题。完成后先查看变更：

	git status
	git diff

确认没有误改文件后，再把修改加入暂存区：

	git add .

如果只想提交某个文件，也可以单独指定文件名。

## 6. 提交本地版本

使用清晰的提交信息记录这次改动：

	git commit -m "docs: update GitHub collaboration guide"

建议提交信息简短、具体，最好说明这次修改的目的。

## 7. 同步上游最新内容

如果原仓库已经有更新，先拉取 upstream 的最新内容，再合并到自己的分支，减少冲突：

	git fetch upstream
	git merge upstream/main


如果合并时出现冲突，先手动解决冲突，再执行：

	git add .
	git commit

## 8. 推送到自己的 Fork

把本地分支推送到自己的 GitHub 仓库：

	git push origin feature/你的功能名

第一次推送时，可能需要加上 upstream 追踪分支：

	git push -u origin feature/你的功能名

## 9. 发起 Pull Request

推送完成后，打开自己 Fork 仓库的 GitHub 页面，点击 Compare & pull request，填写 PR 内容并提交。

PR 描述建议包含这些信息：

- 这次修改了什么
- 为什么要改
- 是否有测试或截图
- 有没有需要特别注意的地方

## 10. 处理评审意见

如果维护者提出修改意见，继续在同一个分支上更新代码，然后再次提交并推送：

	git add .
	git commit -m "fix: address review comments"
	git push

PR 会自动更新，不需要重新新建一个。

## 11. 协作流程总览

完整流程可以记成下面这条链路：

	Fork 仓库 -> 克隆本地 -> 添加 upstream -> 新建分支 -> 修改内容 -> 提交 commit -> 推送到 origin -> 创建 PR -> 根据反馈继续修改

## 常见注意事项

- 每个 PR 尽量只做一类事情，方便审查。
- 提交前先看 git diff，避免把无关文件一起提交。
- 如果你长期协作，记得定期同步 upstream，减少冲突。

## 示例流程

下面是一套最常见的完整操作示例：

	git clone https://github.com/你的账号/仓库名.git
	cd 仓库名
	git remote add upstream https://github.com/bucky1119/AI-Knowledge-Base.git
	git checkout -b feature/update-docs
	# 编辑文件
	git status
	git add .
	git commit -m "docs: improve collaboration guide"
	git push -u origin feature/update-docs

然后到 GitHub 页面创建 Pull Request 即可。

