################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此界面必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

transform say_text_fade:
    alpha 0.0
    linear 0.25 alpha 1.0

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" at say_text_fade:
            line_spacing 30

    imagebutton:
        xpos 1700
        ypos 790
        idle "images/mybutton/delete2.png"
        action HideInterface()
    

    if persistent.enable_chinmoku_score_count and out_talk == False:
        label "得分:%d"%chinmoku_score :
            text_font gui.ui_text_font
            text_size 40
            align (0,0)

    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    # if not renpy.variant("small"):
    add SideImage():
        xpos 119
        ypos 736
        #xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

init -1 python:

    style.rubytext_style = Style(style.default)
    style.rubytext_style.size = 30
    style.rubytext_style.yoffset = -50
    style.rubytext_style.font = 'LXGWWenKaiScreenR.ttf'

    style.default.ruby_style = style.rubytext_style

## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此界面必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他界面之上，
    zorder 100

    if quick_menu:
        imagebutton:
            # 菜单
            xalign 0.99
            yalign 1.0
            idle "images/mybutton/menu_button.png"
            action ShowMenu('game_menu')
        imagebutton:
            xalign 0.99
            yalign 0.88
            if (renpy.is_skipping() == True):
                idle "images/mybutton/skip_on.png"
            else:
                idle "images/mybutton/skip_off.png"
            action Skip() alternate Skip(fast=True, confirm=True)
        imagebutton:
            xalign 0.99
            yalign 0.76
            if (preferences.afm_enable == True):
                idle "images/mybutton/auto_on.png"
            else:
                idle "images/mybutton/auto_off.png"
            action Preference("auto-forward", "toggle")
        if persistent.enable_rollback:
            imagebutton:
                xalign 0.99
                yalign 0.63
                idle "images/mybutton/back_button.png"
                action Rollback()
        #textbutton _("历史") action ShowMenu('history')
        #textbutton _("快存") action QuickSave()
        #textbutton _("快读") action QuickLoad()


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 20


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc"):

            ## 退出按钮在 iOS 上是被禁止使用的，在安卓和网页上也不是必要的。
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu

    add gui.main_menu_background

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## use 语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/main_menu.png"


style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。当此界面与一个或多个子界
## 面同时使用时，这些子界面将被嵌入（放置）在其中。

screen game_menu_qsave():
    tag menu
    timer 0.5 action QuickSave()
    timer 0.5 action ShowMenu("game_menu")

transform imagebutton_trans:
    xoffset 250
    easein 0.5 xoffset 0

transform imagebutton_trans2:
    xoffset -250
    easein 0.5 xoffset 0

screen game_menu():
    tag menu
    style_prefix "game_menu"
    add "gui/overlay/game_menu.png":
        alpha 0.6
    add "images/system/bg/game_menu_bg.png":
        xalign 1.0
        ypos 0.1
    frame:
        background None
        xalign 1.0
        ypos 235
        vbox:    
            spacing 10
            imagebutton:
                idle "images/mybutton/gamemenu/load.png"
                hover "images/mybutton/gamemenu/load2.png"
                insensitive "images/mybutton/gamemenu/load3.png"
                at imagebutton_trans
                action ShowMenu("load")
            imagebutton:
                idle "images/mybutton/gamemenu/save.png"
                hover "images/mybutton/gamemenu/save2.png"
                insensitive "images/mybutton/gamemenu/save3.png"
                at imagebutton_trans
                action ShowMenu("save")
            imagebutton:
                idle "images/mybutton/gamemenu/quickload.png"
                hover "images/mybutton/gamemenu/quickload2.png"
                insensitive "images/mybutton/gamemenu/quickload3.png"
                at imagebutton_trans
                action QuickLoad()
            imagebutton:
                idle "images/mybutton/gamemenu/quicksave.png"
                hover "images/mybutton/gamemenu/quicksave2.png"
                insensitive "images/mybutton/gamemenu/quicksave3.png"
                at imagebutton_trans
                action ShowMenu("game_menu_qsave")
            imagebutton:
                idle "images/mybutton/gamemenu/settings.png"
                hover "images/mybutton/gamemenu/settings2.png"
                at imagebutton_trans
                action ShowMenu("preferences")
            imagebutton:
                idle "images/mybutton/gamemenu/history.png"
                hover "images/mybutton/gamemenu/history2.png"
                at imagebutton_trans
                action ShowMenu("history")
            imagebutton:
                idle "images/mybutton/gamemenu/mainmenu.png"
                hover "images/mybutton/gamemenu/mainmenu2.png"
                at imagebutton_trans
                action MainMenu()
    
    textbutton _("返回"):
        style "return_button"
        xalign 0.95
        yalign 0.98
        action Return()

