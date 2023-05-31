from aiogram.types import *

bosh_sahifa = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Buyurtma berish 👩‍💻")
		],
		[
			KeyboardButton(text="Sozlamalar"),
			KeyboardButton(text="Biz bilan aloqa")
		],
	],resize_keyboard=True
)

def menu():
	menu_dict = {
		"Lavash🌯 🌯":"lavash",
		"Hod Dog🌭 🌭":"hoddog",
		"Sendvich Clab🧇 🧇":"hoddog",
		"Shaurma🌮 🌮":"shaurma",
		"Burger 🍔🍔":"burger",
		"Donar 🍱🍱":"donar",
		"Gazaklar 🍟🍟":"gazaklar",
		"Ichimliklar 🍹🍹":"ichimlik",
		"Desertlar 🍰🍰":"desert",
		"Pizza 🍕🍕":"pizza"
	}

	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))

	return batton
# menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Lavash🌯 🌯",callback_data="lavash"),
# 			InlineKeyboardButton(text="Hod Dog🌭 🌭",callback_data="hoddog"),
# 		],
# 		[
# 			InlineKeyboardButton(text="Sendvich Clab🧇 🧇",callback_data="clab"),
# 			InlineKeyboardButton(text="Shaurma🌮 🌮",callback_data="shaurma")
# 		],
# 		[
# 			InlineKeyboardButton(text="Burger 🍔🍔",callback_data="burger"),
# 			InlineKeyboardButton(text="Donar 🍱🍱",callback_data="donar"),
# 		],
# 		[
# 			InlineKeyboardButton(text="Gazaklar 🍟🍟",callback_data="gazaklar"),
# 			InlineKeyboardButton(text="Ichimliklar 🍹🍹",callback_data="ichimlik")
# 		],
# 		[
# 			InlineKeyboardButton(text="Desertlar 🍰🍰",callback_data="desert"),
# 			InlineKeyboardButton(text="Pizza 🍕🍕",callback_data="pizza")
# 		],
# 	],
# )

def lavash_menu():
	menu_dict = {
	"Mol go'shtlik 🥩":"m_go'sht",
	"Qalampirli mol go'sht🌶🥩": "qalampirli_m_go'sht",
	"Tovuq go'shtlik 🍗":"t_go'sht",
	"Qalamprli tovuq go'sht🌶🍗":"qalampirli_t_go'sht",
	"pishloqli tovuq go'sht🍗🧀":"peshloq_tg",
	"pishloqli mol go'sht🥩🧀":"pishloq_mg",
	"Fitter🍃":"fitter",	
	}

	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga"))
	return batton
# lavash_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Mol go'shtlik 🥩",callback_data="m_go'sht"),
# 			InlineKeyboardButton(text="Qalampirli mol go'sht🌶🥩",callback_data="qalampirli_m_go'sht"),
# 		],
# 		[
# 			InlineKeyboardButton(text="Tovuq go'shtlik 🍗",callback_data="t_go'sht"),
# 			InlineKeyboardButton(text="Qalamprli tovuq go'sht🌶🍗",callback_data="qalampirli_t_go'sht"),
# 		],
# 		[
# 			InlineKeyboardButton(text="pishloqli tovuq go'sht🍗🧀",callback_data="peshloq_tg"),
# 			InlineKeyboardButton(text="pishloqli mol go'sht🥩🧀",callback_data="pishloq_mg")
# 		],
# 		[
# 			InlineKeyboardButton(text="Fitter🍃",callback_data="fitter"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga"),
# 		],
# 	],
# )

def mol_gushlik_menu():
	menu_dict = {
	"Mini 👍":"mini",
	"classik 👍":"classik",	
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# mol_gushlik_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Mini 👍",callback_data="mini"),
# 			InlineKeyboardButton(text="classik 👍",callback_data="classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1")
# 		],
# 	],
# )

def mol_gushti_mini():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_2"))
	return batton
# mol_gushti_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_2"),
# 		],
# 	],
# )

def mol_gushti_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_2"))
	return batton
# mol_gushti_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_2"),
# 		],
# 	],
# )

def q_mol_gushlik_menu():
	menu_dict = {
	"Q_Mini 👍":"q_mini",
	"Q_classik 👍":"q_classik",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# q_mol_gushlik_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Q_Mini 👍",callback_data="q_mini"),
# 			InlineKeyboardButton(text="Q_classik 👍",callback_data="q_classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_1")
# 		],
# 	],
# )

def q_mol_gushti_mini():

	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))

	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_3"))

	return batton
