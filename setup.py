from cx_Freeze import setup, Executable

# Incluindo arquivos adicionais
includefiles = ['C:\\Users\\HP\\Desktop\\Python\\calculadora\\icon\\icon.ico']

# Configurando a build
executables = [Executable("Calculadora Basica.py", base="Win32GUI", icon="C:\\Users\\HP\\Desktop\\Python\\calculadora\\icon\\icon.ico")]

setup(
    name="CalculadoraBasica.exe",
    version="1.0",
    description="Calculadora desenvolvida por Joel",
    options={
        "build_exe": {
            "packages": ["tkinter"],
            "include_files": includefiles,
        }
    },
    executables=executables
)
