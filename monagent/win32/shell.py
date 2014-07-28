import traceback


def shell():
    from config import get_version

    print("""
Datadog Agent v%s - Python Shell

    """ % (get_version()))
    while True:
        cmd = raw_input('>>> ')
        try:
            exec(cmd)
        except Exception as e:
            print(traceback.format_exc(e))

if __name__ == "__main__":
    shell()
