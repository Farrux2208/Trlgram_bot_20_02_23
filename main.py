import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu alaykum.....""",reply_markup=bosh_sahifa)



@dp.message_handler(text="Buyurtma berish 👩‍💻")
async def echo(message: types.Message):
    await message.answer("Quyidagilardan birini tanlang",reply_markup=menu())

@dp.callback_query_handler(text="lavash")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat lavashlar menusi...",reply_markup=lavash_menu())
############################################################
#menuga qaytish
@dp.callback_query_handler(text="ortga")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Quyidagilardan birini tanlang...",reply_markup=menu())
#lavash menuga qaytish
@dp.callback_query_handler(text="ortga_1")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat lavashlar menusi...",reply_markup=lavash_menu())
#mol gushti menu lavosh
@dp.callback_query_handler(text="ortga_2")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=mol_gushlik_menu())
#q_mol gushti menu lavosh
@dp.callback_query_handler(text="ortga_3")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Quyidagilardan birini tanlang...",reply_markup=q_mol_gushlik_menu())
#tv_gushli lavash menuga qaytish
@dp.callback_query_handler(text="ortga_4")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuq_gushlik_menu())
#qp_tv_gushli lavash menuga qaytish
@dp.callback_query_handler(text="ortga_5")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=qp_tovuq_gushlik_menu())
#pishloq tovuq_g menuga qaytish
@dp.callback_query_handler(text="ortga_6")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=pishloq_tg_menu())
#pishloqli mol_g menuga qaytish
@dp.callback_query_handler(text="ortga_7")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=pishloq_mg_menu())
#hoddoglar menusiga qaytish
@dp.callback_query_handler(text="ortga_8")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Hod Doglar menusi...",reply_markup=hoddog_menu())
#sendvechlar menusiga qaytish
@dp.callback_query_handler(text="ortga_9")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Sendvich menusi...",reply_markup=sendvich_clap_menu())
#sendvech menusiga qaytish
@dp.callback_query_handler(text="ortga_10")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Sendvich menusi...",reply_markup=shaurma_menu())
#burger_menu
@dp.callback_query_handler(text="ortga_11")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat burger menusi!!!",reply_markup=burger_menu())
#donar_menuga_qaytish
@dp.callback_query_handler(text="ortga_12")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat donar menusi!!!",reply_markup=donar_menu())

#gazaklar_menusiga_qaytish
@dp.callback_query_handler(text="ortga_13")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat gazaklar menusi!!!",reply_markup=gazaklar_menu())

#ichimliklar_menusiga_aytish
@dp.callback_query_handler(text="ortga_14")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi())

#choy va kofilar menusiga qaytish
@dp.callback_query_handler(text="ortga_15")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=choy_va_kofi_menusi())

#kofilar_menusiga qaytish
@dp.callback_query_handler(text="ortga_16")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=kofilar_menusi())
#choy menusiga qaytish
@dp.callback_query_handler(text="ortga_17")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=choy_menusi())
#yaxna ichimliklar menusi
@dp.callback_query_handler(text="ortga_18")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Yaxna ichimliklar menusi!!!!!!!!""",reply_markup=yaxna_ichimliklar_menusi())
#fresh va tabiy soklar menusiga qaytish
@dp.callback_query_handler(text="ortga_19")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat Frish va tabiiy soklar menusi!!!",reply_markup=firish_va_tabiy_soklar_menusi())
#dissert menusiga qaytish
@dp.callback_query_handler(text="ortga_20")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat Dissertlar menusi!!!",reply_markup=dissert_menusi())
#pizzalar menusiga qaytish
@dp.callback_query_handler(text="ortga_21")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat pizzalar menusi!!!",reply_markup=pizzalar_menusi())





############################################################
@dp.callback_query_handler(text="m_go'sht")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Quyidagilardan birini tanlang...",reply_markup=mol_gushlik_menu())

@dp.callback_query_handler(text="mini")
async def echo(call: types.CallbackQuery):
	foto = open("imgs/Lavash_1.jpg","rb")
	await call.message.answer_photo(photo = foto,caption = """Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=mol_gushti_mini())

@dp.callback_query_handler(text="classik")
async def echo(call: types.CallbackQuery):
	foto = open("imgs/Lavash_2.jpg","rb")
	await call.message.answer_photo(photo = foto,caption =  """Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=mol_gushti_classik())

