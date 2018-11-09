from aip import AipOcr
import configparser


class BaiDuAPI:
    '''调用百度云的API来实现数字的识别
    filePath:
    --------
    是工单信息的ini配置文件全路径
    '''

    def __init__(self, filePath):
        target = configparser.ConfigParser()  # 初始化ConfigParser类
        # r'D:\我的坚果云\Python\Python课件\24点\password.ini'
        target.read(filePath)  # 读取ini文件
        # 读取工单信息
        # target.get第一个参数是section，第二个是键名，返回对应值
        app_id = target.get('工单密码', 'APP_ID')
        api_key = target.get('工单密码', 'API_KEY')
        secret_key = target.get('工单密码', 'SECRET_KEY')

        """ 你的 APPID AK SK """
        APP_ID = app_id
        API_KEY = api_key
        SECRET_KEY = secret_key

        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def picture2Text(self, filePath):
        image = self.get_file_content(filePath)
        """ 调用通用文字识别, 图片参数为本地图片 """
        texts = self.client.basicGeneral(image)
        allTexts = ''
        for words in texts['words_result']:
            allTexts = allTexts + ''.join(words.get('words',''))

        return allTexts

    # """ 读取图片 """

    # @staticmethod
    # def get_file_content(filePath):
    #     with open(filePath, 'rb') as fp:
    #         return fp.read()


    @classmethod
    def get_file_content(cls, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':

    baiduapi = BaiDuAPI(
        r'D:\Windows 7 Documents\Documents\PythonCode\24\password.ini')
    allTexts = baiduapi.picture2Text(
        r'D:\Windows 7 Documents\Documents\PythonCode\24\Snipaste_2018-05-19_22-42-33.png')
    print(allTexts)
