import time, pyautogui, os

# # INI
cyc = 0
print("===========================================================\n"
      "======== Railnation Auto-Werbe-Clicker Version 2.1 ========\n"
      "===========================================================\n")
input("ENTER drücken ...")
while True:
    maxc = int(input("ZYKLEN: "))
    print(" ")
    if maxc == 0: maxc = 999999
    # # SEARCH FOR VIDEO BUTTON
    while True:
        print(f"starte [{cyc + 1}]")
        time.sleep(2)
        if cyc >= maxc:
            print("\nERROR: Angegebene Zyklen erreicht.")
            while True:
                a = input("Programm schließen? (y/n): ")
                if a == "y": exit()
                elif a == "n": break
                else: continue
            break
        cyc += 1
        cords = pyautogui.locateCenterOnScreen("../screens/video_purple.png", confidence=0.8)
        if not cords: cords = pyautogui.locateCenterOnScreen("../screens/video.png", confidence=0.8)
        if not cords:
            print(f"[{cyc}] ERROR: Kein Video gefunden")
            print(f"[{cyc}] STATUS: Starte neu")
            continue
        else:
            print(f"[{cyc}] STATUS: 'Video' gefunden")
            pyautogui.click(cords)
    # # CLICK ON PLAY BUTTON
        time.sleep(2.5)
        cords = pyautogui.locateCenterOnScreen("../screens/ansehen.png", confidence=0.8)
        if not cords:
            print(f"[{cyc}] ERROR: Kein Play-Button gefunden")
            print(f"[{cyc}] STATUS: Starte neu")
            continue
        else:
            print(f"[{cyc}] STATUS: 'Play' gefunden")
            pyautogui.click(cords)
    # # CLICK ON WATCH OR RETRIEVE BUTTON
        count = 1
        found = False
        ext = False
        while not found:
            time.sleep(2)
            cords = pyautogui.locateCenterOnScreen("../screens/einloesen.png", confidence=0.8)
            cords2 = pyautogui.locateCenterOnScreen("../screens/ansehen2.png", confidence=0.8)
            if cords:
                found = True
                print(f"\n[{cyc}] STATUS: 'Einlösen' gefunden, Versuch [{count}]")
                pyautogui.click(cords)
                ext = True
                continue
            elif cords2:
                found = True
                print(f"\n[{cyc}] STATUS: 'Video ansehen' gefunden, Versuch [{count}]")
                pyautogui.click(cords2)
            else:
                print(f"[{cyc}] STATUS: Kein Knopf gefunden, Versuch [{count}]")
                count += 1
        if ext: continue
    # # SEARCH FOR ACTIVATE OR NO THANKS
        time.sleep(1)
        cords = pyautogui.locateCenterOnScreen("../screens/ansehen.png", confidence=0.8)
        if not cords:
            print(f"[{cyc}] ERROR: Kein Play-Button gefunden")
            print(f"[{cyc}] STATUS: Starte neu")
            continue
        pyautogui.click(cords)
        count = 1
        found = False
        while not found:
            cords = pyautogui.locateCenterOnScreen("../screens/einloesen.png", confidence=0.8)
            cords2 = pyautogui.locateCenterOnScreen("../screens/nein_danke.png", confidence=0.8)
            cords3 = pyautogui.locateCenterOnScreen("../screens/close.png")
            if cords:
                found = True
                print(f"\n[{cyc}] STATUS: 'Einlösen' gefunden, Versuch [{count}]")
                pyautogui.click(cords)
            elif cords2:
                found = True
                print(f"\n[{cyc}] STATUS: 'Nein Danke' gefunden, Versuch [{count}]")
                pyautogui.click(cords2)
            elif cords3:
                found = True
                print(f"\n[{cyc}] STATUS: 'Upgrade' gefunden, Versuch [{count}]")
                pyautogui.click(cords3)
            else:
                print(f"[{cyc}] STATUS: Button wurde nicht gefunden, Versuch [{count}]")
                count += 1
    # # END CYCLE
        print(f"\nZyklus [{cyc}] beendet, starte [{cyc + 1}] ...")
        time.sleep(0.5)
        print("3", end="\r")
        time.sleep(1)
        print("2", end="\r")
        time.sleep(1)
        print("1", end="\r")
        time.sleep(1)
        os.system("cls")
