from selenium import webdriver
import chromedriver_binary
from tqdm import tqdm
import time

# 楽天会員ログイン情報
EMAIL = ""
PASSWORD = ""

# 先に楽天会員ページにログイン
driver = webdriver.Chrome()
url = 'https://grp02.id.rakuten.co.jp/rms/nid/login'
driver.get(url)
time.sleep(1)
element = driver.find_element_by_id("loginInner_u")
element.send_keys(EMAIL)
elementp = driver.find_element_by_id("loginInner_p")
elementp.send_keys(PASSWORD)
time.sleep(3)
driver.find_element_by_class_name('loginButton').click()
time.sleep(3)

url_list = [{'url':'https://kuji.rakuten.co.jp/889373540e','name':'InfoseekNewsラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/842378b442','name':'LINE限定 毎日引けるくじ'},
            {'url':'https://kuji.rakuten.co.jp/46211bf9dd','name':'Rakuten TV ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/4ab394dac2','name':'【2022年1月】特別ラッキーくじ（ecoloco（エコロコ） タイアップ版）'},
            {'url':'https://kuji.rakuten.co.jp/bbd394ec6d','name':'【2022年1月】特別ラッキーくじ（イーザッカマニアストアーズ タイアップ版）'},
            {'url':'https://kuji.rakuten.co.jp/34c3943648','name':'【バレンタイン特集2022】スロットを回して豪華賞品を当てよう！'},
            {'url':'https://kuji.rakuten.co.jp/bc23814a75','name':'【楽天toto】楽天totoラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/8c538152dd','name':'【楽天×宝くじ】最大1000ポイントが当たる！楽天×宝くじラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/4263816d7f','name':'【楽天くじ広場】ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/42136c5d7d','name':'【楽天ブックス】facebookラッキーくじ'},
            {'url':'https://app.kuji.rakuten.co.jp/campaign/poikatu/kuji/kuji202112.html','name':'【楽天ポイント活動部】ラッキーくじ（2021年11月～2月通常版）'},
            {'url':'https://kuji.rakuten.co.jp/26d37b04b2','name':'【楽天レシピ】ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/0133942488','name':'スタート1000限定くじ_202201'},
            {'url':'https://kuji.rakuten.co.jp/c5337832c5','name':'ニュースラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/d113946da3','name':'マラソンスロット＜事前告知版＞PC＆SP版'},
            {'url':'https://kuji.rakuten.co.jp/bb738f9ada','name':'楽天Car車検 ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/38c3861fdc','name':'楽天Edyラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/056392e715','name':'楽天×ぐるなび ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/34e2cb79fa','name':'楽天カレンダーラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/9ea32a8dfa','name':'楽天カレンダーラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/6c238469a1','name':'楽天カードラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/4351057845','name':'楽天ツールバーラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/1243541a35','name':'楽天トラベル ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/c1b39547c1','name':'楽天ビューティラッキーくじ（20220112）'},
            {'url':'https://kuji.rakuten.co.jp/ffc1c52299','name':'楽天ブックス・ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/c8437c01c5','name':'楽天ブログラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/7393386d27','name':'楽天ペイ (オンライン決済)ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/26e390eccf','name':'楽天ラクマのラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/ad1321af05','name':'楽天ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/f3a3832d0c','name':'楽天ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/18584163d','name':'楽天不動産ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/14d330d3e0','name':'楽天保険の総合窓口ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/6e7329f994','name':'楽天証券ラッキーカブくじ'},
            {'url':'https://kuji.rakuten.co.jp/85d3944049','name':'Rakuten Link限定ラッキースロット 第3弾'},
            {'url':'https://kuji.rakuten.co.jp/9f23834c4c','name':'アプリ限定 楽天ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/33d38332c2','name':'スマートフォン限定 楽天ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/0d5395c1ad','name':'マネ活ラッキーくじ'},
            {'url':'https://rakucoin.appspot.com/rakuten/kuji/redirect/fc437af2c7','name':'リワード特集ページ ラッキーくじ'},
            {'url':'https://r10.to/hf7Y7J','name':'楽天Edyラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/14039407db','name':'楽天PointClubSPWebラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/1a638459e0','name':'楽天カードスマホラッキーくじ'},
            {'url':'https://rakucoin.appspot.com/rakuten/kuji/redirect/e7a37ae390','name':'楽天リワード ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/27436a510a','name':'毎日ラッキーくじ'},
            {'url':'https://point.rakuten.co.jp/doc/lottery/lucky/','name':'楽天PointClubアプリラッキーくじ'},
            {'url':'https://pointmall.rakuten.co.jp/','name':'楽天ポイントモール DAILY CHANCEくじ'},]



for page in tqdm(url_list):
        try:
            if page['url'] == 'https://pointmall.rakuten.co.jp/':
                driver.get(page['url'])
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="side"]/div[1]/ul/li/div[1]/a/img').click()
                driver.find_element_by_xpath('//*[@id="side"]/div[1]/ul/li/div[2]/div/div[1]/div[6]').click()
                time.sleep(14)

            elif page['url'] == 'https://point.rakuten.co.jp/doc/lottery/lucky/':
                driver.get(page['url'])
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="cp_btn_start"]/a/img').click()
                time.sleep(14)

            else:
                driver.get(page['url'])
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="entry"]').click()
                time.sleep(14)

        except:
            print('###エラー 次のくじに進みます。' + page['name'] + '###')
            time.sleep(1)

# seleniumを終了
driver.close()
driver.quit()
