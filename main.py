from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()

root.geometry('1200x600+180+100')
root.overrideredirect(True)
root.title('Текстовый редактор')

# title bar

def min_win():
    root.attributes("-alpha", 0)
    root.minimized = True

def title():
    title_bar = Frame(root, bg='#2e2e2e', relief='raised')
    title_bar.pack(side=TOP, fill=BOTH)
    title_label = Label(title_bar,
                        text='                                                                                                                                                                                    Текстовый редоктор',
                        bg='#2e2e2e', fg='#7F5DBA')
    title_label.pack(side=LEFT)

    def move_window(event):
        root.geometry(+{0} + {1}.format(event.x_root, event.y_root))

    title_bar.bind('<B1-Motion>', move_window)

    close_button = Button(title_bar, text='  ×  ', command=root.destroy, bg='#2e2e2e',
                          font=("calibri", 13),
                          bd=0, fg='white', highlightthickness=0)
    minimize_button = Button(title_bar, text=' 🗕 ', command=min_win, bg='#2e2e2e', bd=0,
                             fg='white',
                             font=("calibri", 13), highlightthickness=0)
    close_button.pack(side=RIGHT)
    minimize_button.pack(side=RIGHT)

# change_font

def change_color_f():
    my_color = colorchooser.askcolor()[1]

    if my_color:
        color_font = font.Font(text, text.cget('font'))

        text.tag_configure('colored', font=color_font, foreground=my_color)

        current_tags = text.tag_names('sel.first')

        if 'colored' in current_tags:
            text.tag_remove('colored', 'sel.first', 'sel.last')
        else:
            text.tag_add('colored', 'sel.first', 'sel.last')


def bg_color_f():
    my_color = colorchooser.askcolor()[1]

    if my_color:
        text.config(bg=my_color)


def all_color_f():
    my_color = colorchooser.askcolor()[1]

    if my_color:
        text.config(fg=my_color)


def bold():
    bold_font = font.Font(text, text.cget('font'))
    bold_font.configure(weight='bold')

    text.tag_configure('bold', font=bold_font)

    current_tags = text.tag_names('sel.first')

    if 'bold' in current_tags:
        text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        text.tag_add('bold', 'sel.first', 'sel.last')


def italics():
    italics_font = font.Font(text, text.cget('font'))
    italics_font.configure(slant='italic')

    current_tags = text.tag_names('sel.first')

    text.tag_configure('italic', font=italics_font)

    if 'italic' in current_tags:
        text.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        text.tag_add('italic', 'sel.first', 'sel.last')


def overstrike():
    overstrike_font = font.Font(text, text.cget('font'))
    overstrike_font.configure(overstrike=True)

    current_tags = text.tag_names('sel.first')

    text.tag_configure('overstrike', font=overstrike_font)

    if 'overstrike' in current_tags:
        text.tag_remove('overstrike', 'sel.first', 'sel.last')
    else:
        text.tag_add('overstrike', 'sel.first', 'sel.last')


def underline():
    underline_font = font.Font(text, text.cget('font'))

    current_tags = text.tag_names('sel.first')

    if 'underline' in current_tags:
        text.tag_remove('underline', 'sel.first', 'sel.last')
    else:
        text.tag_add('underline', 'sel.first', 'sel.last')
        text.tag_configure('underline', underline=True)


def classic():
    classic_font = font.Font(text, text.cget('font'))
    classic_font.configure()

    current_tags = text.tag_names('sel.first')

    text.tag_configure('classic', font=classic_font)

    if 'classic' in current_tags:
        text.tag_remove('classic', 'sel.first', 'sel.last')
    else:
        text.tag_add('classic', 'sel.first', 'sel.last')


    # commands

def file_close_function():
    file_close = messagebox.askokcancel('Выход', 'Вы действительно хотите выйти из программы?')

    if file_close:
        root.destroy()


def file_open_function():
    file_open = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))

    if file_open:
        text.delete('1.0', END)
        text.insert('1.0', open(file_open, encoding='utf-8').read())


def file_save_function():
    file_save = filedialog.asksaveasfilename(
        filetypes=[('Все файлы', '*'), ('txt файлы', '*.txt'), ('Файлы Python', '*.py'), ('Файлы html', '*.html')])
    file = open(file_save, 'w', encoding='utf-8')
    text_file = text.get('1.0', END)
    file.write(text_file)
    file.close()

    # themes

def theme_selection(theme):
    text['bg'] = great_theme[theme]['text_bg']
    text['fg'] = great_theme[theme]['text_fg']
    text['inscrutable'] = great_theme[theme]['cursor']
    text['selectively'] = great_theme[theme]['select_bg']

    # font

def font_selection(f):
    text['font'] = fonts[f]['font']

    # delete

def delete_all():
    text.delete(1.0, 'end')

    # cut_text

def copy_text():
    text.config(text=text.get('sel.first', 'sel.last'))

def paste_text():
   text.paste(1.0, 'end')

def delete_text():
    text.delete('sel.first', 'sel.last')

# FILE_CLOSE_OPEN_SAVE

menu_main = Menu(root)
root.config(menu=menu_main)

file_m = Menu(menu_main, tearoff=0)
file_m.add_command(label='Открыть...', command=file_open_function)
file_m.add_command(label='Сохранить...', command=file_save_function)
file_m.add_separator()
file_m.add_command(label='Закрыть', command=file_close_function)

# THEMES

