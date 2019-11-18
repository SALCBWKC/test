#!D:\software\python
import tkinter as tk
from tkinter import filedialog
import os


class SphinxUse:
    """how to use sphinx (simple version)
     and some modules are needed: tkinter, os, sys
    """
    def __init__(self):
        """init the class"""
        self.rewrite_dic = {13: 'import os',
                            14: 'import sys',
                            15: "sys.path.insert(0, os.path.abspath('../src'))",
                            33: "extensions = ['sphinx.ext.autodoc',",
                            34: "'sphinx.ext.viewcode']"}

    @staticmethod
    def choose_folder():
        """选择文件夹"""
        # 打开选择文件夹对话框
        root = tk.Tk()
        root.withdraw()
        # 获得选择好的文件夹
        folder_path = filedialog.askdirectory()
        # file_path = filedialog.askopenfilename()  # 获得选择好的文件
        src_path = os.path.join(folder_path, 'src')
        if not os.path.exists(src_path):
            return None, "[choose_folder]: folder 'src' not found at "+folder_path
        file_list = os.listdir(src_path)
        if len(file_list) < 1:
            return None, "[choose_folder]: file not found at "+src_path
        disk = folder_path[0] + ":"
        return disk, folder_path

    @staticmethod
    def quick_start(disk, folder_path):
        """执行sphinx-quickstart"""
        cmd_path = os.path.join(folder_path, "cmd.bat")
        file = open(cmd_path, "a")
        file.write(disk + "\n")
        file.write("cd " + folder_path + "\n")
        file.write("sphinx-quickstart" + "\n")
        file.close()
        os.system(cmd_path)
        os.remove(cmd_path)

    def rewrite_file(self, conf_path):
        """对conf.py进行修改，并将修改结果保存到临时文件"""
        file_name = 'conf.py'
        file_path = os.path.join(conf_path, file_name)
        if not os.path.isfile(file_path):
            print("[rewrite_file]: file not found at ", conf_path)
            return -1
        file = open(file_path, 'r')
        temp_file_path = os.path.join(conf_path, "rewrite_file_temp.py")
        file2 = open(temp_file_path, 'w')
        line_num = 1
        for line in file:
            # print(line)
            if line_num in self.rewrite_dic.keys():
                file2.write(self.rewrite_dic[line_num]+'\n')
            else:
                file2.write(line)
            line_num += 1
        file2.close()
        file.close()
        return 0

    @staticmethod
    def rewrite_conf(conf_path):
        """修改conf.py"""
        conf_name = 'conf.py'
        conf_abs_path = os.path.join(conf_path, conf_name)
        temp_name = 'rewrite_file_temp.py'
        temp_abs_path = os.path.join(conf_path, temp_name)

        temp_file = open(temp_abs_path, 'r')
        conf_file = open(conf_abs_path, 'w')

        for line in temp_file:
            conf_file.write(line)
        conf_file.close()
        temp_file.close()
        os.remove(temp_abs_path)

    @staticmethod
    def make_html(disk, folder_path):
        """执行 sphinx-apidoc -o source src 和 make html"""
        cmd_path = os.path.join(folder_path, "make_html.bat")
        file = open(cmd_path, "a")
        file.write(disk + "\n")
        file.write("cd " + folder_path + "\n")
        file.write("sphinx-apidoc -o source src" + "\n")
        file.write("make html" + "\n")
        file.close()
        os.system(cmd_path)
        os.remove(cmd_path)

    def main(self):
        """run"""
        disk2, folder2 = self.choose_folder()
        if disk2 is None:
            print("Error", folder2)
            return
        self.quick_start(disk2, folder2)
        conf_path = os.path.join(folder2, 'source')
        # 接下来修改conf.py
        self.rewrite_file(conf_path)
        self.rewrite_conf(conf_path)
        # 生成html
        self.make_html(disk2, folder2)


if __name__ == '__main__':
    su = SphinxUse()
    su.main()
