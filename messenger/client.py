# import requests
#
# server = 'http://127.0.0.1:8000/api'
#
# print('\n\n1) Login\n2)Registr\n\n')
#
# method = str(input('Выберите действие > '))
#
# if method.lower() == 'registr':
#     email = str(input('Введите  email > '))
#     params = {'method': 'registr', 'email': email}
#     code = requests.get(server, params=params).json()
#     check_code = int(input('Введите код подтверждения > '))
#     if code['code'] == check_code:
#         password = str(input('Придумайте пароль > '))
#         first_name = str(input('Ваше имя > '))
#         last_name = str(input('Ваша фамилия > '))
#         params = {'method': 'confirm',
#                   'response': 'done',
#                   'email': email,
#                   'pass': password,
#                   'first_name': first_name,
#                   'last_name': last_name}
#         requests.get(server, params=params)
#     else:
#         print('код не верный!')
#
# elif method.lower() == 'login':
#     email = str(input('Введите  email > '))
#     password = str(input('Введите пароль > '))
#     params = {'method': 'login',
#               'email': email,
#               'pass': password}
#     check_login = requests.get(server, params=params).json()
#     if check_login['response'] == '200':
#         print('Успешно')
#     elif 'error' in str(check_login):
#         print('Пользователь не найдет либо пароль не верный')
# else:
#     print('down')
