"""
Pycthoant (Python + Cat) 🐱
==========================================
  1. 所有命令的输出自动加 喵~
  2. 报错信息猫猫化
"""
import sys
import builtins

if getattr(builtins, "_PYCTHOANT_LOADED", False):
    raise ImportError("Pycthoant already loaded")
builtins._PYCTHOANT_LOADED = True


def _wrap_stream(stream):
    original_write = stream.write

    def new_write(text, *args, **kwargs):
        if isinstance(text, str) and text and not text.endswith("喵~"):
            has_nl = text.endswith("\n")
            if has_nl:
                text = text[:-1]
            lines = text.split("\n")
            lines = [line + " 喵~" if line else line for line in lines]
            text = "\n".join(lines)
            if has_nl:
                text += "\n"
        return original_write(text, *args, **kwargs)

    stream.write = new_write
    return stream


sys.stdout = _wrap_stream(sys.stdout)
sys.stderr = _wrap_stream(sys.stderr)


def _meow_excepthook(exc_type, exc_value, tb):
    import traceback as _tb
    lines = _tb.format_exception(exc_type, exc_value, tb)
    sys.stderr.write("".join(lines))
    sys.stderr.write("(\u2032\u0434\uff40) 喵~ 有 bug 哦！\n")

sys.excepthook = _meow_excepthook
