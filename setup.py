from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes = ["sys", "PyQt5", "itertools", "random"], include_files = ["gui.ui", "JaUem/", "MoUem/", "norm_sep_words.txt", "sep_words.txt", "words.txt"])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('Main.py', base=base)
]
setup(
    name='Korean Jumble',
    version = '1.0',
    description = 'A PyQt Word Game',
    options = dict(build_exe = buildOptions),
    executables = executables
)