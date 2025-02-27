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

contact_list = []

main_layout = [

    [sg.VPush()],
    [
        sg.Frame(title='', layout=[
            [sg.Button(button_color=DEFAULT_WHITE,image_filename="./assets/img/new_contact.png", border_width=0, key='--NOVO_CONTATO_BUTTON--')],
            [sg.Text(text='Novo Contato (+)', font=(TYPOGRAPHY_FONT, 14, 'normal'), enable_events=True, key='--NOVO_CONTATO_TEXT--')],
    ], element_justification='center', relief=sg.RELIEF_FLAT, background_color=DEFAULT_WHITE),

        sg.Frame(title='', layout=[
            [sg.Button(button_color=DEFAULT_WHITE,image_filename="./assets/img/send_message.png", border_width=0, key='--ENVIAR_MESAGEM_BUTTON--')],
            [sg.Text(text='Enviar Mensagens', font=(TYPOGRAPHY_FONT, 14, 'normal'), enable_events=True, key='--ENVIAR_MESAGEM_TEXT--')],
    ], element_justification='center', relief=sg.RELIEF_FLAT, background_color=DEFAULT_WHITE),
    ],
    [sg.VPush()]
]

update_contact_form = [
    
        [sg.Text(text='Editar Contato', font=(TYPOGRAPHY_FONT, 18, 'bold') )],
        [sg.HorizontalSeparator(color=SAVE_BUTTON_COLOR)],

        [sg.Text('Nome', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(10,2)), background_color=DEFAULT_WHITE,expand_x=True)],
        [sg.Input(key='--NAME_UPDATE_FORM--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0, focus=True)],

        [sg.Text('Celular', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
        [sg.Input(key='--CELLPHONE_UPDATE_FORM--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

        [sg.Text('Mensagem', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
        [sg.Multiline(key='--MESSAGE_UPDATE_FORM--', background_color=(INPUT_COLOR), pad=((0,0),(0,20)), no_scrollbar=True, expand_y=True, font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

        [
            sg.Push(),
            sg.Button(button_text='Salvar', button_color=(DEFAULT_TEXT_COLOR, SAVE_BUTTON_COLOR), mouseover_colors=HOVER_SAVE_BUTTON_COLOR, size=(15,2), border_width=0, key='--INSERT_SAVE--'),
            sg.Button(button_text='Cancelar', button_color=(DEFAULT_TEXT_COLOR, CANCEL_BUTTON_COLOR), size=(15,2), border_width=0, key='--CANCEL_UPDATE--'),
            sg.Push(),
        ],
    ]

insert_contact_form = [
    
        [sg.Text(text='Criar Contato', font=(TYPOGRAPHY_FONT, 18, 'bold') )],
        [sg.HorizontalSeparator(color=SAVE_BUTTON_COLOR)],

        [sg.Text('Nome', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(10,2)), background_color=DEFAULT_WHITE,expand_x=True)],
        [sg.Input(key='--NAME_INSERT_FORM--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0, focus=True)],

        [sg.Text('Celular', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
        [sg.Input(key='--CELLPHONE_INSERT_FORM--', background_color=(INPUT_COLOR), font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

        [sg.Text('Mensagem', font=(TYPOGRAPHY_FONT, 14), pad=((0,0),(18,2)), background_color=DEFAULT_WHITE, expand_x=True)],
        [sg.Multiline(key='--MESSAGE_INSERT_FORM--', background_color=(INPUT_COLOR), pad=((0,0),(0,20)), no_scrollbar=True, expand_y=True, font=(TYPOGRAPHY_FONT, 12), do_not_clear=False, expand_x=True, border_width=0)],

        [
            sg.Push(),
            sg.Button(button_text='Salvar', button_color=(DEFAULT_TEXT_COLOR, SAVE_BUTTON_COLOR), mouseover_colors=HOVER_SAVE_BUTTON_COLOR, size=(15,2), border_width=0, key='--INSERT_SAVE--'),
            sg.Button(button_text='Cancelar', button_color=(DEFAULT_TEXT_COLOR, CANCEL_BUTTON_COLOR), size=(15,2), border_width=0, key='--CANCEL_INSERT--'),
            sg.Push(),
        ],
    ]

list_contacts_layout = [

    [sg.Text(text='Contatos:', font=(TYPOGRAPHY_FONT, 18, 'bold') )],
    [sg.Listbox(values=contact_list, size=(15, 6), key="-LISTA-", enable_events=True, expand_x=True, expand_y=True),],

]

layout = [

    [
        sg.Column(layout=list_contacts_layout, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True, key='--CONTACT_LIST--'),

        #Lado direito
        sg.Column(layout=main_layout, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True, p=((50,50), (20,20)), key='--MAIN_MENU--'),
        sg.Column(layout=insert_contact_form, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True, p=((50,50), (20,20)), key='--INSERT_CONTACT--', visible=False),
        sg.Column(layout=update_contact_form, background_color=DEFAULT_WHITE, expand_x=True, expand_y=True, p=((50,50), (20,20)), key='--UPDATE_CONTACT--', visible=False),
    ]
]

janela = sg.Window("WhatsApp Automation", layout=layout, font=(TYPOGRAPHY_FONT), background_color=DEFAULT_WHITE, size=(800,550))

while True:
    eventos, valores = janela.read()

    print(eventos, valores)

    if eventos in (sg.WIN_CLOSED, "sair"):
        break

    #Evento para acessar a tela de cadastro de contatos
    if eventos in ['--NOVO_CONTATO_BUTTON--', '--NOVO_CONTATO_TEXT--']:
        janela['--MAIN_MENU--'].update(visible=False)
        janela['--INSERT_CONTACT--'].update(visible=True)

    #Evento que retornar da tela de cadastro para o menu principal
    if eventos in ['--CANCEL_INSERT--']:
        
        resp = sg.Popup('Você deseja cancelar o cadastro? Esta ação é irreversivel!', no_titlebar=True, button_type=sg.POPUP_BUTTONS_OK_CANCEL, button_color=SAVE_BUTTON_COLOR, )

        if (resp in 'OK'):
            janela['--INSERT_CONTACT--'].update(visible=False)
            janela['--NAME_INSERT_FORM--'].update(value='')
            janela['--CELLPHONE_INSERT_FORM--'].update(value='')
            janela['--MESSAGE_INSERT_FORM--'].update(value='')
            janela['--MAIN_MENU--'].update(visible=True)
        
        else:
            pass

    if eventos in ['--VER_CONTATO--']:
        janela['--MAIN_MENU--'].update(visible=False)
        janela['--UPDATE_CONTACT--'].update(visible=True)

    if eventos in ['--CANCEL_UPDATE--']:
        
        resp = sg.Popup('Você deseja cancelar as alterações?', no_titlebar=True, button_type=sg.POPUP_BUTTONS_OK_CANCEL, button_color=SAVE_BUTTON_COLOR, )

        if (resp in 'OK'):
            janela['--UPDATE_CONTACT--'].update(visible=False)
            janela['--NAME_UPDATE_FORM--'].update(value='')
            janela['--CELLPHONE_UPDATE_FORM--'].update(value='')
            janela['--MESSAGE_UPDATE_FORM--'].update(value='')
            janela['--MAIN_MENU--'].update(visible=True)
        
        else:
            pass