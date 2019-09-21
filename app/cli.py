import os
import click

def register(app):
    @app.cli.group()
    def translate():
        """Translation and localisation commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialise a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel init -i message.pot -d app/translations -l ' + lang):
            raise RuntimeError('extract command failed')
        os.remove('messages.pot')

    @translate.command() 
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed') 
        os.remove('messages.pot')

    @translate.command() 
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')
