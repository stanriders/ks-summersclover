﻿label ru_C0:

    scene black
    window hide
    with None 
    
    nvl show dissolve # MAYBE [str]
    
    n "Я всегда верила, что люди делятся на несколько типов."

    n "На тех, кто плывут по течению своей скучной жизни; на тех, кто скачет от одного увлечения к другому; на тех, кто ходит в тени тех, кто гораздо заметнее и так далее."
    
    n "Что касается меня...Я была из тех, которые бежали. Люди, с которыми я хотела быть, что я хотела делать в жизни и где побывать, - я знала ответы на все эти вопросы."

    n "Конечно, у меня были заботы и проблемы, но они ничего не значат, когда у тебя есть цель. Именно эта цель делала меня свободной. И в пролетающее год за годом детство ничто не могло меня остановить."

    n "Все мои мечты были разрушены три года назад."
    
    nvl hide dissolve

    nvl clear
    
    return
    
label ru_C1:

    scene bg school_gardens_ss #black
    with dissolve
    
    window show 
    
    "Звон банки, ударившейся об автомат с напитками, разносится по безлюдному школьному двору. По мере того, как над территорией школы разливалось оранжевое зарево заката, все расходились по общежитиям и домам, чтобы поскорее приступить к урокам или заняться любимым делом."

    "Не зная, чем занять себя, я брожу по непривычно тихим садам, попивая напиток."

    "Лето в этом году выдалось ещё жарче обычного. По крайней мере, на это все жалуются. Я, впрочем, не вижу в этом ничего плохого, так как всегда гораздо лучше переношу жару, чем другие."

    "Кроме как о редких глотках газировки, в таком окружении думать особо не о чем, поэтому я концентрируюсь на мысли, мучающей меня в последнее время."

    "Один день похож на другой. Учебная неделя началась, хожу на уроки, учебная неделя закончилась. Расслабляюсь на выходных и опять всё идёт по кругу. \"Застой\" - вот как это называется."

    "Не сказать, что я ненавижу такую жизнь. Если сравнивать с тем, как я жила раньше, то я скорее дорожу ею."

    "Но моя жизнь также не бесконечна. Время идет, как бы ни старалась я не замечать этого. Возможно, это летние каникулы заставили меня задуматься, а может, экзамены перед ними. В любом случае, такому образу жизни однажды придет конец."
    
    scene bg school_track_ss
    with locationchange
    
    "Одинокая фигура, мелькнувшая в просвете между деревьями, отделявшими беговую дорожку от школьной площади, сразу привлекает мой взгляд."

    "Отбрасывая длинную тень в свете вечернего солнца, незнакомец медленно двигается по дальней части дорожки. Судя по тому, как он размахивает руками, заставляя себя бежать вперед, это дается ему с трудом."

    "Я остановилась у края дорожки и сделала еще один глоток. Вот и желанный способ отвлечься от тяжелых мыслей."

    "Когда незнакомец достигает поворота, у меня наконец появляется возможность рассмотреть его."

    "Эти взъерошенные волосы Хисао я бы узнала где угодно. Несмотря на то, что обычно он проводит время в классной комнате, я пару раз видела, как он ошивался около стадиона вместе с Эми."

    "Одет, как обычно, в свою рубашку. Отсутствие свитера позволяет заметить, что он неплохо сложен. Несмотря на крепкую грудь и широкие плечи, он кажется скромным человеком. Возможно, это его простое лицо создает такое впечатление, или же он просто немного подавлен недавней сменой школы."

    "Мне особо нечего ему сказать, поэтому я просто делаю еще один глоток, пока он продолжает бежать по треку."

    "Наверное, было бы неплохой идеей подбодрить его за то, что он заставил себя бегать в такое время, вот только незаметно, что этот процесс доставляет ему удовольствие."

    "Он все сильнее сбивается с ритма, а его скорость заметно падает. Даже птица, ищущая что-то в траве, не сдвинулась с места, когда он пробежал мимо."

    "Это напомнило мне, как я сама когда-то приходила на стадион и пробегала столько кругов, сколько могла, пока не падала от усталости."

    "Наблюдая, как он завершает очередной круг, я поднесла к губам банку и обнаружила, что она пуста. Отвлекшись от Хисао на, увы, кончившуюся газировку, я не замечаю, как он спотыкается и случайно останавливается прямо передо мной."

    hi "Ты... что-то хотела...?"

    "Я сомневаюсь, что он что-то расслышит с такой отдышкой, поэтому даю ему перевести дух, прежде чем ответить."

    mk "Просто смотрю."

    hi "Ага… Ясно…"

    "Он опирается на колени и тщетно  пытается привести дыхание в норму. Когда он внезапно хватается за грудь и начинает дышать чаще, я ?начинаю? слегка волноваться."

    mk "Ты в порядке? По моему ты немного перестарался."

    hi "Я в порядке. В полном порядке."

    "Мне остается лишь отойти назад и ждать, пока он восстановится."

    "Кроме его дыхания и шелеста листьев ничего не слышно. Это напоминает мне, насколько мы сейчас одни – вероятнее всего, единственные на всем школьном дворе."

    "После нескольких долгих минут он, наконец, справляется с собой и встает прямо. Пот все еще капает с его лица. В его дыхании слышится болезненный хрип, но я тактично делаю вид, что не замечаю этого."

    hi "Миура, да? Я Хисао Накай."

    mk "Тот самый таинственный переведенный ученик. Рада знакомству."

    hi "Так что привело тебя сюда?"

    mk "Просто взяла попить, а тебя?"

    hi "Пропустил утреннюю пробежку. Э… вернее, Ибаразаки сказала, что я должен компенсировать ее вечерней."

    mk "Не переживай, я знаю Эми. Да что уж там, почти вся школа знает."

    "Я кивнула в сторону беговых дорожек. Птица все еще была там, пытаясь утащить брошенный кем-то пакет из-под еды."

    mk "Сколько ты уже тут?"

    hi "Достаточно. Мне, наверное, стоит забросить эту идею и идти ужинать, но она убьет меня, если узнает."

    mk "Чувак, просто забей."

    "Это хороший шанс, если подумать. Ужинать одной скучно, и можно уговорить его заплатить за меня, если повезет."

    mk "Если голоден, то я знаю одно хорошее место неподалеку."

    "Он выглядит слегка удивленным моим предложением и запускает руку в волосы, пытаясь собраться с мыслями. Я практически вижу, как вращаются шестеренки в его голове, пока он выбирает вариант ответа."

    mk "Да ладно, красивая девушка приглашает тебя на ужин. Неужели откажешься?"

    hi "А еще говорят, что скромность – достоинство."

    mk "Никогда не говорила, что я достойная персона."

    "Я дала ему еще времени на раздумья, хотя была почти уверена в ответе. Наконец, он соглашается."

    hi "Ладно, схожу с тобой."
    
