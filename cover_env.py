import argparse


def replace(**environments):
    for key, val in environments.items():
        target = r"https://{}".format(key)
        if key == "APP_URL" or key == 'AIDOUER_URL':
            coverViews(target, val)
        if key == 'HZZ_URL':
            coverHzz(target, val)


def coverViews(oldStr, newStr: str):
    with open('./views.py', mode='r', encoding='utf-8') as f:
        content = f.read().replace(oldStr, newStr)
        with open('./views.py', mode='w', encoding='utf-8') as fin:
            fin.write(content)


def coverHzz(oldStr, newStr: str):
    with open('./endpoint/hzz.py', mode='r', encoding='utf-8') as f:
        content = f.read().replace(oldStr, newStr)
        with open('./endpoint/hzz.py', mode='w', encoding='utf-8') as fin:
            fin.write(content)


if __name__ == '__main__':
    parse = argparse.ArgumentParser('环境变量')
    parse.add_argument('--app_url', type=str, default=None)
    parse.add_argument('--aider_url', type=str, default=None)
    parse.add_argument('--hzz_url', type=str, default=None)
    args = parse.parse_args()

    replace(APP_URL=args.app_url, AIDOUER_URL=args.aider_url, HZZ_URL=args.hzz_url)
