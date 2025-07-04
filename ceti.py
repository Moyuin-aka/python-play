import ssl
import sys

try:
    paths = ssl.get_default_verify_paths()
    print("✅ SSL 库加载成功")
    print("-" * 20)
    print(f"  OpenSSL 版本: {ssl.OPENSSL_VERSION}")
    print(f"  默认 CA 文件 (cafile): {paths.cafile}")
    print(f"  默认 CA 路径 (capath): {paths.capath}")
    print("-" * 20)
    
    if paths.cafile and "certifi" in paths.cafile:
        print("✅ 配置看起来很正常，应该是指向了 certifi 的证书包。")
    elif paths.cafile:
         print("⚠️  CA 文件路径看起来正常，但请确认该文件有效且最新。")
    else:
        print("❌ 错误：找不到默认的 CA 证书文件 (cafile)！这是问题的根源。")
        print("   请确认你是否运行了第一步中的 'Install Certificates.command'。")

except Exception as e:
    print(f"❌ 加载 SSL 默认路径时出错: {e}")