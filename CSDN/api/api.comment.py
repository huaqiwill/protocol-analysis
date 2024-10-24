"""
csdn评论
"""

import requests

cookies = {
    "uuid_tt_dd": "10_37516577790-1724692186952-321991",
    "fid": "20_95226090043-1724692188573-326379",
    "UN": "HuaQi666",
    "p_uid": "U010000",
    "csdn_newcert_HuaQi666": "1",
    "Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac": "6525*1*10_37516577790-1724692186952-321991!5744*1*HuaQi666",
    "c_adb": "1",
    "c_segment": "7",
    "dc_sid": "964b005da4f1c354d68f2e8671cb1f08",
    "Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac": "1729345930,1729492809,1729576571,1729663409",
    "HMACCOUNT": "77878E19201E8E01",
    "SESSION": "671e7575-eeb1-4748-9a49-9dfc5ab458a1",
    "loginbox_strategy": "%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1729664275274%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22Huaqiwill%22%7D",
    "UserName": "HuaQi666",
    "UserInfo": "0a7ac2961dde416b89e6f1344f0bc3e7",
    "UserToken": "0a7ac2961dde416b89e6f1344f0bc3e7",
    "UserNick": "Huaqiwill",
    "AU": "FF2",
    "BT": "1729664291880",
    "csrfToken": "iblB8LU7t2K0gZX-XfLjzSKT",
    "c_dl_prid": "1725187554132_201284",
    "c_dl_rid": "1729666746863_925693",
    "c_dl_fref": "https://blog.csdn.net/",
    "c_dl_fpage": "/",
    "c_dl_um": "distribute.pc_feed_blog_category.none-task-blog-classify_tag-3-142962398-null-null.nonecase",
    "dp_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTM3NDU4NSwiZXhwIjoxNzMwMzAyMzIyLCJpYXQiOjE3Mjk2OTc1MjIsInVzZXJuYW1lIjoiSHVhUWk2NjYifQ.gGJc8G2VCO5uXcCgF1JSl5U3NdlQ2JvFpbZAXrrphpU",
    "https_waf_cookie": "09aa7ce5-9a0c-40e3767b194b9014af59e58acacb972d1dc3",
    "_clck": "15joqmv%7C2%7Cfqa%7C0%7C1699",
    "firstDie": "1",
    "creative_btn_mp": "3",
    "c_first_ref": "www.bing.com",
    "c_first_page": "https%3A//blog.csdn.net/ityard/article/details/135470025",
    "fe_request_id": "1729769542669_7031_8361021",
    "_clsk": "2mzc3n%7C1729769899847%7C4%7C0%7Cu.clarity.ms%2Fcollect",
    "c_pref": "https%3A//blog.csdn.net/ityard/article/details/135470025",
    "c_ref": "https%3A//blog.csdn.net/HuaQi666%3Ftype%3Dblog",
    "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1729769938",
    "log_Id_view": "6",
    "dc_session_id": "10_1729775809985.276297",
    "waf_captcha_marker": "7511d76b45a373a5e6790b1f30cc75b71bb21ff182a61020f159940377788e84",
    "dc_tos": "slv3kj",
    "log_Id_click": "4",
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # 'Cookie': 'uuid_tt_dd=10_37516577790-1724692186952-321991; fid=20_95226090043-1724692188573-326379; UN=HuaQi666; p_uid=U010000; csdn_newcert_HuaQi666=1; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37516577790-1724692186952-321991!5744*1*HuaQi666; c_adb=1; c_segment=7; dc_sid=964b005da4f1c354d68f2e8671cb1f08; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1729345930,1729492809,1729576571,1729663409; HMACCOUNT=77878E19201E8E01; SESSION=671e7575-eeb1-4748-9a49-9dfc5ab458a1; loginbox_strategy=%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1729664275274%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22Huaqiwill%22%7D; UserName=HuaQi666; UserInfo=0a7ac2961dde416b89e6f1344f0bc3e7; UserToken=0a7ac2961dde416b89e6f1344f0bc3e7; UserNick=Huaqiwill; AU=FF2; BT=1729664291880; csrfToken=iblB8LU7t2K0gZX-XfLjzSKT; c_dl_prid=1725187554132_201284; c_dl_rid=1729666746863_925693; c_dl_fref=https://blog.csdn.net/; c_dl_fpage=/; c_dl_um=distribute.pc_feed_blog_category.none-task-blog-classify_tag-3-142962398-null-null.nonecase; dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTM3NDU4NSwiZXhwIjoxNzMwMzAyMzIyLCJpYXQiOjE3Mjk2OTc1MjIsInVzZXJuYW1lIjoiSHVhUWk2NjYifQ.gGJc8G2VCO5uXcCgF1JSl5U3NdlQ2JvFpbZAXrrphpU; https_waf_cookie=09aa7ce5-9a0c-40e3767b194b9014af59e58acacb972d1dc3; _clck=15joqmv%7C2%7Cfqa%7C0%7C1699; firstDie=1; creative_btn_mp=3; c_first_ref=www.bing.com; c_first_page=https%3A//blog.csdn.net/ityard/article/details/135470025; fe_request_id=1729769542669_7031_8361021; _clsk=2mzc3n%7C1729769899847%7C4%7C0%7Cu.clarity.ms%2Fcollect; c_pref=https%3A//blog.csdn.net/ityard/article/details/135470025; c_ref=https%3A//blog.csdn.net/HuaQi666%3Ftype%3Dblog; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1729769938; log_Id_view=6; dc_session_id=10_1729775809985.276297; waf_captcha_marker=7511d76b45a373a5e6790b1f30cc75b71bb21ff182a61020f159940377788e84; dc_tos=slv3kj; log_Id_click=4',
    "Origin": "https://blog.csdn.net",
    "Pragma": "no-cache",
    "Referer": "https://blog.csdn.net/Xxy_1008/article/details/142793385?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-12-142793385-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-12-142793385-null-null.nonecase",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


def comment(content: str):
    data = {
        "commentId": "",
        "content": content,
        "articleId": "142793385",
    }

    response = requests.post(
        "https://blog.csdn.net/phoenix/web/v1/comment/submit",
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.json()["code"] == 200


def get_comments(article_id: str, page=1,size=10,fold_comment: bool = False):

    params = {
        "page": page,
        "size": size,
    }

    if fold_comment:
        params["fold"] = "fold"

    response = requests.post(
        f"https://blog.csdn.net/phoenix/web/v1/comment/list/{article_id}",
        params=params,
        cookies=cookies,
        headers=headers,
    )

    for i in response.json()["data"]["list"]:
        print(i["info"]["content"])


if __name__ == "__main__":
    get_comments("142793385")
