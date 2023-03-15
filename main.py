from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from fpdf import FPDF
import sqlite3
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDColorPicker
from typing import Union
from kivymd_extensions.akivymd.uix.charts import AKBarChart,AKPieChart,AKLineChart
from kivymd.uix.filemanager import MDFileManager
import os

#import matplotlib
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
#from kivy.uix.image import Image
#from kivy.clock import Clock
kv=Builder.load_file("test1.kv")


class F1(Screen):
    pass

class Mbtn2(MDRaisedButton,HoverBehavior):
   
    ti=.2
    def on_enter(self, *args):
        self.md_bg_color = ("red")
        Animation(size_hint=(1, .13),d=self.ti).start(self)
     

    def on_leave(self, *args):
       
        self.md_bg_color = self.theme_cls.primary_light
        Animation(size_hint=(.9, .1),d=self.ti).start(self)

    

class Mcrd1(MDCard,HoverBehavior):
   
    ti=.4
 

    def on_enter(self, *args):
        self.md_bg_color = ("red")
        Animation(size_hint=(.2, .6),d=self.ti).start(self)
       
       

    def on_leave(self, *args):
       
        self.md_bg_color = self.theme_cls.primary_light
        Animation(size_hint=(.1, .5),d=self.ti).start(self)
      
       


class Main1(Screen):
    dbf=[]
  
    crow=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db = sqlite3.connect('main1.db')
        conn=db.cursor()
        cur=conn.execute("select ID,Timestamp,name,palce,amount,extra,status,balance,total from mdoc")
      
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 0.6),
            use_pagination=True,
            check=True,
            column_data=[(i[0],dp(30)) for i in cur.description]     
          
        )
        

        self.data_tables.bind(on_check_press=self.on_check_press)
       
        #self.add_widget(self.data_tables)
        self.ids.tbl.add_widget(self.data_tables)
       # self.sm.get_screen('sc1').ids.tbl.add_widget(self.data_tables)
        db.commit()
        db.close()
       
       



    def remove_row(self) -> None:
        
        
        if  self.crow[:]:
      
            x=self.crow[0]
            db = sqlite3.connect('main1.db')

            conn=db.cursor()
            qry="update mdoc set deadid=0 where ID=?"
            conn.execute(qry,(x,))

            db.commit()
            db.close()

            db1 = sqlite3.connect('main1.db')

            conn1=db1.cursor()

            data=conn1.execute('SELECT ID,Timestamp,name,palce,amount,extra,status,balance,total from mdoc where deadid=1')
        
            self.data_tables.row_data=[(i) for i in data]
            db1.commit()
            db1.close()
        else:
            print("row data in none ")
            Snackbar(text="[color=#ddbb34]Delete pls one row select![/color]",snackbar_x="5dp",snackbar_y="10dp",size_hint_x=.9,bg_color=(0, 0, 1, 1)).open()

    
    def clear(self) -> None:
        db = sqlite3.connect('main1.db')

        conn=db.cursor()
        conn.execute("SELECT ID,Timestamp,name,palce,amount,extra,status,balance,total from mdoc where deadid=1")
        for i in conn:
            try:
                self.data_tables.remove_row(i)
            except:
                Snackbar(text="[color=#ddbb34]list not loadinig![/color]",snackbar_x="5dp",snackbar_y="10dp",size_hint_x=.9,bg_color=(0, 0, 1, 1)).open()
              
                break
            
        db.commit()
        db.close()
 

       
    def list(self) ->None:
      
      

        db = sqlite3.connect('main1.db')

        conn=db.cursor()
        conn.execute('SELECT ID,Timestamp,name,palce,amount,extra,status,balance,total from mdoc where deadid=1')

        self.dbf=conn.fetchall()
        conn.execute('SELECT ID,Timestamp,name,palce,amount,extra,status,balance,total from mdoc where deadid=1')
        
        self.data_tables.row_data=[(i) for i in conn]

        db.commit()
        db.close()
    def search(self):
        a=self.ids.search1.text
        
        j=self.dbf

       
        data=[i for i in j if a in i]
        self.data_tables.row_data=[(x) for x in data]
    def on_update(self,*args):

        a=self.result
        print(a)
     
    

    def on_check_press(self, instance_table, current_row ):
        print(current_row)
        self.crow=current_row
        self.manager.get_screen('sc3').ids.id3.text=current_row[0]
        self.manager.get_screen('sc3').ids.da.text=current_row[1]
        self.manager.get_screen('sc3').ids.pl.text=current_row[2]
        self.manager.get_screen('sc3').ids.na.text=current_row[3]
        self.manager.get_screen('sc3').ids.am.text=current_row[4]
        self.manager.get_screen('sc3').ids.ex.text=current_row[5]
        self.manager.get_screen('sc3').ids.swi.active=current_row[6]
        self.manager.get_screen('sc3').ids.blan.text=current_row[7]

