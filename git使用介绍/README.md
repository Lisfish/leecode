# Git 使用指南

本指南面向当前仓库的日常使用，环境为 **Windows + PowerShell + GitHub**。内容从最常用的提交流程开始，最后附上撤销操作和常见错误排查。

> 仓库目录：`E:\github\leecode`  
> 远程仓库：`https://github.com/Lisfish/leecode.git`  
> 默认分支：`main`

## 目录

- [1. Git 的核心概念](#1-git-的核心概念)
- [2. 开始前的检查](#2-开始前的检查)
- [3. 日常提交的完整流程](#3-日常提交的完整流程)
- [4. 新增文件或文件夹](#4-新增文件或文件夹)
- [5. 看懂 git status](#5-看懂-git-status)
- [6. 查看差异和历史](#6-查看差异和历史)
- [7. 撤销与回退](#7-撤销与回退)
- [8. 与 GitHub 同步](#8-与-github-同步)
- [9. 分支基础](#9-分支基础)
- [10. 提交信息规范](#10-提交信息规范)
- [11. .gitignore 与敏感信息](#11-gitignore-与敏感信息)
- [12. 常见错误排查](#12-常见错误排查)
- [13. 每日操作清单](#13-每日操作清单)
- [14. 常用命令速查](#14-常用命令速查)

## 1. Git 的核心概念

Git 把一次文件修改从本地送到 GitHub，通常要经过四个区域：

```text
工作区（正在编辑的文件）
   │
   │  git add
   ▼
暂存区（准备提交的内容）
   │
   │  git commit
   ▼
本地仓库（本机的提交历史）
   │
   │  git push
   ▼
远程仓库（GitHub）
```

几个关键词：

- **工作区**：你在 VS Code 中看到并编辑的文件。
- **暂存区**：本次准备提交的修改。`git add` 把修改放进去。
- **本地仓库**：`git commit` 后形成的本地历史记录。
- **远程仓库**：GitHub 上的仓库。`git push` 后才会更新。
- **origin**：本仓库给远程地址起的默认名字。
- **main**：当前使用的分支名。

只保存文件不会更新 GitHub。必须依次完成 `add → commit → push`。

## 2. 开始前的检查

### 2.1 进入仓库

```powershell
cd E:\github\leecode
pwd
```

`pwd` 用来确认当前所在目录。Git 的路径是相对于当前目录的：

```powershell
# 在仓库根目录时
git add "基础0-1/1768_initial_code_review.md"

# 已经进入 基础0-1 文件夹时
cd .\基础0-1
git add "1768_initial_code_review.md"
```

不要在 `基础0-1` 里面再写一次 `基础0-1/`，否则 Git 会寻找：

```text
基础0-1\基础0-1\1768_initial_code_review.md
```

### 2.2 检查 Git 和仓库状态

```powershell
git --version
git status
git remote -v
```

正常会看到远程仓库地址：

```text
origin  https://github.com/Lisfish/leecode.git (fetch)
origin  https://github.com/Lisfish/leecode.git (push)
```

### 2.3 首次使用 Git 的身份配置

如果 Git 提示不知道你是谁，执行：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

查看已有配置：

```powershell
git config --global --list
```

### 2.4 中文与换行符显示

PowerShell 中如果中文文件名显示为乱码，可以为当前终端切换到 UTF-8：

```powershell
chcp 65001
```

让 Git 直接显示中文路径，而不是转义字符：

```powershell
git config --global core.quotepath false
```

看到 `LF will be replaced by CRLF` 属于 Windows 换行符提示，一般不会影响文件内容。

## 3. 日常提交的完整流程

假设你刚刚修改了 `基础0-1/1768_initial_code_review.md`。

### 第 1 步：查看状态

```powershell
git status
```

确认哪些文件被修改，以及是否有不想提交的文件。

### 第 2 步：查看具体修改

```powershell
git diff -- "基础0-1/1768_initial_code_review.md"
```

只查看已经暂存的内容：

```powershell
git diff --cached -- "基础0-1/1768_initial_code_review.md"
```

### 第 3 步：加入暂存区

```powershell
git add "基础0-1/1768_initial_code_review.md"
```

多个文件可以一次指定：

```powershell
git add README.md "基础0-1/1768_initial_code_review.md"
```

再次确认：

```powershell
git status
```

文件应该出现在 `Changes to be committed` 下面。

### 第 4 步：创建本地提交

```powershell
git commit -m "docs: update 1768 initial code review"
```

提交后文件才真正进入本地 Git 历史，但还没有上传到 GitHub。

### 第 5 步：推送到 GitHub

```powershell
git push origin main
```

成功后会出现类似：

```text
main -> main
```

### 第 6 步：确认结果

```powershell
git status
```

理想状态：

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## 4. 新增文件或文件夹

### 4.1 新建文件

在 VS Code 中创建并编辑文件后，执行：

```powershell
git status
git add "新文件路径"
git commit -m "docs: add new document"
git push origin main
```

### 4.2 新建空文件夹

Git 不会记录空文件夹。如果暂时没有文件，可以在文件夹中放一个 `.gitkeep`：

```powershell
mkdir "新专题"
New-Item -ItemType File "新专题\.gitkeep"
```

之后有正式文件时，可以删除 `.gitkeep`。

### 4.3 更新 README

新增文件或目录后，建议同步更新根目录 `README.md` 的目录结构，方便在 GitHub 上浏览：

```text
leecode/
├── 基础0-1/
│   ├── 1768_initial_code_review.md
│   └── 1768_merge_strings_alternately.py
└── git使用介绍/
    └── README.md
```

然后一起提交 README 和新文件：

```powershell
git add README.md "新文件路径"
git commit -m "docs: update directory structure"
git push origin main
```

## 5. 看懂 git status

常用短格式：

```powershell
git status --short
```

常见标记：

| 标记 | 含义 |
| :---: | :--- |
| `??` | 新文件，尚未被 Git 跟踪 |
| ` M` | 已跟踪文件被修改，但还没暂存 |
| `M ` | 修改已经暂存，等待提交 |
| `A ` | 新文件已经暂存，等待提交 |
| ` D` | 文件被删除，但删除操作还没暂存 |
| `D ` | 删除操作已经暂存 |
| `MM` | 修改了一部分并暂存，之后又继续修改 |

左侧一列表示暂存区状态，右侧一列表示工作区状态。

## 6. 查看差异和历史

### 6.1 查看差异

```powershell
git diff                  # 工作区 vs 暂存区
git diff --cached         # 暂存区 vs 上一次提交
git diff HEAD             # 工作区 vs 上一次提交
git diff -- <文件路径>     # 只看指定文件
```

### 6.2 查看提交历史

```powershell
git log --oneline -10
git log --oneline --graph --decorate -10
```

查看某次提交的详细内容：

```powershell
git show <提交编号>
```

### 6.3 分页器中的 (END)

执行 `git diff` 或 `git log` 后，如果底部出现 `(END)`，说明内容进入了分页器：

- 按 `q`：退出分页器，回到终端
- 按空格：下一页
- 按 `b`：上一页

不想使用分页器：

```powershell
git --no-pager diff
git --no-pager log --oneline -10
```

## 7. 撤销与回退

> 撤销操作会影响文件或历史。执行前先运行 `git status` 和 `git diff` 确认内容。

### 7.1 取消暂存，但保留文件修改

```powershell
git restore --staged "文件路径"
```

例如把文件从暂存区拿出来，但编辑内容不丢失：

```powershell
git restore --staged "基础0-1/1768_initial_code_review.md"
```

### 7.2 丢弃工作区修改

```powershell
git restore "文件路径"
```

注意：这会丢弃尚未提交的修改，**无法通过 Git 恢复**。确认不需要后再使用。

### 7.3 撤销最近一次本地提交，保留文件修改

适用于刚刚 `commit`，但还没 `push`：

```powershell
git reset --soft HEAD~1
```

提交记录被撤销，修改仍然保留在暂存区，可以重新提交。

### 7.4 修改最近一次提交的说明

如果还没有推送：

```powershell
git commit --amend -m "新的提交说明"
```

如果已经推送到 GitHub，修改历史会造成远程冲突，需要谨慎处理。

### 7.5 撤销已经推送的提交

使用 `git revert` 生成一个反向提交，不删除历史，比较安全：

```powershell
git revert <提交编号>
git push origin main
```

### 7.6 高风险命令

以下命令可能丢失文件或覆盖远程历史，初学阶段不要随意使用：

```powershell
git reset --hard
git clean -fd
git push --force
```

## 8. 与 GitHub 同步

### 8.1 查看远程仓库

```powershell
git remote -v
```

### 8.2 推送本地提交

```powershell
git push origin main
```

第一次推送并绑定上游分支：

```powershell
git push -u origin main
```

之后可以直接：

```powershell
git push
```

### 8.3 拉取远程更新

```powershell
git pull origin main
```

如果 `git status` 显示本地领先远程：

```text
Your branch is ahead of 'origin/main' by 1 commit.
```

说明提交还在本地，执行 `git push` 即可。

### 8.4 推送被拒绝

如果 GitHub 上已有你本地没有的新提交，推送可能被拒绝：

```text
! [rejected] main -> main (fetch first)
```

先把远程提交拉下来，再推送：

```powershell
git pull --rebase origin main
git push origin main
```

发生冲突时先解决冲突文件，再执行：

```powershell
git add <冲突文件>
git rebase --continue
```

不要直接用 `git push --force` 覆盖远程历史。

### 8.5 从 GitHub 克隆仓库

```powershell
cd E:\github
git clone https://github.com/Lisfish/leecode.git
cd .\leecode
```

## 9. 分支基础

单人刷题可以直接在 `main` 上提交；开发较大功能时，建议新建分支。

```powershell
git branch                         # 查看本地分支
git switch -c feature/git-guide    # 新建并切换分支
git add .
git commit -m "docs: add Git guide"
git push -u origin feature/git-guide
```

切换回主分支：

```powershell
git switch main
git pull origin main
```

分支开发完成后，可以在 GitHub 上创建 Pull Request 合并。初学阶段至少理解：

- `main` 是稳定分支。
- 功能分支用于隔离未完成的修改。
- 合并前先同步远程更新。

## 10. 提交信息规范

推荐使用“类型: 简短说明”的格式：

| 类型 | 用途 | 示例 |
| :--- | :--- | :--- |
| `feat` | 新增功能或题目解答 | `feat: add 1768 solution` |
| `fix` | 修复错误 | `fix: correct boundary condition` |
| `docs` | 文档修改 | `docs: add Git usage guide` |
| `refactor` | 重构代码，不改变功能 | `refactor: simplify merge logic` |
| `test` | 添加或修改测试 | `test: add examples for 1768` |
| `chore` | 杂项配置 | `chore: update .gitignore` |

好的提交信息应该：

- 简短说明“做了什么”
- 一次提交只处理一个主题
- 不只写 `update`、`修改` 这类无法判断内容的信息

## 11. .gitignore 与敏感信息

`.gitignore` 用来告诉 Git 不要跟踪某些文件，例如：

```gitignore
__pycache__/
*.pyc
.venv/
.env
.idea/
.vscode/
```

注意：

- `.gitignore` 只对“尚未被 Git 跟踪”的文件生效。
- 如果文件已经被跟踪，需要先取消跟踪：

```powershell
git rm --cached "文件路径"
```

- **不要提交密码、Token、私钥、`.env` 文件。**
- 提交前用 `git status` 和 `git diff` 确认没有敏感内容。

## 12. 常见错误排查

### 12.1 pathspec did not match any files

```text
fatal: pathspec '...' did not match any files
```

原因通常是路径写错，或当前目录和路径发生重复。

```powershell
pwd
ls
cd ..
git status
```

确认当前目录后，再使用正确路径。路径中带中文或空格时，建议加双引号。

### 12.2 中文文件名显示乱码

在 PowerShell 中执行：

```powershell
chcp 65001
```

如果只是 Git 显示为 `\345\237\272...` 的转义形式，可以执行：

```powershell
git config --global core.quotepath false
```

这通常是显示问题，不代表文件损坏。

### 12.3 连接代理失败

如果出现：

```text
Failed to connect to 127.0.0.1 port 7897
```

说明 Git 配置了代理，但代理程序没有启动。可以启动代理，或者只为当前命令临时绕过：

```powershell
git -c http.proxy= -c https.proxy= push origin main
```

查看当前代理配置：

```powershell
git config --global --get http.proxy
git config --global --get https.proxy
```

### 12.4 停在 (END)

按 `q` 退出分页器。下一次可使用：

```powershell
git --no-pager diff
```

### 12.5 nothing to commit

可能原因：

- 文件没有保存。
- 修改没有暂存：先执行 `git add`。
- 已经提交过，但忘记推送：执行 `git push`。
- 当前目录不是你以为的仓库目录：执行 `pwd` 和 `git status` 确认。

### 12.6 not a git repository

```text
fatal: not a git repository
```

当前目录不是 Git 仓库，或者不在仓库内部：

```powershell
cd E:\github\leecode
git status
```

### 12.7 不知道你是谁

```text
Please tell me who you are.
```

配置用户名和邮箱：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 12.8 remote origin already exists

```text
error: remote origin already exists
```

说明已经配置过远程地址。查看：

```powershell
git remote -v
```

如需修改地址：

```powershell
git remote set-url origin https://github.com/Lisfish/leecode.git
```

## 13. 每日操作清单

- [ ] 进入仓库：`cd E:\github\leecode`
- [ ] 查看状态：`git status`
- [ ] 如需同步：`git pull origin main`
- [ ] 编辑文件并保存
- [ ] 查看修改：`git diff`
- [ ] 精确暂存：`git add "文件路径"`
- [ ] 确认暂存：`git status`
- [ ] 创建提交：`git commit -m "类型: 说明"`
- [ ] 推送远程：`git push origin main`
- [ ] 确认状态：`git status`
- [ ] 在 GitHub 页面核对文件

## 14. 常用命令速查

| 操作 | 命令 |
| :--- | :--- |
| 查看当前目录 | `pwd` |
| 查看状态 | `git status` |
| 精简状态 | `git status --short` |
| 查看未暂存差异 | `git diff` |
| 查看已暂存差异 | `git diff --cached` |
| 暂存指定文件 | `git add "文件路径"` |
| 暂存当前目录的全部改动 | `git add .` |
| 暂存整个仓库的全部改动 | `git add -A` |
| 取消暂存 | `git restore --staged "文件路径"` |
| 丢弃工作区修改（危险） | `git restore "文件路径"` |
| 提交 | `git commit -m "说明"` |
| 查看历史 | `git log --oneline -10` |
| 查看某次提交 | `git show <提交编号>` |
| 推送 | `git push origin main` |
| 拉取 | `git pull origin main` |
| 查看远程地址 | `git remote -v` |
| 查看分支 | `git branch` |
| 新建并切换分支 | `git switch -c <分支名>` |
| 切换分支 | `git switch <分支名>` |

> `git add .` 和 `git add -A` 范围较大，使用前一定先运行 `git status` 检查。日常提交优先精确指定文件。

## 参考资料

- [Pro Git 中文版](https://git-scm.com/book/zh/v2)
- [Git 官方文档](https://git-scm.com/docs)