great_theme = dict(white={
    'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg': '#ff80d5'
}, black={
    'text_bg': 'black', 'text_fg': 'white', 'cursor': 'white', 'select_bg': '#999900'
}, mint={
    'text_bg': '#c4ffb3', 'text_fg': 'black', 'cursor': 'white', 'select_bg': '#a3c2c2'
}, purple={
    'text_bg': '#7F5DBA', 'text_fg': '#FF8000', 'cursor': 'white', 'select_bg': '#2e2e2e'
})

themes_m = Menu(menu_main, tearoff=0)
themes = Menu(themes_m, tearoff=0)
themes.add_command(label='Фиолетовая', command=lambda: (theme_selection('purple')))
themes.add_command(label='Темная', command=lambda: (theme_selection('black')))
themes.add_command(label='Светлая', command=lambda: (theme_selection('white')))
themes.add_command(label='Мятная', command=lambda: (theme_selection('mint')))
themes_m.add_cascade(label='Тема', menu=themes)

# FONT

fonts = {
    "Times New Roman":
        {
            'font': ('Times New Roman', 14)
        },
    'Arial':
        {
            'font': ('Arial', 14)
        },
    'Calibri':
        {
            'font': ('Arial', 14)
        },
    'Gill Sans Ultra Bold':
        {
            'font': ('Gill Sans Ultra Bold', 14)
        },
    'Mistral':
        {
            'font': ('Mistral', 14)
        },
    'Algerian':
        {
            'font': ('Algerian', 14)
        },
    'Bookman Old Style':
        {
            'font': ('Bookman Old Style', 14)
        },
    'Edwardian Script ITC':
        {
            'font': ('Edwardian Script ITC', 14)
        },
    'Castellar':
        {
            'font': ('Castellar', 14)
        },
    'Goudy Stout':
        {
            'font': ('Goudy Stout', 14)
        }
}

font_m = Menu(menu_main, tearoff=0)
font_view = Menu(font_m, tearoff=0)

font_view.add_command(label='Times New Roman', command=lambda: font_selection('Times New Roman'))
font_view.add_command(label='Arial', command=lambda: font_selection('Arial'))
font_view.add_command(label='Calibri', command=lambda: font_selection('Calibri'))
font_view.add_command(label='Mistral', command=lambda: font_selection('Mistral'))
font_view.add_command(label='Algerian', command=lambda: font_selection('Algerian'))
font_view.add_command(label='Castellar', command=lambda: font_selection('Castellar'))
font_view.add_command(label='Goudy Stout', command=lambda: font_selection('Goudy Stout'))
font_view.add_command(label='Bookman Old Style', command=lambda: font_selection('Bookman Old Style'))
font_view.add_command(label='Gill Sans Ultra Bold', command=lambda: font_selection('Gill Sans Ultra Bold'))
font_view.add_command(label='Edwardian Script ITC', command=lambda: font_selection('Edwardian Script ITC'))
root.config(menu=menu_main)

# CHANGE_FONT

change_font = Menu(menu_main, tearoff=0)
change = Menu(change_font, tearoff=0)

change_font.add_command(label='Жирный', command=bold)
change_font.add_command(label='Курсив', command=italics)
change_font.add_command(label='Подчеркнутый', command=underline)
change_font.add_command(label='Подчеркнутый по середине', command=overstrike)
change_font.add_separator()
change_font.add_command(label='Обычный', command=overstrike)
root.config(menu=menu_main)

# CHANGE_COLOR

change_color = Menu(menu_main, tearoff=0)
change_m = Menu(change_color, tearoff=0)

change_m.add_command(label='Цвет фона', command=bg_color_f)
change_m.add_command(label='Цвет текста', command=change_color_f)
change_m.add_command(label='Цвет всего текста', command=all_color_f)

# EDIT

edit_m = Menu(menu_main, tearoff=0)
edit = Menu(edit_m, tearoff=0)
edit.add_command(label='Копировать..', command=copy_text)
edit.add_command(label='Вставить..', command=lambda: paste_text)
edit.add_command(label='Вырезать..', command=lambda: delete_text())
edit.add_separator()
text_main = Text(undo=True)
edit.add_command(label='Отменить', command=text_main)
edit.add_command(label='Повторить', command=exit)
root.config(menu=menu_main)

# DELETE_ALL

delete_m = Menu(menu_main, tearoff=0)
delete = Menu(delete_m, tearoff=0)
delete.add_command(label='Очистить все...', command=delete_all)
root.config(menu=menu_main)

# ADD_LIST_MENU

root.config(menu=file_m)
root.config(menu=menu_main)
menu_main.add_cascade(label='   Файл    ', menu=file_m)
menu_main.add_cascade(label='   Редактирование    ', menu=edit)
menu_main.add_cascade(label='   Шрифт  ', menu=font_view)
menu_main.add_cascade(label='   Изменение шрифта    ', menu=change_font)
menu_main.add_cascade(label='   Цвет    ', menu=change_m)
menu_main.add_cascade(label='   Тема    ', menu=themes)
menu_main.add_cascade(label='   Очистить    ', menu=delete)

root.config(menu=menu_main)

# TEXT

text = Frame(root)
text.pack(fill=BOTH, expand=1) 

text = Text(text,
            bg='#7F5DBA',
            fg='#FF8000',
            padx=5,
            pady=10,
            wrap=WORD,
            insertbackground='white',
            selectbackground='#2e2e2e',
            spacing3=5
            )
text.pack(expand=1, fill=BOTH, side=LEFT)  

# SCROLLBAR

scroll = Scrollbar(text, command=text.yview)  
scroll.pack(side=RIGHT, fill=Y)  
text.config(yscrollcommand=scroll.set)  

title()

root.mainloop()
