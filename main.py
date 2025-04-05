import flet as ft
from flet import AlertDialog

class Portafolios(ft.Container):
    def __init__ (self,Page:ft.Page):
        super().__init__()
        self.Page = Page 
        self.Page.padding = 0
        self.Page.fonts = {"marlinui": "../assets/avenir-lt-std-heavy.ttf"}
        self.text_font = 'Tahoma'
        self.Page.title = 'Grenyut - Craft Beer'
        self.expand = True


        self.color_primaria = ft.Colors.BLUE_GREY_900
        self.color_primaria_1 = ft.Colors.RED_500               
        self.color_primaria_2 = ft.Colors.WHITE  
        self.color_primaria_3 = ft.Colors.BLACK       
        self.build()
        self.cambiar_pagina1(0)
        
            

    def build(self):

        list_video = ft.VideoMedia(f"./assets/VID-20250112-WA0003.mp4"),ft.VideoMedia(f"./assets/VID-20250112-WA0002.mp4"),ft.VideoMedia(f"./assets/VID-20250112-WA0001.mp4")

        self.cambiar_modo  = ft.IconButton(icon=ft.Icons.LIGHT_MODE,selected_icon=ft.Icons.DARK_MODE,on_click=self.toggle_icon_button,selected=False)

        self.frame_inicios= ft.Container(expand = True,
                                         
                                         offset=ft.transform.Offset(0,0),
                                         content=ft.Row(expand=True,
                                                        scroll = "auto",
                                                         controls=[
                                                             ft.Container(
                                                                 margin=20,
                                                                 expand=True,
                                                                 content=ft.Column(
                                                                     scroll = "auto",
                                                                    alignment=ft.alignment.top_left,
                                                                     controls=[
                                                                         ft.Text("ORIGEN", size=30,weight=ft.FontWeight.W_900),
                                                                         
                                                                         ft.Text("La nostra gran aventura al món Craft\nva començar el setembre de 2015, Santpedor,\namb el que vam llançar al mercat la nostra primera\nAmerican Pale Ale, APA SANTPE.\n\nDesprés de quatre meravellosos anys, elaborant\nla nostra recepta de fàbrica a fàbrica, de\nmanera nòmada, i després de créixer en \nconeixements al món craf, comencem \na evolucionar ia crear noves fórmules.\n\nL'afany d'aconseguir el màxim control en els\n processos de fabricació i de continuar experimentant,\nva fer que el 2019 adquiríssim la cervesera de la comarca del \nBerguedà, a Puig-Reig, culminant la nostra aventura.\n\nNo ha estat fàcil, però el que sí que tenim clar \nés que sense esforç no hi ha recompensa i \nla nostra millor recompensa sou vosaltres.", size=14),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                            ]
                                                                 )
                                                                 
                                                             ),
                                                                ft.Container(expand = True,
                                                                           
                                                                            padding=10,
                                                                            alignment=ft.alignment.center_right,
                                                                            #width=350,
                                                                            #height=350,
                                                                          shape = ft.BoxShape.CIRCLE,
                                                                          clip_behavior = ft.ClipBehavior.ANTI_ALIAS,
                                                                          margin = 50,
                                                                          shadow = ft.BoxShadow(
                                                                              spread_radius = 50,
                                                                              blur_radius = 180,
                                                                              color = self.color_primaria,
                                                                              
                                                                  
                                                                          ),
                                                                       
                                                                          content = ft.Image(src = "../assets/cropped-Isologo-_ESP_GRENYUT.png")
                                                             
                                                                 
                                                             ),
                                                         ])
        )
        

        self.frame_cervezas  = ft.Container(expand = True,
                                     
                                        offset=ft.transform.Offset(-2,0),
                                        content = ft.Column(
                                             scroll = "auto",
                                             expand = True,
                                             controls = [
                                             ft.ResponsiveRow(                                                 
                                                 expand = True,
                                                 spacing = 20,
                                                 controls = [
                                                ft.Container(
                                                         margin = 5,
                                                         expand = True,
                                                         col = {"md":12,"lg":12},
                                                         height = 200,
                                                         padding = 5,
                                                         border = ft.Border(bottom = ft.BorderSide(2,self.color_primaria)
                                                        ),
                                             
                                                         content = ft.Video(
                                                             expand = True,
                                                             playlist = list_video[0:3],
                                                             
                                                             fill_color = 'BLACK',
                                                             aspect_ratio = 16 / 9,
                                                             filter_quality = 'medium',
                                                             autoplay = True,
                                                             show_controls = False,  
                                                             muted = True,
                                                             fit=ft.ImageFit.COVER,
                                                             playlist_mode=ft.PlaylistMode.LOOP
                                                                                                                                                                           
                                                         )                              
                                                         
                                                     ),
                                                ft.Container (expand = True, 
                                                        content = ft.Column(                                                            spacing = 10,
                                                            visible = True,
                                                            expand = True,
                                                            controls = [
                                                                ft.Container(expand = True,
                                                                            content = ft.Row(
                                                                                expand = True,
                                                                                controls = [
                                                                                    ft.Container(
                                                                                        expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                                      
                                                                                        bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                                                        content = ft.Column( 
                                                                                            controls = [
                                                                                                
                                                                                                ft.Text ('MERLÈS', size = 18,text_align="START",weight =ft.FontWeight.W_900),
                                                                                                ft.Text ('Golden Ale', size = 12,weight =ft.FontWeight.W_700),
                                                                                                ft.Text (f"Cervesa maltosa, fresca i equilibrada, amb un toc cítric.\n\nIngredients: Malt d'ordi,flocs de civada, citra.\n\n5,5% Vol./ IBU 15\n", size = 14),
                                                                                                ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Golden Ale",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Merles.png")
                                                                                            ],
                                                                                                                                                                                
                                                                                        )
                                                                                      
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                               
                                                                                        bgcolor = ft.Colors.with_opacity(0.9, self.color_primaria_3), 

                                                                                        content = ft.Column(
                                                                                            controls = [
                                                                                                
                                                                                                ft.Text ('SANTPE', size = 18,weight =ft.FontWeight.W_900,color=ft.Colors.WHITE),
                                                                                                ft.Text ('American Pale Ale', size = 12,weight =ft.FontWeight.W_700,color=ft.Colors.WHITE),
                                                                                                ft.Text ("Cervesa fresca, aromàtica amb matisos de fruita tropical i floral, una lleugera amargor \nen boca. \n\nIngredients: Extra pale ale, biscuit i flocs de civada. Simcoe i Mossaic. \n\n5% Vol. / IBU 40\n", size=14,color=ft.Colors.WHITE),
                                                                                                ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="American Pale Ale",color_blend_mode = 30,height = 250,width = 200,src = "../assets/APA.png")
                                                                                            ]                                                                                       
                                                                                        )
                                                                                    ),
                                                        
                                                                                ]
                                                                            )
                                                 
                                                                        ),

                                                                ft.Container(expand = True,
                                                                        content = ft.Row(
                                                                            expand = True,
                                                                            
                                                                            controls = [
                                                                                ft.Container(
                                                                                    expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                                        bgcolor = ft.Colors.with_opacity(0.9, self.color_primaria_3),                                                                       
                                                                                    content = ft.Column(
                                                                                        controls = [
                                                                                            ft.Text ('LA GOLOSA', size = 18,weight =ft.FontWeight.W_900,color=ft.Colors.WHITE),
                                                                                            ft.Text ('Imperial Stout', size = 12,weight =ft.FontWeight.W_700,color=ft.Colors.WHITE),
                                                                                            ft.Text ("Cervesa negra amb cos, xocolatada, amb matisos a cacao i fruits secs. \nToc fresc pels seus llúpol.\n\nIngredients: Extra Pale Ale, roasted barley, malt, cacao, flocs de civada. Llúpols Columbus i North brewer.\n\n9% Vol. |  IBU 30.", size = 12,weight =ft.FontWeight.W_700,color=ft.Colors.WHITE),
                                                                                            ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Imperial Stout,\nTEMPORADA: TARDOR I HIVERN.",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Golosa.PNG")
                                                                                            

                                                                                        ]
                                                                                    )
                                                                                ),
                                                                                ft.Container(
                                                                                    expand = True,
                                                                                    padding = 10,
                                                                                    border_radius = 10,
                                                                                
                                                                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                                                    content = ft.Column( 
                                                                                        controls = [
                                                                                            
                                                                                            ft.Text ('ELLYS', size = 18,weight =ft.FontWeight.W_900),
                                                                                            ft.Text ('Indian Pale Ale', size = 12,weight =ft.FontWeight.W_900),
                                                                                            ft.Text (f"Indian Pale Ale (IPA) amb cos, sabors  i aromes florals, tropicals i afruitats amb tocs\nresinosos  i amargor intensa.\n\nIngredients: Extra pale ale, melanoidin, flocs de civada i llúpol mossaic.\n\n6.5% Vol. | IBU  70\n", size = 14),
                                                                                            ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Indian Pale Ale",color_blend_mode = 30,height = 250,width = 200,src = "../assets/ELLYS.png")
                                                                                            ],
                                                                                                                                                                            
                                                                                        )
                                                                                
                                                                                    ),
                                                                                ]
                                                                             )
                                                 
                                                                        ),

                                                                ft.Container(expand = True,
                                                                        content = ft.Row(
                                                                        expand = True,
                                                                    
                                                                    controls = [
                                                                        ft.Container(
                                                                            expand = True,
                                                                                padding = 10,
                                                                                border_radius = 10,
                                                                                bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2),                                                                       
                                                                            content = ft.Column(
                                                                                controls = [
                                                                                    ft.Text ('FRUITS & GOSES', size = 18,weight =ft.FontWeight.W_900),
                                                                                    ft.Text ('Gose', size = 12,weight =ft.FontWeight.W_700),
                                                                                    ft.Text ("Cervesa Cervesa amb acidesa lleugera amb notes de meló i llima.\n\nIngredients: Maltas Pilsen, Malta Blat, Flocs Civada, \nMeló, Llima, Sal del Delta, Lactobaciulus y Llevat.\n\n4,5% Vol. |  IBU 16. Col·laboració Cerveses Grenyut & Cerveses els Minairons", size = 12,weight =ft.FontWeight.W_700),
                                                                                    ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Gose",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Guns.PNG")
                                                                                    

                                                                                ]
                                                                            )
                                                                        ),
                                                                    ft.Container(
                                                                                        expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                                      
                                                                                        bgcolor = ft.Colors.with_opacity(0.9, self.color_primaria_3), 

                                                                                        content = ft.Column( 
                                                                                            controls = [
                                                                                                
                                                                                                ft.Text ('MEROLLA', size = 18,text_align="START",weight =ft.FontWeight.W_900,color=ft.Colors.WHITE),
                                                                                                ft.Text ('Strong Ale', size = 12,weight =ft.FontWeight.W_700,color=ft.Colors.WHITE),
                                                                                                ft.Text (f"Cervesa amb cos i anima, 1 any amb barrica de bourbon més 18 mesos de maduració.\n\nIngredients: Malta d'ordi, flocs de civada, sucre candy. aigua, llevat.\n\n10% Vol. |  IBU 30. Col·laboració Cerveses Grenyut & Cerveses Minera", size = 14,color=ft.Colors.WHITE),
                                                                                                ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Strong Ale",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Marolla.PNG"),
                                                                                                #ft.Icon(name=ft.Icons.ONETWOTHREE_OUTLINED,tooltip = 'Compte enrere', color=ft.Colors.RED, size=50)
                                                                                            
                                                                                            ],
                                                                                                                                                                                
                                                                                        )
                                                                                      
                                                                                    ),


                                                              ]
                                                          )
                                                 
                                                        ),
                                                                    ft.Container(expand = True,
                                                                            content = ft.Row(
                                                                            expand = True,                                                                    
                                                                    controls = [
                                                                                ft.Container(
                                                                                    expand = True,
                                                                                    padding = 10,
                                                                                    border_radius = 10,
                                                                                    
                                                                                    bgcolor = ft.Colors.with_opacity(0.9, self.color_primaria_3), 

                                                                                    content = ft.Column( 
                                                                                        controls = [
                                                                                            
                                                                                            ft.Text ('LITE', size = 18,text_align="START",weight =ft.FontWeight.W_900,color=ft.Colors.WHITE),
                                                                                            ft.Text ('Lager', size = 12,weight =ft.FontWeight.W_700,color=ft.Colors.WHITE),
                                                                                            ft.Text (f"Lager, amb ingredients del Berguedà\ncereals de Espunyola i llúpol d'Avià\n\nIngredients: Pàmola, Ordi recuperat per pagesia responsable i ecològica.\n\n | IBU  7\n", size = 14,color=ft.Colors.WHITE),
                                                                                            ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Lager",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Lite.PNG"),
                                                                                            #ft.Icon(name=ft.Icons.DND_FORWARDSLASH,tooltip = 'No Disponible', color=ft.Colors.RED, size=50)
                                                                                            
                                                                                        ],
                                                                                        
                                                                                                                                                                            
                                                                                    ),
                                                                                    
                                                                                    
                                                                                ),
                                                                                ft.Container(
                                                                                    expand = True,
                                                                                    padding = 10,
                                                                                    border_radius = 10,
                                                                                    
                                                                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                                                    content = ft.Column( 
                                                                                        controls = [
                                                                                            
                                                                                            ft.Text ('ROCK DIPA', size = 18,text_align="START",weight =ft.FontWeight.W_900),
                                                                                            ft.Text ('Doble Indian Pale Ale', size = 12,weight =ft.FontWeight.W_700),
                                                                                            ft.Text (f"D'una col·laboració amb Cervesa els Minairons neix la Rock Dipa.\n\nSedosa en boca i en aroma fruites tropicals.\n\nIngredients: Malta d'ordi, flocs de civada, llúpol Simcoe i Nelson Sauvin.\n\n8.5% Vol. | IBU  70\n", size = 14),
                                                                                            ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="Doble IPA",color_blend_mode = 30,height = 250,width = 200,src = "../assets/Rock1.PNG"),
                                                                                            #ft.Icon(name=ft.Icons.PENDING_OUTLINED,tooltip = 'Pròximament', color=ft.Colors.RED, size=50)
                                                                                            
                                                                                        ],  
                                                                                                                                                                            
                                                                                    )
                                                                                    
                                                                                ),
                                                                            ]
                                                                        )
                                                 
                                                                    ),

                                         ]
                                     )
                                     )
                                                                                                                                  
                                                 ]
                                                 
                                             )
                                             ]
                                         )
        )

        self.titulo_resumen = ft.Text('primero', size = 20, weight = ft.FontWeight.W_900, color = self.color_primaria)

        self.frame_TapR = ft.Container(expand = True,
                                     
                                        offset=ft.transform.Offset(-2,0),
                                        content = ft.Column(
                                             scroll = "auto",
                                             expand = True,
                                             controls = [
                                             ft.ResponsiveRow(                                                 
                                                 expand = True,
                                                 spacing = 20,
                                            controls = [
                                                ft.Container(
                                                    expand = True,
                                                    padding = 10,
                                                    border_radius = 10,
                                                    alignment=ft.alignment.top_left,
                                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                    content = ft.Column(
                                                        controls = [
                                                            
                                                            ft.Text ('TAP ROOM', size = 30,weight =ft.FontWeight.W_900),
                                                            ft.Text ('DESCOBREIX EL ESPAI CREAT PERQUÈ PUGUIS GAUDIR D’UNA BONA CERVESA ARTESANA DE QUALITAT.', size = 12,weight =ft.FontWeight.W_700),
                                                            ft.Text ("Les ganes de compartir el nostre projecte amb vosaltres ens ha portat a crear el  Tap Room, un lloc de trobada per a tots els amants de la cervesa artesana de qualitat, \non poder degustar les nostres varietats en estoc i gaudir d’un bon ambient craft.\n\nCada diumenge de 12h a 15h podreu gaudir d’aquest espai creat per a vosaltres, amb terrassa, 4 assortidors i tota la nostra varietat de cerveses.", size=14)
                                                            
                                                        ]                                                                                       
                                                    )
                                                ),
                                                ft.Container (expand = True, 
                                                        content = ft.Column(
                                                            
                                                            spacing = 10,
                                                            visible = True,
                                                            expand = True,
                                                            controls = [
                                                                ft.Container(expand = True,
                                                                            content = ft.Row(
                                                                                expand = True,
                                                                                controls = [
                                                                                    ft.Container(
                                                                                        expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                                        
                                                                                      
                                                                                        bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                                                        content = ft.Column( 
                                                                                            controls = [                                                                                    
                                                                                                ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="TAP ROOM",color_blend_mode = 30,height = 650,width = 600,src = "../assets/Tap-room-foto-300x300.jpg")
                                                                                            ],
                                                                                                                                                                                
                                                                                        )
                                                                                      
                                                                                    ),
                                                                                    ft.Container(
                                                                                        expand = True,
                                                                                        padding = 10,
                                                                                        border_radius = 10,
                                                                               
                                                                                        bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                                                        content = ft.Column(
                                                                                            controls = [
                                                                                                ft.Image(fit=ft.ImageFit.CONTAIN,tooltip="TERRASSA",color_blend_mode = 30,height = 650,width = 600,src = "../assets/terrassaTaproom.jpg")
                                                                                            ]                                                                                       
                                                                                        )
                                                                                    ),
                                                        
                                                              ]
                                                          )
                                                 
                                                    ),
                                                    
                                               
                                            ft.Container(
                                                    expand = True,
                                                    padding = 10,
                                                    border_radius = 10,
                                                    alignment=ft.alignment.center,
                                                    bgcolor = ft.Colors.with_opacity(0.2, self.color_primaria_2), 

                                                    content = ft.Column(
                                                        controls = [
                                                            
                                                            
                                                            ft.Text ('T’ESPEREM EN TAP ROOM GRENYUT PER A COMPARTIR L’EXPERIÈNCIA AMB TU!', size = 12,weight =ft.FontWeight.W_700),
                                                            ft.Text ("Pots enviar-nos un whatsapp i confirmar-nos la teva assistència ara mateix.", size=14),
                                                            ft.IconButton(icon=ft.Icons.SWIPE_DOWN_ROUNDED,icon_size = 40,on_click=lambda e: e.page.launch_url("https://wa.me/34658860960"))
                                                            
                                                        ]                                                                                       
                                                    )
                                                ),
                                                


                                         ]
                                     )
                                     )
                                                                                                                                  
                                                 ]
                                                 
                                             )
                                             ]
                                         )
        )
        self.frame_contacto = ft.Container(expand = True,
                                       
                                         offset=ft.transform.Offset(-2,0),
                                         content = ft.Column(
                                             scroll = "auto",
                                             expand = True,
                                             controls = [
                                                 ft.ResponsiveRow(
                                                     expand = True,
                                                     controls = [

                                                    ft.Container(
                                                            expand = True,
                                                            margin = 20,
                                                            height = 400,
                                                            padding = 10,
                                                            alignment = ft.alignment.center,
                                                            col = {'xs':12,'sm':6},
                                                            content = ft.Column(expand = True,
                                                                                alignment = ft.CrossAxisAlignment.END,
                                                                                horizontal_alignment = ft.CrossAxisAlignment.END,
                                                                               
                                                                                controls = [
                                                                                    ft.Row(
                                                                                        controls = [
                                                                                            ft.Icon(name = ft.Icons.PHONE,size = 40),
                                                                                            ft.Column(
                                                                                                   spacing = 10,
                                                                                                   controls = [
                                                                                                        
                                                                                                        ft.Text("TRUCA'NS", size = 12, weight = ft.FontWeight.W_900),
                                                                                                        ft.Text('(34) 658 860 960', size = 12,color = self.color_primaria),

                                                                                                   ]
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    ft.Row(
                                                                                        controls = [
                                                                                            
                                                                                            ft.IconButton(icon=ft.Icons.MESSAGE,icon_size = 40,on_click=lambda e: e.page.launch_url("grenyut@grenyut.cat")),
                                                                                            ft.Column(
                                                                                                   spacing = 10,
                                                                                                   controls = [
                                                                                                          ft.Text("CONTACTA'NS", size = 12, weight = ft.FontWeight.W_900),
                                                                                                          ft.Text('grenyut@grenyut.cat', size = 12,color = self.color_primaria),

                                                                                                   ]
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    ft.Row(
                                                                                        controls = [ 
                                                                                            ft.Icon(name = ft.Icons.LOCATION_ON,size = 40),
                                                                                            ft.Column(
                                                                                                   spacing = 10,
                                                                                                   controls = [
                                                                                                        ft.Text("VISITA'NS", size = 12,weight = ft.FontWeight.W_900),
                                                                                                        ft.Text('Polígons industrial La Sala.\nc/Casserres nº13 08692 Puig-Reig', size = 12, color = self.color_primaria),
                                                                                                   ]
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                    ft.Row(
                                                                                        controls = [ 
                                                                                            ft.IconButton(icon=ft.Icons.SWIPE_DOWN_ROUNDED,icon_size = 40,on_click=lambda e: e.page.launch_url("https://www.instagram.com/cervesesgrenyut/")),
                                                                                            ft.Column(
                                                                                                   spacing = 10,
                                                                                                   controls = [
                                                                                                        ft.Text("INSTAGRAM", size = 12,weight = ft.FontWeight.W_900),
                                                                                                        ft.Text('@cervesesgrenyut', size = 12, color = self.color_primaria),
                                                                                                        
                                                                                                   ]
                                                                                            )
                                                                                        ]
                                                                                    ),

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                            ]
                                                                                )

                                                                         
                                                                         
                                                                ),
                                                                ]                                                     
                                                            )
                                                        ]
                                                    )
                                            )                                  

        self.contentsInit =  ft.Container(
            
                   
                    expand=True,
                    #alignment = ft.alignment.center,
                    
                    margin=ft.margin.all(0),            
                    padding=0,
                    content=ft.Image(
                         
                    src=f"../assets/Inisi.png",
                    fit="cover",
                    width=300,
                    height=300,
                    border_radius=ft.border_radius.all(0))

                    
            
                )          
        
        self.contentsInit2 = ft.Container(                                      
            offset=ft.transform.Offset(0,6),
            content =ft.Column(
            controls =  [                
                ft.ElevatedButton('SI', width = 300, on_click=lambda e: e.page.open(self.frame_aviso_cook), style = ft.ButtonStyle(overlay_color={'hovered':self.color_primaria},
                    elevation = 20,alignment=ft.alignment.center,
                    shape = ft.RoundedRectangleBorder(radius = 5),
                    side = ft.BorderSide(1, self.color_primaria),
                   #'''on_click=lambda e:self.cambiar_pagina1(1)
                                                 
                ) 
                )
                ]
            )
        )

        self.contentsInit3 = ft.Container(expand = True,                                       
            offset=ft.transform.Offset(0,7),
            content =ft.Column(
            controls =  [               
                ft.ElevatedButton('NO', width = 300, style = ft.ButtonStyle(overlay_color={'hovered':self.color_primaria_1},
                    elevation = 20,alignment=ft.alignment.center,
                    shape = ft.RoundedRectangleBorder(radius = 5),
                    side = ft.BorderSide(1, self.color_primaria)
                ) 
                )
                ]
            )
        )

        self.contents1 = ft.Column( #Encabezado
            expand = True,
            spacing = 0,
            controls = [
                ft.Container(
                    
                    padding = 2,
                    content = ft.Row(   
                        expand = True,
                        controls =[
                                ft.Container(

                                        alignment = ft.alignment.top_left,
                                        expand=True,
                                        margin=ft.margin.all(0),            
                                        padding=0,
                                        content=ft.Image(
                                        src=f"../assets/imagotipo_GRENYUT.png",
                                        fit="contain",
                                        width=130,
                                        height=55,
                                        border_radius=ft.border_radius.all(0))
                                
                                    ),


                            ft.ResponsiveRow(
                                #alignment=ft.MainAxisAlignment.CENTER,
                                #col={"sm": 6, "md": 4, "xl": 2},
                                spacing=0,
                                expand=True,
                                controls=[
                                    ft.TextButton('Cerveses', style=ft.ButtonStyle(color=self.color_primaria),col=
                                    {"xs":12, "sm":1, "md":3},on_click=lambda e:self.cambiar_pagina(0)),
                                    ft.TextButton('Ens vols conèixer?', style=ft.ButtonStyle(color=self.color_primaria),col=
                                    {"xs":12, "sm":1, "md":3},on_click=lambda e:self.cambiar_pagina(1)),
                                    ft.TextButton('Tap Room', style=ft.ButtonStyle(color=self.color_primaria),col=
                                    {"xs":12, "sm":1, "md":3},on_click=lambda e:self.cambiar_pagina(2)),
                                    ft.TextButton('Contacte', style=ft.ButtonStyle(color=self.color_primaria),col=
                                    {"xs":12, "sm":1, "md":3},on_click=lambda e:self.cambiar_pagina(3)),
                                ]
                                
                            ),
                            ft.Container(width=100,
                                         col={"sm": 6, "md": 4, "xl": 2},
                                         margin=ft.margin.only(right=20),
                                         content=self.cambiar_modo)




                        ]
                    )
                ),
                ft.Container(
                    expand = True,
                    content=ft.Stack(
                        controls=[
                            self.frame_cervezas,
                            self.frame_inicios,
                            
                            self.frame_TapR,
                            self.frame_contacto,
                            
                        ]
                    )

                    

                ),
                ft.Container(
                    
                    padding=2,
                    gradient=ft.LinearGradient(end=ft.alignment.top_center,begin=ft.alignment.top_right,colors=[ft.Colors.TRANSPARENT,self.color_primaria]),
                    
                    content=ft.Text('Copyright 2024 DGL - Tots els drets reservats.                                      LEGAL | PRIVACITAT | COOKIES                                                                                                                                               .',size = 14,color=ft.Colors.WHITE)
                         
                ),
                ft.TextButton("LEGAL",on_click=lambda e: e.page.open(self.frame_aviso_legal))
                
               
                
                
               
            ]
        )

        self.frame_aviso_legal = ft.AlertDialog(
            #adaptive = True,
            elevation = 0,
            modal=False,
            title=ft.Text("AVÍS LEGAL I TERMES DÚS"),
            content=ft.Text("En aquest espai, l'USUARI podrà trobar tota la informació relativa als termes i condicions legals que defineixen les relacions entre els usuaris i nosaltres com a responsables \nd'aquesta web. Com a usuari, és important que coneguis aquests termes abans de continuar la teva navegació. David 3DGL.Com a responsable d'aquesta web, \nassumeix el compromís de processar la informació dels nostres usuaris i clients amb plenes garanties i complir els requisits nacionals i europeus que regulen la recopilació i \nl'ús de les dades personals dels nostres usuaris. Aquesta web, per tant, compleix rigorosament amb el RGPD (REGLAMENT (UE) 2016/679 de protecció de dades) i la LSSI-\nCE la Llei 34/2002, d'11 de juliol, de serveis de la societat de la informació i de comerç electrònic.\n\n"),
            
           
        )

        self.frame_No_Cook = ft.AlertDialog(
            #adaptive = True,
            elevation = 0,
            modal=False,
            title=ft.Text("Acció no permesa¡¡"),
            content=ft.Text("\nPer accedir a aquesta pagina es necessari acceptar les Cookies.\n"),
            
           
        )

        self.frame_aviso_cook = ft.AlertDialog(
            #adaptive = True,
            elevation = 0,
            modal=True,
            title=ft.Text("Accepta cookies"),
            content=ft.Text("Utilitzem cookies pròpies i de tercers per millorar l’experiència d’usuari, analitzar el trànsit del lloc web i personalitzar el contingut.\n En fer clic a 'Accepta les cookies', accepteu l’ús de les cookies.\n\n"),
            actions=[
                ft.TextButton("Si", on_click=lambda e:self.cambiar_pagina1(1)),
                ft.TextButton("No", on_click=lambda e: e.page.open(self.frame_No_Cook))
            ]
        )
        
#----------------------------------------------------------------------------------
    
    def toggle_icon_button(self,e):
        

        if e.control.selected == False:
            self.cambiar_modo.icon = ft.Icons.DARK_MODE
            self.Page.theme_mode = "dark"
           
            self.Page.update()
        if e.control.selected == True:
            self.cambiar_modo.icon = ft.Icons.LIGHT_MODE
            self.Page.theme_mode = "light"
         
            self.Page.update()

        e.control.selected = not e.control.selected
        e.control.update()
   
    def cambiar_pagina1(self,e):

        if  e == 0:
            controls =[self.contentsInit,self.contentsInit2,self.contentsInit3]
            self.Page.add(ft.Stack(controls))
            self.frame_aviso_legal
            self.Page.update()            
           

            
       

        else:
            self.Page.views.clear()
            self.Page.views.append(self.contents1)
            self.cambiar_pagina(0)
            self.Page.update()

    def cambiar_pagina(self,e):
        self.frame_cervezas.offset.x = -2        
        self.frame_inicios.offset.x = -2

        self.frame_TapR.offset.x = -2
        self.frame_contacto.offset.x = -2

        if e==0:
            self.frame_cervezas.offset.x = 0

        if e==1:
            self.frame_inicios.offset.x = 0
        if e==2:
            self.frame_TapR.offset.x = 0
        if e==3:
            self.frame_contacto.offset.x = 0


        self.Page.update()


    def handle_close(self,e):
        self.page.close(self.dlg_modal)
        self.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))


ft.app(target=lambda Page: Portafolios(Page), assets_dir ='assets')
