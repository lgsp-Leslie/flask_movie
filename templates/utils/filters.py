import os
import uuid
from datetime import datetime


# 修改上传文件名称
def change_filename(filename):
    file_info = os.path.splitext(filename)
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + file_info[-1]
    return filename
