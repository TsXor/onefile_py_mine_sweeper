@echo off
python %~dp0res_packer.py > %~dp0msw_ires.py
type %~dp0msw.py >> %~dp0msw_ires.py
