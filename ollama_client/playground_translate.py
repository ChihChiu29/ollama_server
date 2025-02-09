import ollama_client

def main():
  # Using LLaVA for image analysis
  response = ollama_client.client().chat(
    model='llama3.2',
    messages=[
      {
        'role': 'user',
        'content': 'Translate the following into English. Do not give any commentary or suggestions, just translates it.' +
'''
===== START =====
1.

绝不失腰

逃爱记：霸总请你滚远点
查看详情
一、为了腰子而努力

我坐在床边熟练地点了支烟：「别难过了，我会对你负责的。」

男人掀开被子露出冷峻的脸庞和硬朗的下颌线，薄唇微微勾起，邪肆一笑，伸出修长的食指挑起我的下巴：「女人，你想用这种方式引起我的注意？嗯？」

我不动声色地挪开他的手：「啊不，不是……」

天知道为了保住我的一颗肾，正绞尽脑汁让这个男人讨厌我，巴不得他一生气将我扔到非洲去！

我做梦都没想到，自己有朝一日会成为自己笔下的霸道总裁文——《总裁终于后悔了》的圣母女主角。来到这个陌生的世界里，我只能靠对剧情先知的优势生存了。

再过半个月男主赵霆皓的白月光秦梓涵就要回来，如果我没记错的话，回来后的第二天就挖了女主人公，也就是我秦雨薇一颗肾，备胎男二冷轩将刚做完手术的我偷偷带走。

目前最重要的是想办法保住我的肾。

我忽然灵机一动，既然冷轩有能耐带我走，那还不如现在就走。

可现在不知道去哪儿找他，我肠子都快悔青了，为什么就没给冷轩编个家庭地址呢？看来事到如今只能自求多福了。

正沉浸在担忧中，我猛然想起，今天当红女星林卉如要来，记忆告诉我她是故意来找茬的，故意从楼梯上摔下来诬陷我。

依照目前的情况来看，我只能躲了。但这是赵霆皓的地盘，我无论躲哪里他都找得到我的。

思来想去，我决定待在厕所里。

看这时间，林卉如应该快到了，我贴在厕所门后仔细一听，外边果真有动静。

「霆皓，人家想你了。对了，听说雨薇在这儿，怎么不见人呢？」

听见她提起我，我条件反射往后一退，却踢倒一瓶威猛先生，我吓得一激灵，决定先发制人：「卉如，我正上厕所呢！」

赵霆皓语气不耐烦：「秦雨薇，你还要在厕所待多久，都已经一个小时了！」

「我，我便秘。」

又耗了二十分钟，实在没理由再继续耗下去，我只好打开门出来。

林卉如假装贴心地问我有没有哪里不舒服，我瞥了眼赵霆皓，只见他依然冷着张脸。

我回道：「就是痔疮犯了，挺疼的。」

赵霆皓冷笑：「你哪来的痔疮？」

我的脸轰地红了，林卉如的脸唰地白了。我从没有像现在这样后悔给男主创造了毒舌的人设。

林卉如假装淡定地关心了我几句，挽着我的手臂说要去我房间瞧瞧。

开始了，她开始了！

我头摇得像拨浪鼓似的：「不不不，我们就在一楼聊聊天，没必要去我房间。」

可她不依不饶硬是要去，赵霆皓又说看看又不少我一坨肉。

我急得满头汗，急中生智：「那就去吧，只要卉如你不嫌弃我那房间里挂满的裸男海报。我给你说哦，那可都是极品，我每天晚上都要看着满墙的腹肌和大胸肌入睡呢。」

赵霆皓凌厉的眼神射过来，比奥特曼激光的杀伤力还大。

为了在赵霆皓面前维持清纯玉女的形象，林卉如终于放弃上二楼参观。我松了口气，总算躲过一劫。

这段时间打发掉林卉如，又花费好些日子智斗赵霆皓的其他莺莺燕燕们，终于白莲花王者段位的秦梓涵要回来了。

我一筹莫展，食欲也很差，晚饭只吃了两碗，赵霆皓问我：「你怎么了？」

「我肾疼。」

吃了饭后我早早就躺下了，然而辗转反侧大半宿，悟出一个道理：人啊还是得自救。

可能昨晚思虑过多，我起床后已经接近中午，赵霆皓一大早就去了公司，佣人都是赵霆皓的眼线，我悄悄的地来到别墅大门，掏出昨晚偷出来的一大把钥匙。

哼，我就一把一把地试，不信打不开。

我正想开门，shit，忘记了这是密码锁啊！对了，密码！我是作者，没有谁比我更清楚密码了！

我激动地按下：123456

滴滴，门开了。

我出来的第一件事就是去菜市场，一路上琢磨着，人和猪都是哺乳动物，那么人腰子和猪腰子应该也差不多。于是我当即决定买个猪腰子。

我提着猪腰子来到 xx 医院，找到要挖我肾的主刀医师。

他笑着对我说：「我们医生不收病人的礼。」


===== TRANSLATE =====
''',
      },
    ],
  )

  print(response['message']['content'])


if __name__ == '__main__':
  main()