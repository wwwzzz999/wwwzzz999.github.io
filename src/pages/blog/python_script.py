import sys
import re
import os
import shutil

floder_path =""
floder_name =""
def main():
    l = len(sys.argv)
    if l == 2:
        inf = sys.argv[1]
        print(inf)
        floder_name =inf.split('\\')[-1].split('.')[0]
        #生成文件夹地址+
        floder_path ='D:\\Demo\\Blog\\astro-ink\\public\\assets'+floder_name
        if not os.path.exists(floder_path):  # 创建新文件夹
            os.makedirs(floder_path)
        pass
    elif l == 1:
        print('提示：拖入单个文件至.py文件上')
        input('\n按任意键退出...')
    elif l > 2:
        print('提示：只允许拖入单个文件')
        input('\n按任意键退出...')

    
    with open(inf,encoding='utf-8') as f:
        lines = f.read()
        md_png_rude = re.findall("(?:!\[(.*?)\]\((.*?)\))", lines)
    
    md_png_rude = list(md_png_rude)
    for i in md_png_rude:
#         去除网络图片
        s=re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',i[1]) 
        if s == None:
            target_path =floder_path+'\\'+i[1].split("\\")[-1]
            shutil.copyfile(i[1], target_path)    #拷贝图片
#             print(target_path)
            s="\\assets\\"+floder_name+"\\"+i[1].split("\\")[-1]
            lines=lines.replace(i[1],s)

             
    #生成新的.md文件，另存为
    new_md='D:\\Demo\Blog\\astro-ink\\src\\pages\\blog\\'+floder_name+".md"
    with open(new_md, mode="w", encoding="utf-8") as f:
        #         写入md 扩展信息
        intext = "---\nlayout: $/layouts/post.astro\n"
        title = input("输入文章标题:")
        tags = input("输入文章标签 使用空格分隔:")
        tags = tags.split(" ")
        tags_1=""
        for i in tags:
            tags_1+="- "+i+"\n"
        date = input("输入日期 yyyy-mm-dd:")
        description = input("输入文章描述信息:")
        intext = intext +"title: "+title+"\n"+"date: "+ date +"\n"+"description: "+description +"\n"+"tags:\n"+ tags_1+"---"+"\n"
        f.write(intext)


    
        f.write(lines)
        

    input('\n按任意键退出...')


if __name__ == '__main__':

    import traceback
    try:
        main()
    except Exception:
        traceback.print_exc()
        #with open('error.txt', 'w', encoding='utf-8') as f:
        #    traceback.print_exc(file=f)
        input('\n程序运行异常...')
    