import ssl
import socket
import certifi
import requests

# 使用多个测试站点
test_sites = [
    ('httpbin.org', 443),
    ('www.baidu.com', 443),
    ('github.com', 443)
]

print(f"--- 正在测试Python SSL模块 ---")
print(f"Python SSL库版本: {ssl.OPENSSL_VERSION}")
print(f"certifi 证书路径: {certifi.where()}")

# 测试1：使用requests库测试（更简单）
print("\n[测试1: 使用requests库测试HTTPS]")
for site, _ in test_sites:
    try:
        response = requests.get(f"https://{site}", timeout=5)
        print(f">>> {site} - requests测试成功! 状态码: {response.status_code}")
        break
    except Exception as e:
        print(f">>> {site} - requests测试失败: {e}")

# 测试2：socket连接测试（带超时）
print("\n[测试2: socket连接测试]")
for hostname, port in test_sites:
    try:
        context = ssl.create_default_context()
        # 设置较短的超时时间
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(f">>> {hostname} - 默认证书验证成功！")
                print(f"    证书信息: {ssock.getpeercert()['subject']}")
                break
    except Exception as e:
        print(f">>> {hostname} - 连接失败: {e}")

# 测试3：检查本地证书配置
print("\n[测试3: 检查证书配置]")
print(f"默认证书路径: {ssl.get_default_verify_paths()}")

print("\n--- 测试结束 ---")