import requests
import sys
from bs4 import BeautifulSoup
url1 = 'http://login.cuit.edu.cn/Login/xLogin/Login.asp'
url2 ='http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/sj.asp?jkdk=Y'
account = sys.argv[1]
password = sys.argv[2]
r=requests.session()
header1 ={
        'Host':'login.cuit.edu.cn',
    'Content-Length':'146',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure-Requests':'1',
    'Origin':'http://login.cuit.edu.cn',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer':'http://login.cuit.edu.cn/Login/xLogin/Login.asp',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection':'close'
}
data1 ={
    'WinW':'=2560',
    'WinH':'1440',
    'txtId':account,
    'txtMM':password,
    'verifycode':'%B2%BB%B7%D6%B4%F3%D0%A1%D0%B3',
    'codekey':'112300',
    'Login':'Check',
    'IbtnEnter.x':'31',
    'IbtnEnter.y':'46'
}
s = r.post(url=url1,data=data1,headers=header1)
s=r.get(url=url2)
t1=BeautifulSoup(s.text,'lxml')
s1=t1.find(attrs={"http-equiv":"refresh"})['content']
url3=s1[6::]
s=r.get(url3)
t2=BeautifulSoup(s.text,'lxml')
s2 = t2.find_all('a')
s3 = s2[1]
url4 = 'http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/editSj.asp?UTp=Xs&Tx=33_1&ObjId='+account+'&Id='+str(s3)[64:69]
id = str(s3)[64:69]
data2 = {
'RsNum': '3',
'Id': id,
'Tx': '33_1',
'canTj': '1',
'isNeedAns': '0',
'UTp': 'Xs',
'ObjId': account,
'th_1': '21650',
'wtOR_1': '1%5C%7C%2F%CB%C4%B4%A8%5C%7C%2F%B9%E3%D4%AA%5C%7C%2F%C0%FB%D6%DD%5C%7C%2F1%5C%7C%2F',
'sF21650_1': '1',
'sF21650_2': '%CB%C4%B4%A8',
'sF21650_3': '%B9%E3%D4%AA',
'sF21650_4': '%C0%FB%D6%DD',
'sF21650_5': '1',
'sF21650_6': '',
'sF21650_7': '',
'sF21650_8': '',
'sF21650_9': '',
'sF21650_10': '',
'sF21650_N': '10',
'th_2': '21912',
'wtOR_2': '',
'sF21912_1': '1',
'sF21912_2': '1',
'sF21912_3': '1',
'sF21912_4': '06',
'sF21912_5': '3',
'sF21912_6': '23',
'sF21912_N': '6',
'th_3': '21648',
'wtOR_3': 'N%5C%7C%2F%5C%7C%2FN%5C%7C%2F%5C%7C%2FN%5C%7C%2F',
'sF21648_1': 'N',
'sF21648_2': '',
'sF21648_3': 'N',
'sF21648_4': '',
'sF21648_5': 'N',
'sF21648_6': '',
'sF21648_N': '6',
'zw1': '',
'cxStYt': 'A',
'zw2': '',
'B2': '%CC%E1%BD%BB%B4%F2%BF%A8'
}
header2={
'Host':'jszx-jxpt.cuit.edu.cn',
'Content-Length':'632',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests':'1',
'Origin':'http://jszx-jxpt.cuit.edu.cn',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': url4,
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}
r.headers.update(header2)  
s=r.post(url='http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netks/editSjRs.asp',data=data2)
