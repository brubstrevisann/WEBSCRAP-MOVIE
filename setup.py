from cx_Freeze import setup, Executable

base = None    

executables = [Executable("webscrap.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "BrubsScraps",
    options = options,
    version = "1.0.0",
    description = 'First webscrap',
    executables = executables
)