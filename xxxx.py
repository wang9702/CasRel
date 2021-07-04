import os
from pathlib import Path

if __name__ == '__main__':

    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.dirname(__file__)))
    print(os.path.relpath(__file__))
    print(Path(os.path.abspath(os.path.dirname(__file__))))
    root = os.path.dirname(os.path.dirname(__file__))
    checkpoint_dir = root + '/checkpoint/'+'data'
    if not os.path.exists(checkpoint_dir):
        os.mkdir(checkpoint_dir)