class CategoryPosition(object):
    @classmethod
    def category_banner_add_button(cls):
        '''
        新增按钮
        :return:
        '''
        return f"//section[@class='my-layout__r']//span[text()='新增']"
    @classmethod
    def category_banner_select_button(cls):
        '''
        查询按钮
        :return:
        '''
        return f"//section[@class='my-form-c']//span[text()='查询']"
    @classmethod
    def category_banner_reset_button(cls):
        '''
        重置按钮
        :return:
        '''
        return f"//section[@class='my-form-c']//span[text()='重置']"
    @classmethod
    def category_banner_query_input_box(cls):
        '''
        类目名称查询输入框
        :return:
        '''
        return f"//section[@class='my-form-c']//input[@placeholder='请输入']"
    @classmethod
    def category_list_id(cls):
        '''
        列表类目ID
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[1]//div"
    @classmethod
    def category_list_logo(cls):
        '''
        列表类目图标
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[2]//img"
    @classmethod
    def category_list_name(cls):
        '''
        列表类目名称
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[3]//div"

    @classmethod
    def category_list_status(cls):
        '''
        列表类目状态
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[4]"

    @classmethod
    def category_list_create_time(cls):
        '''
        列表类目创建时间
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[5]//div[@class='cell']//p[1]"
    @classmethod
    def category_list_update_time(cls):
        '''
        列表类目更新时间
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[5]//div[@class='cell']//p[2]"
    @classmethod
    def category_list_edit_button(self):
        '''
        列表编辑按钮
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[6]//button[1]"
    @classmethod
    def category_list_delete_button(self):
        '''
        列表删除按钮
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[6]//button[2]"

    @classmethod
    def category_edit_name(cls):
        '''
        编辑类目名称
        :return:
        '''
        # return f"//section[@class='my-layout__r']//div[@class='el-input']//input"
        return f"//label[text()='类目名称']/parent::div//input"

    @classmethod
    def category_edit_logo(cls):
        '''
        编辑类目图标
        :return:
        '''
        return f"//div[@class='el-form-item__content']//div[@class='yun-img-loader__in']"
    @classmethod
    def category_edit_status(cls):
        '''
        编辑类目状态
        :return:
        '''
        return f"//div[@class='el-form-item__content']//div[@class='el-switch__inner']"
    def category_edit_status_text(self):
        '''
        编辑品牌状态文案
        :return:
        '''
        return f"//div[@class='el-form-item__content']//div[@class='el-switch__inner']//span[@class='is-text']"


    def category_edit_logo_upload_button(cls):
        '''
        编辑类目图标上传按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][1]//div[@class='el-scrollbar__view']//input[@class='el-upload__input']"
    def category_edit_logo_choose(cls):
        '''
        编辑类目图标选择图片
        :return: 
        '''''
        return f"//div[@class='el-overlay yun-img-loader__pop']//div[@class='el-scrollbar__view']//div[@class='el-image']//img"
    def category_edit_logo_fix_button(cls):
        '''
        编辑类目图标确定按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop']//button[2]"
    def category_edit_logo_cls(cls):
        '''
        编辑类目图标清除
        :return:
        '''
        return f"//div[text()='图标']/parent::div//li"

    @classmethod
    def category_button_edit_add(cls):
        '''
        新增页面新增按钮
        :return:
        '''

        return f"//span[text()='新增']/parent::button"
    def category_button_edit_submit(cls):
        '''
        编辑提交按钮
        :return:
        '''
        return f"//span[text()='提交']/parent::button"
    @classmethod
    def category_button_edit_cancel(cls):
        '''
        编辑取消按钮
        :return:
        '''
        return f"//span[text()='取消']/parent::button"