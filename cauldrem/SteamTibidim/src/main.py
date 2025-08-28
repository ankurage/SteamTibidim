import json
import flet as ft
import datetime
import os
import random

class DataBase:
    def __init__(self):
        pass

    def create():
        with open("db.json", "w") as file:
            json.dump({}, file, indent=4, ensure_ascii=False)

    def get():
        try:
            with open("db.json", "r") as file:
                data = json.load(file)
            return data
            
        except json.decoder.JSONDecodeError:
            with open("db.json", "w") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)
        return data

    def load(setter):
        with open("db.json", "w") as file:
            json.dump(setter, file, indent=4, ensure_ascii=False)

    def create_cache():
        with open("cache.json", "w") as file:
            json.dump({}, file, indent=4, ensure_ascii=False)

    def get_cache():
        try:
            with open("cache.json", "r") as file:
                data = json.load(file)
            return data
            
        except json.decoder.JSONDecodeError:
            with open("cache.json", "w") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)
        return data
    
    def load_cache(setter):
        with open("cache.json", "w") as file:
            json.dump(setter, file, indent=4, ensure_ascii=False)

    def create_skins():
        with open("skins.json", "w") as file:
            json.dump({}, file, indent=4, ensure_ascii=False)

    def get_skins():
        try:
            with open("skins.json", "r") as file:
                data = json.load(file)
            return data
            
        except json.decoder.JSONDecodeError:
            with open("skins.json", "w") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)
        return data
    
    def load_skins(setter):
        with open("skins.json", "w") as file:
            json.dump(setter, file, indent=4, ensure_ascii=False)

