# 随机组会报告顺序
import random
if __name__ == '__main__':

    nameList = ['朱素佳', '张歌斐', '常宝峰', '王云超', '汤井威',
                '夏旺', '江棨', '李童', '潘律翰', '闫高峰', '应圆中',
                '孙子峰', '梁盼', '彭德玲', '陈佳辉', '叶丹薇']

    while len(nameList) > 0:
        length = len(nameList)
        index = random.randint(0, length-1)
        print(nameList[index])
        del nameList[index]