@dp.callback_query_handler(text="qalampirli_m_go'sht")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=q_mol_gushlik_menu())

@dp.callback_query_handler(text="q_mini")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:19000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=q_mol_gushti_mini())

@dp.callback_query_handler(text="q_classik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=q_mol_gushti_mini())

@dp.callback_query_handler(text="t_go'sht")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=tovuq_gushlik_menu())

@dp.callback_query_handler(text="tv_mini")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuq_gushlik_mini())

@dp.callback_query_handler(text="tv_classik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuq_gushlik_classik())

@dp.callback_query_handler(text="qalampirli_t_go'sht")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=qp_tovuq_gushlik_menu())

@dp.callback_query_handler(text="qp_tg_Mini")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=qp_tovuq_gushlik_mini())

@dp.callback_query_handler(text="qp_tg_classik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=qp_tovuq_gushlik_classik())

@dp.callback_query_handler(text="peshloq_tg")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!! ptg",reply_markup=pishloq_tg_menu())

@dp.callback_query_handler(text="ptg_mini")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=pishloq_tg_mini())

@dp.callback_query_handler(text="ptg_classik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=pishloq_tg_classik())

@dp.callback_query_handler(text="pishloq_mg")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=pishloq_mg_menu())

@dp.callback_query_handler(text="pmg_mini")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=pishloq_mg_mini())

@dp.callback_query_handler(text="pmg_classik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=pishloq_mg_classik())

@dp.callback_query_handler(text="fitter")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=fittir())

@dp.callback_query_handler(text="hoddog")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Hod Doglar menusi...",reply_markup=hoddog_menu())

@dp.callback_query_handler(text="haddog_baget_dabl")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=hod_dog_baget_dabl())

@dp.callback_query_handler(text="classik_hod_dog")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=classik_hod_dog())

@dp.callback_query_handler(text="corolevskiy")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=corolevskiy())

@dp.callback_query_handler(text="tovuqli_hod_dog")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuqli_hod_dog())

@dp.callback_query_handler(text="clab")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Sendvich menusi...",reply_markup=sendvich_clap_menu())

@dp.callback_query_handler(text="classik_sendvich_clap")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=classik_clap_sendvich())

@dp.callback_query_handler(text="tovuqli_sendvich")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuqli_sendvich())

@dp.callback_query_handler(text="shaurma")
async def echo(call: types.CallbackQuery):
	await call.message.answer("Marhamat Shaurma menusi...",reply_markup=shaurma_menu())

@dp.callback_query_handler(text="mol_go'shtli_shaurma")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=mol_goshtli_shaurma())

@dp.callback_query_handler(text="tovuq_shaurma")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuq_shaurma())

@dp.callback_query_handler(text="mol_go'shtli+qalampir")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=mol_goshtli_qalampir())

@dp.callback_query_handler(text="tovuq_go'shtli+qalampir")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""",reply_markup=tovuq_goshtli_qalampir())

@dp.callback_query_handler(text="burger")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat burger menusi!!!",reply_markup=burger_menu())

@dp.callback_query_handler(text="gamburger")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:22000 ming so'm 
Miqdorini tanlang""",reply_markup=gamburger())

@dp.callback_query_handler(text="chezburger")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:20000 ming so'm 
Miqdorini tanlang""",reply_markup=chezburger())

@dp.callback_query_handler(text="donar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat donar menusi!!!",reply_markup=donar_menu())

@dp.callback_query_handler(text="tovuqli")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:22000 ming so'm 
Miqdorini tanlang""",reply_markup=tovuqli())

@dp.callback_query_handler(text="go'shtli")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:20000 ming so'm 
Miqdorini tanlang""",reply_markup=gushtli())

@dp.callback_query_handler(text="gazaklar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat gazaklar menusi!!!",reply_markup=gazaklar_menu())

@dp.callback_query_handler(text="15gramfiri")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:23000 ming so'm 
Miqdorini tanlang""",reply_markup=firi_15_gram())

