def write_mode(mode):
        with open("Windows_Mouse_Movments/vimmode.txt", "w") as f:
            f.truncate(0)
            f.write(mode)
        f.close()