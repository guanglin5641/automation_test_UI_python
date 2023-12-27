import time
from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from position.brand_position import BrandPosition
from common.route import BRAND_LIST, BRAND_SAVE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json

class BrandPositionPage(BasePage, BrandPosition):
    def __init__(self, driver, path=BRAND_LIST):
        super().__init__(driver, path)
    def get_brand_list_text(self):
        '''
        获取列表页的文本内容
        :return: 包含列表页各元素文本信息的字典
        '''
        brand_list_id = self.find_element(position_expression=self.brand_list_id()).text
        brand_list_name = self.find_element(position_expression=self.brand_list_name()).text
        brand_list_logo = self.find_element(position_expression=self.brand_list_logo()).get_attribute('src')
        brand_list_main_img = self.find_element(position_expression=self.brand_list_main_img())
        img_tags = brand_list_main_img.find_elements(By.TAG_NAME, 'img')
        if img_tags:
            # 如果存在图片，返回图片的 src 属性
            brand_list_main_imgs = img_tags[0].get_attribute('src')
        else:
            # 否则返回元素内部的文本内容
            brand_list_main_imgs = brand_list_main_img.text
        brand_list_affiliated_company = self.find_element(position_expression=self.brand_list_affiliated_company()).text
        brand_list_main_categories = self.find_element(position_expression=self.brand_list_main_categories()).text
        brand_list_time = self.find_element(position_expression=self.brand_list_time()).text
        brand_list_sort = self.find_element(position_expression=self.brand_list_sort()).text


        return brand_list_id,brand_list_name,brand_list_logo,brand_list_main_imgs,brand_list_affiliated_company,brand_list_main_categories,brand_list_time,brand_list_sort
    def click_add_brand(self):
        '''
        列表页点击之后跳转到新增页面
        :return:
        '''
        self.find_element(position_expression=self.brand_banner_add_button()).click()
    def enter_brand_name(self, brand_name):
        '''
        输入品牌名称
        :param brand_name:
        :return:
        '''
        if not brand_name:
            return
        self.find_element(position_expression=self.brand_edit_name()).send_keys(brand_name)
    def enter_brand_status(self, brand_status):
        '''
        输入品牌状态
        :param brand_status:
        :return:
        '''
        if not brand_status:
            return

        self.find_element(position_expression=self.brand_edit_status()).click()
    def enter_brand_logo(self, brand_logo):
        '''
        输入品牌logo
        :param brand_logo:
        :return:
        '''
        if not brand_logo:
            return
        self.find_element(position_expression=self.brand_edit_logo()).click()
        self.find_element(position_expression=self.brand_edit_logo_upload_button()).send_keys(brand_logo)
        self.find_element(position_expression=self.brand_edit_logo_choose()).click()
        logo_link = self.find_element(position_expression=self.brand_edit_logo_choose()).get_attribute('src')
        self.find_element(position_expression=self.brand_edit_logo_fix_button()).click()
        return logo_link
    def enter_brand_main_img(self, brand_main_img):
        '''
        输入品牌主图
        :param brand_main_img:
        :return:
        '''
        if not brand_main_img:
            return
        self.find_element(position_expression=self.brand_edit_main_img()).click()
        self.find_element(position_expression=self.brand_edit_main_img_upload_button()).send_keys(brand_main_img)
        time.sleep(1)
        self.find_element(position_expression=self.brand_edit_main_img_choose()).click()
        main_img_link=self.find_element(position_expression=self.brand_edit_main_img_choose()).get_attribute('src')
        self.find_element(position_expression=self.brand_edit_main_img_fix_button()).click()
        time.sleep(1)
        return main_img_link
    def enter_brand_main_categories(self,main_categories):
        '''
        输入品牌主分类
        :param main_categories:
        :return:
        '''
        if not main_categories:
            return
        self.find_element(position_expression=self.brand_edit_main_categories()).click()

    def enter_brand_alias(self,alias):
        '''
        输入品牌别名
        :param alias:
        :return:
        '''
        if not alias:
            return
        self.find_element(position_expression=self.brand_edit_alias()).send_keys(alias)
    def enter_brand_english_name(self,english_name):
        '''
        输入品牌英文名
        :param english_name:
        :return:
        '''
        if not english_name:
            return
        self.find_element(position_expression=self.brand_edit_english_name()).send_keys(english_name)
    def enter_brand_consumer_group(self,consumer_group):
        '''
        输入品牌消费组
        :param consumer_group:
        :return:
        '''
        if not consumer_group:
            return
        self.find_element(position_expression=self.brand_edit_consumer_group()).send_keys(consumer_group)
    def enter_brand_brand_positioning(self,brand_positioning):
        '''
        输入品牌位置
        :param brand_positioning:
        :return:
        '''
        if not brand_positioning:
            return
        self.find_element(position_expression=self.brand_edit_brand_positioning()).send_keys(brand_positioning)
    def enter_brand_sort(self,sort):
        '''
        输入品牌排序
        :param sort:
        :return:
        '''
        if not sort:
            return
        self.find_element(position_expression=self.brand_edit_sort()).send_keys(sort)
    def enter_brand_establishment_time(self,establishment_time):
        '''
        输入品牌成立时间
        :param establishment_time:
        :return:
        '''
        if not establishment_time:
            return
        self.find_element(position_expression=self.brand_edit_establishment_time()).send_keys(establishment_time)
    def enter_brand_origin(self,origin):
        '''
        输入品牌来源
        :param origin:
        :return:
        '''
        if not origin:
            return
        self.find_element(position_expression=self.brand_edit_origin()).send_keys(origin)
    def enter_brand_affiliated_company(self,affiliated_company):
        '''
        输入品牌所属公司
        :param affiliated_company:
        :return:
        '''
        if not affiliated_company:
            return
        self.find_element(position_expression=self.brand_edit_affiliated_company()).send_keys(affiliated_company)
    def enter_brand_remark(self,remark):
        '''
        输入品牌备注
        :param remark:
        :return:
        '''
        if not remark:
            return
        self.find_element(position_expression=self.brand_edit_remark()).send_keys(remark)
    def click_brand_save_button(self):
        '''
        新增页面点击保存按钮
        :return:
        '''
        elm = self.find_element(position_expression=self.brand_button_edit_add())
        self.driver.execute_script("arguments[0].click();", elm)
        wait = WebDriverWait(self.driver, 5)
        ret = wait.until(
            # 任何一个满足条件
            EC.any_of(
                EC.url_changes(self.get_url(BRAND_SAVE)),
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='el-form-item__error']")
                ),
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[@class='el-message__content']")

                ),
            )
        )
        if isinstance(ret, bool):
            # 添加你的额外判断条件
            # return "创建成功"
            # result = self.is_page_in_expected_state(data)  # 自定义的判断函数
            # if result == "符合预期":
            #     return "创建成功"
            # else:
            #     return f"页面状态不符合预期: {result}"
            return "创建成功"
        else:
            return ret.text
    def click_brand_cancel_button(self):
        '''
        新增页面点击取消按钮
        :return:
        '''
        self.find_element(position_expression=self.click_brand_cancel_button()).click()
    def brand_is_page_in_expected_state(self,data):
        try:
            list = self.get_brand_list_text()
            failed_assertions = []

            if 'name' in data and data['name']:
                if data['name'] != list[0]:
                    failed_assertions.append(
                        f"查找 'name' 不存在. 预期: {data['name']}, 实际: {list[0]}")
            if 'type' in data and data['type']:
                if data['type'] != list[1]:
                    failed_assertions.append(
                        f" 'super_type' 不存在. 预期: {data['super_type']}, 实际: {list[1]}")
            if 'resource_type' in data and data['resource_type']:
                if data['resource_type'] != list[2]:
                    failed_assertions.append(
                        f"查找 'resource_type' 不存在. 预期: {data['resource_type']}, 实际: {list[2]}")
            if 'balance_warning' in data and data['balance_warning'] :
                balance_warning = re.search(r'\d+', list[6]).group()
                if data['balance_warning'] != balance_warning:
                    failed_assertions.append(
                        f"查找 'balance_warning' 不存在. 预期: {data['balance_warning']}, 实际: {list[6]}")
            if 'company' in data[0]['company_info']['company'] and data['company_info']['company']:
                company = re.search(r'公司：(.*)', list[3]).group(1)
                if data['company_info']['company'] != company:
                    failed_assertions.append(
                        f"查找 'contact_company' 不存在. 预期: {data['company_info']['company']}, 实际: {list[3]}")
            if 'contact_content' in data[0]['company_info']['contact_content'] and data['company_info']['contact_content']:
                contact_content = re.search(r'联系方式：(.*)', list[4]).group(1)
                if data['company_info']['contact_content'] != contact_content:
                    failed_assertions.append(
                        f"查找 'contact_information' 不存在. 预期: {data['company_info']['contact_content']}, 实际: {list[4]}")
            if 'status' in data and data['status'] != None:
                if data['status'] != list[5]:
                    failed_assertions.append(
                        f"查找 'state' 不存在. 预期: {data['state']}, 实际: {list[5]}")
            if 'remark' in data and data['remark'] != None:
                if data['remark'] != list[8]:
                    failed_assertions.append(
                        f"查找 'remark' 不存在. 预期: {data['remark']}, 实际: {list[8]}")
            if failed_assertions:
                return "\n".join(failed_assertions)
            else:
                return "符合预期"
        except AssertionError as e:
            return str(e)

