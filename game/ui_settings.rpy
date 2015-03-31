# settings.rpy: contains ui and game config, plus simple displayable definitions

init -1 python:
    
    #layout.compat()
    
    #This is a line I found in the final version of ui_settings. I think it turns all Position() calls into Transforms()
    Position = Transform
    
    layout.provides("load_save")
    layout.provides("yesno_prompt")
    layout.provides("preferences")
    layout.button_menu()
    theme.roundrect()

    config.locked = False
    config.time_format = "%b %d, %H:%M"
    config.file_entry_format = "%(time)s\n%(save_name)s"
    config.preferences = { }
    config.all_preferences = { }
    
    #config.layers.insert(1, 'vfx')
    config.layers.insert(0, 'kelpersux')
    config.locked = True

init 1:

    # VERY basic config, more later
    ## FOR RELEASES, ALSO CHECK ui_early.rpy! (save game path)
    $ config.searchpath.append('archived')
    $ config.developer = False
    $ config.window_title = u"" # is completely dynamic
    $ release_is_demo = False # if True, game ends after Festivals
    #$ config.rollback_enabled = False # oh yeah I went there
    $ config.has_autosave = True
    $ config.nvl_show_display_say = say_wrapper
    
    #This is here because this is replacing a non-fuctioning Python function of the same name. This needs to be outside a Python block to work properly -md01
    transform Slide (start_pos, start_anchor, end_pos, end_anchor, my_time, time_warp=_ease_in_time_warp):
        xpos start_pos xanchor start_anchor yalign 1.0
        warp time_warp my_time xpos end_pos xanchor end_anchor
    
    python:
    
    ######## SPRITE WRAPPER #########

        
        def ks_sprite(char, expr_name, suffix_list=[]):
            
            path_trunk = "sprites/" + char + "/"
            
            missingsprite_char = path_trunk + char + "_missing.png"
            if renpy.loadable(missingsprite_char):
               missingsprite = missingsprite_char
            else:
               missingsprite = "sprites/others/generic_missing.png"

            # base file and closeup thereof
            regular_files = [(path_trunk + char + "_" + expr_name + ".png",expr_name),
                             (path_trunk + "close/" + char + "_" + expr_name + "_close.png",expr_name+"_close"),
                             (path_trunk + "superclose/" + char + "_" + expr_name + "_superclose.png",expr_name+"_superclose")]

            # make hard variations (a list of tuples: filename, modified expr_name)
            # also add a closeup for each
            for suffix in suffix_list:
                regular_files.append((path_trunk + char + "_" + expr_name + "_" + suffix + ".png",expr_name+"_"+suffix))
                regular_files.append((path_trunk + "close/" + char + "_" + expr_name + "_" + suffix + "_close.png",expr_name+"_"+suffix+"_close"))
         
            # define the files, including filters
            # we check whether the files actually exist here as well
            for filename, mod_expr_name in regular_files:
                if not renpy.loadable(filename):
                    checked_filename = missingsprite
                else:
                    checked_filename = filename
                renpy.image((char,mod_expr_name), checked_filename)
                for filter, filtersuffix in sp_filters:
                    renpy.image((char,mod_expr_name+"_"+filtersuffix), filter(checked_filename))


        def make_sprites(char, expr_list, suffix_list=[]):
            for expr in expr_list:
                ks_sprite(char, expr, suffix_list)


    ######### BG WRAPPER ########
    
        def ks_bg(bgid):
        
            path = "bgs/"
            tag = "bg"
            
            base_image = path + bgid + ".jpg"

            renpy.image((tag,bgid), base_image)
            for filter, filtersuffix in bg_filters:
                prefiltered = path + bgid + "_" + filtersuffix + ".jpg"
                if renpy.loadable(prefiltered):
                    renpy.image((tag,bgid+"_"+filtersuffix), prefiltered)
                else:
                    renpy.image((tag,bgid+"_"+filtersuffix), filter(base_image))
  


    ########## BACKGROUNDS ##########

    # CITY
        ks_bg("city_alley")
        ks_bg("city_busint")
        ks_bg("city_graveyard")
        ks_bg("city_karaokeext")
        ks_bg("city_karaokeint")
        ks_bg("city_street1")
        ks_bg("city_street2")
        ks_bg("city_street2_ni")
        ks_bg("city_street3_ni")
        ks_bg("city_street3")
        ks_bg("city_street4_ni")
        ks_bg("city_street4")
        ks_bg("city_funeral")
        ks_bg("city_street5")
        ks_bg("city_streetnight")
        ks_bg("city_subway")
        ks_bg("city_trainstation")
        ks_bg("city_busstation")
        
        ks_bg("city_trainscenery")
        ks_bg("city_trainscenerycity")
        ks_bg("city_tokyostation")
        
        ks_bg("city_apartment")
        ks_bg("city_busstat")
        ks_bg("city_houseext")
        ks_bg("city_houseint")
        ks_bg("city_busride")
        ks_bg("city_busride_ni")
        
        ks_bg("city_cafe")

    # MISC
        
        ks_bg("misc_sky_rn")
        ks_bg("misc_sky_rays")
        ks_bg("misc_sky")
        ks_bg("misc_static")
        ks_bg("misc_ceiling")
        ks_bg("misc_heartattack")

    # SCHOOL
        ks_bg("school_auditorium")
        ks_bg("school_backexit")
        ks_bg("school_backstage")
        ks_bg("school_cafeteria")
        ks_bg("school_classroomart")
        ks_bg("school_council")
        ks_bg("school_courtyard")
        ks_bg("school_courtyard_ni")
        ks_bg("school_dormbathroom")

        ks_bg("school_dormext")
        ks_bg("school_dormext_start")
        ks_bg("school_dormext_half")
        ks_bg("school_dormext_full")

        ks_bg("school_dormhallground")
        ks_bg("school_dormhallway")
        ks_bg("school_girlsdormhall")
        ks_bg("school_dormhisao")
        ks_bg("school_dormhisao_blurred")
        ks_bg("school_dormbathroom2")

        ks_bg("school_dormkenji")
    
        ks_bg("school_gate")

        ks_bg("school_gardens")
        ks_bg("school_gardens2")
        ks_bg("school_gardens3")
        ks_bg("school_greendoor")
        ks_bg("school_forest1")
        ks_bg("school_forest2")
        ks_bg("school_forestclearing")
        ks_bg("school_picnic")
        ks_bg("school_picniccliff")
        ks_bg("school_greathall")
        ks_bg("school_hallway2")
        ks_bg("school_hallway3")
        ks_bg("school_hallway3_blurred")
        ks_bg("school_hilltop_border")
        ks_bg("school_hilltop_spring")
        ks_bg('school_hilltop_border_summer')
        ks_bg("school_hilltop_summer")
        ks_bg("school_library")
        ks_bg("school_librarynolights")
        ks_bg("school_lobby")
        ks_bg("school_musicroom")
        ks_bg("school_nursehall")
        ks_bg("school_nurseoffice")
        ks_bg("school_nomiya")
        ks_bg("school_principal")
        ks_bg("school_roof")
        ks_bg("school_scienceroom")
        ks_bg("school_sportstoreroom")
        ks_bg("school_staircase1")
        ks_bg("school_staircase2")
        ks_bg("school_stalls1")
        ks_bg("school_stalls2")
        ks_bg("school_track")
        ks_bg("school_track_on")
        ks_bg("school_track_running")
        ks_bg("school_road")
        ks_bg("school_miyagi")
        ks_bg("school_room32")
        ks_bg("school_room34")  

    # SUBURB
        ks_bg("suburb_konbiniext")
        ks_bg("suburb_konbiniint")
        ks_bg("suburb_park")
        ks_bg("suburb_roadcenter")
        ks_bg("suburb_shanghaiext")
        ks_bg("suburb_shanghaiint")
        ks_bg("suburb_tanabata")
        ks_bg("suburb_artshop")
        ks_bg("tanabata_bamboo")

    
    #This is the static used in the flashback sequences of the final - md01
    python:
        def noisetile(bitmap, opacity=0.10000000000000001):
            return im.Tile(im.Alpha(bitmap, opacity))
    
    image noiseoverlay:
        noisetile("vfx/noise1.png") 
        pause 0.1
        noisetile("vfx/noise2.png") 
        pause 0.1
        noisetile("vfx/noise3.png") 
        pause 0.1
        repeat

    ########## END BACKGROUNDS ##########


    ########## SPRITES ##########
    # Minor characters
    python:
        make_sprites('yuuko',['smile','neutral','happy','closedhappy','worried', 'neurotic', 'panic',], ['shang','up','down'])
        make_sprites('yuukoshang',['smile','neutral','happy','closedhappy','worried', 'neurotic', 'panic','invis', 'noglasses'], ['up','down'])
        make_sprites('kenji',['neutral','happy','tsun','rage','surprised','invis'], ['naked'])
        make_sprites('muto',['normal','smile','irritated','invis'])



    ########## END SPRITES ##########


    ########## EVENT CGS ##########
    # OTHER
    image ev hisao_class_start = im.Crop("event/hisao_class.jpg", 0, 0, 800, 600)
    image ev hisao_class_move = At("event/hisao_class.jpg",Move((0.0, 0.0, 0.0, 0.0), (1.0, 0.0, 1.0, 0.0), 40.0, time_warp=acdc_warp, subpixel=True))
    image ev hisao_class_end = im.Crop("event/hisao_class.jpg", 800, 0, 800, 600)
    
    python:
        def roofcomposite(comppath):
            return im.Composite(None, (0, 0), 'event/rin_roof_boredom.jpg', (300, 200), comppath)
    
    #(((math.sin((((at) / (2.0)) % (2.0)) * (math.pi))) + (1.0)) / (2))

    python:
        def trainwave(at):
            import math
            return (0.0, (((math.cos(math.pi * at))/60) +0.5), 0.0, 0.5)
            

    image city_tokyostation = 'bgs/city_tokyostation.jpg'
    image city_houseext = 'bgs/city_houseext.jpg'
    
    python:
        def traincomposite(comppath):
            return im.Composite(None, (0, 0), 'event/hisao_train/hisao_trainride_ni_norm.png', (321, 200), comppath)

    image ev other_summersclover = "vfx/other_summersclover.jpg"
    #image ev other_summersclover = im.Crop("vfx/other_summersclover.jpg", 800, 0, 800, 600)
    
    # Images available in the extras -> CG gallery menu. May contain internal images names (including the prefix) or tuples of same.
    # The latter will share a thumbnail (the first unlocked one) and will be shown in sequence.
    $ ex_g_images = ("ev other_summersclover",
                     )
    
                     

    ########## END EVENT CGS ##########

    ########## SUPER CGS ##########
    ########## END SUPER CGS ##########

    # experimental stuff
    python:
        def silhouette(disp, color=0):
            return im.Map(disp, rmap=im.ramp(color, color), gmap=im.ramp(color, color), bmap=im.ramp(color, color))

    image kenji silhouette = silhouette("sprites/kenji/kenji_neutral.png")

    image bloodred = Solid("#d00")
    image white = Solid("#fff")
    image pink = Solid("#FF7FD4")
    image darkgrey = Solid("#0D0D0D")
    image bg school_roof_ni_crop = im.Crop("bgs/school_roof_ni.jpg",200,0,800,600)
    image n_vignette = "vfx/narrowvignette.png"
    image sc_comp = "vfx/sc_comp.png"

    image screen = Solid("#000000CC")
    image endscreen = "ui/4lsl.png"

    # prawns courtesy of PDphoto.org via http://commons.wikimedia.org/wiki/Image:Prawns_1.jpg
    python:
        prawn_image = None
        prawns = None
        prawn_images = ("prawns.jpg", "climatic.jpg")
        def make_prawns(a=None, b=None):
            global prawn_image, prawns, prawn_images
            if not prawn_image or not prawns or a < 0.1:
                prawn_image = renpy.random.choice(prawn_images)
                prawns = LiveComposite((800,600),
                                 (0,0), Animation(At("ui/"+prawn_image,Zoom((800,600),(0,0,799,599),(16,12,768,576),0.05, xalign=0.5, yalign=0.5)),0.05,
                                                  At("ui/"+prawn_image,Zoom((800,600),(16,12,768,576),(0,0,799,599),0.7, time_warp=_ease_in_time_warp, xalign=0.5, yalign=0.5)),0.7,
                                                  At("ui/"+prawn_image,Zoom((800,600),(0,0,799,599),(0,0,799,599),0.1, xalign=0.5, yalign=0.5)),0.118,
                                                  At("ui/"+prawn_image,Zoom((800,600),(0,0,799,599),(8,6,784,588),0.05, xalign=0.5, yalign=0.5)),0.02,
                                                  At("ui/"+prawn_image,Zoom((800,600),(8,6,784,588),(0,0,799,599),0.3, time_warp=_ease_in_time_warp, xalign=0.5, yalign=0.5)),0.3),
                                 (610,10), "ui/bt-logoonly.png")
            return (prawns,20)
    
    
    image prawns = DynamicDisplayable(make_prawns)
    
    image fakenvltextbox = "ui/bg-nvl.png"
    
    #black version:
    image alivetext = renpy.ParameterizedText(yalign=0.5, xanchor=0, xpos = 130, style="alive_text", drop_shadow=None, color="#000000")
    #moved white version:
    image walivetext = renpy.ParameterizedText(yalign=0.5, xanchor=0.5, xpos = 0.5, style="alive_text", drop_shadow=None, color="#ffffff")
    

    image nightsky rotation = At("bgs/misc_sky_ni.jpg", Position(xalign=0.5, yalign=0.5), RotoZoom(0, 360, 40, 3, 1.5, 10, rot_repeat=True, zoom_repeat=False, xalign=0.5, yalign=0.5))
    image nightsky normal = At("bgs/misc_sky_ni.jpg", Position(xpos=0.5, ypos=1.0, xanchor=0.5, yanchor=0.9))
    image nightsky zoom = At("bgs/misc_sky_ni.jpg", FactorZoom(1.0, 0.9, 2.0, time_warp=_ease_time_warp, opaque=True), Move((0.5, 1.0, 0.5, 0.9), (0.5, 1.0, 0.5, 1.15), 2.0, time_warp=_ease_time_warp))
    image cityscape zoom = At("vfx/cityscape.png", FactorZoom(1.5, 1.0, 2.0, time_warp=_ease_time_warp, opaque=False), Move((-0.25, 1.0, 0.0, 0.0), (0.0, 1.0, 0.0, 1.0), 2.0, time_warp=_ease_time_warp))
    image hill enter = At("vfx/hillouette.png", Move((0.5, 1.0, 0.5, 0.0), (0.5, 1.0, 0.5, 1.0), 2.0, time_warp=_ease_time_warp))
    image hill pairtouch = "vfx/hillpair1.png"
    image hill pairnotouch = "vfx/hillpair2.png"
    
    image movie = Movie(fps=40, size=(800, 600), xalign=0.5, yalign=0.5)

    image centeredmovie = Movie(fps=25, xalign=0.5, yalign=0.5)
