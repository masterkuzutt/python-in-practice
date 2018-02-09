import os
import sys
import tempfile 

# abstract factory    
def main():
    txt_file_name = os.path.join(tempfile.gettempdir(), "diagram.txt")
    svg_file_name = os.path.join(tempfile.gettempdir(), "diagram.svg")


    txt_diagram = create_diagram(DiagramFactory)
    txt_diagram.save(txt_file_name)
    print("wrote", txt_file_name)

    svg_diagram = create_diagram(SvgDiagramFactory)
    svg_diagram.save(svg_file_name)
    print("wrote", svg_file_name)


# factory method みたいななもの。
# こいつに渡すfactoryがさらにabstract facrtory ってことのなのでは。
# で、こいつにfactory以外の引数で、使うファクトリー決めて作るのが
# ホントの　factory method

def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5,"yellow" )
    text = factory.make_text(7, 3, "Abstract Factory")

    diagram.add(rectangle)
    diagram.add(text)
    return diagram 

# factory 
class DiagramFactory:
    
    @classmethod
    def make_diagram(cls, width, height):
        return cls.Diagram(width, height)

    @classmethod
    def make_rectangle(cls,x, y, width, height, fill="white", stroke="black"):
        return cls.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(cls, x, y, text, fontsize=12):
        return cls.Text(x, y, text, fontsize)

    BLANK = " "
    CORNER = "+"
    HORIZONTAL = "-"
    VERTICAL = "|"
    

    class Diagram(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.diagram = DiagramFactory._create_rectangle(self.width, self.height, DiagramFactory.BLANK)

        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x ] = char

        def save(self, filenameOrFile):
            file = (None if isinstance(filenameOrFile, str) else filenameOrFile)

            try:
                if file is None:
                    file = open(filenameOrFile, "w", encoding="utf-8")
                for row in self.diagram:
                    print("".join(row), file=file)
            finally:
                if isinstance(filenameOrFile, str) and file is not None:
                    file.close()


    class Rectangle(object):
        def __init__(self, x, y, width, height, fill, stroke):
            self.x = x 
            self.y = y 
            self.rows = DiagramFactory._create_rectangle(width,height, DiagramFactory.BLANK if fill == "white" else "%")
    

    class Text(object):
        def __init__(self, x, y, text, fontsize):
            self.x = x 
            self.y = y
            self.rows = [list(text)]

    @staticmethod
    def _create_rectangle(width, height, fill):
        rows = [[fill for _ in range(width)] for _ in range(height)]
        for x in range(1,width - 1 ):
            rows[0][x] = DiagramFactory.HORIZONTAL
            rows[height -1 ][x] = DiagramFactory.HORIZONTAL
        for y in range(1, height - 1):
            rows[y][0] = DiagramFactory.VERTICAL
            rows[y][width -1] = DiagramFactory.VERTICAL
        for y, x in ( (0,0), (0, width -1), (height - 1,0),(height -1, width -1)):
            rows[y][x] = DiagramFactory.CORNER
        return rows



class SvgDiagramFactory(DiagramFactory):
    SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""

    SVG_END = "</svg>\n"

    SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" stroke="{stroke}"/>"""

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20

    class Diagram(object):
        def __init__(self, width, height):
            pxwidth = width * SvgDiagramFactory.SVG_SCALE
            pxheight = height * SvgDiagramFactory.SVG_SCALE
            self.diagram = [SvgDiagramFactory.SVG_START.format(**locals())]
            outline = SvgDiagramFactory.Rectangle(0, 0, width, height, "lightgreen", "black")
            self.diagram.append(outline.svg)
    
        def add(self, component):
            self.diagram.append(component.svg)

        def save(self, filenameOrFile):
            file = (None if isinstance (filenameOrFile,str) else filenameOrFile)

            try:
                if file is None:
                    file = open(filenameOrFile, "w", encoding="utf-8")
                file.write("\n".join(self.diagram))
                file.write("\n" + SvgDiagramFactory.SVG_END)
                
            finally:
                if isinstance(filenameOrFile, str) and file is not None:
                    file.close()

    class Rectangle(object):
        def __init__(self, x, y, width, height, fill, stroke):
            super().__init__()

    class Text(object):
        def __init__(self, x, y, text, fontsize):
            super().__init__()


            
if __name__ == '__main__':
    main()