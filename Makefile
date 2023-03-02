APP_URL=https://www.baidu.com
AIDOUER_URL=https://www.baidu.com
HZZ_URL=https://www.baidu.com

cover:
	@python cover_env.py --app_url=$(APP_URL) --aider_url=$(AIDOUER_URL) --hzz_url=$(HZZ_URL)

build: cover
	pyinstaller -F -w movie.py