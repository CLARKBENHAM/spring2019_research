# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:32:22 2019

@author: Clark Benham
"""
import os
import re

def prev_count(i):
    if re.findall("Section (\d+) Transcript", i):
        return int(re.findall("Section (\d+) Transcript", i)[0])
    else:
        return 0

start_dir = os.getcwd() 
os.chdir(r"C:\Users\Clark Benham\Downloads")
dir_names = [i for i in os.listdir() if "Subtitles.zip" in i]
#grib to move
os.system(r'move *Subtitles.zip "C:\Users\Clark Benham\Desktop\Research\Udacity_GPU"')
os.chdir(start_dir)
#%%    
# dir_names = ["Lesson 2 - GPU Hardware and Parallel Communication Patterns Subtitles.zip"]
dir_names = ["Intro to Parallel Programming Subtitles.zip"]
for dir_name in dir_names: 
    dest_path = dir_name[:dir_name.rfind(".")]
    
    os.system(f'powershell -Command "Expand-Archive -Path \'{dir_name}\' -DestinationPath \'{dest_path}\'"')
    
    sub_dirs = os.listdir(dest_path)#issue of final?
    final_ix = set(ix for ix, v in enumerate(sub_dirs)
                    if "final" in v.lower() or "last" in v.lower())
    sub_dirs = [v for ix, v in enumerate(sub_dirs) if ix not in final_ix] + [sub_dirs[i] for i in final_ix]
    out = ""
    if "." in sub_dirs[0]:#zip file directly contains transcripts
        files = [i for i in sub_dirs if "lang" not in i or "lang_en" in i ]
        for file in files:
            min_offset = min(file.rfind("."), file.rfind("-"))
            file_name = file[:min_offset]
            out += f"============{file_name}============\n\n"
            with open(f"{dest_path}\\{file}") as f:
                srt = [i.strip() for i in f.readlines() if len(i) >= 3 and any(map(lambda j: j.isalpha(), i))]
            out += "".join(srt).replace(".", ".\n")
            out += "\n++++++++++++++++++++++++++++++\n\n\n"
        out += "----------------------------------------\n\n\n\n\n\n"
   
    else:#3 levels deep 
        for sub_dir in sub_dirs:
            out += f"~~~~~~~~~~~~~~~{sub_dir}~~~~~~~~~~~~~~~\n\n\n"
            for file in os.listdir(dest_path + "\\" + sub_dir):
                min_offset = min(file.rfind("."), file.rfind("-"))
                file_name = file[:min_offset]
                out += f"============{file_name}============\n\n"
                with open(f"{dest_path}\\{sub_dir}\{file}") as f:
                    srt = [i.strip() for i in f.readlines() if len(i) > 0 and not i[0].isdigit()]
                out += "".join(srt).replace(".", ".\n")
                out += "\n++++++++++++++++++++++++++++++\n\n\n"
            out += "----------------------------------------\n\n\n\n\n\n"
    
    prev_lect = max([prev_count(i) for i in os.listdir()], default = 0)
    out_name = f"Section {prev_lect + 1} Transcript_ " + dir_name
    
    with open(f"all_lectures", "w") as f:
        f.write(out)


# print(out)
