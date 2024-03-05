這是一個通過dgdemux , ffmpeg, mkvtoolnix, makemkv 來製作符合 本組 remux 標準的 "範例" 流程。

***

### 1.	整理分卷原盤文件結構
如使用dgdemux 路徑只能英文
```
[BDMV] Name S01
├── VOL_01
│   └── BDMV
└── VOL_02
    └── BDMV
```
<img src="/img/01.png" alt="image" width=640>

***

### 2. 使用 dgdemux 來 demux 原盤

建議使用圖中的版本號，印象中後面有些版本有奇怪的bug

輸出在同目錄即可，記得勾選episode demuxing (如果是肉醬盤用這個也沒救)
<img src="/img/02.png" alt="image" width=640>

 ***
 
### 3. Convert pcm to 16bits flac via ffmpeg (python script)
批量處理可參考 <https://github.com/010203le/343-remux-guide/blob/main/scripts/toFLAC.py>
<img src="/img/03.png" alt="image" width=640>

***

### 4. 使用 mkvtoolnix 獲取第一集的封裝指令
<img src="/img/05.png" alt="image" width=640>
 
 (輸出文件名可善用 nastool 識別測試功能，確保命名可被媒體庫識別，範例 Name S01E01-[1080p][JP.BD.Remux].mkv)

***

### 5. 將指令複製成多份，並將每行指令更改為不同集數對應文件
建立bat檔並在末行加上 pause，以便跑完後查看log
(輸出名、視訊軌文件、音軌文件、字幕文件、章節文件)

範例 Hoshikuzu Telepath 01-03 批量指令
```sh

D:\Workspace\remux_tools\mkvtoolnix-64-bit-70.0.0\mkvmerge.exe --ui-language zh_TW --priority lower --output ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDRemux] Hoshikuzu Telepath S01\Hoshikuzu Telepath S01E01-[1080p][JP.BD.Remux].mkv^" --language 0:ja --track-name 0:lolice-EC@OurBits ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [1] PID 1011.264^" ^"^)^" --no-audio --no-video --no-chapters --sync 2:1000 --sub-charset 2:UTF-8 --language 2:zh-Hans --track-name ^"2:[Sakurato]CHS^" --sync 3:1000 --sub-charset 3:UTF-8 --language 3:zh-Hant --track-name ^"3:[Sakurato]CHT^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[Sakurato] Hoshikuzu Telepath [01-12][HEVC-10bit 1080p AAC][CHS^&CHT]\[Sakurato] Hoshikuzu Telepath [01][HEVC-10bit 1080p AAC][CHS^&CHT].mkv^" ^"^)^" --sync 0:0 --language 0:ja --track-name ^"0:FLAC 2.0^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [1] PID 1100 jpn DELAY 0ms.flac^" ^"^)^" --chapter-language en --chapters ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [1].chapters.txt^" --generate-chapters-name-template ^"Chapter ^<NUM:2^>^" --track-order 0:0,2:0,1:2,1:3
D:\Workspace\remux_tools\mkvtoolnix-64-bit-70.0.0\mkvmerge.exe --ui-language zh_TW --priority lower --output ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDRemux] Hoshikuzu Telepath S01\Hoshikuzu Telepath S01E02-[1080p][JP.BD.Remux].mkv^" --language 0:ja --track-name 0:lolice-EC@OurBits ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [2] PID 1011.264^" ^"^)^" --no-audio --no-video --no-chapters --sync 2:1000 --sub-charset 2:UTF-8 --language 2:zh-Hans --track-name ^"2:[Sakurato]CHS^" --sync 3:1000 --sub-charset 3:UTF-8 --language 3:zh-Hant --track-name ^"3:[Sakurato]CHT^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[Sakurato] Hoshikuzu Telepath [01-12][HEVC-10bit 1080p AAC][CHS^&CHT]\[Sakurato] Hoshikuzu Telepath [02][HEVC-10bit 1080p AAC][CHS^&CHT].mkv^" ^"^)^" --sync 0:0 --language 0:ja --track-name ^"0:FLAC 2.0^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [2] PID 1100 jpn DELAY 0ms.flac^" ^"^)^" --chapter-language en --chapters ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [2].chapters.txt^" --generate-chapters-name-template ^"Chapter ^<NUM:2^>^" --track-order 0:0,2:0,1:2,1:3
D:\Workspace\remux_tools\mkvtoolnix-64-bit-70.0.0\mkvmerge.exe --ui-language zh_TW --priority lower --output ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDRemux] Hoshikuzu Telepath S01\Hoshikuzu Telepath S01E03-[1080p][JP.BD.Remux].mkv^" --language 0:ja --track-name 0:lolice-EC@OurBits ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [3] PID 1011.264^" ^"^)^" --no-audio --no-video --no-chapters --sync 2:1000 --sub-charset 2:UTF-8 --language 2:zh-Hans --track-name ^"2:[Sakurato]CHS^" --sync 3:1000 --sub-charset 3:UTF-8 --language 3:zh-Hant --track-name ^"3:[Sakurato]CHT^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[Sakurato] Hoshikuzu Telepath [01-12][HEVC-10bit 1080p AAC][CHS^&CHT]\[Sakurato] Hoshikuzu Telepath [03][HEVC-10bit 1080p AAC][CHS^&CHT].mkv^" ^"^)^" --sync 0:0 --language 0:ja --track-name ^"0:FLAC 2.0^" ^"^(^" ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [3] PID 1100 jpn DELAY 0ms.flac^" ^"^)^" --chapter-language en --chapters ^"D:\Workspace\remux_tools\rclone-v1.59.1-windows-amd64\[BDMV] Hoshikuzu Telepath S01\HOSHIKUZU_TELEPATH_VOL1\66244 [3].chapters.txt^" --generate-chapters-name-template ^"Chapter ^<NUM:2^>^" --track-order 0:0,2:0,1:2,1:3
pause
```

***

### 6. 執行 bat 等待完成

<img src="/img/06.png" alt="image" width=640>

***

### 7. 使用makemkv提取ncop/nced (如果沒有就不用了)
需事先修改makemkv設置
1. 最小標題長 30 秒
2. 開啟專家模式
3. 輸出預設 FLAC

<img src="/img/04.png" alt="image" width=640>

***

### 8. 確認文件封裝正確、字幕時軸匹配

***

### 9. 建立種子

先確認文件結構，以下是範例

```sh
[BDRemux] Hoshikuzu Telepath S01
├── Hoshikuzu Telepath S01E01-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E02-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E03-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E04-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E05-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E06-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E07-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E08-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E09-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E10-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E11-[1080p][JP.BD.Remux].mkv
├── Hoshikuzu Telepath S01E12-[1080p][JP.BD.Remux].mkv
├── NCOP.mkv
└── NCED.mkv
```

之後桌面端可使用qbittorrent 建立 僅v1種子 (勾選私人種子)

如要盒子發種(命令行)，也可使用mktorrent

mktorrent指令範例
```sh
mktorrent -v -p -l 24 -a http://tracker.example -o output.torrent "[BDRemux] Name S01"
```
