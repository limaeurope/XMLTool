import tkinter as tk
import os
import json
import subprocess


class Config(object):
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not Config.singleton:
            Config.singleton = super().__new__(cls)
        return Config.singleton

    def __init__(self):
        CONFIG_JSON = "settings.json"
        if os.path.exists(CONFIG_JSON):
            configJSON = json.load(CONFIG_JSON)
        else:
            configJSON = self.jsonInit()
        self.projectS = configJSON["projects"]

    def jsonInit(self):
        return {
            "projects": {}
        }


class Project:
    def __init__(self, name="", sourceFolder="", destFolder="", transator=None):
        self.name = name
        self.sourceFolder = sourceFolder
        self.destFolder = destFolder
        self.transator = transator


class Translator:
    def __init__(self, name="", path="", command=""):
        self.name = name
        self.path = path
        self.command = command

    def __call__(self, source="", dest="", *args, **kwargs):
        subprocess.call(" ".join([self.path + self.command + source, dest]))

class MainForm:
    def __init__(self):
        self.config = Config()

        self.top = tk.Tk()
        self.bStart = tk.Button(text="Start", command=self.startButtonPressed)
        self.bStart.grid(row=0, column=1)
        self.bStart = tk.Button(text="Settings", command=self.startButtonPressed)
        self.bStart.grid(row=0, column=2)
        self.bStart = tk.Button(text="New", command=self.startButtonPressed)
        self.bStart.grid(row=0, column=3)
        # self.eSource = tk.Entry()
        # self.eSource.grid(row=1, column=0)
        # self.eDest = tk.Entry()
        # self.eDest.grid(row=1, column=1)
        self.sProjectName = tk.StringVar()
        self.lProjectS = ["a", "b"]
        self.dProjects = tk.OptionMenu(self.top, self.sProjectName, *self.lProjectS)
        self.dProjects.grid(row=0, column=0)
        self.top.mainloop()

    def startButtonPressed(self):
        pass

    def newButtonPressed(self):
        w = ProjectForm()


    def settingsButtonPressed(self):
        pass

class ProjectForm:
    def __init__(self):
        self.top = tk.Tk()
        self.eName = tk.Entry()
        self.eName.grid(row=0, column=1)
        self.eSource = tk.Entry()
        self.eSource.grid(row=1, column=0)
        self.eDest = tk.Entry()
        self.eDest.grid(row=1, column=1)
        self.bOK = tk.Button(text="OK", command=self.okButtonPressed)
        self.bOK.grid(row=2, column=0, )

    def okButtonPressed(self):
        p = Project(name=self.eName.get(),
                    sourceFolder=self.eSource.get(),
                    destFolder=self.eDest.get(),)



def main():
    MainForm()

if __name__ == '__main__':
    main()
