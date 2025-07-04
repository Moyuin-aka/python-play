# test.py
import requests

# 直接使用我们手动修复好的 Homebrew 证书路径
ca_file_path = "/opt/homebrew/etc/ssl/cert.pem"

print(f"💡 将使用以下 CA 证书文件进行验证: {ca_file_path}")

domain = input("请输入你的域名(例如：xxx.com):")
url = f"https://{domain}"

try:
    response = requests.get(url, verify=ca_file_path, timeout=10)
    print(f"✅ 连接成功! 状态码: {response.status_code}")
except Exception as e:
    print(f"❌ 依然失败: {e}")