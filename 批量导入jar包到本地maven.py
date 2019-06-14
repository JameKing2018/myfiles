import os

# 批量引入jar包到本地Maven仓库


# 本地存放jar包路径
path='D:/soft/bcjy/svn/ziyuanku/mylib'

# 获取文件列表
files=os.listdir(path)

# 遍历文件列表
for  file in files:
    # 文件名
    filename=file
    # 包名
    jarName=file.replace('-'+file.split('-')[-1],'') 
    # groupId
    groupId='bcjy.tjj'
    # artifactId
    artifactId=jarName
    # cmd命令
    command="mvn install:install-file -Dfile="+path+"/"+filename+" -DgroupId="+groupId+" -DartifactId="+artifactId+" -Dversion=1.0.0 -Dpackaging=jar"

    print(command)
    # 执行命令
    os.system(command)
