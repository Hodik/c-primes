import json
import os
import sys
import sysconfig

# Get Python include path
python_include = sysconfig.get_path("include")

# Create .vscode directory if it doesn't exist
os.makedirs(".vscode", exist_ok=True)

# Create or update c_cpp_properties.json
config = {
    "configurations": [
        {
            "name": (
                "Mac"
                if sys.platform == "darwin"
                else "Linux" if sys.platform.startswith("linux") else "Win32"
            ),
            "includePath": ["${workspaceFolder}/**", python_include],
            "defines": [],
            "macFrameworkPath": (
                [
                    "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks"
                ]
                if sys.platform == "darwin"
                else []
            ),
            "compilerPath": "/usr/bin/clang" if sys.platform != "win32" else "cl.exe",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": (
                "macos-clang-x64"
                if sys.platform == "darwin"
                else (
                    "linux-gcc-x64"
                    if sys.platform.startswith("linux")
                    else "windows-msvc-x64"
                )
            ),
        }
    ],
    "version": 4,
}

with open(".vscode/c_cpp_properties.json", "w") as f:
    json.dump(config, f, indent=4)

print(
    f"Created .vscode/c_cpp_properties.json with Python include path: {python_include}"
)
