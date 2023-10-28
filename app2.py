import subprocess
import os
import sys

from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "stapp.py"]
    sys.exit(stcli.main())


