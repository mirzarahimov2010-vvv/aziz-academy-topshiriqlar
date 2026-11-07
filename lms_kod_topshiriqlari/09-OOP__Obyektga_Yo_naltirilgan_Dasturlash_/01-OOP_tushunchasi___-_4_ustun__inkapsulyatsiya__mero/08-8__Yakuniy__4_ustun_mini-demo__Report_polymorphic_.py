class BaseReport:
    def __init__(self, title):
        self._title = title
        self._lines = []
    def add_line(self, line):
        self._lines.append(line)
    def render(self):
        raise NotImplementedError       
class TextReport(BaseReport):
    def render(self):
        return "\n".join([f"TITLE={self._title}"] + self._lines)
class JsonReport(BaseReport):
    def render(self):
        return '{"title":"'+self._title +'","lines":'+ str(len(self._lines)) + "}"
try:
    kind = input().strip()
    title = input().strip()
    n = int(input().strip())
    if kind not in("TXT","JSON") or not title or n < 0:
        print("BAD")
    else:
        rep = TextReport(title) if kind == "TXT" else JsonReport(title)
        ok = True
        for _ in range(n):
            line = input().strip()
            if not line:
                ok = False
                break
            rep.add_line(line)
        print(rep.render() if ok else "BAD")
except ValueError:
    print("BAD")