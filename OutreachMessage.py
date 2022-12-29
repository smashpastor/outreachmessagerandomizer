import random
import sys
import tkinter as tk
from tkinter import messagebox

import pyperclip

if not sys.executable:
    result = messagebox.showinfo("Python is not detected, please install and try again.")
else:
    print("Python detected")
    # Create a pop-up box asking the user to press OK when they are ready
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askokcancel("Ready?", "Press OK when ready for the greeting message, or Cancel to exit.")

    if not result:
        # User pressed Cancel, so exit the script
        sys.exit()

    # Data sets, plan to pull from a text file instead soon
    data0 = ["Hello there!", "Hey! I hope you're doing well today", "Hello, how are you doing today?"]
    data1 = ["I'm Sean, and I work for a digital rights management/viral clip agency known as Claimable.", "My name is Sean and I work for a digital rights management and viral clip agency known as Claimable. Essentially we search the internet for clips we think have the ability to go viral and purchase them for the purposes of compilations on YouTube.", "I work for a company called Claimable that specializes in digital rights management and viral clips."]
    data2 = ["I discovered your TikTok earlier and I wanted to see if you’d be willing to sell the rights to use one of the clips on YouTube?", "I came across your TikTok earlier and I wanted to see if you’d be interested in selling the rights to use one of the clips on YouTube?", "I came across your TikTok the other day and I wanted to see if you’d be willing to sell the rights to use one of the clips on YouTube?", "I came across your YouTube channel today and I wanted to see if you’d be willing to sell the rights to use a clip from you to use ourselves on YouTube"]
    data3 = ["You wouldn’t need to take the video down and would still have complete creative freedom over when and where your clip gets posted. We just wanted to purchase the rights to use the clip on YouTube for ourselves! Let me know what you think whenever you can, thanks so much!!", "You'd still have complete creative freedom over when and where your clip gets posted. We just wanted to purchase the rights to use the clip on YouTube for ourselves! Let me know what you think whenever you can, thanks so much!!", "You'd still have the freedom over when and where your clip gets posted. We just wanted to purchase YouTube rights! Let me know what you think at your earliest convenience, thanks so much!!"]

    # Pick one random item from each data set
    item0 = random.choice(data0)
    item1 = random.choice(data1)
    item2 = random.choice(data2)
    item3 = random.choice(data3)

    items = [item0]
    # Convert the list to a string and copy it to the clipboard
    text = "\n".join(items)
    pyperclip.copy(text)

    # Create a pop-up box asking the user to press OK when they are ready
    root = tk.Tk()
    root.withdraw()
    result = tk.messagebox.askokcancel("Ready?", "The first message has been copied. Press OK when ready for the second message, or Cancel to exit.")

    if not result:
        # User pressed Cancel, so exit the script
        sys.exit()

    items = [item1]
    # Convert the list to a string and copy it to the clipboard
    text = "\n".join(items)
    pyperclip.copy(text)

    # Create a pop-up box asking the user to press OK when they are ready
    root = tk.Tk()
    root.withdraw()
    result = tk.messagebox.askokcancel("Ready?", "The second message has been copied. Press OK when ready for the third message, or Cancel to exit.")

    if not result:
        # User pressed Cancel, so exit the script
        sys.exit()

    items = [item2]
    # Convert the list to a string and copy it to the clipboard
    text = "\n".join(items)
    pyperclip.copy(text)

    # Create a pop-up box asking the user to press OK when they are ready
    root = tk.Tk()
    root.withdraw()
    result = tk.messagebox.askokcancel("Ready?", "The third message has been copied. Press OK when ready for the fourth message, or Cancel to exit.")

    if not result:
        # User pressed Cancel, so exit the script
        sys.exit()

    items = [item3]
    # Convert the list to a string and copy it to the clipboard
    text = "\n".join(items)
    pyperclip.copy(text)

    # Create a pop-up box asking the user to press OK when they are ready
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showinfo("Ready?", "The last message has been copied. press OK when done.")

    if not result:
        # User pressed Cancel, so exit the script
        sys.exit()


    print("Text copied to clipboard!")
