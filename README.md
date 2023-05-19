# cloud-conference-2023
The repository supports a talk on How to improve your architecture review with pull-request, presented on Cloud Conference Day 2023


# Requisities
- Install the diagrams as code tool (Diagrams) - [https://diagrams.mingrammer.com/docs/getting-started/installation](https://diagrams.mingrammer.com/docs/getting-started/installation)



# Possible problems

I'm using Windows 11 and after try to install diagrams using the command `pip install diagrams` I received the following problem:
 
 ``` bash
 python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [15 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-311
      creating build\lib.win-amd64-cpython-311\typed_ast
      copying typed_ast\ast27.py -> build\lib.win-amd64-cpython-311\typed_ast
      copying typed_ast\ast3.py -> build\lib.win-amd64-cpython-311\typed_ast
      copying typed_ast\conversions.py -> build\lib.win-amd64-cpython-311\typed_ast
      copying typed_ast\__init__.py -> build\lib.win-amd64-cpython-311\typed_ast
      creating build\lib.win-amd64-cpython-311\typed_ast\tests
      copying ast3\tests\test_basics.py -> build\lib.win-amd64-cpython-311\typed_ast\tests
      running build_ext
      building '_ast27' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for typed-ast
  Running setup.py clean for typed-ast
Failed to build typed-ast
ERROR: Could not build wheels for typed-ast, which is required to install pyproject.toml-based projects
 ```

I've tryed different usnsucessfull approaches and after a couple of tests, I found two solutions:

- Modify Visual Studio installation and add the option `Desktop development with C++`. After the installation, the command `pip install diagrams` works fine.
- Install a Windows Subsystem Linux
  - This is a workaround and works fine. You just neet to install the linux subsystem `wsl --install -d Ubuntu-22.04`
  - On the subsystem terminal, you must install python, graphviz and install diagrams using pip