style return_button:
    background "gui/button/empty_return_botton.png"
    xalign 1.0
    yalign 0.95
    xpadding 53
    ypadding 36

style return_button_text:
    font gui.ui_text_font
    size 35
    vertical True

style game_menu_text is gui_text

style game_menu_text:
    font gui.ui_text_font
    color "#000000"
    xpos 240
    xalign 0.5
    text_align 0.5
    xsize 400
    size 30


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义界
## 面。

screen about():

    tag menu
    add 'about_bg'
    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    # use game_menu(_("关于"), scroll="viewport"):

    style_prefix "about"
    label "关于":
        xpos 0.3
        ypos 0.15
    viewport:
        xpos 0.3
        ypos 0.24
        scrollbars "vertical"
        mousewheel True
        draggable True
        vbox:
            spacing 5
            for i in gui.about:
                text i
            null height 30
            label "啦啦啦" text_size 45

    textbutton _("返回"):
        style "return_button"
        action Return()

style about_label is gui_label
style about_label_text is gui_label_text:
    color "#000000"
    font gui.www_font
    size 45
style about_text is gui_text:
    color "#000000"
    font gui.www_font
    size 40

style about_label_text:
    size gui.label_text_size

## 读取和保存界面 #####################################################################
##
## 这些界面负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个界
## 面都是以第三个界面 file_slots 来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():
    tag menu

    use file_slots(_(False))

screen load():

    tag menu

    use file_slots(_(True))

init python:
    auto_page_num = 0

screen file_slots(flag):
    
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    # use game_menu(title):
    if flag:
        add "images/system/bg/load_bg.png"
    else:
        add "images/system/bg/save_bg.png"
    fixed:
        ## 存档位网格。
        hbox:
            for j in range(gui.file_slot_cols):
                $ xxps = 44 + j * 604
                vbox:
                    style_prefix "slot"
                    xpos xxps
                    ypos 236
                    spacing 88
                    for i in range(gui.file_slot_rows):
                        if auto_page_num!=0:
                            $ slot = (auto_page_num-1)*6 + j * gui.file_slot_rows + i + 1
                        else:
                            $ slot = j * gui.file_slot_rows + i + 1
                        button:
                            if flag:
                                action [Stop("music",fadeout = 1.0),FileLoad(slot)]
                            else:
                                action FileSave(slot)
                            has vbox

                            add FileScreenshot(slot) yoffset 2

                            text FileSlotName(slot, gui.file_slot_cols * gui.file_slot_rows, format=_("NO: %s%d")):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

                            imagebutton:
                                xpos 700
                                yoffset -275
                                idle "images/mybutton/delete.png"
                                action FileDelete(slot)

                            text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_title_text"

        ## 用于访问其他页面的按钮。
        hbox:
            style_prefix "page"

            xalign 0.64
            yalign 0.04

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A1") action [FilePage("auto"),SetVariable("auto_page_num",1)]
                textbutton _("{#auto_page}A2") action [FilePage("auto"),SetVariable("auto_page_num",2)]
                textbutton _("{#auto_page}A3") action [FilePage("auto"),SetVariable("auto_page_num",3)]
                textbutton _("{#auto_page}A4") action [FilePage("auto"),SetVariable("auto_page_num",4)]
                textbutton _("{#auto_page}A5") action [FilePage("auto"),SetVariable("auto_page_num",5)]

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action [FilePage("quick"),SetVariable("auto_page_num",0)]

            ## “range(1, 10)”给出 1 到 9 之间的数字。
            for page in range(1, 10):
                textbutton "[page]" action [FilePage(page),SetVariable("auto_page_num",0)]

            textbutton _(">"):
                action FilePageNext(max = 9)

        textbutton _("返回"):
            style "return_button"
            yalign 1.0
            action Return()

