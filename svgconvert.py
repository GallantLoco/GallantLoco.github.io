import subprocess
from pathlib import Path

def pdf_to_svg_single(input_pdf: str, output_svg: str):
    """
    把单页 PDF 转成一个 SVG。
    需要系统里有 pdf2svg 命令。
    """
    subprocess.run(
        ["pdf2svg", input_pdf, output_svg, "1"],  # 第 1 页
        check=True
    )

pdf_to_svg_single("realexp.pdf", "realexp.svg")
