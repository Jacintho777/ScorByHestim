from flet import*
from SCOR import SCOR
from INFOS import INFOS
from dataclasses import dataclass
from quizz import QuizApp

"""
Dark Blue (#002F6C) - Matches the deep blue found in the "HESTIM" text and parts of the logo. It serves as the primary color for headers and major components, maintaining brand consistency.
Red (#D32F2F) - The vibrant red from the logo's design elements can be used for accent buttons, alerts, or interactive elements.
Orange (#F57C00) - This shade can be used for highlights, call-to-action areas, or to add a dynamic touch while complementing the red.
Green (#388E3C) - Taken from the green triangle in the logo, it can be used for success notifications, icons, or background sections that need a fresh, positive feel."""

@dataclass
class scor_tab:
    name : str
    icon : icons
    color : colors

tabs = [
        scor_tab("Processus",icons.REPEAT, colors.BLUE_900),
        scor_tab("Performance",icons.SHOW_CHART,colors.AMBER_900),
        scor_tab("Pratiques",icons.SETTINGS, colors.GREEN_900),
        scor_tab("Personnes",icons.PEOPLE, colors.RED_900)
        ]

def main(page: Page):

    BG = "#FFFFFF"
    FWG = "#F57C00"
    FG = "#002F6C"
    BG_2 = "#388E3C"
    INTERFACE_HEIGHT = 620

    page.fonts = {
        "Kanit": "assets/fonts/Kanit-Regular.ttf",
        "Aleo Bold Italic": "https://raw.githubusercontent.com/google/fonts/master/ofl/aleo/Aleo-BoldItalic.ttf",
        "Roboto": "https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Regular.ttf",
        "Open Sans": "https://raw.githubusercontent.com/google/fonts/master/apache/opensans/OpenSans-Regular.ttf",
        "Lato": "https://raw.githubusercontent.com/google/fonts/master/ofl/lato/Lato-Regular.ttf"
    }

    def nav_section_click(e):
        section_key = e.control.text  # Retrieve the button key
        axe = e.control.parent.parent.title.value
        navigate_to_list(section_key,axe[0]+axe[1:].lower())
    
    def go_back(e):
        if len(page.views) > 1:
            while page.views[-1].route in ['/sub_section_page','/search_page']:
                page.views.pop()
            page.update()

    def navigate_to_search(event):

        search_input = TextField(
            hint_text="Rechercher...",
            expand=True,
            on_change=perform_search,
            color=colors.BLACK87,
        )
        page.views.append(View(
                padding=15,
                route="/search_page",
                controls=[
                    Container(
                        # height=INTERFACE_HEIGHT-30,
                        bgcolor=colors.WHITE,
                        expand=True,
                        content=Column(
                            controls=[
                                Container(
                                    bgcolor=colors.WHITE,
                                    content=Row(
                                        height=40,
                                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            IconButton(
                                                icon=icons.ARROW_BACK,
                                                icon_size=27,
                                                on_click=go_back,
                                                icon_color=FG,
                                            ),
                                            search_input
                                        ]
                                    )
                                ),
                                search_results
                            ]
                        )
                    )
                ]
            ))
        page.go("/search_page")  # Ensure the page navigates to the new view
        page.update()

    def tile_click(e):
        selected_index = list(SCOR.keys()).index(e.control.text)
        navigate_to_tab_page(selected_index=selected_index)

    def go_home(e):
        home_view = page.views[0]
        page.views.clear()
        page.views.append(home_view)
        page.views.append(root_page_container)
        page.go("/")
        page.update()

    def bring_up_quizz(e):
        quizz_app = QuizApp()
        quizz_app.build_ui(page)
        page.update()

    menu = NavigationDrawer(
        # on_dismiss=handle_dismissal,
        # on_change=handle_change,
        bgcolor=colors.GREY_200,
        controls=[
            Container(height=12),
            Row(
                alignment=MainAxisAlignment.SPACE_EVENLY,
                spacing = 0,
                controls=[
                    Image(
                        src=f"/images/scor.png",
                        width=100,
                        fit=ImageFit.CONTAIN,
                    ),
                    Text(
                        value=' By   ', font_family='Kanit'
                    ),
                    Image(
                        src=f"/images/HESTIM.png",
                        width=130,
                        fit=ImageFit.CONTAIN,
                    ),
                ]
            ),
            Divider(thickness=2),
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                # horizontal_alignment=CrossAxisAlignment.STRETCH,
                controls=[
                    IconButton(icon = icons.HOME, icon_size=30, expand=True, on_click=go_home, icon_color=FG),
                    IconButton(icon = icons.HELP_ROUNDED,icon_size=30, expand=True, icon_color=FG,on_click=lambda e: page.launch_url("https://www.apics.org/docs/default-source/scor-training/scor-v12-0-framework-introduction.pdf?sfvrsn=2")),
                ]
            ),
            Column(
                spacing=0,
                width=300,
                controls=[
                    Card(
                        color=colors.WHITE,
                        content=ExpansionTile(
                            title=Text(tab.name.upper(), color=colors.BLACK87, font_family='Kanit', weight=FontWeight.W_500),
                            leading=Icon(tab.icon, color=tab.color),
                            affinity=TileAffinity.LEADING,
                            bgcolor=colors.BLUE_100,
                            # initially_expanded=True,
                            # collapsed_text_color=colors.BLUE,
                            # text_color=colors.BLUE,
                            controls=[
                                Card(
                                    content=FilledButton(
                                                text=section,
                                                width = 400, 
                                                height=40,
                                                on_click=nav_section_click,
                                                style=ButtonStyle(
                                                            shape=RoundedRectangleBorder(radius=0),
                                                            bgcolor=tab.color,
                                                            color = colors.WHITE,
                                                            text_style=TextStyle(font_family="Kanit"),
                                                            )
                                                        ),
                                )
                                        for section in SCOR[tab.name].keys()
                            ],
                        ),
                    ) for tab in tabs
                ],
            ),
        ],
    )

    root_page_container = View(
        drawer=menu,
        route='/',
        controls=[
            Container(
                padding=20,
                height=INTERFACE_HEIGHT,
                bgcolor=colors.GREY_200,
                expand=True,
                content=Column(
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=CrossAxisAlignment.STRETCH,
                    controls=[
                        Row(            expand=True,
                                        spacing = 0,
                                        height=200,
                                        controls=[
                                            Image(
                                                expand=True,
                                                # width=130,
                                                src=f"/images/scor.png",
                                                fit=ImageFit.CONTAIN,
                                            )
                                        ]
                                    ),
                        Row(
                            expand=True,
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment=CrossAxisAlignment.STRETCH,
                            controls=[
                                Card(expand=True,
                                    content=FilledButton(
                                        expand=True,
                                        text="Processus",
                                        on_click=tile_click,
                                        style=ButtonStyle(
                                            bgcolor=colors.BLUE_900,
                                            shape=ContinuousRectangleBorder(2),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                                    ),
                                ),
                                Card(
                                    expand=True,
                                    content=FilledButton(
                                        expand=True,
                                        text="Performance",
                                        on_click=tile_click,
                                        style=ButtonStyle(
                                            bgcolor=colors.AMBER_900,
                                            shape=ContinuousRectangleBorder(2),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                                    ),
                                ),
                            ]
                        ),
                        Row(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment=CrossAxisAlignment.STRETCH,
                            expand=True,
                            controls=[
                                Card(
                                    expand=True,
                                    content=FilledButton(
                                        expand=True,
                                        text="Pratiques",
                                        on_click=tile_click,
                                        style=ButtonStyle(
                                            bgcolor=colors.GREEN_900,
                                            shape=ContinuousRectangleBorder(2),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                                    ),
                                ),
                                Card(
                                    expand=True,
                                    content=FilledButton(
                                        expand=True,
                                        text="Personnes",
                                        on_click=tile_click,
                                        style=ButtonStyle(
                                            bgcolor=colors.RED_900,
                                            shape=ContinuousRectangleBorder(2),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                                    ),
                                ),
                            ]
                        ),
                        Card(
                            margin=15,
                            expand=True,
                            content=FilledButton(
                                expand=True,
                                text = "Rechercher",
                                icon=icons.SEARCH_SHARP,
                                icon_color=colors.WHITE,
                                on_click=navigate_to_search,
                                style=ButtonStyle(
                                            bgcolor=colors.BLUE_ACCENT_700,
                                            shape=ContinuousRectangleBorder(2),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                            ),
                        ),
                        Card(
                            margin=15,
                            expand=True,
                            content=FilledButton(
                                expand=True,
                                text = "SCOR QUIZ",
                                icon=icons.QUIZ_SHARP,
                                icon_color=colors.WHITE,
                                on_click=bring_up_quizz,
                                style=ButtonStyle(
                                            bgcolor=colors.BLUE_ACCENT_700,
                                            shape=ContinuousRectangleBorder(2),
                                            side=BorderSide(width = 1, color=colors.AMBER_700),
                                            color = colors.WHITE,
                                            text_style=TextStyle(font_family="Kanit", size=16),
                                        ),
                            ),
                        ),
                        Container(
                            margin=30,
                            expand=True,
                            content=Column(
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                expand=True,
                                controls=[
                                    Text(
                                        value='Powered By', 
                                        font_family='Kanit', 
                                        size=14, 
                                        text_align=TextAlign.RIGHT,
                                        color=colors.BLACK87,
                                    ),
                                    Image(
                                        src=f"/images/HESTIM.png",
                                        width = 100,
                                        fit=ImageFit.CONTAIN,
                                    ),
                                ],
                            ),
                        ),
                        Divider(thickness=2),
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            # horizontal_alignment=CrossAxisAlignment.STRETCH,
                            controls=[
                                IconButton(icon = icons.LANGUAGE_ROUNDED, icon_size=30, expand=True, icon_color=FG),
                                IconButton(icon = icons.HELP_ROUNDED,icon_size=30, expand=True, icon_color=FG,on_click=lambda e: page.launch_url("https://www.apics.org/docs/default-source/scor-training/scor-v12-0-framework-introduction.pdf?sfvrsn=2")),
                            ]
                        ),
                    ]
                ),
            ),
        ]
    )

    page.padding = 0
    page.title = "SCOR By HESTIM"
    page.bgcolor = colors.WHITE
    # page.add(root_page_container)
    page.views.append(root_page_container)
    page.go('/')
    page.update()

    page.drawer = menu

    selected_tab = 'Processus'

    search_results = Column(
                                scroll=ScrollMode.ADAPTIVE,
                                # height=INTERFACE_HEIGHT-50,
                                expand=True,
                                spacing=0,
                )

    def search_scor_data(data, query):
        if not data:
            return {}

        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                if isinstance(key, tuple):
                    if query.lower() in key[1].lower():
                        result[key] = value
                    else:
                        sub_result = search_scor_data(value, query)
                        if sub_result:
                            result[key] = sub_result
                else:
                    if query.lower() in key.lower():
                        result[key] = value
                    else:
                        sub_result = search_scor_data(value, query)
                        if sub_result:
                            result[key] = sub_result
            return result if result else None

        elif isinstance(data, list):
            result = []
            for item in data:
                sub_result = search_scor_data(item, query)
                if sub_result:
                    result.append(sub_result)
            return result if result else None

        elif isinstance(data, str):
            return data if query.lower() in data.lower() else None

        return None
    
    def rearrange_search(result):
        if result==None:
            return dict()
        else:
            response = dict()
            for axe, axe_content in result.items():
                for section, section_content in axe_content.items():
                    response.update({(axe,section):section_content})
            return response

    def perform_search(e):

            query = e.control.value
            print(query)
            # Perform search logic here and update search_results
            search_results.controls.clear()
            response = rearrange_search(search_scor_data(SCOR, query=query))
            search_results.controls = [
                                        Row(
                                            controls=[
                                                ExpansionTile(
                                                        # affinity=TileAffinity.LEADING,
                                                        disabled=len(axe_section[0])==0,
                                                        affinity= TileAffinity.LEADING if len(axe_section[0])!=0 else None,
                                                        title=Text(
                                                            axe_section[0],
                                                            style="titleMedium",  # Larger font for emphasis
                                                            color="#333333",  # Dark gray for a modern look
                                                            weight="bold"  # Bold for better visibility
                                                        ),
                                                        subtitle=Text(
                                                            value = axe_section[1],
                                                            color="#555555",  # Medium gray for subtle contrast
                                                            size=14,
                                                            font_family="Kanit",
                                                        ),
                                                        bgcolor="#FAFAFA",  # Light background for contrast
                                                        expand=True,
                                                        controls=[
                                                            ExpansionTile(
                                                                    title=Text(
                                                                        value = third_level_section_key[0]+"-"+third_level_section_key[1],
                                                                        style="titleMedium",  # Larger font for emphasis
                                                                        color=[tab for tab in tabs if tab.name==axe_section[0]][0].color,  # Dark gray for a modern look
                                                                        weight="bold"  # Bold for better visibility
                                                                    ),
                                                                    subtitle=Text(
                                                                        "\n".join([code+"-"+value for code,value in dict(third_level_section_value).items()]),
                                                                        # third_level_section_value,
                                                                        color="#555555",  # Medium gray for subtle contrast
                                                                        size = 14,
                                                                    ),
                                                                    bgcolor="#FAFAFA",  # Light background for contrast
                                                                    expand=True,
                                                                    disabled=True,
                                                            ) for (third_level_section_key, third_level_section_value) in section_content.items()
                                                        ],
                                                    ),
                                            ]
                                        )
                                        for (axe_section, section_content) in response.items()

                                            ]
            if len(query) == 0:
                search_results.controls.clear()
            # Add search results to search_results.controls
            search_results.update()

    def navigate_to_list(button_key, axe=selected_tab):
        section = button_key
        page.views.append(View( 
                                bgcolor=colors.WHITE,
                                padding=15,
                                route="/sub_section_page",
                                controls=[
                                    Container(
                                        # height=INTERFACE_HEIGHT-75,
                                        expand=True,
                                        bgcolor=colors.WHITE,
                                        content=Column(
                                            controls=[
                                                Container(
                                                    bgcolor=colors.WHITE,
                                                    content=Row(
                                                        height=25,
                                                        alignment=MainAxisAlignment.SPACE_EVENLY,
                                                        controls=[
                                                            Container( 
                                                                    on_click=go_back,
                                                                    content=Icon(
                                                                                icons.ARROW_BACK, color=FG, size=30
                                                                                )
                                                                    ),
                                                            Text(value=section.upper(), text_align=TextAlign.CENTER,expand=True,size=16, font_family="Kanit",weight=FontWeight.W_700, color=colors.BLACK87),
                                                            IconButton(
                                                                width=30,
                                                                on_click=lambda e : definition(e),
                                                                content=Icon(icons.INFO_OUTLINE_ROUNDED, color=FG, size=30),
                                                                padding=0,
                                                                    ),
                                                                ],
                                                        ),
                                                ),
                                                Divider(thickness=2),
                                                Container(
                                                    # height=INTERFACE_HEIGHT-130,
                                                    expand=True,
                                                    content=Column
                                                        (
                                                        scroll=ScrollMode.ADAPTIVE,
                                                        # height=INTERFACE_HEIGHT-130,
                                                        expand=True,
                                                        spacing=0,
                                                        controls=[
                                                           Row(
                                                               controls=[
                                                                   ExpansionTile(
                                                                            # affinity=TileAffinity.LEADING,
                                                                            # disabled=len(third_level_section)==0,
                                                                            affinity= TileAffinity.LEADING if len(third_level_section)!=0 else None,
                                                                            title=Text(
                                                                                subsection[0],
                                                                                style="titleMedium",  # Larger font for emphasis
                                                                                color="#333333",  # Dark gray for a modern look
                                                                                weight="bold"  # Bold for better visibility
                                                                            ),
                                                                            subtitle=Text(
                                                                                value = subsection[1],
                                                                                color="#555555",  # Medium gray for subtle contrast
                                                                                size=14,
                                                                                font_family="Kanit",
                                                                            ),
                                                                            trailing=IconButton(
                                                                                expand=True,
                                                                                on_click=lambda e : definition(e),
                                                                                content=Icon(
                                                                                    icons.INFO_OUTLINE_ROUNDED,
                                                                                    color="#007BFF",  # Blue color to match the theme
                                                                                    size=20,  # Slightly smaller for subtlety
                                                                                ),
                                                                            ),
                                                                            bgcolor="#FAFAFA",  # Light background for contrast
                                                                            expand=True,
                                                                            controls=[
                                                                                ExpansionTile(
                                                                                        title=Text(
                                                                                            third_level_section_key,
                                                                                            style="titleMedium",  # Larger font for emphasis
                                                                                            color=[tab for tab in tabs if tab.name==axe][0].color,  # Dark gray for a modern look
                                                                                            weight="bold"  # Bold for better visibility
                                                                                        ),
                                                                                        subtitle=Text(
                                                                                            third_level_section_value,
                                                                                            color="#555555",  # Medium gray for subtle contrast
                                                                                            size = 14,
                                                                                        ),
                                                                                        trailing=IconButton(
                                                                                            expand=True,
                                                                                            on_click=lambda e : definition(e),
                                                                                            content=Icon(
                                                                                                icons.INFO_OUTLINE_ROUNDED,
                                                                                                color="#007BFF",  # Blue color to match the theme
                                                                                                size=20  # Slightly smaller for subtlety
                                                                                            ),
                                                                                        ),
                                                                                        bgcolor="#FAFAFA",  # Light background for contrast
                                                                                        expand=True,
                                                                                ) for (third_level_section_key, third_level_section_value) in third_level_section
                                                                            ],
                                                                        ),
                                                               ]
                                                           )
                                                            for (subsection, third_level_section) in SCOR[axe][section].items()
                                                                ]
                                                                )
                                                         ),
                                                    ]
                                                    ),
                                            ),
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    FloatingActionButton(
                                                        icon=icons.ARROW_LEFT_OUTLINED,
                                                        on_click=swap_left,
                                                        height=50,
                                                        width=50,
                                                    ),
                                                    FloatingActionButton(
                                                        icon=icons.ARROW_RIGHT_OUTLINED,
                                                        on_click=swap_right,
                                                        height=50,
                                                        width=50,
                                                    ),
                                                ]
                                            ),
                                        ],
                            )
                            )
        page.go("/sub_section_page")  # Ensure the page navigates to the new view
        page.update()
    
    def definition(e):

        if isinstance(e.control.parent, Row):
            section_title = e.control.parent.controls[1].value
            section_title = section_title[0]+section_title[1:].lower()
            description = INFOS[section_title]
        else:
            try :
                description = INFOS[e.control.parent.title.value]
            except:
                return
        content_text = description

        def close(e):
            dlg.open = False
            page.update()
        
        def text_treatment(long_text):
            long_text_splitted = long_text.strip().split(' ')
            long_text_formatted = " ".join([word.strip() for word in long_text_splitted if word!='\n' and word!=''])

            print(long_text_splitted)

            return long_text_formatted[0].upper()+long_text_formatted[1:]

        dlg = AlertDialog(
            title=Row(
                controls=[
                    Icon(icons.INFO),
                    Text("Definition", font_family="Kanit"),
                ]
            ),
            content=Column(
                height=max(0.5*len(content_text),250),
                scroll=ScrollMode.ALWAYS,
                controls=[
                    Text(text_treatment(description), font_family="Kanit")
                    # Text(line.strip(), font_family="Kanit") for line in content_text.strip().split('\n')
                ]
            ),
            actions=[
                ElevatedButton(text="Close", on_click=lambda e: close(e))
            ],
            actions_alignment="end"
        )


        page.dialog = dlg
        dlg.open = True
        page.update()

    def swap_right(e):
        subsection_upper = e.control.parent.parent.controls[0].content.controls[0].content.controls[1].value
        subsection = subsection_upper[0]+subsection_upper[1:].lower()
        for i,value in SCOR.items():
            if subsection in value.keys():
                section_key = i
                break
        next_index = list(SCOR[section_key].keys()).index(subsection)+1
        if next_index==len(SCOR[section_key].keys()):
            next_index = 0
        navigate_to_list(list(SCOR[section_key].keys())[next_index],section_key)

    def swap_left(e):
        subsection_upper = e.control.parent.parent.controls[0].content.controls[0].content.controls[1].value
        subsection = subsection_upper[0]+subsection_upper[1:].lower()
        for i,value in SCOR.items():
            if subsection in value.keys():
                section_key = i
                break
        next_index = list(SCOR[section_key].keys()).index(subsection)-1
        if next_index==-1:
            next_index = len(SCOR[section_key].keys())-1
        navigate_to_list(list(SCOR[section_key].keys())[next_index],section_key)

    def section_click(e):
        section_key = e.control.text  # Retrieve the button key
        navigate_to_list(section_key,e.control.parent.parent.parent.text)

    def open_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    def navigate_to_tab_page(selected_index):

        tab_page_contents = Container(
            content=Column(
            controls=[
                    Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container( 
                                on_click=lambda e: open_drawer(e),
                                content=Icon(
                                    icons.MENU, color=FG, size=30)),
                                Row(
                                    spacing = 0,
                                    controls=[
                                        Image(
                                            src=f"/images/scor.png",
                                            width=70,
                                            fit=ImageFit.CONTAIN,
                                        ),
                                        Text(
                                            value=' By ', font_family='Kanit', color=colors.BLACK87
                                        ),
                                        Image(
                                            src=f"/images/HESTIM.png",
                                            width=100,
                                            fit=ImageFit.CONTAIN,
                                        ),
                                    ]
                                ),
                                Container(
                                    on_click=navigate_to_search,
                                    content=Icon(icons.SEARCH,color=FG, size=30)
                                ),
                            ],
                        ),
                    Tabs(
                        unselected_label_color=colors.BLACK54,
                        label_color=FG,
                        indicator_color=FG,
                        selected_index=selected_index,
                        animation_duration=300,
                        label_text_style=TextStyle(font_family="Kanit", size=14, letter_spacing=0.2),
                        tabs=[
                            Tab(
                                text=tab.name,
                                icon = tab.icon,
                                content=Container(
                                    # gradient=LinearGradient(
                                    #     begin=alignment.top_center,.
                                    #     end=alignment.bottom_center,
                                    # colors=[colors.WHITE,colors.WHITE, FG],
                                    # ),
                                    bgcolor=colors.GREY_200,
                                    expand=True,
                                    padding = 10,
                                    content=
                                            Column(
                                                expand=True,
                                                spacing = 10,
                                                horizontal_alignment=CrossAxisAlignment.STRETCH,
                                                controls=[
                                                    FilledButton(
                                                        text=section,
                                                        height=45,
                                                        on_click=section_click,
                                                        style=ButtonStyle(
                                                                    shape=RoundedRectangleBorder(radius=7),
                                                                    bgcolor=tab.color,
                                                                    color = colors.WHITE,
                                                                    text_style=TextStyle(font_family="Kanit", size=16),
                                                                    )
                                                                )
                                                    for section in SCOR[tab.name].keys()
                                                ]
                                            ), 
                                    alignment=alignment.top_left
                                ),
                            ) for tab in tabs
                        ],
                        expand=True,
                        # indicator_color=FWG,
                        # label_color=FWG,
                    )
                ]
                )
            )
        
        tabs_page_view = View(
            route='/home_page',
            drawer=menu,
            controls=[
                Container(
                    # # width=400,
                    # height=INTERFACE_HEIGHT,
                    expand=True,
                    bgcolor=BG,
                    border_radius=5,
                    content=Stack(
                    controls=[
                        tab_page_contents
                    ]
                    )
        
                ),
            ]
        )

        page.views.append(tabs_page_view)

        page.go("/home_page")  # Ensure the page navigates to the new view
        page.update()


if __name__=='__main__':
    app(target=main, view=AppView.FLET_APP_WEB, assets_dir='assets')
#©jacinthompeteye