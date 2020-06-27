from lifegraph.lifegraph import Lifegraph, Papersize
from datetime import date

if __name__ == '__main__':
    birthday = date(1990, 11, 1)
    g = Lifegraph(birthday, dpi=300, size=Papersize.A4, max_age=90)
    g.add_title("Time is Not Equal to Money")
    g.save("examples/images/grid_with_title.png")