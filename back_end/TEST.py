import jwt

def decode_jwt_token(token, secret_key):
    try:
        # 解码 JWT Token
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # Token 过期
        print("Token 已过期")
        return None
    except jwt.InvalidTokenError:
        # Token 无效
        print("无效的 Token")
        return None

def main():
    # 输入你的 JWT Token 和密钥
    jwt_token = input("请输入 JWT Token: ")
    secret_key = input("请输入密钥: ")

    # 解析 JWT Token
    decoded_token = decode_jwt_token(jwt_token, secret_key)

    if decoded_token:
        print("解析成功！")
        print("Payload 数据:")
        for key, value in decoded_token.items():
            print(f"{key}: {value}")
    else:
        print("解析失败")

if __name__ == "__main__":
    main()
