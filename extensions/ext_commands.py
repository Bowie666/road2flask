import click

from flask import Flask

'''
进入app.py同级目录 直接运行flask same-text
然后按条件输入
'''
@click.command("same-text", help="judge same text.")
@click.option("--user", prompt=True, help="Who")
@click.option("--text1", prompt=True, help="First text")
@click.option("--text2", prompt=True, help="Second text")
def reset_txt(user, text1, text2):
    if str(text1).strip() != str(text2).strip():
        click.echo(click.style("Text do not match.", fg="red"))
        return

    print(f"User is {user}")
    # 如果需要 db 直接导包 我还没试 应该差不多
    # from extensions.ext_db import db
    # account = db.session.query(Account).filter(Account.email == email).one_or_none()

    click.echo(click.style("Text same successfully.", fg="green"))


def init_app(app: Flask):
    cmds_to_register = [
        reset_txt,
    ]
    for cmd in cmds_to_register:
        app.cli.add_command(cmd)
