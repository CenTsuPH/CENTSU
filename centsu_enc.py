import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))