from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.sesion import run_async, run_js

import asyncio

chat_msgs = []
online_users = set()

MAX_MESEGS_COUNT = 100

async def main():
    global chat_masgs

    put_markdown("## 🧊 добро пожаловать в онлайн чат!\nИсходный код данного чата укладывается в 100 строк!")

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_battom=True)

    nickname = await input("Войти в чат", requierd=True, placeholder="Ваше имя", validate=lambda n: "Tакой ник уже используется!" if n in online_users or n == '📢' else None)
    online_users.add(nikcname)

    chat_msgs.append(('📢', f"`{nickname}` присоеденился к чату!"))
    msg_box.append(put_markdown(f"`{nickname}` присоеденился к чату!"))

   refresh_task = run_async(refresh_msg(nikcname, msg_box))

   while True:
       data await input_group("💭 Новое сообщение",[
           input(placeholder="екст сообщения", name="msg"),
           actions(name="cmd", buttons=["Отправить", {'label':"Выйти из чата", 'type':'cansel'}])
       ], validate=lambda m: ('msg', "Введите текст сообщения") if m["cmd"] == "Отправить" and not m["msg"] else None)

       if data is None:
           break

       msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
       chat_msgs.append((nickname, data ['msg']))

   # exit chat
   refresh_task.close()

   online_users.remove(nickname)
   toast("Вы вышли из чата!")
   msg_box.append(putmarckdowon(f"📢 Пользователь `{nickname}`Покинул чат!"))
   chat_msgs.append(('📢', f"Пользователь `{nickname}`Покинул чат!"))

   put_buttons(["Перезайти"], onclick=lambda btn: run_js('window.location.reload('))

async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs

    while True:
        await asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:
                msg_box.append(put_markdown(f"`{m[0]}` : {m[1]}"))

        # remuve expered
        if len(chat_msgs > MAX_MESEGS_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

            last_idx = len(chat_msgs)

if __name__ "__main__"
    start_server(main, debag=True, port=8080, cdn=Fals)