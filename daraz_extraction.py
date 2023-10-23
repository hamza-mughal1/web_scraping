import requests 
from bs4 import BeautifulSoup

session = requests.Session()


str = "t_fv=1698037523280; t_uid=SskEfQZbFN4BfmopMXEv0PWYd3Pqff82; lzd_cid=39f0f04c-adb6-4ea3-b4a1-22f3284b6809; lzd_sid=138c3f2fc9ac4fa1ec9a6db532903966; _tb_token_=eebd7d366333e; lwrid=AQGLWuxnDfU1hOT9KoVDX380peG0; _gcl_au=1.1.1140994701.1698037525; _gid=GA1.2.1058417882.1698037526; hng=PK|en-PK|PKR|586; curTraffic=lazada; userLanguageML=en-PK; _bl_uid=j8l6dowy2g0ftIpIafU2t7g7zpp9; mi_p_source=undefined; mi_p_medium=undefined; mi_p_campaign=undefined; mi_p_term=undefined; mi_p_content=undefined; mi_p_gclid=undefined; t_sid=dCJ5GrxAilF9iOB832MiYbFn1CLXp8SP; utm_channel=NA; _m_h5_tk=343e773e7552de2c5a4d97a91a1c022b_1698055814415; _m_h5_tk_enc=d7dc8bd59dea93c891b016000ed5fe60; daraz-marketing-tracker=hide; epssw=1*MZP911GPC5HtTFzaIA4SZRwdu5b8Jj9p1Z2sNADGBNi3oGeGiFrstQJ_xH-MjhxGcOYX3cBWNKB9-HWDdt5Rt962NKdM1u9Vd1XxQxe5NCsGj_9f6TO0av9Vqbuc9J-h4_X2AT0cFb2ZdaKNV6CawvOAlz6jxAv8dL3bvp6-xD0RyTBqdGWJ3Jp8fgnnxYB4yaQRrW_jnK5b6by9BxzRPMmnetrnxf..; JSESSIONID=D6CDDF253987E905D1BF3CA645F29F1C; _ga_5L4FRV3KPW=GS1.1.1698046813.2.1.1698046821.52.0.0; _ga_C6SBBPVWWK=GS1.1.1698046813.2.1.1698046821.52.0.0; _ga=GA1.2.466404133.1698037526; tfstk=dg-9FRA6OXcMXoiNHr3ngXv9qLXt-hpwjCJ7msfglBdpFLPGljuNlipOtsjGffSAhIACsCj6DervUK-iQiDNbdoVVbcoq0XwQiSfvFnoqnPm_rloZ0murSX_1bYGhfFAUi2uZcFL23KPCqvFmC5gkhWOW_UG9oExnOQONd1KNb6w33x8TCFlwt4spvU4uN6eTxC0s; l=fBx0m16PP_zAVTDzBOfwPurza77OSKRAguPzaNbMi9fPOX5p53kCW13rFhY9C3MNFsTyR3ohWZKMBeYBqIXN3PYgulPFYMkmnXr9aX5..; isg=BI2N2eNK1FqYKXB1wNekuHwmjKkHasE8GQm62M8S7CSTxq94l7tgDFtENkKgBtn0"

dic = {}
for i in str.split(";"):
    key ,val = i.split("=")
    dic[key] = val

session.cookies = dic


requests_cookies = requests.utils.cookiejar_from_dict(dic)
response = session.get("https://www.daraz.pk/catalog/?spm=a2a0e.home.search.1.35e34076ISp6pa&q=gaming%20pc&_keyori=ss&from=search_history&sugg=gaming%20pc_0_1", cookies=requests_cookies)
print(response)