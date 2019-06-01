name = "python"

version = "2.7.15"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**"]
    return [expand_requires(*requires)]

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

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.prepend("{root}/cmake")
