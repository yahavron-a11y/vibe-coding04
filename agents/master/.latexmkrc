# latexmk configuration for CivicShield AI Preliminary Report
# Ensures LuaLaTeX is used and main.pdf is always synced to the project root.
$pdf_mode = 4; # lualatex
$lualatex = 'lualatex -interaction=nonstopmode %O %S';
$success_cmd = 'powershell -NoProfile -Command "Copy-Item -Path main.pdf -Destination ..\..\CivicShield_AI_Preliminary_Report.pdf -Force"';
