import youtube_dl
import tkinter 
   
def create_window():
    
    #initiate window
    root = tkinter.Tk()
    root.title('Sample from Youtube')

    canvas1 = tkinter.Canvas(root, width = 600, height = 400)
    canvas1.pack()

    entry1 = tkinter.Entry(root) 
    canvas1.create_window(300, 140, window=entry1)
    root.eval('tk::PlaceWindow . center')

    
    def get_text():
        inp = entry1.get()
    
        label = tkinter.Label(root, text = inp)
        canvas1.create_window(300, 230, window = label)
        convert(inp)
        
    button1 = tkinter.Button(text='Get Sample!', command=get_text)
    canvas1.create_window(300, 180, window=button1)
    
    root.mainloop()

def convert(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    create_window()