if __name__ == '__main__':
    a = ["a","b","c","d"]
    b = [['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'] ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS'], ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS']]
    c = ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈', '居家日用', '实物1', '加速器', '移动话费', '松鼠悦读', '好利来', '三只松鼠', '肯德基', '酷狗', '腾讯', '人人视频', 'pptv', '咪咕', '爱奇艺', '乐视', '优酷', '华为视频', '迅雷', '小米', '腾讯', '搜狐', '南瓜', '芒果', '埋堆堆', '欢喜首映', '多多视频', '1905电影网', '迅游', '腾讯', '包图网', '咪咕', '哔哩哔哩', '酷狗', '七猫', '元气桌面', '黄油相机', '移动云盘', '月如绘本馆', 'sure', '懒人听书', '蜻蜓FM', '万兴', '知乎', 'WPS', '掌阅', '喜马拉雅FM', '新浪', '小度', '360安全云盘', '网易云', '腾讯', '扫描全能王', '书旗小说', '启信宝', '陌陌', '懒人畅听', '夸克', '樊登', '酷我', '百度', 'UC网盘', '百果园', '幸福西饼', '超级AI人工智能', '必胜客', '麦当劳', '万达', '中国石化', '瑞幸', '小电', '叮咚买菜', '锦江国际', '货拉拉', '花小猪', 'DQ', '悦途出行', '周黑鸭', '星巴克', '永辉', '沃尔玛', '携程', '亚朵', '苏宁易购', '瑞尔', '朴朴超市', '仟吉', '奈雪的茶', '猫眼电影', '肯德基', '京东', '哈啰', '盒马鲜生', '高德打车', '饿了么', '呷哺呷哺', '曹操专车', '滴滴', '曹操出行', '阿里', 'LITTA乐刻健身', 'Keep', 'e袋洗', '电信话费', '联通话费', '曹操出行', '麦当劳', '美团', '酷狗', '移动话费', '凯叔讲故事', 'WPS', '知乎', '优酷', '百度', '星巴克', '迅雷', '南瓜', '欢喜首映', '爱奇艺', '网易云', '腾讯', '陌陌', '酷我', '瑞幸', '每日瑜伽', '猫眼电影', '肯德基', '京东', '滴滴', '百果园', '阿里', 'Keep', 'e袋洗', 'DY', '苹果', '盛趣', '中华网', '多多CP', 'HJZB', '猫耳FM', '奇乐直播', '战火互娱', '晋江', '比心直播', '陌陌', '黄金岛', '以陌语音', '网易', '腾讯', '虎牙直播', '网龙', '喜马拉雅', '迷你世界', '懒人畅听', '来疯直播', '达龙云', '久游', '骏网', '斗鱼直播', 'KS']



    print(dict(zip(a,b)))