class Add(Screen):
    
    
    switc=False
    
   
    def sw(self,switch,  value):
        if value:
            self.switc=True
        else:
            self.switc=False
    def addbutton(self):
       
        
        date=self.ids.tdate.text
        a=self.ids.t1.text 
        b=self.ids.t2.text  
        c=self.ids.t3.text
        d=self.ids.t4.text 
        f=self.switc
        g=self.ids.t6.text
        h=1

      
        
     
        if a and b and c and d  and g and h and date:
            db = sqlite3.connect('main1.db')
        

            conn = db.cursor()
      
        
        
            sql = ("insert into mdoc(Timestamp,name,palce,amount,extra,status,balance,total,deadid) values(?,?,?,?,?,?,?,?,?);")
            v=int(c)+int(d)
            conn.execute(sql, (date,a, b,c,d,f,g,v,h))
        
            db.commit()
            db.close()
            
          
            self.dialogok()
         
            self.ids.tdate.text=""
            self.ids.t1.text=""
            self.ids.t2.text=""
            self.ids.t3.text=""  
            self.ids.t4.text=""
            
            
            switc=False
            self.ids.t6.text="" 
       
            
           
        else:
           
           
            self.dialogfun() 
  
           
            self.ids.tdate.text=""
            self.ids.t1.text=""
            self.ids.t2.text=""
            self.ids.t3.text=""  
            self.ids.t4.text=""
         
            
            switc=False
            self.ids.t6.text=""
      
    def dialogfun(self):
        self.dialog = MDDialog(
                    text="Not value all value filling",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            on_press=self.chageok
                            
                        ),
                        MDFlatButton(
                            text="ok",
                            on_press=self.chagenotok
                           
                        
                        ),
                    ],
                )
        self.dialog.open()
    def dialogok(self):
        self.dialog = MDDialog(
                    text="sucessfully add your data",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            on_press=self.chageok
                            
                        ),
                        MDFlatButton(
                            text="ok",
                            on_press=self.chagenotok
                           
                        
                        ),
                    ],
                )
        self.dialog.open()
    def chageok(self ,instance_button: MDRaisedButton):
        self.dialog.dismiss()
        self.manager.current = 'sc1'
        
     
    def chagenotok(self,instance_button: MDRaisedButton):
        self.dialog.dismiss()
        self.manager.current = 'sc2'

        

class Update(Screen):
  
   # def __init__(self,**kwargs):
   #     super().__init__(**kwargs)

    switc=None
    def sw(self,switch,  value):
        if value:
            self.switc=True
        else:
            self.switc=False
    def upd(self):
        id3=self.ids.id3.text
        date=self.ids.da.text
        a=self.ids.pl.text 
        b=self.ids.na.text  
        c=self.ids.am.text
        d=self.ids.ex.text 
        f=self.switc
        g=self.ids.blan.text
      
        
        if a and b and c and d  and g  and date:
            db = sqlite3.connect('main1.db')
        

            conn = db.cursor()
            

            v=int(c)+int(d)
         
      
        
        
            sql = "update mdoc set ID=?,Timestamp=?,name=?,palce=?,amount=?,extra=?,status=?,balance=?,total=? where ID=?"
            v=int(c)+int(d)
            conn.execute(sql, (id3,date,a,b,c,d,f,g,v,id3,))
        
            db.commit()
            db.close()
            
         
            self.ids.id3.text=""
            self.ids.da.text=""
            self.ids.pl.text=""
            self.ids.na.text="" 
            self.ids.am.text=""
            self.ids.ex.text=""
            self.switc=False
            self.ids.blan.text=""
            print("update sucessfully")
            Snackbar(text="[color=#ddbb34]update sucessfully![/color]",snackbar_x="5dp",snackbar_y="10dp",size_hint_x=.9,bg_color=(0, 0, 1, 1)).open()
          
        else:
           
           
            
            self.ids.id3.text=""
            self.ids.da.text=""
            self.ids.pl.text=""
            self.ids.na.text="" 
            self.ids.am.text=""
            self.ids.ex.text=""
            self.switc=False
            self.ids.blan.text=""
            Snackbar(text="[color=#ddbb34]pls select one row select![/color]",snackbar_x="5dp",snackbar_y="10dp",size_hint_x=.9,bg_color=("red")).open()


class Export(Screen):
    pass
    
        #url='https://www.google.com'
        #webbrowser.open_new(url)

class Carddev(Screen):
     
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.on_bar_chats()
        self.on_pie_chats()
        self.on_line_chats()

  
    def on_bar_chats(self):    
        
      
       
        self.barchart = AKBarChart(
            x_values=[1,2,3,4],
            y_values=[10,20,40,30],
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            
            
        )
        self.ids.akbarchat.add_widget(self.barchart)

    def on_pie_chats(self):
        #obj=int(5, 2,3,4)
        
        self.piechart = AKPieChart(
            items=[{"python":40,"java":30,"node":20,"ruby":10}],
            pos_hint={"center_x": 0.5, "center_y": 0.5},  
        )
        self.ids.akpiechat.add_widget(self.piechart)
    def on_line_chats(self):
        #obj=int(5, 2,3,4)
          
       
      
        self.linechart = AKLineChart(
            x_values=([1,2,3,4,5,6]),
            y_values=([20,40,60,80,90,110]),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            
            
        )
        self.ids.aklinechat.add_widget(self.linechart)
