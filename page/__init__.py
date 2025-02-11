import pkgutil
import importlib
import os

# 获取当前 `web_page` 目录路径
package_dir = os.path.dirname(__file__)

# 这个列表存储所有可用的类
__all__ = []

# 遍历 `web_page` 目录下的所有子模块
for _ , module_name , _ in pkgutil.walk_packages([package_dir] , prefix="page.") :
	if "__pycache__" in module_name :
		continue  # 跳过 `__pycache__`
	
	try :
		module = importlib.import_module(module_name)  # 动态导入模块
		for attr in dir(module) :
			if not attr.startswith("_") :  # 过滤掉内部变量
				obj = getattr(module , attr)
				if isinstance(obj , type) :  # 确保是类
					globals()[attr] = obj  # 赋值到全局作用域
					__all__.append(attr)  # 加入 `__all__` 让 `import *` 可用'
					print(f"导入模块 {module_name} 成功")
		
	except Exception as e :
		print(f"导入模块 {module_name} 失败: {e}")  # 调试时用，正式环境可删除
