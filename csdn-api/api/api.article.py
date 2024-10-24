import requests
import json


def get_article(user_name, article_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    }
    url = f"https://blog.csdn.net/{user_name}/article/details/{article_id}"
    response = requests.get(url, headers=headers)
    content = response.content.decode("utf-8")
    return content


def save_article():
    headers = {
        "Host": "blog.csdn.net",
        "Origin": "https://editor.csdn.net",
        "Referer": "https://editor.csdn.net/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "Cookie": "uuid_tt_dd=10_37516577790-1724692186952-321991; fid=20_95226090043-1724692188573-326379; UN=HuaQi666; p_uid=U010000; csdn_newcert_HuaQi666=1; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_37516577790-1724692186952-321991!5744*1*HuaQi666; c_adb=1; dc_session_id=10_1729663404275.342608; c_segment=7; dc_sid=964b005da4f1c354d68f2e8671cb1f08; is_advert=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1729345930,1729492809,1729576571,1729663409; HMACCOUNT=77878E19201E8E01; _clck=15joqmv%7C2%7Cfq9%7C0%7C1699; creative_btn_mp=3; c_utm_source=edu_txxl_mh; SESSION=671e7575-eeb1-4748-9a49-9dfc5ab458a1; hide_login=1; loginbox_strategy=%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1729664275274%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22Huaqiwill%22%7D; UserName=HuaQi666; UserInfo=0a7ac2961dde416b89e6f1344f0bc3e7; UserToken=0a7ac2961dde416b89e6f1344f0bc3e7; UserNick=Huaqiwill; AU=FF2; BT=1729664291880; c_first_ref=default; c_utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-3-142962398-null-null.nonecase; c_dl_prid=1725187554132_201284; c_dl_rid=1729666746863_925693; c_dl_fref=https://blog.csdn.net/; c_dl_fpage=/; c_dl_um=distribute.pc_feed_blog_category.none-task-blog-classify_tag-3-142962398-null-null.nonecase; firstDie=1; c_page_id=default; c_first_page=https%3A//editor.csdn.net/md/%3FarticleId%3D139246228; _clsk=1czaput%7C1729668053056%7C25%7C0%7Cu.clarity.ms%2Fcollect; c_dsid=11_1729668148918.966574; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20230921102607.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A14%2C%22type%22%3A2%2C%22oldUser%22%3Atrue%2C%22useSeven%22%3Afalse%2C%22oldFullVersion%22%3Atrue%2C%22userName%22%3A%22HuaQi666%22%7D; c_pref=https%3A//mp.csdn.net/mp_blog/creation/success/139246228; c_ref=https%3A//mp.csdn.net/mp_blog/manage/article%3Fspm%3D1011.2480.3001.5298; log_Id_pv=186; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1729668519; log_Id_view=7109; dc_tos=slsst4; log_Id_click=147",
    }
    data = '{"id":143185656,"title":"你好，测试1213","markdowncontent":"你好，测试3\n回去喝酒我还差\n\n# 一级标题\n## 二级标题\n### 三级标题\n#### 四级标题\n##### 五级标题\n###### 六级标题\n","content":"<p>你好，测试3<br>\n回去喝酒我还差</p>\n<h1><a id="_3"></a>一级标题</h1>\n<h2><a id="_4"></a>二级标题</h2>\n<h3><a id="_5"></a>三级标题</h3>\n<h4><a id="_6"></a>四级标题</h4>\n<h5><a id="_7"></a>五级标题</h5>\n<h6><a id="_8"></a>六级标题</h6>\n\n","readType":"public","level":0,"tags":"","status":2,"categories":"","type":"original","original_link":"","authorized_status":false,"not_auto_saved":"1","source":"pc_mdeditor","cover_images":[],"cover_type":1,"is_new":1,"vote_id":0,"resource_id":"","pubStatus":"draft"}'
    url = "https://bizapi.csdn.net/blog-console-api/v3/mdeditor/saveArticle"
    response = requests.post(url, data=data, headers=headers)
    content = response.content.decode("utf-8")
    # parsed = json.loads(content)
    print(response)
    
    # if parsed["code"] == 200:
    #     print("保存成功")
    # else:
    #     print("保存失败")


if __name__ == "__main__":
    # get_article("csdnnews", "142995335")
    save_article()
