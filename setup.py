from cx_Freeze import setup, Executable

build_exe_options = {"excludes": ["tkinter"]}

setup(
    name="Mini readability",
    version="0.1",
    description="Mini readability",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py")]
)
