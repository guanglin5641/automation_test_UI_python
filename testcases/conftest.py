import os
import glob

fixtures_dir = os.path.dirname(__file__)
fixtures_dir = os.path.abspath(os.path.join(fixtures_dir, '..'))
fixtures_dir = os.path.abspath(os.path.join(fixtures_dir, '..'))
fixture_dir = os.path.join(fixtures_dir, "fixture")
project_root = os.path.dirname(fixtures_dir)  # 项目根目录（上一级）
def find_fixtures(directory):
    """递归查找所有 Python 文件（排除 __init__.py）"""
    fixture_modules = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                # 计算相对于 "fixture 目录" 的路径
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(module_path, fixtures_dir))[0]
                module_name = module_name.replace(os.sep, ".")
                if module_name.startswith("fixture"):
                    fixture_modules.append(module_name)

    return fixture_modules

pytest_plugins = find_fixtures(fixture_dir)