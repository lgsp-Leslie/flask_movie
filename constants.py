from enum import Enum


class UserStatus(Enum):
    """ 用户状态 """
    # 启用，可以登录系统
    USER_ACTIVE = '启用'
    # 禁用，不能登录系统
    USER_IN_ACTIVE = '禁用'


# 允许上传图片的类型
UPLOAD_IMAGE_TYPE = (
    'jpg', 'jpeg', 'png'
)

# 允许上传电影的类型
UPLOAD_MOVIE_TYPE = (
    'avi', 'mp4'
)
