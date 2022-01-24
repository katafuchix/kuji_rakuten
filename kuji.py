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


url_list = [{'url':'https://kuji.rakuten.co.jp/9d91da42ab','name':'infoseeek'},
            {'url':'https://kuji.rakuten.co.jp/889373540e','name':'infoseeekNews'},
            {'url':'https://kuji.rakuten.co.jp/842378b442','name':'LINE'},
            {'url':'https://kuji.rakuten.co.jp/46211bf9dd','name':'TV'},
            {'url':'https://kuji.rakuten.co.jp/bc23814a75','name':'楽天toto'},
            {'url':'https://kuji.rakuten.co.jp/8c538152dd','name':'楽天宝くじ'},
            {'url':'https://kuji.rakuten.co.jp/4ad36145c2','name':'楽天くじ広場'},
            {'url':'https://kuji.rakuten.co.jp/d2b37c7d6a','name':'楽天e-NAVI'},
            {'url':'https://kuji.rakuten.co.jp/fae37d0d91','name':'楽天e-NAVI さかな'},
            {'url':'https://kuji.rakuten.co.jp/8212abcffe','name':'楽天e-NAVI じゃんけん'},
            {'url':'https://kuji.rakuten.co.jp/42136c5d7d','name':'楽天ブックスfacebook'},
            {'url':'https://kuji.rakuten.co.jp/6e2381eb02','name':'pointmall部活'},
            {'url':'https://kuji.rakuten.co.jp/26d37b04b2','name':'楽天レシピ'},
            {'url':'https://kuji.rakuten.co.jp/4e9371dd92','name':'楽天car'},
            {'url':'https://kuji.rakuten.co.jp/10a37ad0e0','name':'楽天×ぐるなび'},
            {'url':'https://kuji.rakuten.co.jp/9ea32a8dfa','name':'楽天カレンダー1'},
            {'url':'https://kuji.rakuten.co.jp/34e2cb79fa','name':'楽天カレンダー2'},
            {'url':'https://kuji.rakuten.co.jp/256356cd1a','name':'楽天カードラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/4351057845','name':'楽天ツールバーラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/9a0381a85d','name':'楽天デリバリー'},
            {'url':'https://kuji.rakuten.co.jp/7a1321943c','name':'スマホアプリ限定ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/a29321bc36','name':'スマホスマホ限定ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/fc437af2c7','name':'スマホリワード特集'},
            {'url':'https://kuji.rakuten.co.jp/95737c358e','name':'楽天edyくじ'},
            {'url':'https://kuji.rakuten.co.jp/1473379bb1','name':'スマホ楽天pointclub'},
            {'url':'https://kuji.rakuten.co.jp/a24364f880','name':'スマホ楽天pointclub'},
            {'url':'https://kuji.rakuten.co.jp/4592a41e4c','name':'スマホ楽天カードスマホ'},
            {'url':'https://kuji.rakuten.co.jp/e7a37ae390','name':'スマホ楽天リワード'},
            {'url':'https://kuji.rakuten.co.jp/2d1381326a','name':'マネ活ラッキーくじ'},
            {'url':'https://kuji.rakuten.co.jp/27436a510a','name':'スマホ毎日ラッキーくじ'},
            #その他、特殊なくじ
            {'url':'https://point.rakuten.co.jp/doc/lottery/lucky/','name':'スマホ楽天pointclub'},
            {'url':'https://pointmall.rakuten.co.jp/','name':'スマホDAILY CHANCEくじ'},]



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
