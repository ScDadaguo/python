# from  urllib import request,parse
import codecs
class csv_code(object):
    def OPEN(self,paths,files):
        for file in files:
            print(file)
            path=paths.format(name=file)
            with open(path,'r',encoding='utf-8') as f:
                lines=f.read().split('\n\n')[:]
                yield lines
    def Mrite(self,src):
        with open(src,'wb') as  datacsv:
            datacsv.write(codecs.BOM_UTF8)
    def writelins(self,src,u):
        with open(src,"a",encoding='utf-8') as  f:
            for item  in  u:
                line=item+'\n'
                f.write(line)
    def UTF(self,paths,src,files):
        contents=self.OPEN(paths,files)
        self.Mrite(src)
        for content in contents:
            print(content)
            self.writelins(src,content)

files=['list1','list2']
#D:\py\list2.csv
paths=r'D:\py\{name}.csv'
src=r'D:\py\list3.csv'
a=csv_code()
a.UTF(paths,src,files)