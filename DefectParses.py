import os
import re
import shutil
import sys
import time
from itertools import count

import dask.dataframe
import numpy as np
import pandas as pd
import datatable


def resize_img():
    return [1]


def post_process():
    pass


def governance():
    pass


class DefectParse_v18:
    def __init__(self):
        self.dd = dask.dataframe.read_csv(r"D:\Pandas_demo\data.csv")
        '''
        初始化
        
        解析
           对于大文件，先defect解析，分段解析，每次循环，直接后处理和治理，并保存文件。
        
        后处理
            解析出来以后，，这里是否是改造后处理的方法，还是重新写一个？
                        小文件按原来的方法正常进行
                        大文件只处理除了defect以外的文件，
        治理
            治理会用到df的方法
        
        最后处理
            先把final_stage重新写一下，把各个文件分开保存。
            对于defect，如果是小文件，才会保存结果
        '''
        pass

    def defect_getter_for_bigfile(self, defect_list):
        '''
        如果是大文件
        :param defect_list:
        :return:
        '''
        columns = ["A", "B", "C"]
        processed_list = list()
        while (len(defect_list) > 0):
            defect_df_section = pd.DataFrame(defect_list[:100000] if len(defect_list) >= 100000 else defect_list,
                                             columns=columns, )
            defect_list = defect_list[100000:]
            processed_list.append(resize_img())

            dask.dataframe.read_csv()

            # 仅针对defect info进行后处理和治理，每一轮都进行后处理。

            post_process()
            governance()


        # 得到defect_df_section之后，


if __name__ == '__main__':
    '''
    
    
    '''
    # df_xlsx = pd.read_excel(r'D:\Pandas_demo\YmsNormlization\cycle.xlsx')
    # df_xlsx.to_csv(r'D:\Pandas_demo\YmsNormlization\cycle.csv')
    #
    input_path = r'D:\Pandas_demo\YmsNormlization\cycle.csv'
    output_path_df = r'D:\Pandas_demo\YmsNormlization\dfsv.csv'
    output_path_dask = r'D:\Pandas_demo\YmsNormlization\daskcsv.csv'
    output_path_dt = r'D:\Pandas_demo\YmsNormlization\dtcsv.csv'

    if os.path.exists(output_path_df):
        os.remove(output_path_df)
    if os.path.exists(output_path_dask):
        os.remove(output_path_dask)
    if os.path.exists(output_path_dt):
        os.remove(output_path_dt)

    c = count(1)

    with open(input_path) as f:
        defect_list = f.readlines()
    columns = defect_list[0].rstrip("\n").split(",")
    defect_list = [item.rstrip("\n").split(",") for item in defect_list[1:]]
    ######################################################################################################
    print("*" * 20, "  df 分块保存  ", "*" * 20)
    t1 = time.time()
    print("开始保存")
    while (len(defect_list) > 0):
        defect_df_section = pd.DataFrame(defect_list[:100000] if len(defect_list) >= 100000 else defect_list)
        print("开始第{}次保存".format(next(c)),
              " defect_list size: ", sys.getsizeof(defect_list),
              " defect_list size: ", sys.getsizeof(defect_df_section))
        del defect_list[:100000]
        defect_df_section.to_csv(path_or_buf=output_path_df, mode='a')
        del defect_df_section

    del defect_list
    print("df分块耗时：", time.time() - t1)
    #
    # ######################################################################################################
    os.remove(output_path_df)
    with open(input_path) as f:
        defect_list = f.readlines()
    defect_list = [item.rstrip("\n").split(",") for item in defect_list[1:]]

    print("*" * 20, "  df 整体保存  ", "*" * 20)
    defect_df_all = pd.DataFrame(defect_list,columns=columns)
    print("开始保存")
    t1 = time.time()
    defect_df_all.to_csv(path_or_buf=output_path_df)
    print("开始第{}次保存".format(next(c)),
            " defect_list size: ", sys.getsizeof(defect_list),
            " defect_list size: ", sys.getsizeof(defect_df_all))
    print("df time:", time.time() - t1)
    del defect_list
    del defect_df_all

    #
    # ######################################################################################################
    #     with open(input_path) as f:
    #         defect_list = f.readlines()
    #     defect_list = [item.rstrip("\n").split(",") for item in defect_list[1:]]
    #     print("*"*20, "  dask 分块保存  ", "*"*20)
    #     print("开始保存")
    #     t1 = time.time()
    #     while (len(defect_list) > 0):
    #         dask_df_section = dask.dataframe.from_pandas(pd.DataFrame(defect_list[:100000] if len(defect_list) >= 100000 else defect_list),
    #                                                      npartitions =10)
    #         print("开始第{}次保存".format(next(c)),
    #               " defect_list size: ", sys.getsizeof(defect_list),
    #               " dask_df_section size: ", sys.getsizeof(dask_df_section),
    #               " dask_df_section.divisions", dask_df_section.divisions)
    #         defect_list = defect_list[100000:]
    #         dask.dataframe.to_csv(df=dask_df_section, filename=output_path_dask, single_file=True)
    #     defect_list = list()
    #     print("dask time:", time.time()-t1)
    ######################################################################################################

    c = count(1)

    with open(input_path) as f:
        defect_list = f.readlines()
    defect_list = [item.rstrip("\n").split(",") for item in defect_list[1:]]
    print("*" * 20, "  dt 分块保存  ", "*" * 20)
    print("开始保存")
    t1 = time.time()
    while (len(defect_list) > 0):
        defect_list_section = defect_list[:100000] if len(defect_list) >= 100000 else defect_list
        defect_list_section = [[row[i] for row in defect_list_section]
        for i in range(len(defect_list_section[0]))]
        defect_dt_section = datatable.Frame(defect_list_section)
        # defect_dt_section = datatable.Frame(np.transpose(defect_list_section).tolist())
        print("开始第{}次保存".format(next(c)),
              " defect_list size: ", sys.getsizeof(defect_list),
              " defect_dt_section size: ", sys.getsizeof(defect_dt_section))
        # defect_list = defect_list[100000:]
        del defect_list[:100000]
        defect_dt_section.to_csv(output_path_dt, append=True)
        del defect_dt_section
        del defect_list_section
    print("dt time:", time.time() - t1)
