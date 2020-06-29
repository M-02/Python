from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from lxml import etree
import matplotlib.pyplot as plt
import numpy as np
import  jieba
import requests
import os
from collections import Counter




def data():
   headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
   }
   url = 'http://www.people.com.cn/'
   res = requests.get(url, headers=headers)
   # str = res.content
   res.encoding = 'gbk'
   str=res.text
   html = etree.HTML(str)
   html_data = html.xpath("//*[@id!='rmw_fuwu']/li/a/text()" )
   print("内容获取成功！\n")
   # print(html)
   path_txt = 'doc/123.txt'
   os.remove(path_txt)  # 删除旧文件
   print("删除旧文件成功！\n")
   for i in html_data:
      replace = i.replace('\n', '').replace(' ', '').replace('人民日报', '').replace('人民网', '').replace('人民', '')
      if replace == '\n' or replace == '' or replace=='人民日报':
         continue
      else:
         print(replace)
         f = open("doc//123.txt", 'a', encoding='utf-8')  #追加模式
         f.write(replace)  # 将字符串写入文件中
         f.close()
   print("\n写入文件成功！\n")

def GetWordCloud():
   print("生成图片中... \n")
   path_txt = 'doc/123.txt'
   path_img = "images/12.jpg"
   f = open(path_txt, 'r',encoding='utf-8').read()
   background_image = np.array(Image.open(path_img))
   # 结巴分词，生成字符串
   #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
   jieba_word = jieba.cut(f, cut_all=False)  # cut_all是分词模式，True是全模式，False是精准模式，默认False
   data = []
   for word in jieba_word:
      data.append(word)
   dataDict = Counter(data)
   with open('doc//词频统计.txt', 'w') as fw:
      for k, v in dataDict.items():
         fw.write("%s,%d\n" % (k, v))
   cut_text = " ".join(jieba.cut(f))
   c = open("doc//分词.txt", 'w',encoding='utf-8')
   c.write(cut_text)  # 将字符串写入文件中
   c.close()

   wordcloud = WordCloud(
       # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
       font_path="C:/Windows/Fonts/DENGB.TTF",
       background_color="white",
       # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
       mask=background_image).generate(cut_text)
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()
   print("保存图片文件...")
   wordcloud.to_file(r"images/wordcloud.png")

if __name__ == '__main__':
   data()
   GetWordCloud()