style page_label is gui_label
style page_label_text is gui_label_text:
    color "#000000"
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    xpos 550
    ypos -100
style slot_title_text is slot_button_text:
    font gui.ui_text_font
    size 30
    xpos 550
    ypos -200
style slot_name_text is slot_button_text:
    font gui.ui_text_font
    xpos 530
    ypos -175
    # bold True
    color "#000000"
    size 50

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    size 55
    font gui.ui_text_font

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许用户配置游戏，使其更适合自己。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

screen preferences_extra():

    tag menu

    add "images/system/bg/settings_mainbg.png"

    vbox:
        xpos 540
        ypos 263
        style_prefix "radio"
        label _("实验性功能")xsize 250
        label "这些功能是移植版增加的" xsize 1200 text_style "preferences_extra_label"
        textbutton _("显示‘攻略’页面") action ToggleVariable("persistent.enable_stragy") xsize 550 left_padding -3
        textbutton _("显示‘好感度统计’页面") action ToggleVariable("persistent.enable_statistics") xsize 550 left_padding -3
        textbutton _("沉默打破模式显示得分") action ToggleVariable("persistent.enable_chinmoku_score_count") xsize 550 left_padding -3
        label "（该选项存在更新延迟，作出选择后无法立即看到分数变化）" xsize 1200 text_style "preferences_extra_label"
        textbutton _("允许回退") action ToggleVariable("persistent.enable_rollback") xsize 550 left_padding -3
        label "（使用鼠标滚轮、安卓的‘返回’操作或对话框上的按钮倒回上一条对话）" xsize 1200 text_style "preferences_extra_label"
        label "（该选项重启后生效，回退功能有时候会出bug，请自行决定是否使用）" xsize 1200 text_style "preferences_extra_label"
    textbutton _("返回"):
        style "return_button"
        action ShowMenu("preferences")

style preferences_extra_label:
    font gui.ui_text_font
    size 35

screen preferences():

    tag menu

    add "images/system/bg/settings_mainbg.png"

    textbutton "实验性功能":
        xpos 540
        ypos 860
        action ShowMenu("preferences_extra")
    vbox:
        xpos 540
        ypos 263
        hbox:
            box_wrap True
            spacing 120
            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    style_prefix "radio"
                    label _("显示")
                    textbutton _("窗口") action Preference("display", "window")
                    textbutton _("全屏") action Preference("display", "fullscreen")

            vbox:
                style_prefix "radio"
                label _("说话动画")xsize 250
                textbutton _("启用") action SetVariable("persistent.disable_animation" , None) left_padding -3
                textbutton _("禁用") action SetVariable("persistent.disable_animation" , True) left_padding -3

            vbox:
                style_prefix "check"
                label _("快进")
                textbutton _("未读文本") action Preference("skip", "toggle") xoffset 20
                # textbutton _("选项后继续") action Preference("after choices", "toggle")
                # textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))
            vbox:
                style_prefix "check"
                label _("自动模式")
                textbutton _("等待语音") action Preference("wait for voice", "toggle")  xoffset 20

            ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
            ## 以添加其他创建者定义的首选项设置。

        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True
            spacing 200

            vbox:

                label _("文字速度")

                bar value Preference("text speed")

                label _("自动前进时间")

                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("音乐音量")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("音效音量")

                    hbox:
                        bar value Preference("sound volume")

                        #if config.sample_sound:
                        #    textbutton _("测试") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("语音音量")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("测试") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("全部静音"):
                        xoffset 20
                        action Preference("all mute", "toggle")
                        style "mute_all_button"
    textbutton _("返回"):
        style "return_button"
        action Return()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    # spacing gui.pref_button_spacing
    # 调整间距以适应横线
    spacing 30