class Main:
    def __init__(self, page: ft.Page):
        self.name = None

        self.page = page
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.title = "SteamTibidim"
        self.page.bgcolor = ft.Colors.ON_SECONDARY
        self.page.window.min_width = 400
        self.page.window.min_height = 500

        self.name_field = ft.TextField(label="Введите имя", border_color="grey900", cursor_color="blue", focused_border_color="grey900", fill_color=ft.Colors.ON_INVERSE_SURFACE)
        self.password_field = ft.TextField(label="Введите пароль", password=True, can_reveal_password=True, border_color="grey900", cursor_color="blue", focused_border_color="grey900", fill_color=ft.Colors.ON_INVERSE_SURFACE)
        self.password_field_repeat = ft.TextField(label="Повторите пароль", password=True, can_reveal_password=True, border_color="grey900", cursor_color="blue", focused_border_color="grey900", fill_color=ft.Colors.ON_INVERSE_SURFACE)

        self.reg_btn = ft.TextButton("Зарегестрироваться", on_click=self.regestration_validate)
        self.auth_btn = ft.TextButton("Войти", on_click=self.auth_validate)
        
        self.go_accs_btn = ft.IconButton(ft.Icons.ARROW_BACK, on_click=self.navigate_accs, icon_color="white")
        self.leave_acc_btn = ft.IconButton(ft.Icons.LOGOUT, icon_color="blue900")

        self.add_skin_btn = ft.IconButton(ft.Icons.ADD, on_click=self.return_users_skins, icon_color="white")

        self.user_skins_add = ft.Row(scroll=ft.ScrollMode.AUTO, tight=True, wrap=True)

        self.discard_buy_skin_btn = ft.TextButton("Отменить", on_click=lambda e: self.page.close(self.buy_skin_dlg))

        self.log_out_btn = ft.IconButton(ft.Icons.LOGOUT, on_click=self.log_out)

        self.change_avatar_btn = ft.TextButton("Поменять аватар на случайный", on_click=self.change_avatar)
        
        self.add_skins_user = {
            "ak1": ft.Container(
                    content=ft.Image(
                        src="skins/ak1.webp",
                        tooltip=f"ak1"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/ak1.webp", name="ak1": self.add_user_skin(e, indef, name)
                ),
                
            "awp1": ft.Container(
                    content=ft.Image(
                        src="skins/awp1.webp",
                        tooltip=f"awp1"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/awp1.webp", name="awp1": self.add_user_skin(e, indef, name)
                ),
            "glock1": ft.Container(
                    content=ft.Image(
                        src="skins/glock1.webp",
                        tooltip=f"glock1"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/glock1.webp", name="glock1": self.add_user_skin(e, indef, name)
                ),
            "m41": ft.Container(
                    content=ft.Image(
                        src="skins/m41.webp",
                        tooltip=f"m41"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/m41.webp", name="m41": self.add_user_skin(e, indef, name)
                ),
            "usp1": ft.Container(
                    content=ft.Image(
                        src="skins/usp1.webp",
                        tooltip=f"usp1"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/usp1.webp", name="usp1": self.add_user_skin(e, indef, name)
                ),
            "xm1": ft.Container(
                    content=ft.Image(
                        src="skins/xm1.webp",
                        tooltip=f"xm1"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, indef="skins/xm1.webp", name="xm1": self.add_user_skin(e, indef, name)
                ),
        }

        self.add_balance_user = ft.TextField(label="Пополнить баланс", on_submit=self.add_balance, suffix_icon=ft.IconButton("send", on_click=self.add_balance), border_color="grey900", cursor_color="blue", focused_border_color="grey900", fill_color=ft.Colors.ON_INVERSE_SURFACE)
        self.panel_navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    label="Рынок",
                    icon=ft.Icons.CARD_TRAVEL,
                ),

                ft.NavigationBarDestination(
                    label="Профиль",
                    icon=ft.Icons.PERSON
                ),

                ft.NavigationBarDestination(
                    label="Инвентарь",
                    icon=ft.Icons.INVENTORY
                )
            ], on_change=self.navigation, bgcolor="grey900", indicator_color="grey700", selected_index=1
        )

        # self.panel_inventory_build = ft.Column(wrap=True, auto_scroll=True, tight=True)
        self.panel_skins = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            wrap=True
        )

        self.page.add(self.panel_accs())

    def change_avatar(self, e):
        self.page.clean()
        avatars = ["avatar.png", "default.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png", "11.png", "12.png", "13.png", "14.png"]
        data = DataBase.get()
        cache = DataBase.get_cache()
        for i in cache:
            name = cache[i]["name"]
        data[name]["avatar"] = random.choice(avatars)
        cache[name]["avatar"] = data[name]["avatar"]

        DataBase.load(data)
        DataBase.load_cache(cache)

        self.page.add(self.panel_profile())
        self.page.update()
    
    def log_out(self, e):
        self.page.navigation_bar = None
        self.page.clean()
        self.page.add(self.panel_accs())
        self.page.update()

    def buy_skin_to_user(self, e, idi):
        cache = DataBase.get_cache()
        data = DataBase.get()
        skins = DataBase.get_skins()
        for i in cache:
            name = cache[i]["name"]

        if data[name]["balance"] >= skins[idi]["cost"]:
            
            data[name]["balance"] -= skins[idi]["cost"]
            data[name]["inventory"].append(
                {
                    "name": skins[idi]["name"],
                    "src": skins[idi]["src"]
                }
            )
            del skins[idi]
            DataBase.load(data)
            DataBase.load_skins(skins)
            self.page.open(ft.SnackBar(ft.Text("Вы успешно купили скин")))
            self.page.close(self.buy_skin_dlg)
        else:
            self.page.open(ft.SnackBar(ft.Text("У вас не достаточно средств")))
            self.page.close(self.buy_skin_dlg)
        self.page.update()


    def add_balance(self, e):
        self.page.clean()
        cache = DataBase.get_cache()
        data = DataBase.get()
        for i in cache:
            name = cache[i]["name"]
        
        data[name]["balance"] += int(self.add_balance_user.value)
        self.add_balance_user.value = ""
        DataBase.load(data)
        self.page.add(self.panel_profile())
        self.page.update()

    def add_user_skin(self, e, skin, skin_name):
        cache = DataBase.get_cache()
        data = DataBase.get()
        skins = DataBase.get_skins()
        for i in cache:
            name = cache[i]["name"]
        
        data[name]["inventory"].append(
            {
                "name": skin_name,
                "src": skin
            }
        )

        DataBase.load(data)
        
    def buy_skin(self, e, idi):
        cache = DataBase.get_cache()
        data = DataBase.get()
        skins = DataBase.get_skins()
        for i in cache:
            name = cache[i]["name"]
            break
        self.buy_skin_btn = ft.TextButton("Купить", on_click=lambda e, idi=idi: self.buy_skin_to_user(e, idi))

        self.buy_skin_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Название: {skins[idi]['name']}\nЦена: {skins[idi]['cost']}\nПродавец: {skins[idi]['seller']}"),
            content=ft.Row(
                [
                    self.buy_skin_btn,
                    self.discard_buy_skin_btn
                ]
            )
        )

        self.page.open(self.buy_skin_dlg)


    def shop_skins(self):
        data = DataBase.get_skins()

        self.shop_skins_list = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            wrap=True
        )

        for i in data:
            self.shop_skins_list.controls.append(
                ft.Container(
                    content=ft.Image(
                        src=data[i]["src"],
                        tooltip=f"{data[i]['name']} - {data[i]['cost']}"
                    ),
                    width=100,
                    height=100,
                    animate_opacity=9000,
                    border=ft.border.all(5, "grey900"),
                    bgcolor="grey700",
                    on_click=lambda e, idi=i: self.buy_skin(e, idi)
                )
            )
        
        self.page.add(self.shop_skins_list)

    def sell_skin(self, e, idi):
        data = DataBase.get()
        user_name = DataBase.get_cache()

        skins_data = DataBase.get_skins()

        name = None
        for i in user_name:
            name = user_name[i]["name"]
        if self.skin_sell_amount.value:
            self.page.close(self.sell_skin_dlg)
            ider = len(skins_data)

            skins_data[ider] = {
                "seller": name,
                "name": data[name]["inventory"][idi]["name"],
                "src": data[name]["inventory"][idi]["src"],
                "cost": int(self.skin_sell_amount.value)
            }

            data[name]["inventory"].pop(idi)
            DataBase.load_skins(skins_data)
            DataBase.load(data)
        else:
            self.page.open(ft.SnackBar(ft.Text("Заполните все поля ввода")))
        

    def return_users_skins(self, e):
        cache = DataBase.get_cache()
        for i in cache:
            user_name = cache[i]["name"]
            break

        self.user_skins_add = ft.Row(scroll=ft.ScrollMode.AUTO, tight=True, wrap=True)
        data = DataBase.get()
        if data[user_name]["inventory"]:
            for i in range(len(data[user_name]["inventory"])):
                self.user_skins_add.controls.append(
                    ft.Container(
                        content=ft.Image(
                            src=data[user_name]["inventory"][i]["src"],
                            tooltip=data[user_name]["inventory"][i]["name"]
                        ),
                        width=100,
                        height=100,
                        animate_opacity=9000,
                        border=ft.border.all(5, "grey900"),
                        bgcolor="grey700",
                        on_click=lambda e, idi=i: self.add_skin(e, idi)
                )
                )
            else:
                self.add_skin_dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Выберите скин для продажи"),
                    content=self.user_skins_add
                )

                self.page.open(self.add_skin_dlg)
        else:
            self.page.open(ft.SnackBar(ft.Text("У вас нету скинов")))

    def add_skin(self, e, id):
        # self.page.close(self.add_skin_dlg)

        # data = DataBase.get()
        # user_name = DataBase.get_cache()
        # name = None
        # for i in user_name:
        #     name = user_name[i]["name"]
        self.skin_sell_amount = ft.TextField(label="Введите сумму скина", on_submit=lambda e, idi=id: self.sell_skin(e, idi), autofocus=True, suffix_icon=ft.IconButton("send", on_click=lambda e, idi=id: self.sell_skin(e, idi)),border_color="grey900", cursor_color="blue", focused_border_color="grey900", fill_color=ft.Colors.ON_INVERSE_SURFACE)

        self.sell_skin_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Введи сумму продажи скина"),
                content=self.skin_sell_amount
            )
        
        self.page.open(self.sell_skin_dlg)

    def return_skins(self):
        cache = DataBase.get_cache()
        name = None
        for i in cache:
            name = cache[i]["name"]
            break

        self.panel_skins.controls.clear()
        data = DataBase.get()

        if data[name]["inventory"]:
            for i in range(len(data[name]["inventory"])):
                self.panel_skins.controls.append(
                    ft.Container(
                        content=ft.Image(
                            src=data[name]["inventory"][i]["src"],
                            tooltip=data[name]["inventory"][i]["name"]
                        ),
                        width=100,
                        height=100,
                        animate_opacity=9000,
                        border=ft.border.all(5, "grey900"),
                        bgcolor="grey700",
                        # on_click=lambda e, idi=i: self.add_skin(e, idi)
                )
                )
        
        self.panel_inventory = ft.Column(
                [
                    ft.Text("Инвентарь: "),
                    ft.Divider(),
                    self.panel_skins
                ]
            )
        
        return self.panel_skins

    def panel_profile(self):
        self.page.navigation_bar = self.panel_navigation_bar

        data = DataBase.get()

        return ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Column([
                                    self.get_account(), 
                                    ft.Row([ft.Text(self.name, weight="bold"), self.log_out_btn]),
                                    ft.Text(f"Баланс: {data[self.name]['balance']}", weight="bold")
                                ]
                                )
                            )
                        ]
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20)
                ),
                # self.return_skins()
                ft.Row(
                    [
                        self.add_skins_user["ak1"],
                        self.add_skins_user["awp1"],
                        self.add_skins_user["glock1"],
                        self.add_skins_user["m41"],
                        self.add_skins_user["usp1"],
                        self.add_skins_user["xm1"]
                    ], scroll=ft.ScrollMode.AUTO, expand=True, wrap=True
                ),
                self.add_balance_user,
                self.change_avatar_btn
            ]
        )
    
    def panel_shop(self):
        return ft.Column(
            [
                ft.Container(
                    content=self.add_skin_btn,
                    alignment=ft.alignment.top_left
                )
            ]
        )
    
    def navigation(self, e):
        index = e.control.selected_index
        self.page.clean()

        if index == 0:
            self.page.add(self.panel_shop())
            self.shop_skins()

        elif index == 1:
            self.page.add(self.panel_profile())
            # self.return_skins()

        elif index == 2:
            self.page.add(self.return_skins())
        
        self.page.update()
    
    def navigation_profile(self, e):
        self.page.clean()
        self.page.add(self.panel_profile())
        self.page.update()

