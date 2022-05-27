import os
file_list = os.listdir('object_detection/protos/')
proto_list = [file for file in file_list if '.proto' in file]
print('object_detection/proto文件夹中共有%d个proto文件' %len(proto_list))
for proto in proto_list:
    execute_command = 'D:\\Python\\Projects\\OpenCVProjects\\TensorflowProjects\\objectdectet\\protoc\\bin\\protoc.exe object_detection/protos/%s --python_out=.' %proto
    os.popen(execute_command)
file_list = os.listdir('object_detection/protos/')
py_list = [file for file in file_list if '.py' in file]
print('通过protoc命令产生的py文件共有%d个' %(len(py_list) - 1))