# imports 
import tkinter as tk

# Retro style theme color
THEME_COLOR = {
    "text": "#31353f",
    "background": "#f4f5f4",
    "primary": "#c0b89b",
    "secondary": "#bec0b1",
    "accent": "#7c7f82"
}

# Global font
REGULAR_TEXT_SIZE = ('monospace', 12)
LARGE_TEXT_SIZE = ('monospace', 14)
HEADING_TEXT_SIZE = ('monospace', 18)

# Window setting
WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Registration Form"

# create window object
window = tk.Tk()

# set window title
window.title(WINDOW_TITLE)

# set window size and not resizable
window.geometry(str(WINDOW_SIZE[0])+'x'+str(WINDOW_SIZE[1]))
window.resizable(0, 0)

# set theme background color
window.config(background=THEME_COLOR["text"])

# create container to store all the widgets
main_frame_pos = (600, 500)
main_frame = tk.Frame(
        window,
        background=THEME_COLOR["primary"],
        width=main_frame_pos[0],
        height=main_frame_pos[1],
        relief="groove",
        bd=10
)

main_frame.place(
        x=WINDOW_SIZE[0] // 2 - (main_frame_pos[0] // 2),
        y=WINDOW_SIZE[1] // 2 - (main_frame_pos[1] // 2)
)

# create heading
tk.Label(
        window,
        text="Registration Form",
        font=HEADING_TEXT_SIZE,
        bg=THEME_COLOR["text"],
        fg=THEME_COLOR["background"],
        bd=5,
).place(x=WINDOW_SIZE[0]//2 - 120, y=2)

# set label frame size
info_box_size = (main_frame_pos[0] - 60, 190)

# - Personal Information
personal_information_frame = tk.LabelFrame(
        main_frame,
        text="Personal Information",
        width=info_box_size[0],
        height=info_box_size[1],
        bg=THEME_COLOR["primary"],
        padx=50,
        pady=50,
        bd=4,
        relief="ridge",
        font=LARGE_TEXT_SIZE
).place(x=20, y=20)

#####################################
#         first name label          #
#####################################
tk.Label(
        main_frame,
        text="First Name",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["primary"]
).place(x=20+20, y=30+20)

fn_entry_var = tk.StringVar()
fn_entry = tk.Entry(
        main_frame,
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["secondary"],
        textvariable=fn_entry_var
).place(x=20+20, y=60+20)


#####################################
#         last name label           #
#####################################
tk.Label(
        main_frame,
        text="Last Name",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["primary"]
).place(x=290+20+20, y=30+20)

ln_entry_var = tk.StringVar()
ln_entry = tk.Entry(
        main_frame,
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["secondary"],
        textvariable=ln_entry_var
).place(x=290+20+20, y=60+20)

#####################################
#         username label            #
#####################################
tk.Label(
        main_frame,
        text="Username",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["primary"]
).place(x=20+20, y=70+30+20)

un_entry_var = tk.StringVar()
un_entry = tk.Entry(
        main_frame,
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["secondary"],
        textvariable=un_entry_var
).place(x=20+20, y=70+60+20)

#####################################
#         password label            #
#####################################
tk.Label(
        main_frame,
        text="Password",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["primary"]
).place(x=290+20+20, y=70+30+20)

pwd_entry_var = tk.StringVar()
pwd_entry = tk.Entry(
        main_frame,
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR["secondary"],
        show="*",
        textvariable=pwd_entry_var
).place(x=290+20+20, y=70+60+20)

# - General Information
general_information_frame = tk.LabelFrame(
        main_frame,
        text="General Information",
        width=info_box_size[0],
        height=info_box_size[1],
        bg=THEME_COLOR["primary"],
        padx=50,
        pady=50,
        bd=4,
        relief="ridge",
        font=LARGE_TEXT_SIZE
).place(x=20, y=20+info_box_size[1])

tk.Label(
        main_frame,
        text="Preffered Language",
        bg=THEME_COLOR["primary"],
        font=LARGE_TEXT_SIZE
).place(x=40, y=20+info_box_size[1]+30)

c_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="C",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=c_cb
).place(x=40, y=20+info_box_size[1]+40+20)

cpp_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="C++",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=cpp_cb
).place(x=40, y=20+info_box_size[1]+40+60)

java_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="Java",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=java_cb
).place(x=40, y=20+info_box_size[1]+40+100)

