﻿#gui文件为更改UI
#options更改游戏基本设施
#screen游戏界面设置
#script为根目录
#define定义角色

#room是游戏初始界面的背景————猪脑过载
#资源尽量用小写英文，要不然读取不到————猪脑过载

#无前缀直接用""是无角色对白
#角色 """...."""表示三引号之间的内容都为此角色所说。话与话之间要用回车键隔开

#scene是清除当前界面所有图像，然后显示该图像
#show为直接展示该图像，hide为隐藏图像;show 图片 at right/left可以仿制图片左右
#with是图像变换句

#Music默认循环播放音乐
#Sound默认播放一次
#Voice默认播放一次而且点击就会停止
#stop可以立即停止音乐

#define的用法：define e = Character("艾琳")


# 游戏在此开始。
#以下的BG都是早期暂定的背景，后续要改的话记得改下文件名
#所有的音效什么的都没加，前面加了#号防止错误

image end_pic:
    "images/end_pic.png"
    xoffset 5
image black = "#000000"
image white = "#FFFFFF"

define h = Character("比企谷八幡", image='h', what_suffix="{image=end_pic}",voice_tag="h")
image side h = "images/side HCM.png"
define l = Character("一色彩羽", image='l', what_suffix="{image=end_pic}",voice_tag="l")
image side l = "images/side IRO.png"
define t = Character("比企谷小町", image='t', what_suffix="{image=end_pic}",voice_tag="k")
image side t = "images/side KOM.png"
      
transform shake:
    # 初始位置
    xpos 0 ypos 0
    # 在 0.05 秒内向右移动 5 个像素
    linear 0.08 xpos 10
    # 在 0.05 秒内向左移动 10 个像素
    linear 0.08 xpos -20
    # 在 0.05 秒内恢复到初始位置
    linear 0.08 xpos 0 ypos 0

