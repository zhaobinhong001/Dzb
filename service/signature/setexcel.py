# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd


def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print('null')


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='file.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1, nrows):

        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list



def main():
    tables = excel_table_byindex()
    for row in tables:
        name, cardname, cardnum, cardtype = row.split('****')
        # Blog.objects.create(title=title, content=content)
        print(row)

if __name__ == "__main__":
    main()