# q_mol_gushti_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_3"),
# 		],
# 	],
# )

def q_mol_gushti_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_3"))
	return batton
# q_mol_gushti_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_3"),
# 		],
# 	],
# )

def tovuq_gushlik_menu():
	menu_dict = {
	"tv_Mini 👍":"tv_mini",
	"tv_classik 👍":"tv_classik"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# tovuq_gushlik_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="tv_Mini 👍",callback_data="tv_mini"),
# 			InlineKeyboardButton(text="tv_classik 👍",callback_data="tv_classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="ortga",callback_data="ortga_1")
# 		],
# 	],
# )

def tovuq_gushlik_mini():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_4"))
	return batton
# tovuq_gushlik_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_4"),
# 		],
# 	],
# )
def tovuq_gushlik_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_4"))
	return batton
# tovuq_gushlik_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_4"),
# 		],
# 	],
# )

def qp_tovuq_gushlik_menu():
	menu_dict = {
	"qp_tg_Mini 👍":"qp_tg_Mini",
	"qp_tg_classik 👍":"qp_tg_classik"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# qp_tovuq_gushlik_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="qp_tg_Mini 👍",callback_data="qp_tg_Mini"),
# 			InlineKeyboardButton(text="qp_tg_classik 👍",callback_data="qp_tg_classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1")
# 		],
# 	],
# )
def qp_tovuq_gushlik_mini():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_5"))
	return batton
# qp_tovuq_gushlik_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_5"),
# 		],
# 	],
# )

def qp_tovuq_gushlik_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_5"))
	return batton
# qp_tovuq_gushlik_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_5"),
# 		],
# 	],
# )

def pishloq_tg_menu():
	menu_dict = {
	"🍗🧀Mini 👍":"ptg_mini",
	"🍗🧀classik 👍":"ptg_classik"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# pishloq_tg_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="🍗🧀Mini 👍",callback_data="ptg_mini"),
# 			InlineKeyboardButton(text="🍗🧀classik 👍",callback_data="ptg_classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_1")
# 		],
# 	],
# )

def pishloq_tg_mini():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_6"))
	return batton
# pishloq_tg_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_6"),
# 		],
# 	],
# )

def pishloq_tg_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_6"))
	return batton
# pishloq_tg_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_6"),
# 		],
# 	],
# )

def pishloq_mg_menu():
	menu_dict = {
	"🥩🧀Mini 👍":"pmg_mini",
	"🥩🧀classik 👍":"pmg_classik"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_1"))
	return batton
# pishloq_mg_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="🥩🧀Mini 👍",callback_data="pmg_mini"),
# 			InlineKeyboardButton(text="🥩🧀classik 👍",callback_data="pmg_classik"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_1")
# 		],
# 	],
# )

def pishloq_mg_mini():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_7"))
	return batton
# pishloq_mg_mini = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_7"),
# 		],
# 	],
# )

def pishloq_mg_classik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_7"))
	return batton
# pishloq_mg_classik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_7"),
# 		],
# 	],
# )


def fittir():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_1"))
	return batton
# fittir = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_1"),
# 		],
# 	],
# )

def hoddog_menu():
	menu_dict = {
	"Hod Dog Baget Dabl👍":"haddog_baget_dabl",
	"Classik Hod Dog👍":"classik_hod_dog",
	"Corolevskiy👍":"corolevskiy",
	"Tovuqli Hod Dog 👍":"tovuqli_hod_dog"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# hoddog_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Hod Dog Baget Dabl👍",callback_data="haddog_baget_dabl"),
# 			InlineKeyboardButton(text="Classik Hod Dog👍",callback_data="classik_hod_dog"),
# 		],
# 		[
# 			InlineKeyboardButton(text="Corolevskiy👍",callback_data="corolevskiy"),
# 			InlineKeyboardButton(text="Tovuqli Hod Dog 👍",callback_data="tovuqli_hod_dog"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
# 		],
# 	],
# )

def hod_dog_baget_dabl():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"))
	return batton
# hod_dog_baget_dabl = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"),
# 		],
# 	],
# )

def classik_hod_dog():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"))
	return batton
# classik_hod_dog = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"),
# 		],
# 	],
# )

def corolevskiy():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"))
	return batton
# corolevskiy = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"),
# 		],
# 	],
# )

def tovuqli_hod_dog():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"))
	return batton
# tovuqli_hod_dog = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_8"),
# 		],
# 	],
# )

def sendvich_clap_menu():
	menu_dict = {
	"classik clap sendvich 👍":"classik_sendvich_clap",
	"Tovuqli sendvich 👍":"tovuqli_sendvich"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# sendvich_clap_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="classik clap sendvich 👍",callback_data="classik_sendvich_clap"),
# 			InlineKeyboardButton(text="Tovuqli sendvich 👍",callback_data="tovuqli_sendvich"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
# 		],
# 	],
# )

def classik_clap_sendvich():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_9"))
	return batton
# classik_clap_sendvich = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_9"),
# 		],
# 	],
# )

def tovuqli_sendvich():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_9"))
	return batton
# tovuqli_sendvich = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_9"),
# 		],
# 	],
# )

def shaurma_menu():
	menu_dict = {
	"Mol go'shtli shaurma👍":"mol_go'shtli_shaurma",
	"Tovuq shaurma👍":"tovuq_shaurma",
	"Mol go'shtli+qalampir👍":"mol_go'shtli+qalampir",
	"Tovuq go'shtli+qalampir👍":"tovuq_go'shtli+qalampir"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# shaurma_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Mol go'shtli shaurma👍",callback_data="mol_go'shtli_shaurma"),
# 			InlineKeyboardButton(text="Tovuq shaurma👍",callback_data="tovuq_shaurma"),
# 		],
# 		[
# 			InlineKeyboardButton(text="Mol go'shtli+qalampir👍",callback_data="mol_go'shtli+qalampir"),
# 			InlineKeyboardButton(text="Tovuq go'shtli+qalampir👍",callback_data="tovuq_go'shtli+qalampir"),
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
# 		],
# 	],
# )

def mol_goshtli_shaurma():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"))
	return batton
# mol_goshtli_shaurma = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"),
# 		],
# 	],
# )

def tovuq_shaurma():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"))
	return batton
# tovuq_shaurma = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"),
# 		],
# 	],
# )

def mol_goshtli_qalampir():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"))
	return batton
# mol_goshtli_qalampir = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"),
# 		],
# 	],
# )

def tovuq_goshtli_qalampir():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"))
	return batton
# tovuq_goshtli_qalampir = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1",callback_data="number"),
# 			InlineKeyboardButton(text="2",callback_data="number"),
# 			InlineKeyboardButton(text="3",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4",callback_data="number"),
# 			InlineKeyboardButton(text="5",callback_data="number"),
# 			InlineKeyboardButton(text="6",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7",callback_data="number"),
# 			InlineKeyboardButton(text="8",callback_data="number"),
# 			InlineKeyboardButton(text="9",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_10"),
# 		],
# 	],
# )

def burger_menu():
	menu_dict = {
	"Gamburger 👍":"gamburger",
	"Chezburger 👍":"chezburger",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# burger_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Gamburger 👍",callback_data="gamburger"),
# 			InlineKeyboardButton(text="Chezburger 👍",callback_data="chezburger")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga"),
# 		],
# 	],
# )

def gamburger():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_11"))
	return batton
# gamburger = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_11"),
# 		],
# 	],
# )

def chezburger():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_11"))
	return batton
# chezburger = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_11"),
# 		],
# 	],
# )

def donar_menu():
	menu_dict = {
	"tovuqli 👍":"tovuqli",
	"go'shtli 👍":"go'shtli",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# donar_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="tovuqli 👍",callback_data="tovuqli"),
# 			InlineKeyboardButton(text="go'shtli 👍",callback_data="go'shtli")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga"),
# 		],
# 	],
# )

def tovuqli():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_12"))
	return batton
# tovuqli = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_12"),
# 		],
# 	],
# )

def gushtli():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_12"))
	return batton
# gushtli = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_12"),
# 		],
# 	],
# )

def gazaklar_menu():
	menu_dict = {
	"15 gram Fri 👍":"15gramfiri",
	"Kartoshka Derevenski 👍":"kartoshka_d",
	"Guruch katta 👍":"guruch_katta",
	"Guruch kichik 👍":"guruch_kichik"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# gazaklar_menu = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="15 gram Fri 👍",callback_data="15gramfiri"),
# 			InlineKeyboardButton(text="Kartoshka Derevenski 👍",callback_data="kartoshka_d")
# 		],
# 		[
# 			InlineKeyboardButton(text="Guruch katta 👍",callback_data="guruch_katta"),
# 			InlineKeyboardButton(text="Guruch kichik 👍",callback_data="guruch_kichik")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga"),
# 		],
# 	],
# )

def firi_15_gram():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"))
	return batton
# firi_15_gram = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"),
# 		],
# 	],
# )

def Kartoshka_Derevenski():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"))
	return batton
# Kartoshka_Derevenski = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"),
# 		],
# 	],
# )

def guruch_katta():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"))
	return batton
# guruch_katta = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"),
# 		],
# 	],
# )

def guruch_kichik():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"))
	return batton
# guruch_kichik = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_13"),
# 		],
# 	],
# )


def ichimliklar_menusi():
	menu_dict = {
	"Choy va kofi 👍":"choy_va_kofi",
	"Yaxna ichimliklar 👍":"yaxna_ichimliklar",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))
	return batton
# ichimliklar_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Choy va kofi 👍",callback_data="choy_va_kofi"),
# 			InlineKeyboardButton(text="Yaxna ichimliklar 👍",callback_data="yaxna_ichimliklar")
# 		],
# 		[
# 			InlineKeyboardButton(text="Fresh va tabiiy soklar 👍",callback_data="firish_va_tabiy_soklar")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
# 		],
# 	],
# )

def choy_va_kofi_menusi():
	menu_dict = {
	"Kofilar 👍":"kofiylar",
	"Choylar 👍":"choylar"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_14"))
	return batton
# choy_va_kofi_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Kofilar 👍",callback_data="kofiylar"),
# 			InlineKeyboardButton(text="Choylar 👍",callback_data="choylar")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_14")
# 		],
# 	],
# )

def kofilar_menusi():
	menu_dict = {
	"Amircano 👍":"amircano",
	"Capuchino 👍":"capuchino"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_15"))
	return batton

# kofilar_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Amircano 👍",callback_data="amircano"),
# 			InlineKeyboardButton(text="Capuchino 👍",callback_data="capuchino")
# 		],
# 		[
# 			InlineKeyboardButton(text="Kofi 3/1 👍",callback_data="kofi_3/1"),
# 			InlineKeyboardButton(text="Latte 👍",callback_data="latte")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_15")
# 		],
# 	],
# )

def amercano():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"))
	return batton
# amercano = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"),
# 		],
# 	],
# )

def capucheno():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"))
	return batton
# capucheno = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"),
# 		],
# 	],
# )

def cofi_3v1():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"))
	return batton
# cofi_3v1 = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"),
# 		],
# 	],
# )

def latte():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"))
	return batton
# latte = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_16"),
# 		],
# 	],
# )

def choy_menusi():
	menu_dict = {
	"Ko'k choy 👍":"ko'k_choy",
	"Qora choy 👍":"qora_choy",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_15"))
	return batton
# choy_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Ko'k choy 👍",callback_data="ko'k_choy"),
# 			InlineKeyboardButton(text="Qora choy 👍",callback_data="qora_choy")
# 		],
# 		[
# 			InlineKeyboardButton(text="Limon choy 👍",callback_data="limon_choy")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_15")
# 		],
# 	],
# )

def kuk_choy():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"))
	return batton
# kuk_choy = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"),
# 		],
# 	],
# )

def qora_choy():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"))
	return batton
# qora_choy = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"),
# 		],
# 	],
# )

def limon_choy():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"))
	return batton
# limon_choy = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_17"),
# 		],
# 	],
# )

def yaxna_ichimliklar_menusi():
	menu_dict = {
	"Ko'k choy 👍":"ko'k_choy",
	"Qora choy 👍":"qora_choy",
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_14"))
	return batton
# yaxna_ichimliklar_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Fanta 👍",callback_data="fanta"),
# 			InlineKeyboardButton(text="Spriate 👍",callback_data="sprite")
# 		],
# 		[
# 			InlineKeyboardButton(text="Coca Cola 👍",callback_data="cola"),
# 			InlineKeyboardButton(text="Nestle 👍",callback_data="nestle")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_14")
# 		],
# 	],
# )

def fanta():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"))
	return batton
# fanta = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"),
# 		],
# 	],
# )

def sprite():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"))
	return batton
# sprite = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"),
# 		],
# 	],
# )

def cocacola():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"))
	return batton
# cocacola = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"),
# 		],
# 	],
# )

def nestli():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"))
	return batton
nestli = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_18"),
		],
	],
)

def firish_va_tabiy_soklar_menusi():
	menu_dict = {
	"Bliss sok 1 👍":"bliss_sok",
	"Olma va sbzi frish 👍":"olma_sabzi_frish"
	}
	batton = InlineKeyboardMarkup(row_width = 2)
	for nomi,c_data in menu_dict.items():
		batton.insert(InlineKeyboardButton(text = nomi, callback_data = c_data))
	batton.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga_14"))
	return batton
# firish_va_tabiy_soklar_menusi = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="Bliss sok 1 👍",callback_data="bliss_sok"),
# 			InlineKeyboardButton(text="Olma va sbzi frish 👍",callback_data="olma_sabzi_frish")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_14")
# 		],
# 	],
# )

def bliss_sok():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_19"))
	return batton
# bliss_sok = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_19"),
# 		],
# 	],
# )

def olma_va_sabzi_soki():
	batton = InlineKeyboardMarkup(row_width = 3)
	for i in range(1,10):
		batton.insert(InlineKeyboardButton(text = i, callback_data = "number"))
	batton.add(InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_19"))
	return batton
# olma_va_sabzi_soki = InlineKeyboardMarkup(
# 	inline_keyboard=[
# 		[
# 			InlineKeyboardButton(text="1️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="2️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="3️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="4️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="5️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="6️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="7️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="8️⃣",callback_data="number"),
# 			InlineKeyboardButton(text="9️⃣",callback_data="number")
# 		],
# 		[
# 			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_19"),
# 		],
# 	],
# )

dissert_menusi = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Asal 👍",callback_data="asal"),
			InlineKeyboardButton(text="Qulupnay 👍",callback_data="qulupnay")
		],
		[
			InlineKeyboardButton(text="Choko 👍",callback_data="choko")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
		],
	],
)

dissert_asal = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_20"),
		],
	],
)

dissert_qulupnay = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_20"),
		],
	],
)

dissert_choko = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_20"),
		],
	],
)

pizzalar_menusi = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Peperoni 👍",callback_data="peperonlik"),
			InlineKeyboardButton(text="Ananaslik 👍",callback_data="ananaslik")
		],
		[
			InlineKeyboardButton(text="Margaritta 👍",callback_data="margaritta")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga")
		],
	],
)


peperoni = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_21"),
		],
	],
)

ananaslik = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_21"),
		],
	],
)

margaritto = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="1️⃣",callback_data="number"),
			InlineKeyboardButton(text="2️⃣",callback_data="number"),
			InlineKeyboardButton(text="3️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="4️⃣",callback_data="number"),
			InlineKeyboardButton(text="5️⃣",callback_data="number"),
			InlineKeyboardButton(text="6️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="7️⃣",callback_data="number"),
			InlineKeyboardButton(text="8️⃣",callback_data="number"),
			InlineKeyboardButton(text="9️⃣",callback_data="number")
		],
		[
			InlineKeyboardButton(text="⬅️Ortga",callback_data="ortga_21"),
		],
	],
)