class Gmap(Screen):


    
       
    def on_map(self):
        from temp.kivy_garden.mapview import MapView
        self.map = MapView(zoom=11, lat=50.6394, lon=3.057)
        self.ids.mapping.add_widget(self.map)
        
class Color1(Screen):
    pass

        

class MainApp(MDApp):

    sm = ScreenManager()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.date_dialog = MDDatePicker(min_year=2000, max_year=2040)
       
        self.color_picker= MDColorPicker()

        self.pdf = FPDF()
        self.file =MDFileManager(
            select_path=self.filepath,
            exit_manager=self.exitmanger,
            preview=True
        ) 
      
      
     
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='Purple'
        self.sm.add_widget(F1(name='sc0'))
        self.sm.add_widget(Main1(name='sc1'))
        self.sm.add_widget(Add(name='sc2'))
        self.sm.add_widget(Update(name='sc3'))
        self.sm.add_widget(Export(name='sc4'))
        self.sm.add_widget(Carddev(name='sc5'))
        self.sm.add_widget(Gmap(name='sc6')) 
        self.sm.add_widget(Color1(name='sc7'))          
        
        return self.sm
  

 
    
    def on_cancel(self, instance, value):
        print(value)

    def on_save(self, instance, value, date_range):
     
        self.sm.get_screen('sc2').ids.tdate.text=str(value)
        self.sm.get_screen('sc3').ids.da.text=str(value)
        

    def show_date_picker(self):
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.date_dialog.open()

    

    def filepath(self,path):
        
        self.dir=path
        self.exitmanger()
    def open_file_mgr(self):
        from kivy.utils import platform
        
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
            self.file.show('/')
        else:
            Snackbar(text="[color=#ddbb34]pls need primisstion![/color]",snackbar_x="5dp",snackbar_y="10dp",size_hint_x=.9,bg_color=("red")).open()

    def exitmanger(self):
        self.file.close()

    def pdffun(self):
        j=[]
        i=[]
        db = sqlite3.connect('main1.db')

        conn=db.cursor()
        conn.execute("SELECT ID,Timestamp,name,palce,amount,extra,balance,total from mdoc where deadid=1")
      
        
  
        self.pdf.add_page()
 
        self.pdf.set_font("Arial", size = 10)
        self.pdf.cell(0, 5, txt = "this header", align = 'C',ln=1,border=1)
      
         
            #i='{} {} {} {} {} {} {} {}'.format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7])
       
           
        self.pdf.cell(10, 10, txt = "ID", align = 'L',border=1)
        self.pdf.cell(20, 10, txt = "Date", align = 'L',border=1)
        self.pdf.cell(40, 10, txt = "Name", align = 'L',border=1)
        self.pdf.cell(40, 10, txt = "address", align = 'L',border=1)
        self.pdf.cell(20, 10, txt = "amount", align = 'L',border=1)
        self.pdf.cell(20, 10, txt = "extra", align = 'L',border=1)
        self.pdf.cell(20, 10, txt = "balance", align = 'L',border=1)
        self.pdf.cell(20, 10, txt = "total", align = 'L',border=1,ln=1)


        

    
       
      #  self.pdf.line(5,10,205,10)
            
        for j in conn:
         
            #i='{} {} {} {} {} {} {} {}'.format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7])
       
            self.pdf.cell(10, 10, txt = str(j[0]), align = 'L',border=1)
            self.pdf.cell(20, 10, txt = str(j[1]), align = 'L',border=1)
            self.pdf.cell(40, 10, txt = str(j[2]), align = 'L',border=1)
            self.pdf.cell(40, 10, txt = str(j[3]), align = 'L',border=1)
            self.pdf.cell(20, 10, txt = str(j[4]), align = 'L',border=1)
            self.pdf.cell(20, 10, txt = str(j[5]), align = 'L',border=1)
            self.pdf.cell(20, 10, txt = str(j[6]), align = 'L',border=1)
            self.pdf.cell(20, 10, txt = str(j[7]), align = 'L',border=1,ln=1)


            
           
       
        self.pdf.ln(h='')
        self.pdf.set_y(-25)
        self.pdf.set_font("Arial", size = 10)
        self.pdf.cell(0, 10, txt = 'this is footer ', align = 'C',border=1,)
           
       
      

 
        self.pdf.output(self.dir+"/op.pdf")
      
        db.commit()
        db.close()
    

    def open_pdf_file(self):
        pdf_file_name = 'op.pdf'
        import webbrowser, os
        #webbrowser.open(f'file://{os.getcwd()}/{pdf_file_name}')
        webbrowser.open(f'file://{self.dir}/{pdf_file_name}')


  
        
if __name__ == "__main__":
    MainApp().run()


