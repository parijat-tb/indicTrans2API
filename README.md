# IndicTrans2 Inference Setup

## Prerequisites

### Microsoft Visual C++ Build Tools (Windows Only)
The `IndicTransToolkit` library requires compiling C++ extensions. On Windows, you must have **Microsoft Visual C++ 14.0 or greater** installed.

1.  Download the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2.  Run the installer.
3.  Select the **"Desktop development with C++"** workload.
4.  Ensure **"MSVC v142 - VS 2019 C++ x64/x86 build tools"** (or a later version) and **"Windows 10 SDK"** are selected.
5.  Click **Install**.
6.  Restart your computer if requested.

## Installation

Once the build tools are installed, run:

```bash
pip install -r requirements.txt
```

## Usage

Run the test script to verify the installation:

```bash
python test_inference.py
```
