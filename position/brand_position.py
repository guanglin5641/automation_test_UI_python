class BrandPosition(object):
    @classmethod
    def brand_banner_add_button(cls):
        '''
        新增按钮
        :return:
        '''
        return f"//section[@class='my-form-c']//span[text()='新增']"
    @classmethod
    def brand_banner_select_button(cls):
        '''
        查询按钮
        :return:
        '''
        return f"//section[@class='my-form-c']//span[text()='查询']"
    @classmethod
    def brand_banner_reset_button(cls):
        '''
        重置按钮
        :return:
        '''
        return f"//section[@class='my-form-c']//span[text()='重置']"
    @classmethod
    def brand_banner_query_input_box(cls):
        '''
        品牌查询输入框
        :return:
        '''
        return f"//section[@class='my-form-c']//input[@placeholder='请输入']"
    @classmethod
    def brand_list_id(cls):
        '''
        列表品牌ID
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[1]"
    @classmethod
    def brand_list_name(cls):
        '''
        列表品牌名称
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[2]//p[@class='font-bold']"
    @classmethod
    def brand_list_logo(cls):
        '''
        列表品牌logo
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[2]//img"
    @classmethod
    def brand_list_main_img(cls):
        '''
        列表品牌主图
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[3]//div[@class='cell']"
    @classmethod
    def brand_list_affiliated_company(cls):
        '''
        列表品牌所属公司
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[4]//div[@class='cell']"
    @classmethod
    def brand_list_main_categories(cls):
        '''
        列表品牌主营类目
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[5]//div[@class='cell']"
    @classmethod
    def brand_list_time(cls):
        '''
        列表品牌创建时间
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[6]//div[@class='cell']"
    @classmethod
    def brand_list_sort(cls):
        '''
        列表品牌排序
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[7]//div[@class='cell']"
    @classmethod
    def brand_list_edit_button(self):
        '''
        列表编辑按钮
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[8]//button[1]"
    @classmethod
    def brand_list_delete_button(self):
        '''
        列表删除按钮
        :return:
        '''
        return f"//tr[@class='el-table__row'][1]//td[8]//button[2]"

    @classmethod
    def brand_edit_name(cls):
        '''
        编辑品牌名称
        :return:
        '''
        return f"//label[text()='品牌名称']/parent::div//input"
    @classmethod
    def brand_edit_status(cls):
        '''
        编辑品牌状态
        :return:
        '''
        return f"//label[text()='状态']/parent::div//div[@class='el-switch__inner']"
    def brand_edit_status_text(self):
        '''
        编辑品牌状态文案
        :return:
        '''
        return f"//label[text()='状态']/parent::div//span[@class='is-text']"
    @classmethod
    def brand_edit_logo(cls):
        '''
        编辑品牌logo
        :return:
        '''
        return f"//div[text()='logo']/parent::div//div[@class='yun-img-loader__in']"

    def brand_edit_logo_upload_button(self):
        '''
        编辑品牌logo上传按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][1]//div[@class='el-scrollbar__view']//input[@class='el-upload__input']"
    def brand_edit_logo_choose(self):
        '''
        编辑品牌logo选择图片
        :return: 
        '''''
        return f"//div[@class='el-overlay yun-img-loader__pop'][1]//div[@class='el-scrollbar__view'][1]//div[@class='el-image']//img"
    def brand_edit_logo_fix_button(self):
        '''
        编辑品牌logo确定按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][1]//span[text()='确定']/parent::button"
    def brand_edit_logo_cls(self):
        '''
        编辑logo清除
        :return:
        '''
        return f"//div[text()='logo']/parent::div//li"
    @classmethod
    def brand_edit_main_img(cls):
        '''
        编辑品牌主图
        :return:
        '''
        return f"//div[text()='主图']/parent::div//div[@class='yun-img-loader__in']"
    def brand_edit_main_img_upload_button(self):
        '''
        编辑品牌主图上传按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][2]//div[@class='el-scrollbar__view']//input[@class='el-upload__input']"
    def brand_edit_main_img_choose(self):
        '''
        编辑品牌主图选择图片
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][2]//div[@class='el-scrollbar__view'][1]//div[@class='el-image']//img"
    def brand_edit_main_img_fix_button(self):
        '''
        编辑品牌主图确定按钮
        :return:
        '''
        return f"//div[@class='el-overlay yun-img-loader__pop'][2]//span[text()='确定']/parent::button"
    def brand_edit_main_img_cls(self):
        '''
        编辑logo清除
        :return:
        '''
        return f"//div[text()='主图']/parent::div//li"
    @classmethod
    def brand_edit_main_categories(cls):
        '''
        编辑品牌主营类目
        :return:
        '''
        return f"//label[text()='主营类目']/parent::div//div[@class='el-dropdown w-full']"
    @classmethod
    def brand_edit_main_categories_select_box_one_click(cls):
        '''
        编辑品牌主营类目选择框
        :return:
        '''
        return f"//div[@class='el-scrollbar__view el-dropdown__list']//p[text()='一级类目']/parent::section//li[1]//span[@class='el-tag el-tag--small el-tag--light']"
    @classmethod
    def brand_edit_alias(cls):
        '''
        编辑品牌别名
        :return:
        '''
        return f"//label[text()='别名']/parent::div//input"
    @classmethod
    def brand_edit_english_name(cls):
        '''
        编辑品牌英文名称
        :return:
        '''
        return f"//label[text()='英文名']/parent::div//input"
    @classmethod
    def brand_edit_consumer_group(cls):
        '''
        消费群体
        :return:
        '''
        # return f"//label[text()='消费群体']/parent::div//input"
        return f"/html/body/div[1]/div[1]/section/main/div[2]/form/div[8]/div/div/div/input"
    @classmethod
    def brand_edit_brand_positioning(cls):
        '''
        编辑品牌定位
        :return:
        '''
        return f"//label[text()='品牌定位']/parent::div//input"
    @classmethod
    def brand_edit_sort(cls):
        '''
        编辑品牌排序
        :return:
        '''
        return f"//label[text()='排序']/parent::div//input"
    @classmethod
    def brand_edit_establishment_time(cls):
        '''
        编辑创立时间
        :return:
        '''
        return f"//label[text()='创立时间']/parent::div//input"
    @classmethod
    def brand_edit_origin(cls):
        '''
        编辑品牌发源地
        :return:
        '''
        return f"//label[text()='发源地']/parent::div//input"
    @classmethod
    def brand_edit_affiliated_company(cls):
        '''
        编辑品牌所属公司
        :return:
        '''
        return f"//label[text()='所属公司']/parent::div//input"
    @classmethod
    def brand_edit_remark(cls):
        '''
        编辑备注
        :return:
        '''
        return f"//label[text()='备注']/parent::div//div//textarea"
    @classmethod
    def brand_button_edit_add(cls):
        '''
        编辑新增按钮
        :return:
        '''

        return f"//span[text()='新增']/parent::button"
    def brand_button_edit_submit(cls):
        '''
        编辑提交按钮
        :return:
        '''
        return f"//span[text()='提交']/parent::button"
    @classmethod
    def brand_button_edit_cancel(cls):
        '''
        编辑品牌取消按钮
        :return:
        '''
        return f"//span[text()='取消']/parent::button"