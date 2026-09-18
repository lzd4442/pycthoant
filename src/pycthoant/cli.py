"""Pycthoant CLI - pycthoant <script.py> 或 pycthoant -c <code>"""
import sys, os, runpy

def main():
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "-c":
        ns = {"__name__": "__main__"}
        exec(compile(args[1], "<cmd>", "exec"), ns)
    elif len(args) >= 1:
        runpy.run_path(args[0], run_name="__main__")
    else:
        import code
        code.interact(banner="🐱 Pycthoant 交互模式 - 输入 exit() 退出")
