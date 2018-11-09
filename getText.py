import win32con

import win32clipboard as w


class GetText:
    '''用于把图像识别的内容返回到剪贴板\n
    实现的原理就是传递一个参数给setText()方法\n
    然后用getText()方法将参数复制到剪切板里面
    '''

    @staticmethod
    def getText():
        '''获取剪贴板的内容'''

        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    @classmethod
    def setText(cls, aString):
        '''需要传递一个参数用于复制到剪贴板'''

        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()


if __name__ == '__main__':

    # 会把setText里面的参数复制到剪切板里面
    GetText.setText('666777888')
    GetText.getText()
