import shutil
import nox
import os

@nox.session
def example_projects(session: nox.Session):
    session.install("-U", "pip", "build", "pytest")
    dist_dir = os.getenv('PY_BUILD_CMAKE_WHEEL_DIR')
    if dist_dir is None:
        session.run("python", "-m", "build", ".")
        dist_dir = "dist"
    session.env["PIP_FIND_LINKS"] = os.path.abspath(dist_dir)
    session.install("py-build-cmake~=0.0.11a0")
    with session.chdir("examples/minimal"):
        session.install("mypy")
        shutil.rmtree('.py-build-cmake_cache', ignore_errors=True)
        session.run("python", "-m", "build", ".")
        session.install(".")
        session.run("pytest")
    with session.chdir("examples/pybind11-project"):
        session.install("pybind11", "pybind11_stubgen", "mypy")
        shutil.rmtree('.py-build-cmake_cache', ignore_errors=True)
        session.run("python", "-m", "build", ".")
        session.install(".")
        session.run("pytest")
    with session.chdir("examples/minimal-program"):
        shutil.rmtree('.py-build-cmake_cache', ignore_errors=True)
        session.run("python", "-m", "build", ".")
        session.install(".")
        session.run("pytest")


@nox.session
def tests(session: nox.Session):
    session.install("-U", "pip", "pytest")
    dist_dir = os.getenv('PY_BUILD_CMAKE_WHEEL_DIR')
    if dist_dir:
        session.env["PIP_FIND_LINKS"] = os.path.abspath(dist_dir)
        session.install("py-build-cmake~=0.0.11a0")
    else:
        session.install(".")
    session.run('pytest')
