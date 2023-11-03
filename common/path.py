import os
class GetPath():

    def get_image_path(self,image_name):
        """获取图片的绝对路径

        Args:
            image_name: 图片的名称

        Returns:
            图片的绝对路径
        """
        # 构建图片目录的路径
        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_data_path = os.path.join(parent_directory, "data/image_data")

        # 构建图片的完整路径
        image_path = os.path.join(image_data_path, image_name)
        # 判断图片是否存在
        if os.path.exists(image_path):
            return image_path
        else:
            return ""

    def get_case_path(self,case_name):
        """获取用例文件的绝对路径

        Args:
            case_name: 用例文件的名称

        Returns:
            用例文件的绝对路径
        """


        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        case_data_path = os.path.join(parent_directory, "data/case_data")

        # 构建用例的完整路径
        case_path = os.path.join(case_data_path, case_name)
        # 判断用例是否存在
        if os.path.exists(case_path):
            return case_path
        else:
            return ""

if __name__ == '__main__':
    get_path = GetPath()
    print(get_path.get_case_path("brand_case.xlsx"))


