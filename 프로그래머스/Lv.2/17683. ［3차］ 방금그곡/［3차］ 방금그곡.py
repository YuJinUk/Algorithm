from collections import deque
def solution(m, musicinfos):
    answer = ''
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    running_time = 0
    for mu in musicinfos:
        s, e, title, note = mu.split(',')
        note = note.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        s, e = list(map(int, s.split(':'))), list(map(int, e.split(':')))
        time = (e[0] - s[0]) * 60 + (e[1] - s[1])
        mok, mod = divmod(time, len(note))
        new_note = note * mok + note[:mod]
        if m in new_note and running_time < time:
            answer = title
            running_time = time
    return answer if len(answer) else '(None)'