# -*- coding: UTF-8 -*-
import os


def load_creator_data(file_name):
    '''读取标注好的医疗语料
        
    把文档中的语料加载为列表格式，并分别返回'''
    lines = []
    with open(file_name, encoding='UTF-8') as f:
        lines = f.readlines()
    
    data_x = []
    data_y = []
    para_x = []
    para_y = []
    for line in lines:
        if line=='\n':
            if para_x and para_y:
                data_x.append(para_x)
                data_y.append(para_y)
                para_x = []
                para_y = []
        else:
            [word, label] = line.split()
            para_x.append(word)
            para_y.append(label)
    
    return [data_x,data_y]


if __name__ == '__main__':
    data_x,data_y = load_creator_data(os.path.join('C:\\Users\\Mr.Yang\\Documents\\GitHub\\ner_creator','creator_med_data'))
    print(len(data_x),len(data_y))