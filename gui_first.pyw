from tkinter import *
from tkinter import filedialog
from styles.estilo_colores import  *

#from estilo_colores import tema_selector
raiz = Tk()
raiz.title("CA-AD")
raiz.iconbitmap("BLUE_D_MULTI.ico")
raiz.config(bg=ef1)


#abrir archivo de tipo ETABS o SAP
def abrirarchivo():
    archivo=filedialog.askopenfilename(title="Abrir archivo Etabs",filetypes=(("Archivo Etabs","*.edb"),("Archivo SAP","*.sdb"),("Todos los Archivos", "*.*")))
    print(archivo)
bt_abrir=Button(raiz,text="Abrir Archivo",command=abrirarchivo)
bt_abrir.config(bg=ef3,fg=et1)
bt_abrir.pack()



#------------------------------------------------------------------------------






raiz.mainloop()



