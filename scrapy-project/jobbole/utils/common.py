import hashlib


def get_md5(src):
    md5 = hashlib.md5()
    src = src if isinstance(src, str) else src.encode('utf-8')
    md5.update(src)
    return md5.hexdigest()