label start:
    play music "audio/bgm/BGM1.mp3"
    scene gatemorning
    play sound "audio/脚步.mp3"
    narrator "4月16日"
    #这段感觉可以黑屏开局，然后在倒数第三局的时候背景渐变出背景一色的立绘
    #imo:我设想的是，先展示总务高，然后跳出八幡的内心活动，会不会比黑屏好一点？

    h """(在策划惊喜时，最重要的是什么？)

        (要自然。)

        (突如其来的惊喜才会让人感动。)

        (不管是用心策划的恶作剧，还是不可思议的魔术技巧，一旦事情败露，就会败兴而归。)

        (同样的道理也适用于生日庆祝。)

        (庆祝生日，更应该谨慎小心，更加自然地表现。)

        (因为关系亲密，在日常相处之中，微小的差异就可能产生不信任感。)"""
        
    h "(尤其是，对于今天的惊喜派对的主角，一色彩羽。)"
    window hide
    show cg01
    play sound "audio/相机.mp3"
    with dissolve
    
    pause
    
    window show
    
    h """
        (她是我们学校的学生会长，是足球部的经理，还是我们侍奉部的常客。)

        (顺便一提，她还有世界上最可爱的小恶魔的头衔。一个由砂糖、香辛料和某些美好的东西组成的可爱女孩。)"""

    stop music
    scene activitymorning
    play sound "audio/开门.mp3"
    with hpunch
    
    show komachi02
    voice "audio/log/k01.ogg"
    
    t "给你一个艰巨而又伟大的任务。"
    hide komachi02
    voice "audio/log/h01.mp3"
    h "我这种渺小又平庸的人做不了艰巨又伟大的任务。"
    play music "audio/bgm/BGM3.ogg"
    show komachi01
    voice "audio/log/k02.mp3"
    t "哥哥不要贫嘴了，我们忙着给一色前辈准备惊喜呢。你要给我们争取时间，在我们准备完成之后把一色前辈带来活动室。"

    scene corridor
    with fade

    h """话题、话题……无论什么时候都能让人兴奋的话题……

        最近“血压”、“尿酸值”、“健忘”、“半夜突然口渴”等等这些不健康的话题很受欢迎，但这样的话题即使是一色也不太可能说“太有道理了～”。

        嗯，还是像往常那样随意地聊些毫无意义的话题会比较自然吧……"""

    #Act1,Scene 2
    #BG02
    

    scene stuunion
    with fade
    ##play music "audio/bgm/BGM1.mp3"
    ##说改bgm没说改哪首我也不会改——gklx
    show iroha01
    play sound "audio/敲门.mp3"
    h   "......"
    scene stuunion
    show iroha15
    voice "audio/log/i16.ogg"
    l   "请进"
    hide iroha15
    voice "audio/log/h04.mp3"
    h   "打扰了"
   
    scene stuunion
    show iroha14 
    voice "audio/log/i01.mp3"
    l   "啊，是前辈呀"#失望
    hide iroha14
    voice "audio/log/h02.ogg"
    h   "嗯，辛苦了 。可以和你说两句吗？"
    show iroha11
    voice "audio/log/i04.ogg"
    l   "当然可以……啊，让我先把这个文件处理一下。"
    hide iroha11
    window hide
    show cg05
    with fade
    
    pause
    
    window show
    #sound #拉椅子音效
    play sound "audio/chair.mp3"
    # h   "（八幡点点头，拉开椅子）"
    #这段要加吗？
    #imo:我加了CG，所以把旁白删了，你们觉得需要加吗
    h   "……"
    scene stuunion
    with fade
    show iroha09
    voice "audio/log/i02.ogg"
    l   "前辈久等了"
    hide iroha09
    voice "audio/log/h03.mp3"
    h   "没事，看起来你很忙啊"
    scene stuunion
    show iroha16
    voice "audio/log/i08.ogg"
    l   "不，其实并没有那么忙。新学期前确实比较忙碌，但现在已经稍微闲下来了。所以，其他成员今天都休息了。"
    hide iroha16
    voice "audio/log/h04.mp3"
    h   "哦……"
    h   "(原来如此。怪不得副会长、秘书等人都不在。没有特殊工作需要处理的时候，会让他们好好休息……哈哈，看来她是个称职的上司啊。)"
    voice "audio/log/h06.ogg"
    h   "（露出老父亲的笑容）原来你当学生会长还挺称职的嘛。"#这里表情怎么体现啊，加点笑声？
    show iroha04
    voice "audio/log/i04.ogg"
    l   "突然这么说是什么意思？夸奖也不会有什么好处的"
    hide iroha04
    play sound "audio/chair.mp3"
    narrator   "一色突然站起，走向学生会的迷你冰箱"#可以加推开椅子的音效#有条件的话想要在这里加一个背影的立绘————猪脑过载
    show iroha09
    voice "audio/log/i09.ogg"
    l   "……要喝点什么吗？"
    hide iroha09
    voice "audio/log/h05.ogg"
    h   "哦，谢谢。"
    h   "(刚刚还说不会有什么好处，不愧是一色。)"
    scene stuunion
    show iroha12
    voice "audio/log/i10.ogg"
    l   "要喝咖啡吗？还是红茶？……或者是，『乐•活•水』"#这个抑扬顿挫有什么可以利用的音效吗
    hide iroha12
    voice "audio/log/h04.mp3"
    h   "咖啡。"
    scene stuunion
    show iroha04
    voice "audio/log/i11.ogg"
    l   "这个时候不应该选乐活水吗？"
    scene stuunion
    show iroha07
    queue sound ["audio/log/i05.ogg" ,"audio/log/i06.ogg"]
    #找这玩意找了半个多小时，笑死了，学校早八交作业交不了喽-gklx
    l   "嘛，前辈，是咖啡党呢。"
    hide iroha07
    voice "audio/log/h07.ogg"
    h   "也不是这个原因……嘛，最近经常喝。顺便用来提神。"
    show iroha09
    voice "audio/log/i13.ogg"
    l   "啊，说起来你是备考生呢。有效果吗？"
    hide iroha09
    voice "audio/log/h08.ogg"
    h   "非常有效。迷迷糊糊中碰到了桌子，一下就醒过来了。"
    scene stuunion
    show iroha13#这个尴尬的笑感觉挺合适————猪脑过载
    voice "audio/log/i14.ogg"
    l   "那是正确的使用方法吗？"#这里加吐槽声音很合适
    scene stuunion
    show iroha11b#“好奇.jpg”————猪脑过载
    #imo:我认为这里是突然严肃说正事的感觉
    voice "audio/log/i07.ogg"
    l   "所以，今天有什么事情吗？"
    hide iroha11b
    h   "(说实话，我并没有什么好说的，自然的搪塞过去吧。我最擅长这种事情了。)"
    queue sound ["audio/log/h10.ogg", "audio/log/h11.ogg"]
    h   "没什么，嗯……就想稍微商量点事情……你不是说周末要出去吗。有想去哪里吗？"
    scene stuunion
    show iroha15#找不到适合的图了————猪脑过载
    voice "audio/log/i15.mp3"
    l   "周末？哈？"#有佐仓的惊讶声音就加上去吧
    hide iroha15
    voice "audio/log/h09.ogg"
    ##个人意见选09-gklx
    h   "额……，什么啊这种反应……你说过要出去玩的啊……"
    show iroha08
    l   """……

            ……

            ……

            ……"""
    scene stuunion
    show iroha18
    voice "audio/log/i16.ogg"
    l   """啊，那个……好像是有这事来着"""
    hide iroha18
    show iroha08
    voice "audio/log/i17.ogg"
    l   """ ……诶，你是认真的吗"""#好想加点语气词啊可恶
    hide iroha08
    voice "audio/log/h12.ogg"
    h   "等下，你这么说真的好吗？我现在感觉像是一个把客套话当真的可怜人……"
    scene stuunion
    show iroha02#惊讶.jpg————猪脑过载
    voice "audio/log/i18.ogg"
    l   "可以吗？和我一起出去什么的。"
    hide iroha02
    voice "audio/log/h04.mp3"
    h   "嗯，那个，就是，大家一起出去玩嘛。就是，最近也没什么机会，顺便庆祝生日，大家一起……"#紧张
    scene stuunion
    show iroha07#不满.jpg————猪脑过载
    voice "audio/log/i15.mp3"
    l   "大家一起。哈。这样啊。你是想拒绝我一个人和你出去玩吗。"#加一色不满的“哈”的声音
    hide iroha07
    show iroha03
    voice "audio/log/i19.mp3"
    l   "但是，大家一起出去也不错呢。去哪里好呢？……啊，难得的机会，去合宿吧。"
    hide iroha03
    voice "audio/log/h04.mp3"
    h   "呃……合宿？也许您不知道，我们的社团，是侍奉部这种谜一样的社团。和运动部不同，没必要去合宿练习。"#阴阳怪气
    scene stuunion
    show iroha17#得意.jpg————猪脑过载
    voice "audio/log/i05.ogg"
    l   "难道不是什么都可以吗？文化系社团也在普通地合宿哦。我们学校，还有合宿部这种东西，所以别想那么多了。"
    hide iroha17
    voice "audio/log/h08.ogg"
    h   "啊，是吗？"#这句应该有原话的吧
    show iroha11
    voice "audio/log/i05.ogg"
    l   "正好是现在这个时期，比起认真练习，为了拉近关系而举行的合宿比较多吧。顺便一提，足球部也准备举行。"
    hide iroha11
    voice "audio/log/h07.ogg"
    h   "啊，有种迎新合宿的感觉。有些一开始营造出开心和睦的气氛，巧妙的欺骗新人并强迫拽进社团的家伙呢。"
    scene stuunion
    show iroha04
    voice "audio/log/i06.ogg"
    l   """你的说法也太差劲了……但大概是有的，所以很难否定。"""
    scene stuunion
    show iroha07
    queue voice ["audio/log/i05.ogg","audio/log/i14.ogg","audio/log/i20.ogg"]
    l   """嘛，开心的只有新入部员们，做准备的经纪人很辛苦呢……
    
        要整理预定的计划，又要收钱，还要申请，菜单也必须考虑……

        哈，好麻烦。是真的很麻烦，不知道有啥意义，麻烦死了！"""
    hide iroha07
    voice "audio/log/h13.ogg"
    h   "(这家伙，真的在认真做着足球部经理的工作呢)"
    scene stuunion
    show iroha10
    voice "audio/log/i21.ogg"
    l   "新人不来也可以……我想成为永远被爱的后辈~"#可以加一色卖萌语气
    hide iroha10
    voice "audio/log/h03.mp3"
    h   "呀，这种事情稍微有点难哦。"
    show iroha02
    voice "audio/log/i22.ogg"
    l   "为什么呢。我觉得我是一个非常受欢迎的后辈角色。"
    hide iroha02
    voice "audio/log/h14.ogg"
    h   "如果像你那样，为了后辈做了那么多努力，已经是优秀的前辈了吧，虽然我也不是很明白。"
    scene stuunion
    show iroha01
    voice "audio/log/i08.ogg"
    l   "不，没有那种事……我也没有努力。"
    hide iroha01
    voice "audio/log/h15.ogg"
    h   "是吗？没有干劲的话就差不多糊弄完，或者把工作扔给谁偷懒。根本不会感觉到麻烦"
    h   "感觉麻烦是因为在努力啊……"#(自嘲的笑了笑)
    scene stuunion
    show iroha18
    voice "audio/log/i23.ogg"
    l   "哈！莫非现在你在追求我吗虽然被能干的上司认真注视这样的感觉很难不心动但请身材变好后再来吧对不起。"
    hide iroha18
    voice "audio/log/h08.ogg"
    h   "嗯，好的"
    scene stuunion
    show iroha04
    voice "audio/log/i24.ogg"
    l   "出现了，完全没有听人讲话的家伙……"
    hide iroha04
    voice "audio/log/h03.mp3"
    h   "不，是因为我已经习惯了……"
    show iroha11b
    voice "audio/log/i25.ogg"
    l   "习惯了……原来如此。正是因为习惯了，所以做一些不同的事情可能会比较有新鲜感。"
    hide iroha11b
    stop music
    #sound #手机提示音
    #这里可以给一个手机的界面，黑屏也可以，要表现出是手机的信息
    #imo:有类似素材，等我找找
    window hide
    show message at center
    play sound "audio/message.mp3"
    $ renpy.pause()
    hide message
    window show
    h   "(差不多该把一色带到部室了。)"
    voice "audio/log/h16.ogg"
    h   "啊，一色。差不多该……"
    scene stuunion
    show iroha03
    play music "audio/bgm/BGM4.ogg"
    voice "audio/log/i09.ogg"
    l   "是啊。差不多该去部室了。大家还在等着吧？"
    hide iroha03
    voice "audio/log/h17.ogg"
    h   "诶，什，什么？"
    show iroha07
    voice "audio/log/i26.ogg"
    l   "你好不擅长制造惊喜啊。完全暴露了。"
    hide iroha07
    show iroha09
    voice "audio/log/i27.ogg"
    l   "平时明明不会来学生会室的，今天突然过来了。这种事情你稍微做的自然点啊。"
    hide iroha09
    voice "audio/log/h18.ogg"
    h   "哦，哦……"#可加音效
    h   "(这家伙不简单，应该能轻松通过比企谷鉴定考试三级)"
    scene stuunion
    show iroha17
    voice "audio/log/i28.ogg"
    l   "怎么办？要表现的非常吃惊吗？虽然我很擅长那样，但还是反过来给对方制造惊喜吧？"
    hide iroha17
    show iroha03
    voice "audio/log/i29.ogg"
    l   "前辈快出去啦，我要锁门了。"#兴奋#可加一色兴奋的“前辈”sound
    hide iroha03


    #Act 2, Scene 1
    #BG01b

    scene gateafternoon
    with fade
    show iroha11
    voice "audio/log/i30.ogg"
    l "可以稍微绕个路吗？我想买点东西作为手信。"
    hide iroha11
    voice "audio/log/h03.mp3"
    h "哎，你是被祝贺的一方啊。不用这么客气的。"
    show iroha17#得意.jpg————猪脑过载
    voice "audio/log/i31.ogg"
    l "没关系的，我们来个反向惊喜。顺便去一下百元店买个拉炮吧！一边进部室一边拉响拉炮，肯定会吓到他们的！"
    hide iroha17
    show iroha10
    voice "audio/log/i13.ogg"
    l "这可真是一个超酷的点子！"#兴奋
    hide iroha10
    voice "audio/log/h18.ogg"
    h """啊，啊，嗯……是这样吗……

        (原本的计划就是一色进部室后，部员们一起拉响拉炮来迎接她，这也算是不谋而合了。)

        (或许我应该委婉地阻止她……)

        (但是，今天是一色的生日……)

        (今天的主角是一色，我们应该尽最大努力满足她的愿望。)"""
    voice "audio/log/h19.ogg"
    h "那么买完东西之后再去部室吧。"
    h "（总之先和小町联络一下吧。）"
    #这段怎么表现
    #⚠待解决问题2（imo:出现一下手机然后点一下再出现一色立绘？）
    show iroha11b
    voice "audio/log/i32.ogg"
    l "不行哦。如果特地联络的话，他们会觉得有什么事的"
    hide iroha11b
    voice "audio/log/h15.ogg"
    h "是吗？他们真的会想得那么深吗……"
    show iroha11
    voice "audio/log/i33.ogg"
    l "会的。会觉得哪里和平时不一样，从而非常地猜疑。就像今天的前辈一样"#认真
    hide iroha11
    voice "audio/log/h04.mp3"
    h "哦，哦……原来如此"
    voice "audio/log/h06.ogg"
    h "(听说女生的观察力和直觉很强吗，还是小心点吧……)"
    $ renpy.movie_cutscene("movies/whisper.webm")
    show cg06
    voice "audio/log/i07.ogg"
    l "所以，对大家保密哦。……为了不被发现……请自然一点吧？"#缩短了半步的距离，慢慢地把脸靠近八幡的肩膀，用甜甜的声音耳语道
    #哦哦哦哦哦这段又纯又欲完完全全的小恶魔本性暴露的句子该怎么处理啊，原文那个左声道很合适但是内容完全对不上啊
    #这段是不是可以做一个立绘突然变大表示距离靠近（被削头的立绘有用了）
    scene gateafternoon
    with fade
    h "(好近的距离，拜托，这样我真的会心动的！)"
    voice "audio/log/h12.ogg"
    h "时间不早了，我们该走了。"


    #Act 2, Scene 2
    #BG06

    scene sky
    play music "audio/bgm/BGM5.ogg"
    with fade
    "前往百元店的路上"
    
    h """（这学妹有够会装可爱的，虽然她的可爱是刻意装的，也无法掩盖她本来就可爱的事实，因此更令我不知如何是好）

        （老实说她长得确实可爱，行为举止也显得刻意了些，但依然讨人喜欢。）

        （再说到性格，虽然某部分令人头痛，但她刻意表现出可爱模样的精神本身，也不禁让人怜爱。）

        （糟糕，这家伙真的很可爱啊，可爱到如果站在舞台上大喊我是各位的学园偶像——彩羽哟！也不会让人觉得不自然。）"""
    window hide
    show iroha12
    play sound "audio/开门.mp3"
    with hpunch
    $ renpy.pause(2.0)
    window show
    show iroha12
    voice "audio/log/i34.ogg"
    l "前辈，你再盯着我看要撞到树上了哦"
    hide iroha12
    ##voice "audio/log/h18.ogg"
    ##voice "audio/log/h04.mp3"
    ## 你们选——gklx
    h "啊……哦，请放心，作为前辈，学校到百元店的这段路我闭着眼睛也能走到哦"#回神
    show iroha07
    voice "audio/log/i06.ogg"
    l "前辈的技能点又点在了奇怪的地方"
    hide iroha07

    #Act 2, Scene 3

    scene gateafternoon
    with fade

    h "那么，我给他们发消息说我们要回去了"
    show iroha11
    l "前辈，记得表现得自然一点哦"#是不是可以加个一色鬼脸
    hide iroha11
    h """（虽然被说自然点，但是，如果心里有点什么事情的话很难自然……）

        （因为一旦我到了班级里，基本上总是不自然的，所以想要自然地去做会感觉到不自然。这种东西是最难的。）

        （但是，对于一色来说也许不是那么难的事情）

        （在侍奉部什么都不做泰然自若喝着茶的一色彩羽）

        （在学生会室用会长样子认真努力工作的一色彩羽）

        （在足球部一边抱怨一边努力做好经理的一色彩羽）

        （丝毫不想让出永远被爱的后辈的位置的一色彩羽）

        （但是不知什么时候开始成为出色前辈的一色彩羽）

        （还有，在两个人在一起的时候夹杂着玩笑的不正经，露出小恶魔面的一色彩羽）

        （无论在什么地方，无论有着怎样的头衔，无论在展现怎样的外在，她一定会保持着自然）

        （表现着心机可爱的时候，也会突然改变态度，将真实的自己流露出来，用“这就是我！”的态度笑着）

        （所以，果然）

        （一色彩羽是最强的学妹！）"""#这里是不是可以从内心转成说出来的话，不过动画好像没原文，不好扒拉
    #最后这段内心独白怎么做比较好啊
    #BG淡化退出
    #可以放BGM和一色CG了，当然可以做点别的（片尾，制作人名单什么的）


    "感谢游玩"










    return