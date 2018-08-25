# RESTful_api_Test
# 問題1 環境熟悉

請試著在 python 2.7.13 或 python 3.5.3 下，用 pip 安裝 pytest 套件, 版本需為 3.0.7。
（建議使用 virtualenv 或任意可讓環境獨立的套件, 如 docker）

1. 簡單描述如何安裝指定版本的 python binary
> 進入virtualenv 打：pip install pytest==3.0.7
2. 安裝完 pytest 3.0.7 後, 請用 pip 將當前環境印出並付上


# 問題2 除錯

```python
def extend_list(val, l=[]):
    l.append(val)
    return l

def test_extend_list():
    # 1
    assert extend_list(1) == [1]
    # 2
    assert extend_list(2, []) == [2]
    # 3
    assert extend_list(3) == [3]

if __name__ == '__main__':
    test_extend_list()
```

1. 請問 `if __name__ == '__main__':` 的用意為何？
> python 會去判斷，如果一個檔案被import，會被判斷 name == 被import的名稱。
如果一個檔案他是主要被執行的，而不是被引入的，name== main
2. 這段 code 會在第三個 assert 出錯了, 為什麼？
> 因為第三個 aessert 沒有把 extend_list 給初始化，在list裡面有2，所以append 3 後, list裡面應該是[2,3] 因此斷言錯誤

# 問題3 簡答

問題
1. 請試著簡述你在 python 2 中如何處理 str 與 unicode 的轉換？
 
```
str to unicode: u'string' ; 
unicode to str: u'string'.encode('utf8')

```
2. python 3 為何不需再考慮上述問題？
>ans: 因為在python3 ,str被視為unicode
3. 若要用 python 開一個 MVC project(比方說 web server), 你的資料夾會打算如何配制？
> 我會先建一個專案名稱：CW 然後在其下面再創建一個app名為:nba
> 然後在nba裡面設置views, urls, models
> CW下的urls會把路徑導去nba下的urls，這樣比較好讓nbs控制url


# 問題4 實做

請試著實做一個 decorator，能夠接受兩個 argument type datetime，
若 function 運行當下的時間是在這兩個時間內, 則 `print('in time!')`。
（兩個 datetime 順序不一定要按 ascending 排序）
```
import datetime

no2 =no+datetime.timedelta(minutes=10)
t1= datetime.datetime.now()+datetime.timedelta(minutes=10)
t2= datetime.datetime.now()+datetime.timedelta(minutes=-10)
def a(t1,t2):
    def aa(func):
        def aaa(*args):
            bb= func(*args)  
            if (bb<=t1 and bb>=t2) or (bb>=t1 and bb<=t2):
                print('in time') 
        return aaa
    return aa
@a(t1,t2)
def b(now):
    return now
t1= datetime.datetime.now()+datetime.timedelta(minutes=10)
t2= datetime.datetime.now()+datetime.timedelta(minutes=-10)
def a(t1,t2):
    def aa(func):
        def aaa(*args):
            bb= func(*args)  
            if (bb<=t1 and bb>=t2) or (bb>=t1 and bb<=t2):
                print('in time') 
        return aaa
    return aa
@a(t1,t2)
def b():
    now =datetime.datetime.now()
    return now
b()

```
# 問題5 RESTful api 實做
請用 python flask 或習慣的語言 撰寫給前端的 user API 的login服務

服務內容包含:
* 取得使用者列表
* 取得使用者資料
* 新增使用者
* 修改使用者

使用者必填寫欄位:
* account
* password
* name

