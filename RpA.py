import pywinauto, time
from pywinauto import Application, keyboard
from pywinauto.keyboard import send_keys
app_path  = "C:\Program Files (x86)\WinSCP\WinSCP.exe"
#deschidere aplicatie
app = Application().start(cmd_line=u'' + app_path + '')

#asteptare aparitie fereastra
app.Window_(title_re='Login').Wait('visible', timeout=20, retry_interval=1)

#conectare cu fereastra de login
#app.connect(title="Login")
#app.TLoginDialog.print_control_identifiers()

#apasare enter pentru login
#keyboard.send_keys("{ENTER}")
#user_name = app.TLoginDialog.child_window(title="root", class_name="TEdit").wrapper.object()
#user_name.type_keys("sadasdsa")
app.TLoginDialog['Edit2: Edit'].set_text("root")

app.TLoginDialog.LoginButton.click()


#deschiedere aplicatie principala
app.Window_(title_re='Pitu*').Wait('visible', timeout=20, retry_interval=1)

#app.WinSCPTScpCommanderForm.MenuItem(u'&Local->&Change Drive').click()
#keyboard.send_keys('%{F1}')

