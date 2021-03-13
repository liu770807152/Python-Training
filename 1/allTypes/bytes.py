s = "中国"  # 内存中使用的是unicode
# 编码
bs = s.encode("utf-8")
print(bs)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(bs.decode("utf-8"))
