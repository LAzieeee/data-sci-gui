from tkinter import messagebox
import pandas as pd
from tkinter import *
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
df = pd.read_csv("D:\main_project\csv\googleplaystore.csv")

df_nonan = df.fillna("0")

main_window = Tk()
main_window.title('with user')
main_window.configure(bg="#FAEBD7")
nickname = Label(main_window, text="Nickname:", background='#FAEBD7')
nickname.place(relx=0.46, rely=0.3, anchor=N)
your_name = Entry(main_window)
your_name.place(relx=0.53, rely=0.3, anchor=N)
category_set = set(df_nonan["Category"])
category_list = list(category_set)
list_cate = []
for i in range(len(category_list)):
    list_cate.append(category_list[i])

def program_app():
    newWindow = Tk()
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    newWindow.configure(bg='#FAEBD7')

    title = Label(newWindow, text="Hello, " + your_name.get() + "." + " This program will help you to choose app that you want.", background="#FAEBD7")
    title.config(font =("Times", 20))
    title.pack(pady=30)

    dropd_cate = Combobox(newWindow, width=35, font=('Times', 20, 'bold'), height=20)
    dropd_cate["values"] = list_cate
    dropd_cate.set("Choose app category")
    dropd_cate.place(relx=0.5, rely=0.1, anchor=N)

    dropd_type_apps = Combobox(newWindow, width=35, font=('Times', 20, 'bold'))
    dropd_type_apps["values"] = ["Free apps","Paid apps","All apps"]
    dropd_type_apps.set("Choose app type")
    dropd_type_apps.place(relx=0.5, rely=0.2, anchor=N)

    dropd_popular_apps = Combobox(newWindow, width=35, font=('Times', 20, 'bold'))
    dropd_popular_apps["values"] = ["High","Medium","Low","Not choose"]
    dropd_popular_apps.set("Choose app popular level")
    dropd_popular_apps.place(relx=0.5, rely=0.3, anchor=N)
    
    def type_value():
        global list_size_apps_for_details, list_last_update_for_details, list_current__ver_for_details, list_android_ver_for_details, list_rating_apps_fordetails, list_contentrating_apps_for_details
        list_apps = []
        list_types = []
        list_apps_installs = []
        list_apps_installs_nosymbols = []
        list_price = []
        global list_combo_box_apps
        list_combo_box_apps = []
        list_last_update = []
        list_current__ver = []
        list_android_ver = []
        list_size_apps = []
        list_size_apps_for_details = []
        list_last_update_for_details = []
        list_current__ver_for_details = []
        list_android_ver_for_details = []
        list_rating_apps = []
        list_rating_apps_fordetails = []
        list_contentrating_apps = []
        list_contentrating_apps_for_details = []
        if dropd_type_apps.get() == dropd_type_apps["values"][0]:
            df_cate = df_nonan[df_nonan["Category"] == str(dropd_cate.get())]
            for i in df_cate["Type"]:
                list_types.append(i)
            for l in df_cate["App"]:
                list_apps.append(l)
            for p in df_cate["Installs"]:
                list_apps_installs.append(p)
            for n in list_apps_installs:
                number1 = n.replace(",", "")
                number2 = number1.replace("+", "")
                list_apps_installs_nosymbols.append(number2)
            for h in df_cate["Size"]:
                list_size_apps.append(h)
            for d in df_cate["Last Updated"]:
                list_last_update.append(d)
            for g in df_cate["Current Ver"]:
                list_current__ver.append(g)
            for a in df_cate["Android Ver"]:
                list_android_ver.append(a)
            for f in df_cate["Rating"]:
                list_rating_apps.append(f)
            for m in df_cate["Content Rating"]:
                list_contentrating_apps.append(m)
            for j in range(len(list_types)):
                if list_types[j] == "Free":
                    if dropd_popular_apps.get() == dropd_popular_apps["values"][0]:
                        if int(list_apps_installs_nosymbols[j]) < 1000000:
                            txt = list_apps[j]
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    elif dropd_popular_apps.get() == dropd_popular_apps["values"][1]:
                        if int(list_apps_installs_nosymbols[j]) >= 1000000 and int(list_apps_installs_nosymbols[j]) < 10000000:
                            txt = list_apps[j]
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    elif dropd_popular_apps.get() == dropd_popular_apps["values"][1]:
                        if int(list_apps_installs_nosymbols[j]) > 10000000:
                            txt = list_apps[j]
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    else:
                        txt = list_apps[j]
                        list_combo_box_apps.append(txt)
                        list_size_apps_for_details.append(list_size_apps[j])
                        list_last_update_for_details.append(list_last_update[j])
                        list_current__ver_for_details.append(list_current__ver[j])
                        list_android_ver_for_details.append(list_android_ver[j])
                        list_rating_apps_fordetails.append(list_rating_apps[j])
                        
                    

        elif dropd_type_apps.get() == dropd_type_apps["values"][1]:
            df_cate = df_nonan[df_nonan["Category"] == str(dropd_cate.get())]
            for i in df_cate["Type"]:
                list_types.append(i)
            for l in df_cate["App"]:
                list_apps.append(l)
            for p in df_cate["Installs"]:
                list_apps_installs.append(p)
            for n in list_apps_installs:
                number1 = n.replace(",", "")
                number2 = number1.replace("+", "")
                list_apps_installs_nosymbols.append(number2)
            for y in df_cate["Price"]:
                list_price.append(y)
            for h in df_cate["Size"]:
                list_size_apps.append(h)
            for d in df_cate["Last Updated"]:
                list_last_update.append(d)
            for g in df_cate["Current Ver"]:
                list_current__ver.append(g)
            for a in df_cate["Android Ver"]:
                list_android_ver.append(a)
            for f in df_cate["Rating"]:
                list_rating_apps.append(f)
            for m in df_cate["Content Rating"]:
                list_contentrating_apps.append(m)
            for j in range(len(list_types)):
                if list_types[j] == "Paid":
                    if dropd_popular_apps.get() == dropd_popular_apps["values"][0]:
                        if int(list_apps_installs_nosymbols[j]) < 1000000:
                            txt = list_apps[j] + " " + str(list_price[j])
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    elif dropd_popular_apps.get() == dropd_popular_apps["values"][1]:
                        if int(list_apps_installs_nosymbols[j]) >= 1000000 and int(list_apps_installs_nosymbols[j]) < 10000000:
                            txt = list_apps[j] + " " + str(list_price[j])
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    elif dropd_popular_apps.get() == dropd_popular_apps["values"][1]:
                        if int(list_apps_installs_nosymbols[j]) > 10000000:
                            txt = list_apps[j] + " " + str(list_price[j])
                            list_combo_box_apps.append(txt)
                            list_size_apps_for_details.append(list_size_apps[j])
                            list_last_update_for_details.append(list_last_update[j])
                            list_current__ver_for_details.append(list_current__ver[j])
                            list_android_ver_for_details.append(list_android_ver[j])
                            list_rating_apps_fordetails.append(list_rating_apps[j])
                    else:
                        txt = list_apps[j] + " " + str(list_price[j])
                        list_combo_box_apps.append(txt)
                        list_size_apps_for_details.append(list_size_apps[j])
                        list_last_update_for_details.append(list_last_update[j])
                        list_current__ver_for_details.append(list_current__ver[j])
                        list_android_ver_for_details.append(list_android_ver[j])
                        list_rating_apps_fordetails.append(list_rating_apps[j])


        elif dropd_type_apps.get() == dropd_type_apps["values"][2]:
            df_cate = df_nonan[df_nonan["Category"] == str(dropd_cate.get())]
            for i in df_cate["App"]:
                list_apps.append(i)
            for h in df_cate["Size"]:
                list_size_apps.append(h)
            for d in df_cate["Last Updated"]:
                list_last_update.append(d)
            for g in df_cate["Current Ver"]:
                list_current__ver.append(g)
            for a in df_cate["Android Ver"]:
                list_android_ver.append(a)
            for f in df_cate["Rating"]:
                list_rating_apps.append(f)
            for m in df_cate["Content Rating"]:
                list_contentrating_apps.append(m)
            for j in range(len(df_cate["App"])):
                txt = list_apps[j]
                list_combo_box_apps.append(txt)
                list_size_apps_for_details.append(list_size_apps[j])
                list_last_update_for_details.append(list_last_update[j])
                list_current__ver_for_details.append(list_current__ver[j])
                list_android_ver_for_details.append(list_android_ver[j])
                list_rating_apps_fordetails.append(list_rating_apps[j])

        def moredetails():
                    root = Tk()
                    root.configure(bg="#FAEBD7")
                    root.attributes('-fullscreen', True)
                    bt_exit = Button(root, text="exit", command=root.destroy)
                    bt_exit.pack(side=BOTTOM)
                    for i in range(len(list_combo_box_apps)):
                        if dropd_choose_apps.get() == list_combo_box_apps[i]:
                            details = Label(root, text="App: " + str(list_combo_box_apps[i]) + "\n" + "Rating: "+ str(list_rating_apps_fordetails[i]) + "\n" + "Size: " + str(list_size_apps_for_details[i])+ "\n" + "Last update: " + str(list_last_update_for_details[i])+ "\n" + "Current version: " + str(list_current__ver_for_details[i])+ "\n" + "Andriod version: " + str(list_android_ver_for_details[i]), foreground="black", background='#FAEBD7')
                            details.config(font =("Times", 30))
                            details.place(relx=0.5, rely=0.45, anchor=CENTER)

        if len(list_combo_box_apps) > 0:
            global dropd_choose_apps
            dropd_choose_apps = Combobox(newWindow, width=60, font=('Times', 20, 'bold'))
            dropd_choose_apps["values"] = list_combo_box_apps
            dropd_choose_apps.set("There're apps for you," + your_name.get() + " .Please choose your app =>")
            dropd_choose_apps.place(relx=0.5, rely=0.6, anchor=N)
            bt_details_app = Button(newWindow, text="more app details", command=moredetails)
            bt_details_app.place(relx=0.5, rely=0.7, anchor=N)
        else:
            messagebox.showinfo("message","There are no apps like this on my list.Try again!")
            newWindow.destroy()

        
    bt_cate = Button(newWindow, text="Find apps", command=type_value, width=20)
    bt_cate.place(relx=0.5, rely=0.4, anchor=N)

    bt_exit = Button(newWindow, text="exit", command=newWindow.destroy)
    bt_exit.pack(side=BOTTOM)

    newWindow.attributes('-fullscreen', True)
    newWindow.mainloop()

