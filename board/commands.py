import click
from board import app, db
from board.models import Message


# 用于生成虚拟数据
# app.cli.command 自定义flask命令装饰器
# 在command line 输入 flask forge 即可触发
@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    # 生成虚拟数据前会删除重建数据库表
    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
