# 🐱 Pycthoant

> 让所有 Python 输出都加 **喵~**！

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 效果

```bash
$ pycthoant -c "print('hello world')"
hello world 喵~

$ pycthoant -c "raise ValueError('oops')"
(′д｀) 喵~ 有 bug 哦！
```

## Windows 一键版（推荐）

下载 [Releases](https://github.com/lzd4442/pycthoant/releases) 中的 Pycthoant-Windows-Portable.zip，解压即用，**无需安装 Python**：

```bat
pycthoant.bat -c "print('hello')"
pycthoant.bat script.py
```

## 原理

Hook sys.stdout.write + 替换 sys.excepthook，纯 monkey-patch，**不改 Python 源码**。

## 开发版 / Linux/macOS 安装

```bash
git clone https://github.com/lzd4442/pycthoant.git
cd pycthoant
pip install .

pycthoant                    # 交互模式
pycthoant script.py          # 运行脚本
pycthoant -c "print('hi')"  # 一行命令
```

## License

MIT — 随便用，喵~ 🐱