def program_graph():
    graph_tk = Tk()
    graph_tk.configure(bg="#FAEBD7")
    #plot1
    df2 = set(df["Category"])
    list_df2 = list(df2)
    rating_list = []
    for i in range(len(list_df2)):
        df_category = df[df["Category"] == list_df2[i]]
        rating_ave = df_category["Rating"].mean()
        rating_round = round(rating_ave, 2)
        rating_list.append(rating_round)
    
    number_of_colors = len(list_df2)
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)]
    fig = Figure(figsize = (20, 10),dpi = 70)
    fig.patch.set_facecolor('#FAEBD7')
    plot1 = fig.add_subplot(111)
    plot1.barh(list_df2,rating_list, color= color) 
    plot1.set_title('Average rating of each category', fontsize=30)
    plot1.set_xlabel('Average rating', fontsize=30)
    plot1.set_ylabel('Category', fontsize=30)
    plot1.set_facecolor('#FAEBD7')
    plot1.yaxis.label.set_color('red')
    plot1.xaxis.label.set_color('red')
    plot1.title.set_color('red')
    canvas = FigureCanvasTkAgg(fig, master = graph_tk)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, graph_tk)   
    toolbar.update()
    canvas.get_tk_widget().pack()

    bt_exit = Button(graph_tk, text="exit", command=graph_tk.destroy)
    bt_exit.pack(side=BOTTOM)

    graph_tk.attributes('-fullscreen', True)
    graph_tk.mainloop()

