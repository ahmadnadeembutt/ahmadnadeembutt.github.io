# 🌐 Local Hosting Guide

This guide shows you multiple ways to run your portfolio website locally for testing and development.

## 🚀 **Method 1: Python HTTP Server (Recommended)**

### Quick Start:
1. **Double-click** `start-server.bat` in your portfolio folder
2. **OR** run in command prompt: `python -m http.server 8000`
3. Open browser: `http://localhost:8000`

### Why Use a Local Server?
- **File Protocol Issues**: Opening `index.html` directly in browser can cause issues with:
  - External CDN resources (Tailwind, GSAP, Feather Icons)
  - Canvas animations and WebGL
  - Form submissions
  - CORS (Cross-Origin Resource Sharing) restrictions

## 🛠️ **Alternative Methods**

### **Method 2: Node.js HTTP Server**
If you have Node.js installed:
```bash
# Install http-server globally
npm install -g http-server

# Start server
http-server -p 8000

# Access at: http://localhost:8000
```

### **Method 3: Live Server (VS Code Extension)**
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"
4. Automatically opens in browser with live reload

### **Method 4: PHP Built-in Server**
If you have PHP installed:
```bash
php -S localhost:8000
```

### **Method 5: Simple File Opening (Not Recommended)**
- **Issue**: May not work properly due to CORS restrictions
- **Workaround**: Open `index.html` directly in browser
- **URL**: `file:///D:/PORTFOLIO/index.html`

## 🔧 **Troubleshooting**

### **Port Already in Use Error:**
```bash
# Try different port
python -m http.server 3000
# Then access: http://localhost:3000
```

### **Python Not Found:**
- Install Python from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

### **Animations Not Working:**
- Ensure you're using `http://localhost:8000` (not `file://`)
- Check browser console for errors (F12)
- Try different browser (Chrome recommended)

### **External Resources Not Loading:**
- Check internet connection
- CDN resources (Tailwind, GSAP, Feather Icons) need internet access

## 📱 **Testing Your Website**

### **Desktop Testing:**
- Chrome (recommended for WebGL)
- Firefox
- Safari
- Edge

### **Mobile Testing:**
1. Find your computer's IP address
2. Access from mobile: `http://YOUR_IP:8000`
3. Example: `http://192.168.1.100:8000`

### **Find Your IP Address:**
```bash
# Windows Command Prompt
ipconfig

# Look for "IPv4 Address" under your network adapter
```

## 🎯 **Development Workflow**

1. **Start local server**: `python -m http.server 8000`
2. **Make changes** to HTML/CSS/JS files
3. **Refresh browser** to see changes
4. **Test on different devices** using your IP address
5. **When ready**, deploy to GitHub Pages

## 🚀 **Quick Commands Reference**

```bash
# Start Python server (port 8000)
python -m http.server 8000

# Start Python server (port 3000)
python -m http.server 3000

# Start Python server (specific IP)
python -m http.server 8000 --bind 0.0.0.0

# Stop server
Ctrl + C
```

## 📝 **Notes**

- **Keep server running** while developing
- **Browser cache**: Use Ctrl+F5 to hard refresh
- **File changes**: Automatically reflected on refresh
- **Performance**: Local server is faster than GitHub Pages for development

---

**Ready to deploy?** Check `DEPLOYMENT.md` for GitHub Pages instructions!


