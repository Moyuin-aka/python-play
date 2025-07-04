import ssl
import socket
from datetime import datetime

def check_ssl_cert(hostname, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                print(f"=== {hostname} SSL 证书信息 ===")
                print(f"主题: {dict(cert['subject'])}")
                print(f"颁发者: {dict(cert['issuer'])}")
                print(f"有效期从: {cert['notBefore']}")
                print(f"有效期到: {cert['notAfter']}")
                print(f"序列号: {cert['serialNumber']}")
                
                # 检查是否过期
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                if not_after < datetime.now():
                    print("❌ 证书已过期！")
                else:
                    print("✅ 证书有效")
                    
                return True
                
    except Exception as e:
        print(f"❌ SSL 检查失败: {e}")
        return False

# 检查你的域名
check_ssl_cert("google.com")