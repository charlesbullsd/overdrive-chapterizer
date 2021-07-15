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