# === РЕГИСТРАЦИЯ === #
    def clear_error_accs(self):
        self.password_field.border_color = ft.Colors.GREY_900
        self.password_field_repeat.border_color = ft.Colors.GREY_900
        self.name_field.border_color = ft.Colors.GREY_900

        self.password_field.helper_text = None
        self.password_field_repeat.helper_text = None
        self.name_field.helper_text = None

        self.password_field.value = ""
        self.password_field_repeat.value = ""
        self.name_field.value = ""

        self.page.update()

    def regestration(self, e):
        name = self.name_field.value
        password = self.password_field.value
        password_rep = self.password_field_repeat.value
        created = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}"


        self.name = name
        data = DataBase.get()
        data_c = {}
        data[name] = {"name": name, "password": password, "balance": 0, "created": created, "inventory": [], "settings": {}, "admin": False, "banned": False, "avatar": "default.png"}
        data_c[name] = {"name": name, "avatar": "default.png"}

        DataBase.load(data)
        DataBase.load_cache(data_c)

        self.clear_error_accs()
        
        # self.page.clean()
        # self.page.add(self.panel_menu())

    def regestration_validate(self, e):
        name = self.name_field.value
        password = self.password_field.value
        password_rep = self.password_field_repeat.value

        data = DataBase.get()

        if name not in data:
            self.name_field.border_color = ft.Colors.GREY_900
            self.name_field.helper_text = None
            if name:
                self.name_field.border_color = ft.Colors.GREY_900

                if all([password, password_rep]) and len(password) > 3 and len(password_rep) > 3:
                    if password == password_rep:
                        self.regestration(e)
                    else:
                        self.password_field.border_color = ft.Colors.ON_ERROR
                        self.password_field_repeat.border_color = ft.Colors.ON_ERROR
                        self.password_field.helper_text = "Пароли не совподают"
                        self.password_field_repeat.helper_text = None

                else:
                    self.password_field.border_color = ft.Colors.ON_ERROR
                    self.password_field_repeat.border_color = ft.Colors.ON_ERROR
                    self.password_field.helper_text = "В пароле должно быть не менее 4 символов"
                    self.password_field_repeat.helper_text = "В пароле должно быть не менее 4 символов"

            else:
                self.name_field.border_color = ft.Colors.ON_ERROR
        else:
            self.name_field.border_color = ft.Colors.ON_ERROR
            self.name_field.helper_text = "Такой аккаунт уже существует"
        self.page.update()

    def auth(self, e):
        name = self.name_field.value
        password = self.password_field.value
        created = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
        self.name = name
        data = DataBase.get()
        data_c = {}
        data_c[name] = {"name": name, "avatar": data[name]["avatar"]}

        DataBase.load_cache(data_c)

        self.clear_error_accs()
        
        # self.page.clean()
        # self.page.add(self.panel_menu())

    def auth_validate(self, e):
        name = self.name_field.value
        password = self.password_field.value

        data = DataBase.get()

        if name in data:
            self.name_field.border_color = ft.Colors.GREY_900
            self.name_field.helper_text = None

            if name:
                self.name_field.border_color = ft.Colors.GREY_900

                if password and len(password) > 3:
                    if password == data[name]["password"]:
                        self.auth(e)
                    else:
                        self.password_field.border_color = ft.Colors.ON_ERROR
                        self.password_field.helper_text = "Пароли не совподают"

                else:
                    self.password_field.border_color = ft.Colors.ON_ERROR
                    self.password_field.helper_text = "В пароле должно быть не менее 4 символов"

            else:
                self.name_field.border_color = ft.Colors.ON_ERROR
        else:
            self.name_field.border_color = ft.Colors.ON_ERROR
            self.name_field.helper_text = "Такого аккаунт не существует"
        self.page.update()

    def navigate_accs(self, e):
        self.page.clean()
        self.clear_error_accs()
        self.page.add(self.panel_accs())

    def navigate_auth(self, e):
        self.page.clean()
        self.clear_error_accs()
        self.page.add(self.panel_auth())

    def navigate_reg(self, e):
        self.page.clean()
        self.clear_error_accs()
        
        self.page.add(self.panel_reg())
    
    def get_account(self):
        data = DataBase.get()
        cache = DataBase.get_cache()
        
        if cache:
                for i in cache:
                    self.name = cache[i]["name"]
                    return ft.Container(content=ft.Container(width=100, on_click=self.navigation_profile, height=100, content=ft.Image(src=cache[i]["avatar"]), border=ft.border.all(5, "grey900"), tooltip=cache[i]["name"], animate_opacity=9000), alignment=ft.alignment.center)
        else:
            return ft.Container(content=ft.IconButton("add", icon_size=50, icon_color="grey", on_click=self.navigate_reg), alignment=ft.alignment.center)

    def panel_auth(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=self.go_accs_btn,
                        alignment=ft.alignment.top_left
                    ),
                    
                    ft.Container(
                        content=ft.Text("Вход", weight=ft.FontWeight.BOLD, size=50),
                        margin=ft.Margin(bottom=100, top=0, left=0, right=0),
                        alignment=ft.alignment.center
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=self.name_field
                                ),
                                ft.Container(
                                    content=self.password_field
                                ),
                                self.auth_btn
                            ]
                        )
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.TextButton("Создать аккаунт", on_click=self.navigate_reg, style=ft.ButtonStyle(color="blue", bgcolor=ft.Colors.ON_INVERSE_SURFACE)),
                    )
                ]
            ),
            # alignment=ft.alignment.center,
            # margin=ft.Margin(bottom=100, top=0, left=0, right=0)
        )

    def panel_reg(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=self.go_accs_btn,
                        alignment=ft.alignment.top_left
                    ),
                    
                    ft.Container(
                        content=ft.Text("Регестрация", weight=ft.FontWeight.BOLD, size=50),
                        margin=ft.Margin(bottom=100, top=0, left=0, right=0),
                        alignment=ft.alignment.center
                    ),

                    ft.Container(
                        ft.Container(
                            width=100,
                            height=100,
                            content=ft.Image(src="default.png"),
                            border=ft.border.all(5, "grey900"),
                            tooltip="Выбрать аватар",
                            animate_opacity=9000,
                        ),
                        # margin=ft.Margin(bottom=0, top=0, left=19, right=0),
                        alignment=ft.alignment.center
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=self.name_field
                                ),
                                ft.Container(
                                    content=self.password_field
                                ),
                                ft.Container(
                                    content=self.password_field_repeat
                                ),
                                self.reg_btn
                            ]
                        )
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.TextButton("Войти в аккаунт", on_click=self.navigate_auth, style=ft.ButtonStyle(color="blue", bgcolor=ft.Colors.ON_INVERSE_SURFACE)),
                    )
                ]
            ),
            # alignment=ft.alignment.center,
            # margin=ft.Margin(bottom=100, top=0, left=0, right=0)
        )
    
    def panel_accs(self):
        img = "avatar.png"
        return ft.Container(
            content=ft.Column(
                [
                    
                    ft.Container(
                        content=ft.Text("Вход", weight=ft.FontWeight.BOLD, size=50),
                        margin=ft.Margin(bottom=100, top=0, left=0, right=0),
                        alignment=ft.alignment.center
                    ),

                    self.get_account(),

                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.TextButton("Войти в аккаунт",  on_click=self.navigate_auth, style=ft.ButtonStyle(color="blue", bgcolor=ft.Colors.ON_INVERSE_SURFACE))
                    )
                ]
            ),
            # alignment=ft.alignment.center,
            # margin=ft.Margin(bottom=100, top=0, left=0, right=0)
        )

def start(page: ft.Page):
    if not os.path.exists("db.json"):
        DataBase.create()
    if not os.path.exists("cache.json"):
        DataBase.create_cache()
    if not os.path.exists("skins.json"):
        DataBase.create_skins()
        DataBase.load_skins(
        {
        # "0": {
        #     "name": "ak1",
        #     "src": "skins/ak1.webp",
        #     "cost": 3000
        # },
        # "1": {
        #         "name": "awp1",
        #     "src": "skins/awp1.webp",
        #     "cost": 2500
        # },
        # "2": {
        #     "name": "glock1",
        #     "src": "skins/glock1.webp",
        #     "cost": 250
        # },
        # "3": {
        #     "name": "m41",
        #     "src": "skins/m41.webp",
        #     "cost": 500
        # },
        # "4": {
        #     "name": "usp1",
        #     "src": "skins/usp1.webp",
        #     "cost": 150
        # },
        # "5": {
        #     "name": "xm1",
        #     "src": "skins/xm1.webp",
        #     "cost": 10
        # }
    }
)
    app = Main(page)

ft.app(target=start, assets_dir="assets")
