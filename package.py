name = "python"

version = "2.7.11"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

variants = [
    ["platform-linux"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

uuid = "repository.python"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.PYTHON_INCLUDE_DIRS = "{root}/include"
        env.PYTHON_LIBRARIES = "{root}/lib/python2.7/config/libpython2.7.a"
