import ssl
import socket
import certifi

hostname = 'memos.moyuin.top'
port = 443

print(f"--- 正在测试Python SSL模块 ---")
print(f"Python SSL库版本: {ssl.OPENSSL_VERSION}")
print(f"certifi 证书路径: {certifi.where()}")

# 测试1：使用Python的默认证书设置
print("\n[测试1: 使用默认证书]")
try:
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(">>> 默认证书验证成功！")
except ssl.SSLError as e:
    print(f">>> 默认证书验证失败: {e}")

# 测试2：强制使用 certifi 提供的证书
print("\n[测试2: 强制使用certifi证书]")
try:
    context = ssl.create_default_context(cafile=certifi.where())
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(">>> certifi 证书验证成功！")
except ssl.SSLError as e:
    print(f">>> certifi 证书验证失败: {e}")

print("\n--- 测试结束 ---")