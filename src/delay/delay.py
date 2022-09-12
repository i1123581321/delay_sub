import subprocess
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("time", type=str)


def process():
    args = parser.parse_args()
    filename = args.filename
    time = args.time
    output = Path.cwd() / "output"
    output.mkdir()
    for f in Path.cwd().glob(filename):
        subprocess.run([
            "ffmpeg",
            "-itsoffset",
            time,
            "-i",
            str(f),
            "-c",
            "copy",
            str(output / f.name)
        ])
