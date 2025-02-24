import PySimpleGUI as sg

#inicio do código    

sg.theme("LightGrey1")

INPUT_COLOR = '#EAF1F1'
DEFAULT_WHITE = '#FFFBFB'
WHITE = "#FFFFF"
SAVE_BUTTON_COLOR = '#11CC4F'
HOVER_SAVE_BUTTON_COLOR = '#0CFA5B'
CANCEL_BUTTON_COLOR = '#B3B8B7'
DEFAULT_TEXT_COLOR = '#312D2D'
GRAY = '#807676'

TYPOGRAPHY_FONT ='./assets/RobotoCondensed-VariableFont_wght.ttf'

contact_list = dict() #Dicionário de contatos

def create_contact_card(name : str, contact : str, id : str):

    return [sg.Frame(title="", layout=[
        
        [sg.Text(text=name, font=(TYPOGRAPHY_FONT, 14, 'normal') )],
        [sg.Text(text='Ver contato', text_color=GRAY, font=(TYPOGRAPHY_FONT, 11, 'underline'), enable_events=True, key="--VER_CONTATO--")],



    ], border_width=1, relief=sg.RELIEF_SUNKEN, expand_x=True)]



create_form_layout = [
    
    [sg.Text(text='Criar Contato', font=(TYPOGRAPHY_FONT, 18, 'bold') )],
    [sg.HorizontalSeparator(color=SAVE_BUTTON_COLOR)],

    [sg.Text('Nome', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(10,2)), background_color=DEFAULT_WHITE,expand_x=True)],
    [sg.Input(key='--NAME--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0, focus=True)],

    [sg.Text('Celular', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
    [sg.Input(key='--CELLPHONE--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

    [sg.Text('Mensagem', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
    [sg.Multiline(key='--MESSAGE--', background_color=(INPUT_COLOR), pad=((0,0),(0,20)), no_scrollbar=True, expand_y=True, font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

    [
        sg.Push(),
        sg.Button(button_text='Salvar', button_color=(DEFAULT_TEXT_COLOR, SAVE_BUTTON_COLOR), mouseover_colors=HOVER_SAVE_BUTTON_COLOR, size=(15,2), border_width=0, key='--SAVE--'),
        sg.Button(button_text='Cancelar', button_color=(DEFAULT_TEXT_COLOR, CANCEL_BUTTON_COLOR), size=(15,2), border_width=0, key='--CANCEL--'),
        sg.Push(),
    ],
]

list_contacts_layout = [

    [sg.Text(text='Contatos:', font=(TYPOGRAPHY_FONT, 18, 'bold') )],
    [sg.HorizontalSeparator(color=SAVE_BUTTON_COLOR)],

    create_contact_card('Liedson dos Reis Pereira', "(xx) 9xxxx-xxxx", '--CARD1--')

]

layout = [

    [
        sg.Column(layout=list_contacts_layout, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True,scrollable=True, vertical_scroll_only=True, sbar_relief=sg.RELIEF_FLAT),
        sg.Column(layout=create_form_layout, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True, p=((50,50), (20,20)))
    ]
]

janela = sg.Window("WhatsApp Automation", layout=layout, font=(TYPOGRAPHY_FONT), background_color=DEFAULT_WHITE, size=(800,550))

while True:
    eventos, valores = janela.read()

    print(eventos)
    print(valores)

    if eventos in (sg.WIN_CLOSED, "sair"):
        break
