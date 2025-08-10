#!/usr/bin/env python3

import base64, os, secrets


def gen_aes_key():
	key=os.urandom(32)
	return base64.b64encode(key).decode()
	
def gen_jwt_secret():
	return secrets.token_urlsafe(32)


if __name__ == "__main__":
	print("AES_SECRET_KEY=" + gen_aes_key())
	print("JWT_SECRET=" + gen_jwt_secret())
