# 🐱 Pycthoant

> 让所有 Python 输出都加 **喵~**！

[![PyPI version](https://img.shields.io/pypi/v/pycthoant.svg)](https://pypi.org/project/pycthoant/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 效果

```bash
$ pycthoant -c "print('hello world')"
hello world 喵~

$ pycthoant -c "raise ValueError('oops')"
(′д｀) 喵~ 有 bug 哦！
```

## 安装

**PyPI 一键安装（推荐）**
```bash
pip install pycthoant
```

**Windows 便携版（无需 Python）**

下载 [Releases](https://github.com/lzd4442/pycthoant/releases) 中的 `Pycthoant-Windows-Portable.zip`，解压即用：
```bat
pycthoant.bat -c "print('hello')"
pycthoant.bat script.py
```

**源码安装**
```bash
git clone https://github.com/lzd4442/pycthoant.git
cd pycthoant
pip install .
```

## 使用

```bash
pycthoant                    # 交互模式
pycthoant script.py          # 运行脚本
pycthoant -c "print('hi')"  # 一行命令
```

## 原理

Hook `sys.stdout.write` + 替换 `sys.excepthook`，纯 monkey-patch，**不改 Python 源码**。

## License

MIT — 随便用，喵~ 🐱