img = PhotoImage(file='D:\main_project\project\images/tumblr_omdunsURAr1rsvr3vo1_540.png')
bg_point = Label(main_window,image=img, bg='#FAEBD7')
bg_point.pack()
bg_point.place(relx=0.9, rely=0.7, anchor=CENTER)

from tkinter.ttk import *
style_app = Style()
style_app.configure('W.TButton', font =('Times', 30))
style_app.map('W.TButton', foreground=[('!active', 'black'),('pressed', 'black'), ('active', 'black')],background=[('!active', 'yellow'),('active', 'lightblue')])

style_graph = Style()
style_graph.configure('E.TButton', font =('Times', 30))
style_graph.map('E.TButton', foreground=[('!active', 'black'),('pressed', 'black'), ('active', 'black')],background=[('!active', 'yellow'),('active', 'lightblue')])

style_exit = Style()
style_exit.configure('A.TButton', font =('Times', 10))
style_exit.map('A.TButton', foreground=[('active', 'red'),('!active', 'red')])

bt_app = Button(main_window, style="W.TButton", text="App selector", command=program_app, width=13)
bt_app.place(relx=0.5, rely=0.4, anchor=N)

bt_graph = Button(main_window, style="E.TButton", text="Graph", command=program_graph, width=13)
bt_graph.place(relx=0.5, rely=0.5, anchor=N)

bt_exit_main = Button(main_window, text="exit", command=main_window.destroy, style="A.TButton")
bt_exit_main.pack(side=BOTTOM)
main_window.attributes('-fullscreen', True)
main_window.mainloop()

