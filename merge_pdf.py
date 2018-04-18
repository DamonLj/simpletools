#!/user/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger, PdfFileReader

import os

def merge_to_pdf(filepath):
    all_files = [os.path.join(filepath, p) for p in os.listdir(filepath)]
    pdf_files = list(filter(lambda f:os.path.splitext(f)[-1] == '.pdf', all_files))  # 筛选出pdf文件

    merge_files = pdf_files
    pp_merger = PdfFileMerger()
    merge_num = 0
    for i in range(len(merge_files)):
        try:
            with open(merge_files[i], 'rb') as f:
                pp_file = PdfFileReader(f)
                pp_merger.merge(merge_num, pp_file)
                pages_num = pp_file.getNumPages()
                merge_num += pages_num
        except Exception:
            print("Failed:%s" % merge_files[i])

    with open(os.path.join(filepath, os.path.basename(filepath) + '.pdf'), 'wb') as f:
        pp_merger.write(f)

def merge_all_dir(dir_path):
    dir_list = [os.path.join(dir_path, x) for x in os.listdir(dir_path)]
    dir_list = filter(lambda x: os.path.isdir(x), dir_list)
    for d in dir_list:
        merge_to_pdf(filepath=d)


if __name__ == "__main__":
    filepath = input("输入文件夹路径：")
    # merge_all_dir(filepath)
    merge_to_pdf(filepath)
