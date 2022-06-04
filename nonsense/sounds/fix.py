import os

originaldir = "originals"
fixeddir = r"..\..\app\src\main\res\raw"
for originalfilename in os.listdir(originaldir):
    print(originalfilename)
    os.system(f'ffmpeg -i {os.path.join(originaldir, originalfilename)}  -af silenceremove=1:0:-50dB -af loudnorm -vn -ar 44100 -ac 2 -b:a 192k LOL.mp3')
    if os.path.exists(os.path.join(fixeddir, originalfilename)):
        os.remove(os.path.join(fixeddir, originalfilename))
    os.rename("LOL.mp3", os.path.join(fixeddir, originalfilename))