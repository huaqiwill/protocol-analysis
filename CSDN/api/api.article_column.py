"""
文章专栏
"""


class Bis:
    articleId: int
    description: str
    editUrl: str
    picList: list
    title: str
    url: str
    collectCount: int
    commentCount: int
    diggCount: int
    formatTime: str
    postTime: str
    viewCount: int
    forcePlan: bool

    def __str__(self) -> str:
        return f"文章ID：{self.articleId} 文章标题：《{self.title}》"
        # return (
        # f"标题: {self.title}\n"
        # f"文章ID: {self.articleId}\n"
        # f"描述: {self.description}\n"
        # f"编辑链接: {self.editUrl}\n"
        # f"图片列表: {self.picList}\n"
        # f"文章链接: {self.url}\n"
        # f"收藏数: {self.collectCount}\n"
        # f"评论数: {self.commentCount}\n"
        # f"点赞数: {self.diggCount}\n"
        # f"发布时间: {self.postTime}\n"
        # f"查看数: {self.viewCount}\n"
        # f"格式化时间: {self.formatTime}"
        # )


import requests
import json


def get_business_list(user_name, page=1, size=10):
    """
    获取专栏列表
    """
    headers = {
        "Host": "blog.csdn.net",
        "Referer": f"https://blog.csdn.net/{user_name}?type=blog",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    }
    url = f"https://blog.csdn.net/community/home-api/v1/get-business-list?page={page}&size={size}&businessType=blog&orderby=&noMore=false&year=&month=&username={user_name}"
    response = requests.get(url, headers=headers)
    content = response.content.decode("utf-8")
    parsed = json.loads(content)

    if parsed["code"] != 200:
        raise RuntimeError("数据获取错误")

    data_list = parsed["data"]["list"]
    total = parsed["data"]["total"]
    bis_list = []

    for item in data_list:
        bis = Bis()
        bis.articleId = item["articleId"]
        bis.title = item["title"]
        bis.editUrl = item["editUrl"]
        bis.description = item["description"]
        bis.picList = item["picList"]
        bis.collectCount = item["collectCount"]
        bis.commentCount = item["commentCount"]
        bis.diggCount = item["diggCount"]
        bis.formatTime = item["formatTime"]
        bis.postTime = item["postTime"]
        bis.url = item["url"]
        bis.viewCount = item["viewCount"]
        bis_list.append(bis)

    return bis_list, total


def get_business_list_all(user_name):
    """获取专栏列表的全部文章，不推荐使用"""
    data = get_business_list(user_name, 1, 1)
    dict_data = json.loads(data)
    total = dict_data["data"]["total"]
    return get_business_list(user_name, 1, total)


if __name__ == "__main__":
    # data = get_business_list_all("2302_78391795")
    # print(data)
    data, total = get_business_list("HuaQi666", 1, 10)
    print(total)
    for da in data:
        print(da)
