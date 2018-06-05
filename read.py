import click
import io
import random
import sys
import time
import pygame
from gtts import gTTS

def tts(text, slow=False):
    tts = gTTS(text=text, lang='zh-cn', slow=False)
    with io.BytesIO() as fp:
        tts.write_to_fp(fp)
        fp.seek(0)
        pygame.mixer.music.load(fp)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.set_allowed(pygame.USEREVENT)
        pygame.mixer.music.play()
        pygame.event.wait()


@click.command()
@click.argument('files', nargs=-1)
@click.option('--order/--no-order', default=False)
def main(files, order):
    pygame.mixer.init()
    pygame.init()
    words = []
    for f in files:
        with open(f, 'r') as fp:
            words.extend(fp.read().strip().split('\n'))
    if order:
        random.shuffle(words)
        for i, random_word in enumerate(words):
            x = ''
            while True:
                tts(random_word, slow=x == 's')
                x = input("Command[%u]> " % i)
                if x == 'n':
                    break
                if x == 'p':
                    print(random_word)
    else:
        random_word = random.choice(words)
        while True:
            x = input("Command> ")
            if x == 'n':
                random_word = random.choice(words)
            else:
                pass
            if x == 'p':
                print(random_word)
            tts(random_word, slow=x == 's')


if __name__ == "__main__":
    main()
