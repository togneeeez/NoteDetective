class Window():
    def __init__ (self, window_name):
        self.w_name = window_name

    def title(self, width, height, text):
        o_str = " "

        for i in range(width):
            o_str += "—"
        print (o_str)

        o_str = ""

        k = 0

        for i in range(height):
            o_str = "|"
            for j in range(width):
                if (k < len(text) and i == height//2):
                    if (j < (width//2 - len(text)//2)) or (j > (width//2 + len(text)//2)):
                        o_str += " "
                    else:
                        o_str += text[k]
                        k += 1
                else:
                    o_str += " "
            print(o_str + "|")

        o_str = " "
        
        for i in range(width):
            o_str += "—"
        print (o_str + "\n")

    def option(self, width, text):
        o_str = "| "
        k = 0
        for i in range(width):
            if k < len(text):
                o_str += text[k]
                k += 1
        print(o_str)