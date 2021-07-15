# Copyright (c) 2021 Charles F. (charlesbullsd)
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from argparse import ArgumentParser

import eyed3

def ms_to_hhmm(ms):

    s = ms / 1000

    m = int(s / 60)
    s = int(s % 60)

    return f"{m:02}:{s:02}"

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('file', help="MP3 file to dump")
    args = parser.parse_args()

    mp3 = eyed3.load(args.file)

    chap_eid = [chap.element_id for chap in mp3.tag.chapters]

    for cid in chap_eid:
        chap = mp3.tag.chapters.get(cid)
        start = ms_to_hhmm(chap.times.start)
        end = ms_to_hhmm(chap.times.end)
        print(f"[{start} {end}] - {chap.title}")
