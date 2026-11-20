import os
import re
import sys
from pathlib import Path

MASTER_DIR = Path(r"C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\vibe-coding04\agents\master")
PDF_PATH = MASTER_DIR / "CivicShield_AI_Preliminary_Report.pdf"
LOG_PATH = MASTER_DIR / "lualatex_3.log"
CHAPTERS_DIR = MASTER_DIR / "chapters"

def check_pdf_pages(pdf_path: Path):
    if not pdf_path.exists():
        return False, 0, "PDF not found"
    data = pdf_path.read_bytes()
    # Count /Type /Page (not /Pages)
    pages = len(re.findall(rb"/Type\s*/Page\b", data))
    # Also try pypdf if available
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        pages = len(reader.pages)
    except Exception:
        pass
    return True, pages, f"Size={pdf_path.stat().st_size} bytes"

def check_log(log_path: Path):
    if not log_path.exists():
        return {"exists": False}
    raw = log_path.read_bytes()
    enc = "utf-16" if raw.startswith((b"\xff\xfe", b"\xfe\xff")) else "utf-8"
    text = raw.decode(enc, errors="replace")
    lines = text.splitlines()
    errors = []
    rmfamily_errors = []
    overfull_hbox = []
    undef_refs = []
    undef_cites = []
    output_pages = None
    for i, line in enumerate(lines, 1):
        if line.startswith("! "):
            ctx = " | ".join(lines[i-1:min(len(lines), i+4)])
            errors.append((i, ctx))
            if "rmfamily" in line or (i < len(lines) and "rmfamily" in lines[i]):
                rmfamily_errors.append((i, ctx))
        if "Overfull \\hbox" in line:
            overfull_hbox.append((i, line.strip()))
        if "Reference `" in line and "undefined" in line:
            undef_refs.append((i, line.strip()))
        if "Citation `" in line and "undefined" in line:
            undef_cites.append((i, line.strip()))
        m = re.search(r"Output written on .*?\((\d+) pages", line)
        if m:
            output_pages = int(m.group(1))
    return {
        "exists": True,
        "output_pages": output_pages,
        "errors": errors,
        "rmfamily_errors": rmfamily_errors,
        "overfull_hbox_count": len(overfull_hbox),
        "overfull_hbox_samples": overfull_hbox[:10],
        "undef_refs": undef_refs,
        "undef_cites": undef_cites,
    }

def check_tex_files(chapters_dir: Path):
    results = {}
    for tex in sorted(chapters_dir.glob("*.tex")):
        content = tex.read_text(encoding="utf-8", errors="replace")
        # Check for \textenglish inside math mode ($...$)
        math_textenglish = re.findall(r"\$[^$]*\\textenglish\{[^}]*\}[^$]*\$", content)
        # Check for figures / tikz
        figs = len(re.findall(r"\\includegraphics", content))
        tikz = len(re.findall(r"\\begin\{tikzpicture\}", content))
        tables = len(re.findall(r"\\begin\{table", content))
        # Check for raw English acronyms not wrapped (heuristic: 3+ uppercase letters outside commands/math)
        # Simple check for anti-censorship red flags
        results[tex.name] = {
            "lines": len(content.splitlines()),
            "math_textenglish": math_textenglish,
            "includegraphics": figs,
            "tikzpicture": tikz,
            "tables": tables,
        }
    return results

def main():
    exists, pages, info = check_pdf_pages(PDF_PATH)
    print(f"PDF_EXISTS: {exists} | PAGES_EST: {pages} | {info}")
    log = check_log(LOG_PATH)
    print(f"LOG_EXISTS: {log.get('exists')} | LOG_OUTPUT_PAGES: {log.get('output_pages')}")
    print(f"LATEX_ERRORS_COUNT: {len(log.get('errors', []))}")
    for ln, ctx in log.get("errors", []):
        print(f"  ERR line {ln}: {ctx[:220]}")
    print(f"RMFAMILY_MATH_ERRORS_COUNT: {len(log.get('rmfamily_errors', []))}")
    print(f"OVERFULL_HBOX_COUNT: {log.get('overfull_hbox_count')}")
    for ln, line in log.get("overfull_hbox_samples", [])[:5]:
        print(f"  OVERFULL line {ln}: {line}")
    print(f"UNDEF_REFS: {len(log.get('undef_refs', []))} | UNDEF_CITES: {len(log.get('undef_cites', []))}")
    tex_stats = check_tex_files(CHAPTERS_DIR)
    print("CHAPTER_STATS:")
    for name, st in tex_stats.items():
        print(f"  {name}: lines={st['lines']} figs={st['includegraphics']} tikz={st['tikzpicture']} tables={st['tables']} math_textenglish={len(st['math_textenglish'])}")
        for m in st["math_textenglish"]:
            print(f"    MATH_TEXTENGLISH: {m}")

if __name__ == "__main__":
    main()