#centered "~ Timeskip ~" with dissolve

    scene bg suburb_shanghaiext_ss
    with shorttimeskip#locationchange
    
    "То, что «Шанхай» расположен в городе неподалеку, всегда было удобно. Я, было, подумала, что даже столь небольшое расстояние может быть чересчур для Хисао, учитывая его истощение, но он прекрасно справился."
    
    scene bg suburb_shanghaiint
    with locationchange
    
    "Мне нравится их форма, пусть я и считаю ее слегка нетрадиционной. Принеся заказы, официантка оставляет нас, направляясь к группе посетителей в противоположной части кафе."

    "Я была не особенно голодна, поэтому взяла лишь кусок пирога и напиток. А вот сэндвичи Хисао выглядят так, будто не продержатся долго - один из них уже исчез у него во рту."

    "Он ловит мой пристальный взгляд и смущается, неуклюже поперхнувшись."

    hi "Просто, я просто..."

    mk "Это нормально – быть голодным после занятий, чувак. Давай, можешь наворачивать за обе щеки."

    "Хисао покорно продолжает – правда, уже аккуратнее."

    mk "Так что там у вас с Эми?"

    hi "Она иногда вынуждает меня бегать с ней. Думаю, просто наслаждается моим обществом. Так же, как ты сейчас."

    mk "Но не похоже, что ты сам наслаждаешься этими пробежками."

    hi "Ну, я пытаюсь вернуться в форму. Насколько смогу, по крайней мере."

    "Он хмуро ощупывает худое предплечье, засучив рукав. Под футболкой он определенно так же щупл, хотя, возможно, я не лучший судья."

    mk "Что ж, в таком случае, она – именно тот, кто тебе нужен. Просто смотри, чтобы Эми не загнала тебя в могилу раньше времени."

    hi "Поверь, она близка к этому."

    "Его тон слишком серьезен для шутки. Похоже, Ибарадзаки та еще садистка."

    "Приступив к еде, я обнаруживаю, что на удивление голодна. В итоге мы оба быстро разобрались со своими заказами, оставив после себя только крошки, разбросанные по столу."

    "Закончив с ужином, Хисао расслабленно откидывается на спинку сиденья и довольно похлопывает себя по животу.  Я ногтем выковыриваю остатки еды, застрявшие в зубах, смакуя последние кусочки."

    "Могло показаться, что Хисао просто скучающе пялится в окно, но один быстрый взгляд выдет его. Он пытается отвлечься от забинтованной культи, покоящейся на столе."

    "Едва ли я стала бы относиться к нему хуже только из-за того, что он пялится на нее. Ведь это нормально, когда человек отвлекается на что-то необычное. Поэтому я просто улыбаюсь в надежде, что он немного расслабится."

    hi "Прости."

    mk "Поверь мне, не ты первый, кто заметил. В конце концов, такую вещь сложно упустить из виду."

    "Надеясь слегка разрядить обстановку, я усмехаюсь и взмахиваю культей, чтобы подчеркнуть свою точку зрения. Прочитать эмоции Хисао невероятно просто, даже когда он изо всех сил старается подавлять их."

    hi "Я до сих пор не могу привыкнуть к этому месту."

    mk "К городу или Ямаку?"

    "Он только повел бровью."

    mk "Так в чем проблема?"

    hi "Хм… Я думаю, «Сопоставление» будет верным словом."

    hi "Не каждый день видишь кого-то со шрамами на пол-лица или пытаешься общаться с кем-то, кто не может слышать. Или еще очевидный пример Эми…"

    mk "Ну, ты в чем-то прав. Тебе еще тяжелее, так как ты совсем недавно сюда перевелся."

    mk "Попробуй взглянуть на это с другой стороны. Например, что мы сейчас делаем?"

    hi "Болтаем в кафе?"

    mk "А что ты делал до этого сегодня?"

    hi "Проснулся, оделся, пошел на занятия, пообедал и выпил чаю в клубной комнате, еще занятия, пошел на беговую дорожку и потом начал общаться с тобой."

    mk "Разве не похоже на типичный день в старшей школе?"

    "Он хотел возразить, но вдруг понял, что не может подобрать нужных слов. Поразмыслив, он неохотно признал, что я в чем-то права."

    mk "Ты скоро привыкнешь. Если остальные нормально к этому относятся, то лишь из-за того, что у них было больше времени, чтобы приспособиться."

    hi "А если я случайно задену чьи-то чувства? Как чуть не произошло тогда, помнишь?"

    mk "Хм… ну и что? Просто найди себе другого собеседника. Здесь сотни людей, из которых можно выбрать. Черт, со мной же ты довольно легко общаешься!"

    hi "Типичная старшая школа,  значит…"

    mk "Именно. Просто найди себе друзей, выбери путь и следуй ему до конца года. И все будет в порядке."

    "Он отвернулся к окну, размышляя над беседой. Ему идет это выражение созерцателя."

    "Придя, очевидно, к выводу, он кивает, прежде чем повернуться ко мне."

    hi "Спасибо, я постараюсь помнить об этом."

    "Улыбка, которую он дарит мне, по-своему милая. Слабая, но ужасно искренняя. Все, что я могу сделать – удовлетворенно усмехнуться в ответ."

    "Такая случайная встреча вряд ли сильно изменит что-то для меня, но, если я смогу помочь Хисао встать на верный путь, я хотя бы буду полезна кому-то."

    "Погода сегодня и правда прекрасная."

    window hide
    
    scene black
    with dissolve
    
    return