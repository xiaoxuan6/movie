import argparse
import os
from shutil import copyfile


def writer(**kwargs):
    envPath = r"{}/{}".format(os.getcwd(), '.env')
    if not os.path.exists(envPath):
        copyfile(r"{}/{}".format(os.getcwd(), '.env.example'), envPath)

    with open(envPath, encoding='utf-8', mode='w') as f:
        for key, val in kwargs.items():
            f.write("{}={}\n".format(key, val))


if __name__ == '__main__':
    parse = argparse.ArgumentParser('环境变量')
    parse.add_argument('--app_url', type=str, default=None)
    parse.add_argument('--aider_url', type=str, default=None)
    parse.add_argument('--hzz_url', type=str, default=None)
    args = parse.parse_args()

    writer(APP_URL=args.app_url, AIDOUER_URL=args.aider_url, HZZ_URL=args.hzz_url)
