import locale
# from .views.index import language

class Links():
        mainpage = {
        	'ru':  {
            'lan': 'Русский',
            'about': 'О нас',
            'doc': 'Документация',
            'contacts': 'Контакты',
            'phrase': 'Пройденный путь и есть награда',
            'start': 'Начать использование',
			'start_mobile': 'Начать',
			'chronology': 'Хронология',
        	},

	        'en': {
	            'lan': 'English',
	            'about': 'About us',
	            'doc': 'Documentation',
	            'contacts': 'Contacts',
	            'phrase': 'The path traveled is the reward',
	            'start': 'Start using',
				'start_mobile': 'Start',
				'chronology': 'Chronology',
      	  	}
        }
        start_page = {
        	'ru': {
        		'title': "MapDial. Начало работы"
        	},
        	'en':{
        		'title': 'MapDial. Beginning of work'
        	}
        }
        about = {
        	'ru': {
        		'title': 'О нас'
        	},
        	'en': {
        		'title': 'About us'
        	}
        }
        chronology = {
			'ru': {
				'title': 'Хронология'
			},
			'en': {
				'title': 'Chronology',
				'error_with_language': 'The chronology of events is written exclusively in Russian. We apologize for these inconveniences.'
			}
		}

lan = 'en'

lanlist = [('en','English'), ('ru', 'Русский')]

print(locale.getdefaultlocale())

# if language:
# 	lan = language
# else:
# 	if locale.getdefaultlocale()[0] == 'ru_RU':
# 	    lan = 'ru'
# 	else:
# 	    lan = 'en'

if locale.getdefaultlocale()[0] == 'ru_RU':
	lan = 'ru'
else:
    lan = 'en'