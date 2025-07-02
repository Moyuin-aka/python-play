import requests
import certifi
import sys
def get_memos():
    url=input("请输入你的memos域名(例如：memos.xxx.com):")
    try:
        cert_path = certifi.where()
        response=requests.get(f"https://{url}/api/v1/memos")
        response.raise_for_status()  # Check for HTTP errors
        data=response.json()
        memos_list=data.get('memos')
        if not isinstance(memos_list, list):
            print( "获取到的数据格式不正确，可能是域名错误或API未返回预期数据。")
        print(f"一共获取到 {len(memos_list)} 条memos")
        print("------------------------------------------------")
        for i,memo in enumerate(memos_list,1):
            content=memo.get('content','(这条memos是空的！)')
            print(f"memos {i}:\n{content}")
            print("------------------------------------------------")
    except requests.RequestException as e:
        print( f"获取 memos 时出现问题: {e}")
    except ValueError:
        print( "网络连接失败，请检查你的域名是否正确，或者网络连接是否正常。")
if __name__ == "__main__":
    get_memos()
    sys.exit(0)