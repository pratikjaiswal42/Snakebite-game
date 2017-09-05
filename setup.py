import cx_Freeze

executables = [cx_Freeze.Executable("Snakebite.py")]

cx_Freeze.setup(

    name="Snakebite",
    options={"build_exe":{"packages":["pygame"],

            "include_files":["ratatta.png","snakebite.png","snake.gif","snake_.wav","button.mp3","control.mid","gameloop.mid","iron man.mp3"]}},
    description = "Snakebite",
    executables = executables
    )
