from cefpython3 import cefpython as cef
import sys
import platform
from threading import Thread
import tkinter as tk
from tkinter import ttk

class CefBrowser:
    def __init__(self, master):
        self.master = master
        self.master.title("CEF Python Browser")
        self.master.geometry("1024x700")

        # Toolbar
        toolbar = tk.Frame(master)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.back_btn = ttk.Button(toolbar, text="Back", command=self.back)
        self.back_btn.pack(side=tk.LEFT)
        self.forward_btn = ttk.Button(toolbar, text="Forward", command=self.forward)
        self.forward_btn.pack(side=tk.LEFT)
        self.reload_btn = ttk.Button(toolbar, text="Reload", command=self.reload)
        self.reload_btn.pack(side=tk.LEFT)

        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(toolbar, textvariable=self.url_var, width=80)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.url_entry.bind("<Return>", self.navigate_to_url)

        # Browser frame
        self.browser_frame = tk.Frame(master)
        self.browser_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize CEF
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(window_handle=self.get_window_handle(),
                                             url="https://www.google.com")
        cef.MessageLoopWork()  # Start message loop integration

        # Update URL bar
        self.update_url()

    def get_window_handle(self):
        if platform.system() == "Windows":
            return self.browser_frame.winfo_id()
        elif platform.system() == "Linux":
            return self.browser_frame.winfo_id()
        elif platform.system() == "Darwin":
            # MacOS requires special handling (offscreen mode)
            return self.browser_frame.winfo_id()
        else:
            raise Exception("Unsupported OS")

    def navigate_to_url(self, event=None):
        url = self.url_var.get()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.LoadUrl(url)

    def back(self):
        if self.browser.CanGoBack():
            self.browser.GoBack()

    def forward(self):
        if self.browser.CanGoForward():
            self.browser.GoForward()

    def reload(self):
        self.browser.Reload()

    def update_url(self):
        self.url_var.set(self.browser.GetUrl())
        self.master.after(1000, self.update_url)  # update every second


if __name__ == "__main__":
    root = tk.Tk()
    app = CefBrowser(root)
    root.protocol("WM_DELETE_WINDOW", cef.Shutdown)
    root.mainloop()