python_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="Python",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=python_cb
).place(x=145, y=20+info_box_size[1]+40+20)

rust_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="Rust",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=rust_cb
).place(x=145, y=20+info_box_size[1]+40+60)

go_cb = tk.IntVar()
tk.Checkbutton(
        main_frame,
        text="Golang",
        bg=THEME_COLOR["primary"],
        font=REGULAR_TEXT_SIZE,
        variable=go_cb
).place(x=145, y=20+info_box_size[1]+40+100)

# course thingy
tk.Label(
        main_frame,
        text="Certification",
        bg=THEME_COLOR["primary"],
        font=LARGE_TEXT_SIZE
).place(x=40+245, y=20+info_box_size[1]+30)

course_kind_rb = tk.IntVar(); course_kind_rb.set(1) # set default value to be `online`
tk.Radiobutton(
        main_frame,
        text="Online",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR['primary'],
        value=1,
        variable=course_kind_rb
).place(x=145+140, y=20+info_box_size[1]+40+20)

tk.Radiobutton(
        main_frame,
        text="Offline",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR['primary'],
        value=2,
        variable=course_kind_rb
).place(x=145+280, y=20+info_box_size[1]+40+20)


tk.Label(
        main_frame,
        text="Select Course",
        bg=THEME_COLOR["primary"],
        font=LARGE_TEXT_SIZE
).place(x=40+245, y=20+info_box_size[1]+110)

course_lb_item = tk.StringVar(); course_lb_item.set("WebDev AI Python Java C C++ DSA")
course_lb_getter = tk.StringVar()

course_scrollbar = tk.Scrollbar(
        main_frame,
        orient=tk.VERTICAL
)
course_scrollbar.place(x=145+280, y=20+info_box_size[1]+40+100)

course_lb = tk.Listbox(
        main_frame,
        yscrollcommand=course_scrollbar.set,
        listvariable=course_lb_item,
        height=1,
        width=13,
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR['secondary']
)
course_lb.place(x=145+140, y=20+info_box_size[1]+40+100)
course_scrollbar['command'] = course_lb.yview

def submit_button_action():
    first_name = fn_entry_var.get()
    last_name = ln_entry_var.get()
    username = un_entry_var.get()
    password = pwd_entry_var.get()

    checkbuttons = (
            c_cb,
            cpp_cb,
            java_cb,
            python_cb,
            rust_cb,
            go_cb
    )

    checkbuttons_title = (
            "C",
            "C++",
            "Java",
            "Python",
            "Rust",
            "Go"
    )

    print("----------------------------\n\n")

    checkbutton_printable = ["%8s: %s\n" % (checkbuttons_title[checkbutton_index], 'true' if checkbuttons[checkbutton_index].get() == 1 else 'false') for checkbutton_index in range(len(checkbuttons))]
    print("%12s: %s\n%12s: %s\n%12s: %s\n%12s: %s" % ("First Name", first_name, "Last Name", last_name, "Username", username, "Password", password))

    print("\n----------------------------\n")

    for cp in checkbutton_printable: print(cp, end='')

    print("\n----------------------------\n")

    courses = course_lb_item.get()
    courses = courses.replace("'", "").replace("(", "").replace(")", "").replace(',', '')

    print("  -> User has selected %4s as %s Certification course." % (courses.split(' ')[course_lb.nearest(0)], 'Online' if course_kind_rb.get() == 1 else 'Offline'))

    print("\n----------------------------\n\n")

    fn_entry_var.set("")
    ln_entry_var.set("")
    un_entry_var.set("")
    pwd_entry_var.set("")

    [checkbutton.set(0) if checkbutton.get() == 1 else None for checkbutton in checkbuttons]

# sumbit button
tk.Button(
        main_frame,
        text="Submit",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR['secondary'],
        fg=THEME_COLOR['text'],
        relief='raised',
        bd=2,
        command=submit_button_action
).place(x=main_frame_pos[0]//2-140, y=main_frame_pos[1]-80)

# cancel button
tk.Button(
        main_frame,
        text="Cancel",
        font=REGULAR_TEXT_SIZE,
        bg=THEME_COLOR['secondary'],
        fg=THEME_COLOR['text'],
        relief='raised',
        bd=2,
        command=window.destroy
).place(x=main_frame_pos[0]//2+20, y=main_frame_pos[1]-80)

# run app
window.mainloop()
