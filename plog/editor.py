import os
import subprocess
import tempfile

_PROCESS_WAIT_FLAG = "-w"

_FILE_HEADER = """

"""


def from_editor() -> str:
    editor = os.environ.get('EDITOR', 'code')
    initial_message = b'Hello world!'
    with tempfile.NamedTemporaryFile(suffix='.tmp') as tf:
        tf.write(initial_message)
        tf.flush()
        subprocess.Popen([editor, _PROCESS_WAIT_FLAG, tf.name]).wait()

        tf.seek(0)
        return str(tf.read())
