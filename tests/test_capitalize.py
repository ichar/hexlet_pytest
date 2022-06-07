from src.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('error!')

if capitalize('') != '':
    raise Exception('error!')

print('OK!')