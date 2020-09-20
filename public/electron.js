const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const { PythonShell } = require("python-shell");

const path = require("path");

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 900,
    height: 680,
    webPreferences: {
      plugins: true,
      webviewTag: true,
    },
    icon: __dirname + "/icon.ico",
  });

  mainWindow.loadURL(`file://${path.join(__dirname, "../build/index.html")}`);

  // mainWindow.openDevTools();
  PythonShell.run(
    __dirname.slice(0, __dirname.indexOf("\\resources\\") + 11) +
      "\\extraResources\\electron-backend\\app.py",
    null,
    function (err) {
      if (err) {
        throw err;
      }
      console.log("finished");
    }
  );
  mainWindow.on("closed", () => (mainWindow = null));
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (mainWindow === null) {
    createWindow();
  }
});
