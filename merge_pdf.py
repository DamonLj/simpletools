#!/user/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger, PdfFileReader

import os

def merge_pdf():
    filepath = input("输入文件夹路径：")
    all_files = [os.path.join(filepath, p) for p in os.listdir(filepath)]
    pdf_files = list(filter(lambda f:os.path.splitext(f)[-1] == '.pdf', all_files))  # 筛选出pdf文件

    merge_files = pdf_files  # 合并pdf还是合并所有
    pp_merger = PdfFileMerger()
    merge_num = 0
    for i in range(len(merge_files)):
        try:
            with open(merge_files[i], 'rb') as f:
                # f.write("%%EOF")
                pp_file = PdfFileReader(f)
                pp_merger.merge(merge_num, pp_file)
                pages_num = pp_file.getNumPages()
                merge_num += pages_num
        except Exception:
            print("Failed:%s" % merge_files[i])

    with open(os.path.join(filepath, os.path.basename(filepath) + '.pdf'), 'wb') as f:
        pp_merger.write(f)

if __name__ == "__main__":
    merge_pdf()