style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    left_padding 6
    top_padding 10

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    # spacing gui.pref_button_spacing
    spacing 30

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    left_padding -20
    top_padding 10

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 338
    ysize 71

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    xmargin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 400
    yoffset -19
    #spacing 5


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu
    add "images/system/bg/history_bg.png"
    ## 避免预缓存此界面，因为它可能非常大。
    predict False
    frame:
        style "log_frame_style"
        frame:
            style "log_history_window_frame_style"
            viewport:
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                # 确保整个Frame塞满
                side_yfill True
                side_xfill True
                vscrollbar_xoffset 25
                vbox:
                    spacing 20
                    for h in _history_list:
                        hbox:
                            if h.voice.filename != None:
                                imagebutton:
                                    idle 'images/mybutton/play_voice.png'
                                    action Play('voice',h.voice.filename)
                            else:
                                null width 70
                            frame:
                                background None
                                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条目。
                                has fixed:
                                    yfit True
                                if h.who:
                                    label h.who:
                                        style "history_name"
                                        substitute False
                                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述人文本中。
                                        if "color" in h.who_args:
                                            text_color h.who_args["color"]
                                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                label what:
                                    yminimum 100
                                    # 直接使用history_text，也可以自定义其他样式
                                    style "log_text_style"
                                    substitute False

                if not _history_list:
                    label _("尚无对话历史记录。")

    textbutton _("返回"):
        style "return_button"
        yalign 0.95
        action [Stop('voice',fadeout = 0.5),Return()]

# log界面主体显示区域样式
style log_frame_style:
    ypos 290
    left_padding 300
    right_padding 60
    bottom_padding 250

# log界面文本标签区域样式
style log_label_frame_style:
    top_padding 50
    xfill True

# log界面窗口区域样式
style log_history_window_frame_style:
    bottom_padding 100
    xfill True

# log文本样式
style log_text_style:
    color "#444444"
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font gui.text_font
    size 43

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    ysize None
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至后来的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.cn/doc/self_voicing.html}机器朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退操作区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## skip_indicator 界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    font gui.ui_text_font

transform dateappear:
    #on show:
    #    alpha 0.0
    #    linear 0.25 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0
init -1 python:
    last_date = ''
    picdict = {'7':'jul,png','8':'aug.png','9':'sep.png'}
screen showdate(date):
    zorder 200
    if date != '' and date!=last_date:
        $ Mon = date[0]
        $ Day = date[2:-1]
        $ fnm = 'images/system/'+picdict[Mon]
        $ last_date = date
        frame at autosaveicon:
            xpos 0.2
            xsize 218
            ysize 181
            yoffset -25
            background Frame(fnm)
            foreground Text(Day,color = '#ffffff',size = 60,xalign = 0.6,yalign = 0.5,font = gui.ui_text_font,bold = True)
            # text Day
    timer 2.0 action Hide('showdate')

style showdate_frame is empty

## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


init -2 python:
    nvl_mode = 1
    MC_Name = '比企谷八幡'

screen nvl(dialogue, items=None):
    use chat_dialogue(dialogue, items)

define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

# 这是邮件模式的页面,参考了https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=62837%20上的代码(原作者已表明可以使用他的代码)



transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_y(pDirection):
    alpha 0.0
    yoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0


transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform phone_appear:
    alpha 0.0
    ease 0.8 alpha 1.0

transform phone_slip(start,end):
    ypos start
    linear 0.5 ypos end


screen chat_dialogue(dialogue, items=None):

    window:
        style "nvl_window"
        background None
        # Transform("images/bg/VM_BG01.png", xcenter=0.5,yalign=0.5)
        vbox:
            style "nvl_vbox"
            xpos 250
            null height 50
            use nvl_chattext(dialogue)
            null height 100

screen nvl_chattext(dialogue):
    style_prefix None
    $ cnt_image = 0
    for id_d, d in enumerate(dialogue):
        vbox:
            xsize 1400
            yalign 1.0
            yoffset -30
            # spacing 10
            frame:
                background Frame("images/system/mailframe.png",0,0,0,0)
                xsize 557
                yminimum  238
                if d.who == MC_Name:
                    xalign 0.0
                else:
                    xalign 1.0

                if d.current:
                    if d.who == MC_Name:
                        at message_appear(-1)
                    else:
                        at message_appear(1)

                text d.what:
                    pos (15,20)
                    xsize 525
                    slow_cps False
                    color "#000"
                    font gui.www_font
                    size  40
                    id d.what_id

################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
