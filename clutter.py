import os
def createifnotexist(folder):
    if not  os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files=os.listdir()
    # files.remove("mains.py")
createifnotexist('Movies')
createifnotexist('Images')
createifnotexist('Documents')
createifnotexist('Others')
createifnotexist('Compressed')
createifnotexist('Music')
imgExts=[".png",".jpg",".jpeg",".dng",".ico"]
Image= [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
movExts=[".mp4",".mkv",".avi"]
Movies= [file for file in files if os.path.splitext(file)[1].lower() in movExts]
docExts=[".pdf",".ppt",".pptx",".doc",".docx",".txt"]
Documents= [file for file in files if os.path.splitext(file)[1].lower() in docExts]
musicExts=[".mp3",".wav"]
Music= [file for file in files if os.path.splitext(file)[1].lower() in musicExts]
comExts=[".zip",".rar",".iso"]
Compressed= [file for file in files if os.path.splitext(file)[1].lower() in comExts]
others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in movExts) and (ext not in docExts) and (ext not in musicExts) and (ext not in comExts) and os.path.isfile(file):
        others.append(file)

move("Images", Image)
move("Movies", Movies)
move("music", Music)
move("Documents", Documents)
move("Compressed", Compressed)
move("others", others)
    
for dirpath, dirnames, files in os.walk('.'):
  if not (files or dirnames):
    os.rmdir(dirpath)
