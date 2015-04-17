init -3 python:
    # this is the master language so it lives at init level -3, not -2 like the others
    ### ENGLISH
    
    init_language("en")
    
    displayDict["en"].styleoverrides = {"font": mainfont, 
                                        "language": "western",
                                        "line_spacing": 0}
    
    displayDict["en"].timeformat = "%b %d, %H:%M"
    
    displayDict["en"].sayfont = mainfont
    
    displayDict["en"].quote_outer_open = u"“"
    displayDict["en"].quote_outer_close = u"”"
    displayDict["en"].quote_inner_open = u"‘"
    displayDict["en"].quote_inner_close = u"’"
    
    displayDict["en"].activeLanguage = "English"
    displayDict["en"].allLanguages = {}
    displayDict["en"].allLanguages["en"] = displayDict["en"].activeLanguage
    displayDict["en"].allLanguages["de"] = "German"
    displayDict["en"].allLanguages["it"] = "Italian"
    displayDict["en"].allLanguages["jp"] = "Japanese"
    displayDict["en"].allLanguages["ru"] = "Russian"
    
    displayDict["en"].act_term = u"Act"
    displayDict["en"].window_name = u"Katawa Shoujo: Summer's Clover"
    
    displayDict["en"].main_menu_start = u"Start"
    displayDict["en"].main_menu_load = u"Load"
    displayDict["en"].main_menu_extra = u"Extras"
    displayDict["en"].main_menu_config = u"Options"
    displayDict["en"].main_menu_quit = u"Quit"

    displayDict["en"].game_menu_return = u"Return"
    displayDict["en"].game_menu_show = u"Show image"
    displayDict["en"].game_menu_history = u"Text history"
    displayDict["en"].game_menu_skip = u"Skip mode"
    displayDict["en"].game_menu_auto = u"Auto mode"
    displayDict["en"].game_menu_config = u"Options"
    displayDict["en"].game_menu_save = u"Save"
    displayDict["en"].game_menu_load = u"Load"
    displayDict["en"].game_menu_main = u"Main menu"
    displayDict["en"].game_menu_quit = u"Quit"
    displayDict["en"].game_menu_current_scene = u"Current Scene"
    displayDict['en'].game_menu_current_music = u"Current music track"
    displayDict["en"].game_menu_replay_indicator = u"Replay"

    displayDict["en"].return_button_text = u"Return"

    displayDict["en"].hdisabled_label = u"Disable adult content"
    displayDict["en"].config_page_caption = u"Options"
    displayDict["en"].config_fullscreen_label = u'Fullscreen mode'
    displayDict["en"].config_transitions_label = u'Disable transitions'
    displayDict["en"].config_skip_unseen_label = u'Skip unread text'
    displayDict["en"].config_skip_after_choice_label = u'Keep skipping after choices'
    displayDict["en"].config_textspeed_label = u'Text speed'
    displayDict["en"].config_afmspeed_label = u'Auto mode delay'
    displayDict["en"].config_musicvol_label = u"Music volume"
    displayDict["en"].config_musicvol_jukebox_label = u"Vol."
    displayDict["en"].config_sfxvol_label = u"SFX volume"
    displayDict["en"].config_sfxtest_label = u"Test"
    displayDict["en"].config_gamepad_label = u"Gamepad keymap…"

    displayDict["en"].config_language_sel = u"Language selection…"
    displayDict["en"].config_language_caption = u"Options > Language selection"
    displayDict["en"].config_language_restart_note = "Note: Changing the language while a session is in progress will return the game to the latest script node."

    displayDict["en"].gamepad_caption = u"Options > Gamepad keymap"
    displayDict["en"].gamepad_key_na = u"Not assigned"
    displayDict["en"].gamepad_request_key = u"Press the button you want to assign “%s” to.\nClick the mouse or the select button to clear the mapping."

    displayDict["en"].yesno_yes = u"Yes"
    displayDict["en"].yesno_no = u"No"
    displayDict["en"].yesno_okay = u"Continue"
    displayDict["en"].yesno_savesuccess = u"Progress successfully saved\nas number %s."
    displayDict["en"].yesno_quit = u"Are you sure you want to\nquit Katawa Shoujo?"
    displayDict["en"].yesno_return_to_main = u"Are you sure you want to\nreturn to the main menu?"
    displayDict["en"].save_page_caption = u"Save"
    displayDict["en"].new_save_button = u"Create new save state"
    displayDict["en"].load_page_caption = u"Load"
    displayDict["en"].yesno_load_in_game = u"Are you sure you want to\ndiscard your progress?"
    displayDict["en"].yesno_save_overwrite = u"Are you sure you want to\noverwrite your save?"
    displayDict["en"].yesno_delete_savegame = u"Are you sure you want to\ndelete save number %s?"
    displayDict["en"].play_time_label = u"Play time"
    displayDict["en"].show_manual_saves = u"Manual"
    displayDict["en"].show_auto_saves = u"Auto"

    displayDict["en"].text_history_caption = u"Text history"

    displayDict["en"].extra_menu_caption = "Extras"
    displayDict["en"].extra_music_button_label = "Jukebox"
    displayDict["en"].extra_gallery_button_label = "Gallery"
    displayDict["en"].extra_scene_button_label = "Library"
    displayDict["en"].extra_omake_button_label = "Omake"
    displayDict["en"].extra_opening_button_label = "Cinema"
    displayDict["en"].commentary_label = "Enable commentary"

    displayDict["en"].music_page_caption = "Extras > Jukebox"
    displayDict["en"].music_stop_button_text = "Stop"
    displayDict["en"].music_now_playing = "Now playing"

    displayDict["en"].gallery_page_caption = "Extras > Gallery"
    displayDict["en"].gallery_onelocked = "One further image not unlocked."
    displayDict["en"].gallery_manylocked = "%d further images not unlocked."
    displayDict["en"].gallery_singlelocked = "Image %d of %d is not unlocked."
    displayDict["en"].gallery_num_page_prefix = "Page "
    displayDict["en"].gallery_num_page_error = "No images to display"

    displayDict["en"].scene_page_caption = "Extras > Library"
    displayDict["en"].scene_completion_label = "Completion: %s%%"
    displayDict["en"].scene_playthrough_label = "Use replay flow (recommended)"
    
    displayDict["en"].joy_left = "Left"
    displayDict["en"].joy_right = "Right"
    displayDict["en"].joy_up = "Up"
    displayDict["en"].joy_down = "Down"
    displayDict["en"].joy_dismiss = "Select/Advance"
    displayDict["en"].joy_rollback = "Text history"
    displayDict["en"].joy_holdskip = "Hold to skip"
    displayDict["en"].joy_toggleskip = "Skip mode"
    displayDict["en"].joy_hide = "Show image"
    displayDict["en"].joy_menu = "Show menu"

    ##Names

    displayDict["en"].name_hi = "Hisao"
    displayDict["en"].name_all = "All"
    displayDict["en"].name_ha = "Hanako"
    displayDict["en"].name_emi = "Emi"
    displayDict["en"].name_rin = "Rin"
    displayDict["en"].name_li = "Lilly"
    displayDict["en"].name_shi = "Shizune"
    displayDict["en"].name_mi = "Misha"
    
    displayDict["en"].name_ke = "Kenji"
    displayDict["en"].name_mu = "Mutou"
    displayDict["en"].name_nk = "Nurse"
    displayDict["en"].name_no = "Nomiya"
    displayDict["en"].name_yu = "Yuuko"
    displayDict["en"].name_sa = "Sae"
    displayDict["en"].name_aki = "Akira"
    displayDict["en"].name_hh = "Hideaki"
    displayDict["en"].name_hx = "Jigoro"
    displayDict["en"].name_emm = "Meiko"
    
    displayDict['en'].name_mk = "Miki"
    
    displayDict["en"].name_mystery = "???"

    displayDict["en"].name_ha_ = "Purple-haired girl"
    displayDict["en"].name_emi_ = "Twintails girl"
    displayDict["en"].name_rin_ = "Strange girl"
    displayDict["en"].name_li_ = "Wavy-haired girl"
    displayDict["en"].name_mi_ = "Laughing girl"
    displayDict["en"].name_ke_ = "Bespectacled hallmate"
    displayDict["en"].name_mu_ = "Tall man"
    displayDict["en"].name_yu_ = "Librarian"
    displayDict["en"].name_no_ = "Silver-haired man"
    displayDict["en"].name_sa_ = "Gallerist"
    displayDict["en"].name_aki_ = "Well-dressed person"
    displayDict["en"].name_nk_ = "Smiling man"
    displayDict["en"].name_hx_ = "Shizune's father"
    displayDict["en"].name_hh_ = "Slim girl"
    displayDict["en"].name_emm_ = "Emi's mother"
    
    displayDict["en"].name_har = "Haru"
    displayDict["en"].name_suz = "Suzu"
    displayDict["en"].name_yuk = "Yukio"
    displayDict["en"].name_jun = "Dad"
    displayDict["en"].name_tsu = "Tsubasa"
    displayDict["en"].name_yam = "Yamada"
    
    displayDict["en"].name_dad = "Suzu's father"
    displayDict["en"].name_mot = "Suzu's mother"
    
    # Scenes available in the extras -> scene select menu. Name, label, description, path (path may also be a tuple).
    displayDict["en"].s_scenes = (("Prologue", "C0", True, "Act 1"),
                                    ("The Runner", "C1", True, "Act 1"),
                                    ("Singalong", "C2", True, "Act 1"),
                                    ("A Girl Named Suzu", "C3", True, "Act 1"),
                                    ("Shared Table", "C4", True, "Act 1"),
                                    ("Evening Stroll", "C5", True, "Act 1"),
                                    ("To Town, To Town", "C6", True, "Act 1"),
                                    ("Troubled Correspondence", "C7", True, "Act 1"),
                                    ("One Night in July", "C8", True, "Act 1"),
                                    ("Echoes of the Past", "C9", True, "Act 1"),
                                    
                                    ("Study and Such", "H1", True, "Hisao"),
                                    ("Homecoming", "H2", True, "Hisao"),
                                    ("Country Jaunt", "H3", True, "Hisao"),
                                    ("Blood and Sweat", "H4", True, "Hisao"),
                                    ("Past Zenith", "H5", True, "Hisao"),
                                    ("Over the Hills", "H6", True, "Hisao"),
                                    ("Hello, Yamaku", "H7", True, "Hisao"),
                                    ("Into the Deep", "H8", True, "Hisao"),
                                    ("Noon Run", "H9", True, "Hisao"),
                                    ("Disconnection", "H10", True, "Hisao"),
                                    ("Goodbye, Hello", "H11", True, "Hisao"),
                                    
                                    ("Serendipity", "S1", True, "Suzu"),
                                    ("Reverie", "S2", True, "Suzu"),
                                    ("Fireworks", "S3", True, "Suzu"),
                                    ("The New World", "S4", True, "Suzu"),
                                    ("Hand in Hand", "S5", True, "Suzu"),
                                    ("Morning Stroll", "S6", True, "Suzu"),
                                    ("Sands of Time", "S7", True, "Suzu"),
                                    ("Night on the Town", "S8", True, "Suzu"),
                                    ("Frayed Knot", "S9", True, "Suzu"),
                                    ("Amends", "S10", True, "Suzu"),
                                    ("Small Hope", "S11", True, "Suzu"),
                                    ("Loss", "S12", True, "Suzu"),
                                    ("Reminiscence", "S13", True, "Suzu"),
                                    ("Redemption", "S14", True, "Suzu"),
                                    )

# TITLE CARDS
    # Definition. This maps an id tuple to a tuple of displayed text, filename modifier, and the position of said text.
    # the display function is tcard() in ui_code.rpy
    displayDict["en"].act_names = {(1, "all"): ("The Runner", "act1", 100, 70), 
                                 (2, "suzu"): ("Suzu", "act2suzu", 100, 250), 
                                 (2, "hisao"): ("Hisao", "act2hisao", 200, 120), 
                                }
    # credits
    
    displayDict["en"].creditstring = """{b}Head Writer{/b}
Suriko

{b}Music{/b}
Nicol Armarfi

{b}Artists{/b}
raemz
Katawa Shoujo artists


{b}Engineering{/b}
StanR
Kickaha

{b}Producer{/b}
Suriko

                                     
                                     

{b}Thanks{/b}
Four Leaf Studios




{b}Special Thanks{/b}
PyTom
KSG Threads on /vg/
RAITA
Prealpha Repair Team"""
