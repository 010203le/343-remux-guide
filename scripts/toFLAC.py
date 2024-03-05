import os

path = r'D:\path\to\demux_floder'

# 需要將ffmpeg加入環境變數，或嘗試將os.system那行的ffmpeg修改為ffmpeg.exe路徑
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".w64"):
            os.system('ffmpeg -i "' + os.path.join(root, file) + '" -c:a flac -sample_fmt s16 "' + os.path.join(root, file[:-4] + '.flac') + '"')

'''     
#肉醬盤切割後專用
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".mkv"):
            os.system('ffmpeg -i "' + os.path.join(root, file) + '" -map 0 -c copy -c:a flac -sample_fmt s16 "' + os.path.join(root, file[:-4] + '-flac.mkv') + '"')
'''