init python:

    
    ########## IMAGE FILTERS ###########
    def rain(img_in):
        return im.MatrixColor(img_in, ((im.matrix.saturation(0.40000000000000002)) * (im.matrix.tint(0.94999999999999996, 0.94999999999999996, 1.0))) * (im.matrix.brightness(-(0.10000000000000001))))
    def sp_rain(img_in):
        return im.MatrixColor(img_in, ((im.matrix.saturation(0.59999999999999998)) * (im.matrix.tint(0.95999999999999996, 0.95999999999999996, 1.0))) * (im.matrix.brightness(-(0.050000000000000003))))
    
    def night(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6))
       
    def sunset(img_in):
       return im.MatrixColor(img_in, im.matrix.tint(1.1, 0.95, 0.85) * im.matrix.brightness(0.1) * im.matrix.saturation(1.2))
    
    def sp_sunset(img_in):
       return im.MatrixColor(img_in, im.matrix.tint(1.02, 0.95, 0.9) * im.matrix.brightness(0.05) * im.matrix.saturation(1.1))
       
    #Added in past filter, hopefully -md01
    def past(img_in):
        return im.MatrixColor(img_in, (im.matrix.saturation(0.14999999999999999)) * (im.matrix.tint(1.0, 0.93999999999999995, 0.76000000000000001)))
        
    #This is the filter used on Yuuko in scene S33 (Watershed) -md01
    #For im.matric.tint, colors are Red, Green, Blue
    def nolights(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.9, 0.9, 0.9) * im.matrix.saturation(0.8))
    
    
    bg_filters = ((sunset,'ss'),
                  (night,'ni'),
                  (rain,'rn'),
                  (past,'fb'),
                  (nolights, 'nl'),
                  )
    
    sp_filters = ((sp_sunset,'ss'),
                  (night,'ni'),
                  (sp_rain,'rn'),
                  (past,'fb'),
                  (nolights,'nl'),
                  )
    
    # Simple animations
    # splash logo
    flslogo = At(anim.TransitionAnimation(Solid("#000"), 1.0, pixellate,
                                       "ui/4lsl.png", 6.0, Dissolve(1.0),
                                       Solid("#000")), Zoom((800, 600), (0, 0, 800, 600), (50, 37, 700, 525), 10.0))

    # letterbox
    letterbox = LiveComposite((800,600),
                              (0,0), Solid("#000", ymaximum=75),
                              (0,525), Solid("#000", ymaximum=75))
    renpy.image("letterbox",letterbox)

    #OP1 fadeout
    passoutOP1 = anim.TransitionAnimation(Solid("#0000"), 0.0, ImageDissolve(im.Tile("ui/tr-flashback.png"), 6.0, 32, alpha=True),
                                          Solid("#000"))
    renpy.image("passoutOP1", passoutOP1)

    letter_in = ImageDissolve(im.Tile("ui/tr-letter.png"), 1.0, 8, reverse=True)
    letter_out = ImageDissolve(im.Tile("ui/tr-letter.png"), 1.0, 8)

    hands_in = ImageDissolve("vfx/handsdissolve.png", 0.2, ramplen=256, reverse=True)
    hands_out = ImageDissolve("vfx/handsdissolve.png", 0.2, ramplen=256)
    
    hands_inslow = ImageDissolve("vfx/handsdissolve.png", 0.3, ramplen=256, reverse=True)

    #snow
    snowfg = SnowBlossom("vfx/snowflake.png", start=3.0, count=30, border=50, xspeed=(20, 50), yspeed=(120, 180), fast=True)
    snowbg = SnowBlossom(im.Scale("vfx/snowflake.png",5,5), count=60, yspeed=(80, 120), start=3.0, border=50, xspeed=(20, 50), fast=True)
    renpy.image("snow",LiveComposite((800,600),
                                     (0,0),snowbg,
                                     (0,0),snowfg))

    flash = Fade(0.25, 0,.75, color="#FFFFFF")
    
    shortflash = Fade(0.25, 0, 0.4, color="#FFFFFF")
    
    
    whiteout = Fade(0.5, 0.2, 2.0, color="#FFFFFF")

    #crowd
    crowd = anim.TransitionAnimation("vfx/crowd1.png", 1.0, Dissolve(0.2, alpha=True),
                                     "vfx/crowd2.png", 1.0, Dissolve(0.2, alpha=True),
                                     "vfx/crowd3.png", 1.0, Dissolve(0.2, alpha=True))

    

    renpy.image("crowd", crowd)

    
    crowd_ss = anim.TransitionAnimation(sunset("vfx/crowd1.png"), 1.0, Dissolve(0.2, alpha=True),
                                        sunset("vfx/crowd2.png"), 1.0, Dissolve(0.2, alpha=True),
                                        sunset("vfx/crowd3.png"), 1.0, Dissolve(0.2, alpha=True))

    renpy.image("crowd_ss", crowd_ss)
    
    crowd_ni = anim.TransitionAnimation(night("vfx/crowd1.png"), 1.0, Dissolve(0.2, alpha=True),
                                        night("vfx/crowd2.png"), 1.0, Dissolve(0.2, alpha=True),
                                        night("vfx/crowd3.png"), 1.0, Dissolve(0.2, alpha=True))

    renpy.image("crowd_ni", crowd_ni)

    #steam
    steam = anim.TransitionAnimation("vfx/steam1.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam2.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam3.png", 1.5, Dissolve(0.5, alpha=True))
    steam2 = anim.TransitionAnimation("vfx/steam3.png", 0.75, Dissolve(0.5, alpha=True),
                                     "vfx/steam1.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam2.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam3.png", 0.75, None)

    renpy.image("steam", steam)
    renpy.image("steam2", steam2)


    flashback = ImageDissolve(im.Tile("ui/tr-flashback.png"), 2.0, 32, alpha=True)
    flashback_slow = ImageDissolve(im.Tile("ui/tr-flashback.png"), 3.0, 32, alpha=True)
    clockwipe = ImageDissolve(im.Tile("ui/tr-clockwipe.png"), 2.0, 8)
    renpy.image("kslogo heart", "ui/bt-logolarge-heartonly.png")    
    renpy.image("kslogo words", "ui/bt-logolarge.png")
    
    renpy.image("credits mask", "ui/roll_mask.png")
    
  
    
    runningspline = SplineMotion([
        ((0.470, 0.485,),),
        ((0.508, 0.525,), (0.484, 0.464,), (0.482, 0.541,),),
        ((0.518, 0.483,), (0.534, 0.512,), (0.532, 0.488,),),
        ((0.480, 0.528,), (0.506, 0.464,), (0.500, 0.544,),),
        ((0.470, 0.485,), (0.466, 0.520,), (0.452, 0.507,),),
        ], 1.1, anchors=(0.5, 0.5), repeat=True)
    
    fastrunningspline = SplineMotion([
        ((0.470, 0.485,),),
        ((0.508, 0.525,), (0.484, 0.464,), (0.482, 0.541,),),
        ((0.518, 0.483,), (0.534, 0.512,), (0.532, 0.488,),),
        ((0.480, 0.528,), (0.506, 0.464,), (0.500, 0.544,),),
        ((0.470, 0.485,), (0.466, 0.520,), (0.452, 0.507,),),
        ], 0.8, anchors=(0.5, 0.5), repeat=True) 

    
    
    def Updownpan(time, dir="down"):
        uppos = (0.0,0.0,0.0,0.0)
        downpos = (0.0,1.0,0.0,1.0)
        if dir == "down":
            return Move(uppos,downpos,time, time_warp=acdc_warp, subpixel=True)
        else:
            return Move(downpos,uppos,time, time_warp=acdc_warp, subpixel=True)
    
    
    
    def Fullpan(time, dir="right"):
        leftpos = (0.0,0.0,0.0,0.0)
        rightpos = (1.0,0.0,1.0,0.0)
        if dir == "right":
            return Move(leftpos,rightpos,time, time_warp=acdc_warp, subpixel=True)
        else:
            return Move(rightpos,leftpos,time, time_warp=acdc_warp, subpixel=True)
    
    #Replaced this with new slide from final -md01
    #def Slide(start_pos, start_anchor, end_pos, end_anchor, time, time_warp=_ease_in_time_warp):
        #return Move((start_pos,1.0,start_anchor,1.0),(end_pos,1.0,end_anchor,1.0),time, time_warp=time_warp, subpixel=True)
        

    
    # very code-heavy stuff is in ui.rpy: Fireworks, rain, doublespeak(), wallodrugs, etc.

    # OTHER
    # display tools
    twoleft = Position(xanchor=0.5, xpos=0.3, yanchor=0.5, ypos=0.5)
    tworight = Position(xanchor=0.5, xpos=0.7, yanchor=0.5, ypos=0.5)
    
    twoleftsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.3, ypos=1.15)
    tworightsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.7, ypos=1.15)
    leftsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.15, ypos=1.15)
    rightsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.85, ypos=1.15)
    centersit = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.15)
    centersit2 = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.07)
    centersitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.25)   
    
    closeleft = Position(xanchor=0.5, xpos=0.25, yanchor=0.5, ypos=0.5)
    closeright = Position(xanchor=0.5, xpos=0.75, yanchor=0.5, ypos=0.5)
    closeleft2 = Position(xanchor=0.5, xpos=0.20,yanchor=0.5, ypos=0.5)

    rightedge = Position(xanchor=0.5, xpos=0.92, yanchor=0.5, ypos=0.5)
    leftoff = Position(xanchor=0.5, xpos=0.13, yanchor=0.5, ypos=0.5)
    centeroff = Position(xanchor=0.5, xpos=0.52, yanchor=0.5, ypos=0.5)
    
    twoleftoff = Position(xanchor=0.5, xpos=0.32, yanchor=0.5, ypos=0.5)
    tworightoff = Position(xanchor=0.5, xpos=0.68, yanchor=0.5, ypos=0.5)
    centeroff = Position(xanchor=0.5, xpos=0.52, yanchor=0.5, ypos=0.5)
    twocenteroff = Position(xanchor=0.5, xpos=0.39, yanchor=0.5, ypos=0.5)
    twocenteroff2 = Position(xanchor=0.5, xpos=0.41, yanchor=0.5, ypos=0.5)
    twocenteroff3 = Position(xanchor=0.5, xpos=0.59, yanchor=0.5, ypos=0.5)

    tworightstagger = Position(xanchor=0.5, xpos=0.6, yanchor=0.5, ypos=0.5)
        
    leftdoor = Position(xanchor=0.5, xpos=0.10, yanchor=0.5, ypos=0.5)
    leftdooropen = Position(xanchor=0.5, xpos=-0.1, yanchor=0.5, ypos=0.5)
    rightwallopen = Position(xanchor=0.5, xpos=0.85, yanchor=0.5, ypos=0.5)
    roomopen = Position(xanchor=0.5, xpos=0.45, yanchor=0.5, ypos=0.5)

    bgleft = Position(xanchor=0.5, xpos=0.4, yanchor=0.5, ypos=0.5)
    bgright = Position(xanchor=0.5, xpos=0.6, yanchor=0.5, ypos=0.5)
    


    ######## CHARACTERS - ADV characters ########

    #config.nvl_page_ctc = anim.Blink("ui/ctc.png", offset=1.0, ypos=570, xpos=772)
    config.nvl_page_ctc = anim.Filmstrip("ui/ctc_strip.png", (16,16), (8,8), 0.03, ypos=560, xpos=772) #This MAY be more efficient...
    config.nvl_page_ctc_position = "fixed"

    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)

    #actually fix quotation
    def change_quotes(what):
        innerwhat = what [1:-1]
        innerwhat = innerwhat.replace(displayStrings.quote_outer_open,displayStrings.quote_inner_open)
        innerwhat = innerwhat.replace(displayStrings.quote_outer_close,displayStrings.quote_inner_close)
        what = what[0] + innerwhat + what[-1]
        return what

    # this fixes quotation levels in dialogue (except for doublespeak and rinbabble)
    def quotefixer(who, what, **kwargs):
        return say_wrapper(who, change_quotes(what), **kwargs)
    
    def define_characters(): # now a function for i18n purposes
        
        add_styles = prefix_dict(displayStrings.styleoverrides, prefix="what_", combine=True)
        
        # We overwrite this character, since all ADV characters automatically inherit from it
        #adv = Character(name=None, ctc=config.nvl_page_ctc, ctc_position = "fixed", show_function=say_wrapper)
        store.adv = ReadbackADVCharacter(name=None,
                                         ctc=config.nvl_page_ctc,
                                         ctc_position = "fixed",
                                         show_function=quotefixer,
                                         what_prefix=displayStrings.quote_outer_open,
                                         what_suffix=displayStrings.quote_outer_close,
                                         **add_styles)
        
        store.name_only = Character(None, kind=adv)

        #base characters

        store.hi = Character(displayStrings.name_hi, color="#629276")
        store.all = Character(displayStrings.name_all, color="#FFFFFF")
        store.ha = Character(displayStrings.name_ha, color="#897CBF")
        store.emi = Character(displayStrings.name_emi, color = "#FF8D7C")
        store.rin = Character(displayStrings.name_rin, color = "#b14343")
        store.li = Character(displayStrings.name_li, color="#F9EAA0")
        store.shi = Character(displayStrings.name_shi, color="#72ADEE")
        store.mi = Character(displayStrings.name_mi, color="#FF809F")

        store.mi_shi = Character(displayStrings.name_shi, color="#FF809F")
        store.mi_not_shi = Character("{s}"+displayStrings.name_shi+"{/s} "+displayStrings.name_mi, color="#FF809F")

        store.ke = Character(displayStrings.name_ke, color="#CC7C2A")
        store.mu = Character(displayStrings.name_mu, color = "#FFFFFF")
        store.nk = Character(displayStrings.name_nk, color = "#FFFFFF")
        store.no = Character(displayStrings.name_no, color="#E0E0E0")
        store.yu = Character(displayStrings.name_yu, color="#2c9e31")
        store.sa = Character(displayStrings.name_sa, color="#D4D4FF")
        store.aki = Character(displayStrings.name_aki, color="#eb243b")
        store.hh = Character(displayStrings.name_hh, color="#6299FF")
        store.hx = Character(displayStrings.name_hx, color="#99AACC")
        store.emm = Character(displayStrings.name_emm, color="#995050")
        
        
        store.mk = Character(displayStrings.name_mk, color="#AD735E")

        store.mystery = Character(displayStrings.name_mystery)

        #derived characters

        store.ssh = Character(displayStrings.name_shi, kind=shi, what_prefix="[ ", what_suffix=" ]")

        store.ha_ = Character(displayStrings.name_ha_, kind=ha)
        store.emi_ = Character(displayStrings.name_emi_, kind=emi)
        store.rin_ = Character(displayStrings.name_rin_, kind=rin)
        store.li_ = Character(displayStrings.name_li_, kind=li)
        store.mi_ = Character(displayStrings.name_mi_, kind=mi)
        store.ke_ = Character(displayStrings.name_ke_, kind=ke)
        store.mu_ = Character(displayStrings.name_mu_, kind=mu)
        store.yu_ = Character(displayStrings.name_yu_, kind=yu)
        store.no_ = Character(displayStrings.name_no_, kind=no)
        store.sa_ = Character(displayStrings.name_sa_, kind=sa)
        store.aki_ = Character(displayStrings.name_aki_, kind=aki)
        store.nk_ = Character(displayStrings.name_nk_, kind=nk)
        store.hx_ = Character(displayStrings.name_hx_, kind=hx)
        store.hh_ = Character(displayStrings.name_hh_, kind=hh)
        store.emm_ = Character(displayStrings.name_emm_, kind=emm)

        # new characters! [str]
        store.har = Character(displayStrings.name_har, color="#F9EAA0")
        store.suz = Character(displayStrings.name_suz, color="#72ADEE")
        store.yuk = Character(displayStrings.name_yuk, color="#897CBF")
        store.jun = Character(displayStrings.name_jun, color="#eb243b")
        store.tsu = Character(displayStrings.name_tsu, color="#CC7C2A")
        store.yam = Character(displayStrings.name_tsu, color="#FF8D7C")
        
        store.dad = Character(displayStrings.name_dad, color="#DDDDDD")
        store.mot = Character(displayStrings.name_mot, color="#DDDDDD")
        
        # CHARACTERS - NVL characters

        # NOT overwriting nvl here (although that's possible) because the script already uses a base NVL character called "n" which we can derive from
        store.n = ReadbackNVLCharacter(None, 
                                       kind=nvl,
                                       ctc=anim.Blink(im.Rotozoom("ui/ctc.png", 270, 1.0),
                                       offset=1.0, ypos=560, xpos=772),
                                       ctc_position = "fixed",
                                       **add_styles)

        store.nb = Character(None, 
                               kind=adv,
                               ctc=None,
                               what_color="#000000",
                               what_line_spacing=8,
                               what_prefix="",
                               what_suffix="",
                               show_function=say_wrapper,
                               window_style="b_nvl_window")

        store.rinbabble = Character(None,
                                    kind=n,
                                    what_prefix=u"{color=#FF8D7C}{b}"+displayStrings.name_rin+"{/b}{/color}\n" + displayStrings.quote_outer_open,
                                    what_suffix=displayStrings.quote_outer_close)

        
        # CHARACTERS - special characters
        # Ren'Py would create these late, but only if we don't define them ourselves
        # "name_only" (on-the-fly characters) is identical to "adv"

        store.narrator = Character(' ', what_prefix="", what_suffix="", show_function=say_wrapper)
        store.centered = Character(None, what_style="centered_text", window_style="centered_window", what_prefix="", what_suffix="", show_function=say_wrapper)
        store.centered_b = Character(None, kind=centered, what_color="#000000", what_drop_shadow=None, what_style="alive_text")
        store.centered_alive = Character(None, kind=centered_b, window_xpos=130, window_xanchor=0, window_xpadding=0)

    #define_characters() #now called at language init

    # CONSTRUCTORS etc.
    dotwipe_down = ImageDissolve(im.Tile("ui/tr-dots_col.png"), 0.5, 32, ramptype="mcube")
    dotwipe_up = ImageDissolve(im.Tile("ui/tr-dots_col.png"), 0.5, 32, ramptype="mcube", reverse = True)
    slowfade = Fade(1.0, 0.5, 1.0)
    openeye = ImageDissolve('vfx/tr_eyes.png', 2.0, 64, ramptype='cube')
    openeyeslow = ImageDissolve('vfx/tr_eyes.png', 3.5, 64, ramptype='cube')
    shuteye = ImageDissolve('vfx/tr_eyes.png', 2.0, 64, ramptype='mcube', reverse=True)

    
    
    openeyefast = ImageDissolve('vfx/tr_eyes.png', 0.5, 64, ramptype='cube')
    shuteyefast = ImageDissolve('vfx/tr_eyes.png', 0.20000000000000001, 64, ramptype='mcube', reverse=True)
    shuteyemed = ImageDissolve('vfx/tr_eyes.png', 1.00000000000000001, 64, ramptype='mcube', reverse=True)
    openeye_shock = ImageDissolve('vfx/tr-openshock.png', 0.80000000000000004, 64, ramptype='cube')
    
    #alpha style
    #openeye = CropMove(2.0, mode='custom', startcrop=(0.0, 0.5, 1.0, 0.0), startpos=(0.0,0.5))
    #shuteye = CropMove(2.0, mode='custom', startcrop=(0.0, 0.0, 1.0, 1.0), startpos=(0.0,0.0), endcrop=(0.0, 0.5, 1.0, 0.0), endpos=(0.0,0.5), topnew=False)
    
    #openeyefast = CropMove(0.5, mode='custom', startcrop=(0.0, 0.5, 1.0, 0.0), startpos=(0.0,0.5))
    #shuteyefast = CropMove(0.2, mode='custom', startcrop=(0.0, 0.0, 1.0, 1.0), startpos=(0.0,0.0), endcrop=(0.0, 0.5, 1.0, 0.0), endpos=(0.0,0.5), topnew=False)
    
    # This creates a whole bunch of transitions
    define.move_transitions("charamove", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions('charamove_slow', 2.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions("charamove_old", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp, old=True) 

    define.move_transitions("ease_accel", 0.5, _ease_out_time_warp) 
    define.move_transitions("ease_decel", 0.5, _ease_in_time_warp)
        
    define.move_transitions("slice_in", 0.2, _ease_in_time_warp)
    
    define.move_transitions("charamove_accel", 1.0, _ease_out_time_warp) 
    define.move_transitions("charamove_decel", 1.0, _ease_in_time_warp) 
    
    define.move_transitions('charafast', 0.20000000000000001, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    
    # [str]
    define.move_transitions('charamove_faster', 0.40000000000000001, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    
    def Dissolvemove(time, time_warp=_ease_time_warp):
        top = Dissolve(time)
        before = MoveTransition(time, factory=MoveFactory(time_warp=time_warp), old=True)
        after = MoveTransition(time, factory=MoveFactory(time_warp=time_warp))
        return ComposeTransition(top, before=before, after=after)
    
    dissolvecharamoveslowish = Dissolvemove(2.0)
    dissolvecharamove = Dissolvemove(1.0)
    dissolvecharamoveslow = Dissolvemove(3.0)
    dissolvecharamovefast = Dissolvemove(0.75)
    dissolvecharamovereallyfast = Dissolvemove(0.15)
    
    def Dissolveease(time, time_warp=_ease_out_time_warp):
        top = Dissolve(time)
        before = MoveTransition(time, factory=MoveFactory(time_warp=time_warp), old=True)
        after = MoveTransition(time, factory=MoveFactory(time_warp=time_warp))
        return ComposeTransition(top, before=before, after=after)
        
    dissolveeaseaccel = Dissolveease(0.5)
        
    delayed_dissolve = MultipleTransition([False,Dissolve(0.5),False,Dissolve(0.5),True])
    shownote = ComposeTransition(delayed_dissolve, None, charamoveinbottom)
    hidenote = ComposeTransition(Dissolve(0.5, alpha=True), charamoveoutbottom, None)

    delayblinds = ImageDissolve("vfx/tr-delayblinds.png", 1.0)
    
    delayblindsfade = MultipleTransition([False, SoundTransition('sfx/time.ogg'), False, delayblinds, Solid('#000'), delayblinds, True])
    delayblindsfadesilent = MultipleTransition([False, delayblinds, Solid('#000'), delayblinds, True])
    shorttimeskipsilent = delayblindsfadesilent
    
    # effect abstractions
    menueffect = dissolve
    charaenter = dissolve
    charaexit = dissolve
    charachange = dissolve
    characlose = dissolve
    charadistant = dissolve
    locationchange = dissolve
    locationskip = fade
    shorttimeskip = delayblindsfade
    #next was added by SemisoftCheese for whatever reason:
    flash = Fade(.25, 0, .75, color="#fff")
    
    #This is stolen from the final version. All the tracks have been changed over because I'm badass like that. -md01
    #Now having gone through all the tracks, there are a lot of duplicates and a few mislabels. For compatibilities sake, I'm including all of them. -md01
    ex_m_tracks = []
    def ks_music(filename, alias):
        fullpath = (('bgm/') + (filename)) + ('.ogg')
        setattr(store, ('music_') + (alias), fullpath)
        store.ex_m_tracks.append((filename.replace('_', ' '), fullpath))
    ks_music('Afternoon', 'tranquil')
    ks_music('Ah_Eh_I_Oh_You', 'nurse')
    ks_music('Air_original', 'soothing')
    ks_music('Another_Day', 'another')
    ks_music("Aria_de_l'Etoile", 'twinkle')
    ks_music('Breathlessly', 'moonlight')
    ks_music('BVW1010_Sarabande', 'cellosolo')
    ks_music('Cold_Iron', 'tragic')
    ks_music('Comfort', 'comfort')
    ks_music('Concord', 'lilly')
    ks_music('Daylight', 'daily')
    ks_music('Ease', 'ease')
    ks_music('flashback', 'static')
    ks_music('Friendship', 'friendship') 
    ks_music('Generic_Happy', 'comedy')
    ks_music('Happiness', 'happiness')
    ks_music('High_Tension', 'tension')
    ks_music('Hokabi', 'running')
    ks_music('Innocence', 'innocence')
    ks_music('Letting_my_Heart_Speak', 'heart')
    ks_music('Lullaby_of_Open_Eyes', 'serene')
    ks_music('Moment_of_Decision', 'drama')
    ks_music('Moonlight', 'moon')
    ks_music('Nocturne', 'night')
    ks_music('Out_of_the_Loop', 'kenji')
    ks_music('Painful_History', 'hanako')
    ks_music('Painful_History_Final', 'hanakofinal')
    ks_music('Painful_History_FinalPiano', 'hanakohscene')
    ks_music('Painful_History_Mus', 'hanakofire')
    ks_music('Parity', 'rin')
    ks_music('Passing_of_Time', 'timeskip')
    ks_music('Raindrops_and_Puddles', 'dreamy')
    ks_music('Rain', 'rain')
    ks_music('Red_Velvet', 'jazz')
    ks_music('Romance_in_Andante_II', 'romance')
    ks_music('Romance_in_Andante', 'credits')
    ks_music('Sarabande_musicbox', 'musicbox')
    ks_music('School_Days', 'normal')
    ks_music('Shadow_of_the_Truth', 'sadness')
    ks_music('Sketchy', 'sketch')
    ks_music('Standing_Tall', 'emi')
    ks_music('Stride', 'pearly')
    ks_music('The_Japanese_Rock', 'crappy')
    ks_music('The_Student_Council', 'shizune')
    ks_music('To_Become_One', 'one')
    ks_music('Wiosna', 'menus')
    
    #config.main_menu_music = music_menus # this screws with scene_select
    config.main_menu_music = None
    
    # Tracks available in the extras -> music menu. Name and file name.

    # Emi's running speeds, ordered from fastest to slowest: sprinting > pacing > running > jogging
    
    # sfx mapping
    sfx_tcard = "sfx/tcard.ogg"
    sfx_4lslogo = "sfx/4lsaudiologo.ogg"
    sfx_alarmclock = "sfx/alarm.ogg"
    sfx_alarm_loud = "sfx/alarm_loud.ogg"
    sfx_normalbell = "sfx/carillon.ogg"
    sfx_warningbell = "sfx/chaimu.ogg"
    sfx_crunchydeath = "sfx/crunch.ogg"
    sfx_fireworks = "sfx/fireworks.ogg"
    sfx_rain = "sfx/rain.ogg"
    sfx_rustling = "sfx/rustling.ogg"
    sfx_impact = "sfx/wumph.ogg"
    sfx_impact2 = "sfx/wumph_2.ogg"
    sfx_heartfast = "sfx/heart_single_fast.ogg"
    sfx_heartslow = "sfx/heart_single_slow.ogg"
    sfx_heartstop = "sfx/heart_stop.ogg"
    sfx_emijogging = "sfx/emijogging.ogg"
    sfx_emirunning = "sfx/emirunning.ogg"
    sfx_emipacing = "sfx/emipacing.ogg"
    sfx_emisprinting = "sfx/emisprinting.ogg"
    sfx_startpistol = "sfx/startpistol.ogg"
    sfx_crowd_cheer = "sfx/crowd_cheer.ogg"
    sfx_crowd_indoors = "sfx/crowd_indoors.ogg"
    sfx_crowd_outdoors = "sfx/crowd_outdoors.ogg"
    sfx_can_clatter = "sfx/can_clatter.ogg"
    sfx_door_creak = "sfx/door_creak.ogg"
    sfx_doorknock = "sfx/doorknock.ogg"
    sfx_doorknock2 = "sfx/doorknock2.ogg"
    sfx_dooropen = "sfx/dooropen.ogg"
    sfx_doorclose = "sfx/doorclose.ogg"
    sfx_doorslam = "sfx/doorslam.ogg"
    sfx_flash = "sfx/flash.ogg"
    sfx_cicadas = "sfx/cicadas.ogg"
    sfx_dropglasses = "sfx/dropglasses.ogg"
    sfx_scratch = "sfx/scratch.ogg"
    sfx_scratch2 = "sfx/scratch2.ogg"
    sfx_traffic = "sfx/traffic.ogg"
    sfx_rumble = "sfx/rumble.ogg"
    sfx_skid = "sfx/skid2.ogg"
    sfx_gymbounce = "sfx/emibounce.ogg"
    sfx_hammer = "sfx/hammer.ogg"
    sfx_paper = "sfx/paper.ogg"
    sfx_pillow = "sfx/pillow.ogg"
    sfx_paperruffling = "sfx/paperruffling.ogg"
    sfx_birdstakeoff = "sfx/birdstakeoff.ogg"
    sfx_storebell = "sfx/storebell.ogg"
    sfx_thunder = "sfx/thunder.ogg"
    sfx_slide = "sfx/slide.ogg"
    sfx_slide2 = "sfx/slide2.ogg"
    sfx_crash = "sfx/skid2.ogg"
    sfx_static = "sfx/flashback.ogg"
    sfx_draw = "sfx/sword_draw.ogg"
    sfx_lock = "sfx/lock.ogg"
    sfx_businterior = "sfx/businterior.ogg"
    sfx_time = "sfx/time.ogg"
    sfx_switch = "sfx/switch.ogg"
    sfx_can = "sfx/can.ogg"
    sfx_rooftop = "sfx/rooftop.ogg"
    sfx_teacup = "sfx/teacup.ogg"
    sfx_footsteps_hard = "sfx/footsteps_hard.ogg"
    sfx_footsteps_soft = "sfx/footsteps_soft.ogg"
    sfx_powerout = "sfx/powerout.ogg"
    sfx_lighter = "sfx/lighter.ogg"
    sfx_housefire = "sfx/housefire.ogg"
    sfx_park = "sfx/parkambience.ogg"
    sfx_whiteout = "sfx/whiteout.ogg"
    sfx_trainint = "sfx/trainint.ogg"
    sfx_trainchime = "sfx/trainchime.ogg"
    sfx_shower = "sfx/shower.ogg"
    sfx_blop = "sfx/blop.mp3"
    sfx_snap = "sfx/snap.ogg"
    sfx_sword_draw = "sfx/sword_draw.ogg"
    sfx_tray_rattling = "sfx/tray_rattling.mp3"
    sfx_camera = "sfx/shutterfilm.ogg"
    sfx_cellphone = "sfx/cellphone.ogg"
    sfx_running = "sfx/running.ogg"
    sfx_sitting = "sfx/sitting.ogg"
    
    
    #video mapping
    vid_tca1 = "video/tc_act1.mkv"
    vid_op = "video/op_1.mkv"
    vid_disc = "video/disc.mpg"
    vid_dream = "video/nightmare.mpg"
    

    # CONFIG

    config.screen_width = 800
    config.screen_height = 600

    config.mouse = {"default": [("ui/mousecursor.png",1,0)]}

    _preferences.afm_time = 0
    if not persistent.afm_time:
        persistent.afm_time = 5

    config.default_fullscreen = False
    config.default_text_cps = 70
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.has_autosave = False

    config.skip_indicator = False # we use a custom one

    config.window_icon = "ui/icon.png"

    config.enter_transition = dotwipe_down
    config.exit_transition = dotwipe_up
    config.intra_transition = dissolve
    config.main_game_transition = dotwipe_down
    config.game_main_transition = dotwipe_up
    config.end_splash_transition = slowfade
    config.end_game_transition = dotwipe_up
    config.after_load_transition = dotwipe_up
    
    config.window_show_transition = Dissolve(0.2)
    config.window_hide_transition = Dissolve(0.2)

    def wdt_hide(trans=dissolve):
        wdt_off()
        narrator("", interact=False)
        renpy.with_statement(None)
        renpy.with_statement(trans)

    def wdt_show(trans=dissolve):
        narrator("", interact=False)
        renpy.with_statement(trans)
        wdt_on()

    
    # aggressive caching; we use a lot of images sometimes.
    #config.image_cache_size = 42

    # some tricks for ui_labels.rpy
    config.label_overrides = {"_noisy_return": "custom_noisy_return",
                              "_return": "custom_return",
                              "_confirm_quit": "quit_from_os"}

    # STYLES
    # helper defs

    def ib_base(image, **options): # basic imagebutton fadeout
        return im.MatrixColor(image, im.matrix.opacity(0.4), **options)
    def ib_disabled(image, **options): # disabled imagebutton fadeout
        return im.MatrixColor(image, im.matrix.opacity(0.1), **options)

    # general styles
    style.default.font = mainfont

    # mm styles
    style.mm_root.background = "ui/bg-main.png"
    style.mm_menu_frame.background = None
    #style.mm_menu_frame_vbox.box_layout = "horizontal"
    style.mm_menu_frame.xanchor = 0.0
    style.mm_menu_frame.yanchor = 1.0 # anchor the menu block in the lower left corner. Still lots of invisible padding.
    style.mm_menu_frame.xpos = 65
    #style.mm_menu_frame.xalign = 0.5
    style.mm_menu_frame.ypos = 540
    style.mm_button.background = None
    style.mm_button.xminimum = 0
    style.mm_button_text.xalign = 0
    style.mm_button_text.font = titlefont
    style.mm_button_text.color = "#00000066"
    style.mm_button_text.insensitive_color = "#00000019"
    style.mm_button_text.hover_color = "#000000"
    
    style.prompt_text.color = "#00000066"
    
    # replay menu
    style.create("rpa_button", "button")
    style.rpa_button.background = None
    style.create("rpa_button_text", "mm_button_text")
    
    style.create("rpa_active_button", "rpa_button")
    style.create("rpa_active_button_text", "rpa_button_text")
    style.rpa_active_button_text.insensitive_color = "#000000"

    # ingame styles

    style.say_window.background = "ui/bg-say.png"
    style.say_window.left_padding = 14
    style.say_window.right_padding = 30
    
    style.say_window.top_padding = 10
    style.say_window.xmargin = 0
    style.say_window.ymargin = 0
    style.say_window.yminimum = 180
    
    style.say_vbox.spacing = 15
    
    
    style.say_dialogue.first_indent = 14
    style.say_dialogue.rest_indent = 14
    
    style.say_dialogue['rollback'].color="#DDDDDD"
    

    style.centered_text.size = 26
    style.centered_text.outlines = [ (1,"#000C") ]

    style.create("alive_text", "centered_text")
    style.alive_text.outlines = []
    
    style.create("note_window", "centered_window")
    style.note_window.background=Frame("ui/bg-note.png", 0, 16, tile=True)
    style.note_window.xalign=0.5
    style.note_window.yalign=0.5
    style.note_window.top_padding=14
    style.note_window.left_padding=35
    #style.note_window.right_padding=16
    style.note_window.xmaximum=402
    style.note_window.yfill = False
    #style.note_window.ymaximum=302
    style.note_window.xminimum=402
    #style.note_window.yminimum=302
    
    style.create("note_text", "centered_text")
    style.note_text.size = 25
    style.note_text.outlines = []
    style.note_text.color = "#000244"
    style.note_text.text_align=0.0
    style.note_text.xalign=0.0
    style.note_text.yalign=0.0
    style.note_text.slow_cps = False
    #style.note_text.layout = "greedy"
    
    style.nvl_window.background = "ui/bg-nvl.png"
    style.nvl_window.top_padding = 25    
    style.say_window.left_padding = 14
    style.say_window.right_padding = 30

    style.create("b_nvl_window", "nvl_window")
    style.b_nvl_window.background = None
    style.b_nvl_window.top_padding = 140
    style.b_nvl_window.left_padding = 80

    style.menu_choice_button.background = "ui/bg-choice.png"
    style.menu_choice.take(style.mm_button_text)
    style.menu_choice.xalign = 0.5
    style.menu_choice.size = 20
    style.menu_choice_button.top_padding = 5

    style.hyperlink_text.color = "#F99"
    style.hyperlink_text.underline = False

    style.create("readback_text", "say_dialogue")
    style.readback_text.size= 16
    style.readback_text.color = "#00000066"
    style.create("readback_label", "readback_text")
    style.readback_label.bold = True

    style.create("comment_frame", "default")
    style.comment_frame.background = Frame("ui/bg-comment.png", 8,8,tile=True)
    style.comment_frame.xmargin = 4
    style.comment_frame.ymargin = 4
    style.comment_frame.xpadding = 16
    style.comment_frame.top_padding = 12
    style.comment_frame.bottom_padding = 18
    style.comment_frame.xminimum = 800
    
    style.create("comment_label", "say_label")
    
    style.create("comment_text", "say_dialogue")
    style.comment_text.first_indent = 0
    style.comment_text.rest_indent = 0
    
    # gm styles
    # general
    style.gm_root.background = Solid("#0000007F")
    style.gm_root[None].background = None # gm screens will supply their own
    style.gm_nav_frame.xalign = 0.5
    style.gm_nav_frame.yalign = 0.4
    style.gm_nav_frame.xminimum= 200
    style.gm_nav_frame.yminimum = 306

    style.gm_nav_frame.background = "ui/bg-gm.png"

    style.gm_nav_frame.top_padding = 54
    style.gm_nav_box.xalign = 0.5
    style.gm_nav_box.yalign = 0.5
    style.gm_nav_button.take(style.mm_button)
    style.gm_nav_button_text.take(style.mm_button_text)
    style.gm_nav_button.xalign = 0.5
    style.gm_nav_button_text.xalign = 0.5
    

    # yes / no dialog
    # Define styles
    style.yesno_frame = Style(style.menu_frame, help="frame containing a yes/no prompt and yes/no buttons")
    style.yesno_frame_vbox = Style(style.vbox, help="box separating yes/no prompt from yes/no buttons")

    style.yesno_prompt = Style(style.prompt, help="a yes/no prompt")
    style.yesno_prompt_text = Style(style.prompt_text, help="a yes/no prompt (text)")

    style.yesno_button_hbox = Style(style.hbox, help="the box separating yes and no buttons")
    style.yesno_button = Style(style.button, help="a yes or no button")
    style.yesno_button_text = Style(style.button_text, help="a yes or no button (text)")

    # Alter styles.
    style.yesno_frame.xfill = True
    style.yesno_frame.ypadding = .05
    
    style.yesno_frame_vbox.xalign = 0.5
    style.yesno_frame_vbox.yalign = 0.5
    style.yesno_frame_vbox.box_spacing = 30
    
    style.yesno_button_hbox.xalign = 0.5
    style.yesno_button_hbox.spacing = 100

    style.yesno_button.size_group = "yesno"
    
    style.yesno_frame.xalign = 0.5
    style.yesno_frame.yalign = 0.5
    style.yesno_frame.xmaximum = 331 # Size of the background. Can't find out how to automate this.
    style.yesno_frame.xpadding = 0.1
    style.yesno_frame.xmargin = 0
    style.yesno_frame.background = "ui/bg-popup.png"
    style.yesno_prompt.color = "#00000066"
    style.yesno_button_hbox.box_spacing = 20
    style.yesno_button.background = None
    style.yesno_button_text.take(style.mm_button_text)
    style.yesno_button_text.xalign = 0.5

    # load / save
    # Define styles
    style.file_picker_entry = Style(style.large_button, help="used to select a file to load or save")
    style.file_picker_entry_box = Style(style.hbox, help="the box inside a file picker entry")

    style.file_picker_text = Style(style.large_button_text, help="text inside a file picker entry")
    style.file_picker_empty_slot = Style(style.file_picker_text, help="text inside an empty file picker entry slot")
    style.file_picker_extra_info = Style(style.file_picker_text)
    style.file_picker_new = Style(style.file_picker_text)
    style.file_picker_old = Style(style.file_picker_text)

    style.file_picker_frame = Style(style.menu_frame, help="the frame enclosing the entire file picker")
    style.file_picker_frame_box = Style(style.vbox, help="the box containing the navbox and the grid of file picker entries")

    style.file_picker_navbox = Style(style.hbox, help="the box containing navigation buttons")

    style.file_picker_nav_button = Style(style.small_button, help="a file picker navigation button")
    style.file_picker_nav_button_text = Style(style.small_button_text, help="file picker navigation button text")

    style.file_picker_grid = Style(style.default, help="a grid containing file picker navigation buttons")

    # Adjust styles.
    style.file_picker_entry.xminimum = 0.5

    style.file_picker_frame.xmargin = 6
    style.file_picker_frame.ymargin = 6

    style.file_picker_frame_box.box_spacing = 4            
    style.file_picker_entry_box.box_spacing = 4

    style.file_picker_frame.background = None
    style.file_picker_frame.xalign = 0.5
    style.file_picker_frame.yalign = 0.42
    style.file_picker_frame.xmaximum = 480
    style.file_picker_navbox.xalign = 0.5
    style.file_picker_new.bold = True
    style.file_picker_new.color = "#00000066"
    style.file_picker_new.hover_color = "#000000"
    style.file_picker_old.color = "#00000066"
    style.file_picker_old.hover_color = "#000000"
    style.file_picker_extra_info.color = "#00000066"
    style.file_picker_extra_info.line_spacing = 5
    style.file_picker_extra_info.hover_color = "#000000"
    style.file_picker_empty_slot.color = "#00000066"
    style.file_picker_empty_slot.hover_color = "#000000"
    style.file_picker_entry.xfill=False
    style.file_picker_entry.xminimum=380
    style.file_picker_entry.background = ib_base("ui/bt-scribble.png")
    style.file_picker_entry.hover_background = "ui/bt-scribble.png"
    style.file_picker_entry.top_padding = 3

    style.vscrollbar.thumb_offset = -10
    style.vscrollbar.ymaximum = 250
    style.vscrollbar.xmaximum = 24
    style.vscrollbar.top_gutter = 15
    style.vscrollbar.bottom_gutter = 14
    style.vscrollbar.top_bar = ib_base("ui/bt-vscrollbar.png")
    style.vscrollbar.hover_top_bar = "ui/bt-vscrollbar.png"
    style.vscrollbar.bottom_bar = ib_base("ui/bt-vscrollbar.png")
    style.vscrollbar.hover_bottom_bar = "ui/bt-vscrollbar.png"
    style.vscrollbar.thumb = ib_base("ui/bt-vscrollthumb.png")
    style.vscrollbar.hover_thumb = "ui/bt-vscrollthumb.png"

    style.create("vscrollbar_disabled", "vscrollbar")
    style.vscrollbar_disabled.top_gutter = 0
    style.vscrollbar_disabled.top_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.hover_top_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.bottom_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.hover_bottom_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.thumb = None
    style.vscrollbar_disabled.hover_thumb = None

    style.create("vscrollbar2", "vscrollbar")
    style.vscrollbar2.ymaximum = 224
    style.vscrollbar2.top_bar = ib_base("ui/bt-vscrollbar2.png")
    style.vscrollbar2.hover_top_bar = "ui/bt-vscrollbar2.png"
    style.vscrollbar2.bottom_bar = ib_base("ui/bt-vscrollbar2.png")
    style.vscrollbar2.hover_bottom_bar = "ui/bt-vscrollbar2.png"

    style.create("vscrollbar2_disabled", "vscrollbar2")
    style.vscrollbar2_disabled.top_gutter = 0
    style.vscrollbar2_disabled.top_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.hover_top_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.bottom_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.hover_bottom_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.thumb = None
    style.vscrollbar2_disabled.hover_thumb = None

    # preferences
    # Styles
    style.prefs_frame = Style(style.default, help="the frame containing all of the preferences")
    style.prefs_frame_box = Style(style.default, help="the box inside the frame containing all of the preferences")
    
    style.prefs_pref_frame = Style(style.menu_frame, help="a frame containing a single preference")
    style.prefs_pref_box = Style(style.vbox, help="the box separating the preference label from the preference choices")
    style.prefs_pref_choicebox = Style(style.vbox, help="the box containing the preference choices")

    style.prefs_label = Style(style.label, help="a preference label (window)")
    style.prefs_label_text = Style(style.label_text, help="a preference label (text)")

    style.prefs_button = Style(style.radio_button, help="preference value button")
    style.prefs_button_text = Style(style.radio_button_text, help="preference value button (text)")

    style.prefs_slider = Style(style.slider, help="preference value slider bar")

    style.prefs_volume_box = Style(style.vbox, help="box containing a volume slider and soundtest button")
    style.prefs_volume_slider = Style(style.prefs_slider, help="volume slider bar")
    
    style.soundtest_button = Style(style.small_button, help="soundtest button")
    style.soundtest_button_text = Style(style.small_button_text, help="soundtest button (text)")

    style.prefs_jump = Style(style.prefs_pref_frame, help="jump preference frame")
    style.prefs_jump_button = Style(style.button, help="jump preference button")
    style.prefs_jump_button_text = Style(style.button_text, help="jump preference button (text)")
    
    # Create styles.
    style.prefs_column = Style(style.vbox, help="preference columns")
    style.prefs_left = Style(style.prefs_column, help="the left preference column")
    style.prefs_center = Style(style.prefs_column, help="the center preference column")
    style.prefs_right = Style(style.prefs_column, help="the right preference column")

    # Customize styles.
    style.prefs_pref_frame.xfill = True
    style.prefs_column.xanchor = 0.5

    style.prefs_pref_box.box_spacing = 12

    style.prefs_column.xmaximum = 250
    style.prefs_column.box_spacing = 10
    style.prefs_frame.top_margin = 10

    style.prefs_left.xpos = 137
    style.prefs_center.xpos = 400
    style.prefs_right.xpos = 663

    style.prefs_slider.xmaximum = 200
        
    style.prefs_pref_box.xfill = True
    style.prefs_volume_box.xfill = True
    style.prefs_pref_choicebox.xfill = True
    style.prefs_button.xalign = 1.0
    style.prefs_jump_button.xalign = 1.0
    style.prefs_slider.xalign = 1.0
    style.soundtest_button.xalign = 1.0

    style.prefs_button.size_group = "prefs"
    style.prefs_jump_button.size_group = "prefs"
    
    style.prefs_pref_frame.background = None
    style.prefs_pref_frame.bottom_margin = 0
    style.prefs_button.take(style.mm_button)
    style.prefs_button_text.take(style.mm_button_text)
    style.prefs_label.take(style.yesno_prompt)
    style.prefs_label.xalign = 0.0
    style.prefs_label_text.take(style.prompt_text)

    style.prefs_slider.clear()
    style.prefs_slider.left_bar = ib_base("ui/bt-cf-bar-left.png")
    style.prefs_slider.hover_left_bar = "ui/bt-cf-bar-left.png"
    style.prefs_slider.right_bar = ib_base("ui/bt-cf-bar-right.png")
    style.prefs_slider.hover_right_bar = "ui/bt-cf-bar-right.png"
    style.prefs_slider.thumb = ib_base("ui/bt-cf-thumb.png")
    style.prefs_slider.hover_thumb = "ui/bt-cf-thumb.png"
    style.prefs_slider.left_gutter = 12
    style.prefs_slider.right_gutter = 12
    style.prefs_slider.xmaximum = 200
    style.prefs_slider.thumb_offset = -3

    style.create("page_caption", "prefs_label")
    style.page_caption.bold = True
    
    



    # general variables that might be preexisting or not

    if not persistent.hdisabled:
        persistent.hdisabled = False
        
    #print persistent.emi, persistent.hanako, persistent.lilly, persistent.shizune, persistent.rin, persistent.bad

    def init_vars():
        # just a simple wrapper; this stuff has to be reset rather frequently
        store.seen_labels = []
        store.current_line = None

    init_vars()
    _game_menu_screen = "gm_bare"
    prefs_looped = False
    playthroughflag = True
    devlvl = 0
    entered_from_game = False
    coming_from_prefs_sub = False
    gm_active = False
    quit_from_os_flag = False
    ask_to_quit = False
    last_visited_label = None
    last_scene_label = None
    gm_exit_to = None
    previous_language = None
    np_current_language = None
    may_afm = True
    
