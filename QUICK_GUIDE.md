# Flask Authentication App - Quick Guide

## How to Run the Application
1. **Start the app**: Double-click `start_app.bat` or run:
   ```
   "c:/Users/snipe/Downloads/New WinRAR ZIP archive/Project/.venv/Scripts/python.exe" app.py
   ```

2. **Open your browser**: Go to `http://127.0.0.1:5000`

## How to Manage Database

### Clear Database Data
You have several options to remove database data:

#### Option 1: Use the Database Management Script
Double-click `manage_database.bat` and choose:
- **Option 1**: Reset entire database (removes all tables and data)
- **Option 2**: Clear only users (keeps table structure)
- **Option 3**: Show current users

#### Option 2: Use Command Line
```bash
# Show all users
python reset_database.py show

# Clear all users (keeps table structure)
python reset_database.py clear

# Reset entire database (removes everything)
python reset_database.py reset
```

#### Option 3: Delete Database File
Simply delete the database file:
```bash
# Delete the database file
del "instance\database.db"
```

#### Option 4: Manual Database Reset
Delete the database file and restart the app - it will create a new empty database automatically.

## App Features
- ✅ User Registration with validation
- ✅ Password hashing with bcrypt
- ✅ Email-based OTP verification
- ✅ Session management
- ✅ Beautiful responsive UI
- ✅ Flash message notifications
- ✅ Security features (CSRF protection, input validation)

## Testing Mode
The app runs in testing mode by default (DISABLE_EMAIL=True), which means:
- OTP codes are displayed in flash messages instead of being sent via email
- You can still test the full authentication flow
- No email configuration needed for testing

## Email Configuration
To enable real email sending, create a `.env` file with:
```
DISABLE_EMAIL=False
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## Project Structure
```
Project/
├── app.py                 # Main Flask application
├── reset_database.py      # Database management script
├── start_app.bat         # Easy app launcher
├── manage_database.bat   # Database management GUI
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md            # Project documentation
├── templates/           # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── verify_otp.html
│   └── success.html
└── instance/
    └── database.db      # SQLite database file
```

## Troubleshooting
1. **App won't start**: Make sure virtual environment is activated
2. **Database errors**: Try resetting the database with `reset_database.py reset`
3. **Email not working**: Check if DISABLE_EMAIL is set to True for testing
4. **Permission errors**: Run terminal as administrator if needed