@dp.callback_query_handler(text="kartoshka_d")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:22000 ming so'm 
Miqdorini tanlang""",reply_markup=Kartoshka_Derevenski())

@dp.callback_query_handler(text="guruch_katta")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:23000 ming so'm 
Miqdorini tanlang""",reply_markup=guruch_katta())

@dp.callback_query_handler(text="guruch_kichik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:22000 ming so'm 
Miqdorini tanlang""",reply_markup=guruch_kichik())

@dp.callback_query_handler(text="ichimlik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat ichimliklar menusi!!!",reply_markup=ichimliklar_menusi())

@dp.callback_query_handler(text="choy_va_kofi")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=choy_va_kofi_menusi())

@dp.callback_query_handler(text="kofiylar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=kofilar_menusi())

@dp.callback_query_handler(text="amircano")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Ameicani narxi 12000!!!!!!""",reply_markup=amercano())

@dp.callback_query_handler(text="capuchino")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Coppuccino Narxi 18000!!!!!!""",reply_markup=capucheno())

@dp.callback_query_handler(text="kofi_3/1")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Kofe 3 v 1☕️ 3000ming so'm!!!!""",reply_markup=cofi_3v1())

@dp.callback_query_handler(text="latte")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Latte big 120g☕️ 15000mig so'm!!!!""",reply_markup=latte())

@dp.callback_query_handler(text="choylar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Katigoryalardan birini tanlang!!!",reply_markup=choy_menusi())

@dp.callback_query_handler(text="ko'k_choy")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Choy ko'k 3000mig so'm!!!!""",reply_markup=kuk_choy())

@dp.callback_query_handler(text="qora_choy")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Choy qora 3000mig so'm!!!!""",reply_markup=qora_choy())

@dp.callback_query_handler(text="limon_choy")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Limon choy 5000mig so'm!!!!!!!!""",reply_markup=limon_choy())

@dp.callback_query_handler(text="yaxna_ichimliklar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Yaxna ichimliklar menusi!!!!!!!!""",reply_markup=yaxna_ichimliklar_menusi())

@dp.callback_query_handler(text="fanta")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Fanta narxi: 11000!!!!!!!!""",reply_markup=fanta())

@dp.callback_query_handler(text="sprite")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Sprite narxi: 8000!!!!!!!!""",reply_markup=sprite())

@dp.callback_query_handler(text="cola")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Cola narxi: 12000!!!!!!!!""",reply_markup=cocacola())

@dp.callback_query_handler(text="nestle")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Nestli narxi: 5000!!!!!!!!""",reply_markup=nestli())

@dp.callback_query_handler(text="firish_va_tabiy_soklar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat Frish va tabiiy soklar menusi!!!",reply_markup=firish_va_tabiy_soklar_menusi())

@dp.callback_query_handler(text="bliss_sok")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅Biliss sok narxi: 11000!!!!!!!!""",reply_markup=bliss_sok())

@dp.callback_query_handler(text="olma_sabzi_frish")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""✅ Olma va sabzi soki narxi: 12000!!!!!!!!""",reply_markup=olma_va_sabzi_soki())
###
@dp.callback_query_handler(text="desert")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat Dissertlar menusi!!!",reply_markup=dissert_menusi)

@dp.callback_query_handler(text="asal")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang""",reply_markup=dissert_asal)

@dp.callback_query_handler(text="qulupnay")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:14000 ming so'm 
✅Qulupnayli Muss.
Miqdorini tanlang""",reply_markup=dissert_qulupnay)

@dp.callback_query_handler(text="choko")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang""",reply_markup=dissert_choko)

@dp.callback_query_handler(text="pizza")
async def echo(call: types.CallbackQuery):
	await call.message.answer("✅Marhamat pizzalar menusi!!!",reply_markup=pizzalar_menusi)

@dp.callback_query_handler(text="peperonlik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:65000 ming so'm 
✅Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang""",reply_markup=peperoni)

@dp.callback_query_handler(text="ananaslik")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:65000 ming so'm 
✅Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang""",reply_markup=ananaslik)

@dp.callback_query_handler(text="margaritta")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""Narxi:65000 ming so'm 
✅Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang""",reply_markup=margaritto)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
