"""
Pycthoant 下载器 - 检查 GitHub 最新版本，一键下载并解压
"""
import sys, os, json, ssl, ctypes, zipfile
from urllib.request import urlopen, Request
from urllib.error import URLError
import io

# ── GitHub 信息 ──────────────────────────────────────────────
REPO = "lzd4442/pycthoant"
VERSION_URL = f"https://api.github.com/repos/{REPO}/releases/latest"

# ── 颜色（Windows 兼容）────────────────────────────────────────
try:
    kernel32 = ctypes.windll.kernel32
    STD_OUTPUT_HANDLE = -11
    h = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    def _color(code):
        kernel32.SetConsoleTextAttribute(h, code)
    def GREEN(t):   _color(0x0A); print(t); _color(7)
    def RED(t):     _color(0x0C); print(t); _color(7)
    def YELLOW(t):  _color(0x0E); print(t); _color(7)
except Exception:
    def GREEN(t):   print(t)
    def RED(t):     print(t)
    def YELLOW(t):  print(t)

# ── 进度条 ───────────────────────────────────────────────────
def progressbar(sofar, total, bar=40):
    pct = int(sofar * bar / total) if total else 0
    bar_str = "\u2588" * pct + "\u2591" * (bar - pct)
    sys.stdout.write(f"\r  [{bar_str}] {sofar//1024}/{total//1024} KB    ")
    sys.stdout.flush()

# ── HTTP 请求 ────────────────────────────────────────────────
def fetch_json(url):
    ctx = ssl.create_default_context()
    req = Request(url, headers={"User-Agent": "PycthoantDownloader/1.0"})
    with urlopen(req, context=ctx, timeout=15) as r:
        return json.loads(r.read())

def fetch_bytes(url):
    ctx = ssl.create_default_context()
    req = Request(url, headers={"User-Agent": "PycthoantDownloader/1.0"})
    with urlopen(req, context=ctx, timeout=120) as r:
        total = int(r.headers.get("Content-Length", 0))
        buf, sofar = b"", 0
        while True:
            chunk = r.read(65536)
            if not chunk:
                break
            buf += chunk
            sofar += len(chunk)
            progressbar(sofar, total)
        print()
    return buf

# ── 入口 ─────────────────────────────────────────────────────
def main():
    print()
    print("=" * 50)
    print("   \uD83D\uDC31  Pycthoant 下载器")
    print("=" * 50)

    # 检查最新版本
    download_url = (
        f"https://github.com/{REPO}/releases/download/v1.0.0/"
        "Pycthoant-Windows-Portable.zip"
    )
    try:
        data = fetch_json(VERSION_URL)
        tag  = data.get("tag_name", "")
        ver  = tag.lstrip("v") or "?"
        assets = data.get("assets", [])
        zip_asset = next((a for a in assets if "portable" in a["name"].lower()), None)
        if zip_asset:
            download_url = zip_asset["browser_download_url"]
            size_mb = zip_asset["size"] / 1024 / 1024
            YELLOW(f"\n  最新版本：v{ver}  ({size_mb:.1f} MB)")
        else:
            YELLOW(f"\n  最新版本：v{ver}")
    except Exception as e:
        YELLOW(f"\n  版本检查失败，继续下载 … ({e})")

    script_dir = os.path.dirname(os.path.abspath(__file__)) or "."
    GREEN(f"\n  下载目标：{script_dir}")

    GREEN("\n[1/2] 正在下载 Pycthoant …")
    try:
        data = fetch_bytes(download_url)
    except URLError as e:
        RED(f"\n[错误] 下载失败：{e}")
        input("\n  按回车退出 …")
        sys.exit(1)

    GREEN("[2/2] 正在解压 …")
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            z.extractall(script_dir)
    except Exception as e:
        RED(f"\n[错误] 解压失败：{e}")
        input("\n  按回车退出 …")
        sys.exit(1)

    GREEN("\n\u2705 完成！双击 pycthoant.bat 即可使用\n")
    input("  按回车退出 …")

if __name__ == "__main__":
    main()
