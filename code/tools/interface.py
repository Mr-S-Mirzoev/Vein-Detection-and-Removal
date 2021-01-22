from filter import filter_mask, filter_pipe
from filter import median_filter, equalize_filter
import image

# img_viewer.py

from copy import deepcopy
import PySimpleGUI as sg
import os.path
import cv2

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(filename="", key="-IMAGE-")],
]

filter_choose_column = [
    [sg.Text("Choose which filters to apply:")],
    [sg.Checkbox('Gray Equalize', size=(12, 1), key='-GRAY-EQUALIZE-'), sg.Checkbox('Equalize', size=(20, 1), key='-EQUALIZE-')],
    [[sg.Checkbox('Median', size=(12, 1), key='-MEDIAN-')]
    [sg.Button("Save result", key='-SAVE-'), sg.Button("Apply", key='-APPLY-')],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(filter_choose_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout, icon='code/tools/image.png')
last_file = None
last_filtered_file = None

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)

            imgCV = image.ImageData(filename)
            last_file = imgCV
            imgbytes = imgCV.make_gui_format()
            
            window["-IMAGE-"].update(data=imgbytes)

        except Exception as e:
            print("Failed: {}".format(e))
            pass

    elif event == '-APPLY-':
        if last_file:
            imgCV = deepcopy(last_file)

            pipe = list()
            mask = filter_mask.get_bit_mask(values)
            
            if filter_mask.is_equalized(mask):
                pipe.append(equalize_filter.EqualizeFilter())

            if filter_mask.is_g_equalized(mask):
                pipe.append(equalize_filter.EqualizeFilter(gray=True))

            if filter_mask.is_normalized(mask):
                pipe.append(median_filter.MedianBlurFilter())

            fil_pipe = filter_pipe.FilterPipe(pipe)
            result = fil_pipe.work(imgCV)
            last_filtered_file = deepcopy(result)
            
            imgbytes = result.make_gui_format()

            window["-IMAGE-"].update(data=imgbytes)

    elif event == '-SAVE-':
        sg.theme("DarkTeal2")
        """
        fname = sg.Window('My Script',
                        [[sg.Text('Document to open')],
                        [sg.In(), sg.FileBrowse()],
                        [sg.Save(), sg.Cancel()]],
                        icon="code/tools/save.png").read(close=True)[1][0]
       
        if not fname:
            sg.popup("Cancel", "No filename supplied",
                     icon="code/tools/save.png")
            print("Cancelling: no filename supplied")
        else:
            sg.popup('The filename you chose was', fname)
        """
        import PySimpleGUI as sg

        layout = [
            [
                sg.InputText(key='File to Save', default_text='filename',
                            enable_events=True),
                sg.InputText(key='Save As', do_not_clear=False,
                            enable_events=True, visible=False),
                sg.FileSaveAs(initial_folder='.')
            ],
            [
                sg.Button(button_text="OK", key="--SAVE-PATH-VERIFIED--")
            ]
        ]
        sub_window = sg.Window(
            'Choose a path where to save file', 
            layout, 
            icon="code/tools/save.png"
        )

        while True:
            event, values = sub_window.Read()
            print("event:", event, "values: ", values)
            if event is None or event == 'Exit':
                break
            elif event == 'Save As':
                filename = values['Save As']
                if filename:
                    sub_window['File to Save'].update(value=filename)
            elif event == '--SAVE-PATH-VERIFIED--':
                last_filtered_file.save(filename)
                print("Wrote file to {}".format(filename))

        sub_window.close()
                
   
window.close()
