import os
class get_path():

    def get_image_path(image_name):
        """获取图片的绝对路径

        Args:
            image_name: 图片的名称

        Returns:
            图片的绝对路径
        """

        # 获取当前工作目录
        current_working_directory = os.getcwd()

        # 构建图片目录的路径
        # images_directory = os.path.join(current_working_directory, "images")
        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_data_path = os.path.join(parent_directory, "data/image_data")

        # 构建图片的完整路径
        image_path = os.path.join(image_data_path, image_name)
        # 判断图片是否存在
        if os.path.exists(image_path):
            return image_path
        else:
            return ""

if __name__ == '__main__':
    image_path = get_image_path("logo.jpg")
    print(image_path)
