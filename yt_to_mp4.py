from tkinter import *
from pytube import YouTube
import os
from tkinter import messagebox
from hurry.filesize import size

class Main():
    
    def __init__(self,root):

        self.label = Label(root, text= "! Youtube To MP4 Converter !",bg = 'bisque',fg= 'darkred',bd = "5",font= ("Comic Sans Ms",20,"bold"))
        self.label.place(x= 100,y= 20)

        self.entry2 = Entry(root,textvariable= mytext2,width= 35,fg= 'indigo',bg= "white", font= 25 )
        self.entry2.insert(0,"  Paste Your Download Path Here  ")
        self.entry2.place(x = 110,y = 80)
        
        self.set_path = Button(root, text= "SET PATH",fg= "black",bg= 'lightcoral',font= ("Arial",15,"bold"),bd= 8,command= self.set_path_btn)
        self.set_path.place(x = 230,y = 130)
          
        self.exit = Button(root, text= " EXIT ",fg= "black",bg= "lightcoral",font= ("Arial",15,"bold"),bd= 10,command= self.exit_btn)
        self.exit.place(x = 240,y = 515)

    def set_path_btn(self):

        self.path = self.entry2.get()

        self.entry1 = Entry(win,textvariable= mytext1,width= 35,fg= "indigo", font= 25 ,bg= "white")
        self.entry1.insert(0,"  Paste Your Video Link Here  ")
        self.entry1.place(x = 110,y = 80)

        self.submit = Button(win, text= "SUBMIT",fg= "black",bg= "lightcoral",font= ("Arial",15,"bold"),bd= 8,command= self.submit_btn)
        self.submit.place(x = 230,y = 130)

        self.set_path.destroy()
      
    def submit_btn(self):
        try:

            try :

                self.mp3_size.destroy()
                self.three_six_zero_size.destroy()
                self.seven_two_0_size.destroy()

                self.mp3.destroy()
                self.download3.destroy()

                self.seven_two_0.destroy()
                self.download2.destroy()

            
                self.three_six_zero.destroy()
                self.download1.destroy() 

            except AttributeError as v  :
                print("  ")

            self.link =  self.entry1.get()

            self.yt_obj = YouTube(self.link)

            self.filter = self.yt_obj.streams.filter(progressive= True)
            

            
            self.quality  = Label(win,text= "QUALITY",fg= 'darkred',bg= "bisque",font= ("Comic Sans Ms",17,"bold"),borderwidth=10)
            self.quality.place(x= 30,y=210)

            self.sizes  = Label(win,text= "SIZE",fg= 'darkred',bg= "bisque",font= ("Comic Sans Ms",17,"bold"),bd= 5)
            self.sizes.place(x= 250,y=210)

            self.downloads  = Label(win,text= "DOWNLOAD",fg= 'darkred',bg= "bisque",font= ("Comic Sans Ms",17,"bold"),bd= 5)
            self.downloads.place(x= 390,y=210)
        
            self.sizee = self.yt_obj.streams.filter(type= "audio",file_extension= "webm")
            self.size_byte_mp3 = self.sizee.first().filesize
            self.size_covert = size(self.size_byte_mp3)


            self.mp3 = Label(win,text= "MP3 ",fg= "darkred",bg= "bisque",bd= 5,font= ("Arial",15,"bold"))
            self.mp3.place(x= 50, y = 430)
            
            self.download3 = Button(win, text= "DOWNLOAD",bd= 5, font= ("Arial",13,"bold"),bg= "salmon",fg= "black",command= root.download3_btn)
            self.download3.place(x = 400,y = 430)
            
            self.mp3_size = Label(win,text= self.size_covert,fg= "darkred",bg= "bisque",bd= 5,font= ("Arial",15,"bold"))
            self.mp3_size.place(x= 260, y = 430)

            if self.filter.get_by_resolution("360p") in self.filter :
            
                self.size3 = self.yt_obj.streams.filter(progressive= True,res= "360p")
                self.size_byte_360 = self.size3.first().filesize
                self.size_converterr = size(self.size_byte_360)

                self.three_six_zero = Label(win,text= "360p",fg= "darkred",font= ("Arial",15,"bold"),bg= "bisque",bd= 5)
                self.three_six_zero.place(x = 50,y = 290)

                self.download1 = Button(win, text= "DOWNLOAD",bd= 5, font= ("Arial",13,"bold"),bg= "salmon",fg= "black",command= root.download1_btn)
                self.download1.place(x = 400,y = 290)
            
                self.three_six_zero_size = Label(win,text= self.size_converterr,fg= "darkred",bg= "bisque",bd= 5,font= ("Arial",15,"bold"))
                self.three_six_zero_size.place(x= 260, y = 290)
                
                

                if self.filter.get_by_resolution("720p") in self.filter :

                    self.size7 = self.yt_obj.streams.filter(progressive= True,res= "720p")
                    self.size_byte_720 = self.size7.first().filesize
                    self.size_covert = size(self.size_byte_720)

                    self.seven_two_0= Label(win,text= "720p",fg= "darkred",font= ("Arial",15,"bold"),bg= "bisque",bd= 5)
                    self.seven_two_0.place(x = 50,y = 360)    

                    self.download2 = Button(win, text= "DOWNLOAD",bd= 5, font= ("Arial",13,"bold"),bg= "salmon",fg= "black",command= root.download2_btn)
                    self.download2.place(x = 400,y = 360)
                        
                    self.seven_two_0_size = Label(win,text= self.size_covert,fg= 'darkred',bg= "bisque",bd= 5,font= ("Arial",15,"bold"))
                    self.seven_two_0_size.place(x= 260, y = 360)

                else : 
                    self.seven_two_0.destroy()
                    self.download2.destroy()
            else:
                self.three_six_zero.destroy()
                self.download1.destroy() 

        except Exception as e:
            print("   ")
   
    def download1_btn(self):
    
        try:
            self.path = self.entry2.get()
            self.pathl = self.path.replace("\\","/")

            self.three =   self.filter.get_by_resolution("360p").download(self.pathl)    
            self.msg = messagebox.showinfo("showinfo", "DOWNLOADED") 
                    
        except FileNotFoundError as f :      
            print("PATH NOT SET")
        
    def download2_btn(self):
        try:
            self.path = self.entry2.get()
            self.pathl = self.path.replace("\\","/")
    
            self.seven = self.filter.get_by_resolution("720p").download(self.pathl)     
            self.msg = messagebox.showinfo("INFO", "DOWNLOADED") 

        except FileNotFoundError as f :
            print("PATH NOT SET ")  

    def download3_btn(self):

        try :

            self.path = self.entry2.get()
            self.pathl = self.path.replace("\\","/")

            self.filter2 = self.yt_obj.streams.filter(type= "audio",file_extension= "webm")

            self.file_name =  self.filter2.first().download(output_path= self.pathl)
            self.msg = messagebox.showinfo("INFO", "DOWNLOADED")
            self.name = self.file_name

            self.p = self.name.replace("webm","mp3")            
            self.path2 = self.file_name.replace("\\","/")
            self.path3 = self.p.replace("\\","/")
        
            self.rename = os.rename(self.path2,self.path3)
            
        except FileExistsError as f :
            print("File is already exit !!")    
        
        except FileNotFoundError as g :
            print("PATH NOT SET")
            
    
    def exit_btn(self):
        win.destroy()

if __name__ == '__main__':
   
    win = Tk()
    mytext1 = StringVar()
    mytext2 = StringVar()
    mytext3 = StringVar()
    mytext4 = StringVar()

    root = Main(win)
    win.geometry("600x600")
    win.maxsize(600,600)
    win.minsize(600,600)
    win.title("CONVERTER")
    
    win.config(background= 'bisque')
    
    win.mainloop()
