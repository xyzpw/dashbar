import dashbar
import time
import shutil

def showcase():
    dashTypes: list = [d for d in dashbar.all_bars]
    dashbarLength = int(shutil.get_terminal_size().columns * 0.75)
    print()
    for dash in dashTypes:
        if dash == "custom":
            continue
        steps =  dashbarLength - len(str(dash))
        for i in dashbar.dash(steps=steps, dash_type=dash, desc=dash):
            time.sleep(1.5/dashbarLength)
        if dashTypes.index(str(dash)) != len(dashTypes) - 1:
            print()

if __name__ == "__main__":
    showcase()
