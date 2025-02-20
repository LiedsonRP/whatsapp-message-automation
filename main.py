import PySimpleGUI as sg

#inicio do código    

sg.theme("LightGrey1")

INPUT_COLOR = '#EAF1F1'
DEFAULT_WHITE = '#FFFBFB'
TYPOGRAPHY_FONT ='./assets/RobotoCondensed-VariableFont_wght.ttf'

"""
Cria um input padronizado no código
"""
def create_input(label_text : str, key_name : str):
    
    return [
        [sg.Text(label_text, font=(TYPOGRAPHY_FONT, 16))],
        [sg.Input(key=key_name, background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, pad=(6,6))]
    ]

"""
Cria um textarea padronizado no código
"""
def create_text_area(label_text : str, key_name : str):
    
    return [
        [sg.Text(label_text, font=(TYPOGRAPHY_FONT, 16))],
        [sg.Multiline(key=key_name, background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, justification='left', autoscroll=False, size=(40, 10), pad=(6,6))]
    ]



create_form_layout = [

    [sg.Text(text='Criar Contato', font=(TYPOGRAPHY_FONT, 22, 'bold') )],
    [sg.VerticalSeparator()],    
    [sg.VerticalSeparator()],    
    [create_input('Nome', '--NAME--')],
    [sg.VerticalSeparator()],
    [sg.VerticalSeparator()],
    [create_input('Celular', '--CELLPHONE--')],
    [sg.VerticalSeparator()],
    [sg.VerticalSeparator()],
    [create_text_area('Mensagem', '--MESSAGE--')],
    [sg.VerticalSeparator()],
    [sg.VerticalSeparator()],
    [
        sg.Button(button_text='Salvar'),
        sg.Button(button_text='Cancelar')
    ]
    
]

layout = [
    [create_form_layout]
]

janela = sg.Window("WhatsApp Automation", layout=layout, font=(TYPOGRAPHY_FONT), size=(800,500), margins=(30,30), background_color=(DEFAULT_WHITE))

while True:
    eventos, valores = janela.read()

    if eventos in (sg.WIN_CLOSED, "sair"):
        break
