"""Pycthoant Launcher - 让所有输出都加 喵~！"""
import sys, os, site, runpy

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    sp = os.path.join(base, "Lib", "site-packages")
    if sp not in sys.path:
        sys.path.insert(0, sp)
    try:
        site.addsitedir(sp)
    except Exception:
        pass
    import meow
    del meow

    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "-c":
        ns = {"__name__": "__main__"}
        exec(compile(args[1], "<cmd>", "exec"), ns)
    elif len(args) >= 1:
        runpy.run_path(args[0], run_name="__main__")
    else:
        import code
        code.interact(banner="🐱 Pycthoant 交互模式 - 输入 exit() 退出")

if __name__ == "__main__":
    main()
