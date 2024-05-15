import { app, BrowserWindow } from 'electron';
import { fileURLToPath } from 'node:url'; // Import fileURLToPath function to convert import.meta.url to a file path
import path from 'node:path';

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    transparent: true,
    vibrancy: {
      theme: 'dark',
      effect: 'acrylic',
      disableOnBlur: true,
    },
    backgroundColor: '#00000000',
    webPreferences: {
      preload: path.join(fileURLToPath(import.meta.url), 'preload.js') // Use fileURLToPath to convert import.meta.url to a file path
    }
  });

  win.loadFile('index.html');
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
}).catch(error => {
  console.error('Error starting the app:', error);
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
