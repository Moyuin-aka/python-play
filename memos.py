import requests
import certifi
import sys

def get_memos():
    url = input("请输入你的memos域名(例如：memos.xxx.com):")
    try:
        # 使用 certifi 证书
        response = requests.get(
            f"https://{url}/api/v1/memos",
            verify=certifi.where(),
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        memos_list = data.get('memos')
        
        if not isinstance(memos_list, list):
            print("获取到的数据格式不正确，可能是域名错误或API未返回预期数据。")
            return
            
        print(f"一共获取到 {len(memos_list)} 条memos")
        print("------------------------------------------------")
        for i, memo in enumerate(memos_list, 1):
            content = memo.get('content', '(这条memos是空的！)')
            print(f"memos {i}:\n{content}")
            print("------------------------------------------------")
            
    except requests.exceptions.SSLError as e:
        print(f"SSL 证书验证失败: {e}")
        print("尝试跳过证书验证...")
        try:
            # 临时跳过 SSL 验证（仅用于测试）
            response = requests.get(
                f"https://{url}/api/v1/memos",
                verify=False,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            memos_list = data.get('memos')
            
            if isinstance(memos_list, list):
                print(f"⚠️  使用不安全连接成功获取到 {len(memos_list)} 条memos")
                print("建议检查你的域名 SSL 证书配置")
            else:
                print("获取到的数据格式不正确")
        except Exception as fallback_e:
            print(f"即使跳过SSL验证也失败了: {fallback_e}")
            
    except requests.RequestException as e:
        print(f"获取 memos 时出现问题: {e}")
    except ValueError:
        print("响应数据解析失败，请检查API返回格式")

if __name__ == "__main__":
    get_memos()
    sys.exit(0)