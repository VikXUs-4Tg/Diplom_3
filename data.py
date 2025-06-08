WEBPAGE= 'https://stellarburgers.nomoreparties.site'

const = {
'WAIT_TIMER' : 10,
'COUNTER_ALL_TIME_ORDERS_DEAL' : 'Выполнено за все время:',
'COUNTER_TODAY_ORDERS_DEAL' : 'Выполнено за сегодня:',
# Константы, необходимые для работы с API:
'HANDLER_REGISTRATION_USER' : ('post', WEBPAGE + '/api/auth/register/'),
'HANDLER_AUTHORIZATION_USER' : ('post', WEBPAGE + '/api/auth/login/'),
'HANDLER_DELETE_USER' : ('delete', WEBPAGE + '/api/auth/user/'),
'HANDLER_GET_INGREDIENTS' : ('get', WEBPAGE + '/api/ingredients/'),
'USER_EMAIL_PARAMETER_NAME' : 'email',
'USER_PASSWORD_PARAMETER_NAME' : 'password',
'USER_NAME_PARAMETER_NAME' : 'name',
'USER_ACCESS_TOKEN_PARAMETER_NAME' : 'accessToken',
'USER_AUTHORIZATION_PARAMETER_NAME' : 'authorization',
}

results = {
'BUTTON_TO_RECOVERY_TEXT' : 'Восстановить',
'FIELD_TO_CHANGE_PASSWORD_TEXT' : 'Введите новый пароль',
'FIELD_WITH_OUT_HIDE_TYPE' : 'text',
'BUTTON_LOGIN_TEXT' : 'Войти',
'PERSONAL_ACCOUNT_TITLE_INFO_TEXT' : 'В этом разделе вы можете изменить свои персональные данные',
'CONSTRUCTOR_TITLE_INFO_TEXT' : 'Соберите бургер',
'ORDER_FEED_TITLE_INFO_TEXT' : 'Лента заказов',
'UNEXPECTED_COUNTER_VALUE' : 0,
'UNEXPECTED_IDENTIFIER_VALUE' : 9999,
}
