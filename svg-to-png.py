import os
import shutil
import subprocess


svg_path = 'C:\\Users\\josep\\Downloads\\weather-icons-master\\weather-icons-master\\svg'
png_path = os.path.join(svg_path, 'png')

if os.path.exists(png_path):
    shutil.rmtree(png_path)
os.mkdir(png_path)

f = []
for (dirpath, dirnames, svg_filenames) in os.walk(svg_path):
    f.extend(svg_filenames)

for (filename) in f:
    cmd = ['C:\\Users\\josep\\AppData\\Roaming\\npm\\svg2png.cmd', os.path.join(svg_path, filename), f"--output={os.path.join(png_path, filename.replace('.svg', '.png'))}", '--width=200', '--height=200']
    out = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    print(stdout)
    print(stderr)
    # print(f"svg2png {os.path.join(svg_path, filename)} --output={os.path.join(png_path, filename.replace('.svg', '.png'))} --width=200 --height=200")