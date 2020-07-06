import urllib.request

print('Beginning file download with urllib2...')

url = 'http://s8.bitdl.ir/Series/Samurai.Jack/S01/Samurai.Jack.S01E13.720p.BluRay-Pahe.Bia2HD.mkv'
urllib.request.urlretrieve(url, '/home/ngecu/Desktop/Projects/ytd/Samurai.Jack.S01E13.720p.BluRay-Pahe.Bia2HD.mkv')
