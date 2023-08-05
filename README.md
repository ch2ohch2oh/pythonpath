# PYTHONPATH

Python will search `PYTHONPATH` for imports.


Without custom `PYTHONPATH`

    $ ./custom_python_path.py

The output

    ['/home/dazhi/python-env-vars', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
    PYTHONPATH ==> None
    PYTHONHOME ==> None
    Traceback (most recent call last):
    File "./custom_python_path.py", line 14, in <module>
        import whereisdis
    ModuleNotFoundError: No module named 'whereisdis'

With custom `PYTHONPATH`

    $ PYTHONPATH=mylibs ./custom_python_path.py

The output is

    ['/home/dazhi/python-env-vars', '/home/dazhi/python-env-vars/mylibs', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
    PYTHONPATH ==> mylibs
    PYTHONHOME ==> None
    You found me!