import os
from datetime import datetime

def main():
    name = os.environ.get('INPUT_NAME')

    print(f'Hello, {name}! Welcome to continuous integration!')
    timestamp = datetime.now().isoformat()

    print(f'Welcome logged at: {timestamp}')
    print(f'::set-output name=timestamp::{timestamp}')

if __name__ == '__main__':
    main()