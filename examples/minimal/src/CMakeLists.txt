cmake_minimum_required(VERSION 3.18)
project(minimal)

# Find the Python development files
find_package(Python3 REQUIRED COMPONENTS Development)

# Add the module to compile
Python3_add_library(_add_module MODULE "add_module.c")

# Install the module
install(TARGETS _add_module
        EXCLUDE_FROM_ALL
        COMPONENT python_modules
        DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME})

# Install stubs to get autocomplete and type hints
install(FILES _add_module.pyi
        EXCLUDE_FROM_ALL
        COMPONENT python_modules
        DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME})
