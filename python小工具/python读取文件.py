def read_csv_to_dict(filePath = ""):
    """
    读取csv文件内容到字典dict，其中第一行是key，剩下的每一行是每一条记录，返回值是一个列表，列表内的每一条数据是字典
    :param filePath:
    :return:
    """
    result = []  # 函数返回值
    if filePath == "":  # 判断文件地址是否存在，如果不存在，那么赋值文件地址，用来直接运行，
        filePath = "文件地址"
    if not os.path.exists(filePath):  # 用来判断文件存在还是不存在
        print("文件地址不存在")
        return None
    # 打开文件
    with open(filePath, 'r', encoding='utf-8') as f:
        header = f.readline()
        header = header.split(',')
        listLength = len(header)
        line = f.readline().strip()
        while line:
            # 用“,”划分信息
            line = line.split(',')
            dict_data = {}
            for i in range(listLength):
                dict_data[header[i]] = line[i]
            result.append(dict_data)
            # 更新，读取新的一行
            line = f.readline().strip()
    # 返回结果
    return result
