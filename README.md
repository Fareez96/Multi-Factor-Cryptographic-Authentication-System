# Flask Authentication System with OTP

A complete Flask-based authentication system with OTP (One-Time Password) verification.

## Features

- User registration with password hashing
- User login with credentials validation
- OTP-based two-factor authentication
- Email OTP delivery (configurable)
- Session management
- Secure password storage with bcrypt
- Flash messages for user feedback
- Responsive Bootstrap UI

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**
   - Copy `.env.example` to `.env` and configure your settings
   - For development, `DISABLE_EMAIL=True` is set by default
   - For production, configure real email settings

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   - Open your browser and go to `http://127.0.0.1:5000`
   - You'll be redirected to the login page

## How It Works

### Registration Process
1. User fills out registration form (username, email, password)
2. Password is hashed using bcrypt before storage
3. User data is stored in SQLite database
4. Success message is displayed

### Login Process
1. User enters username and password
2. Credentials are validated against database
3. If valid, a 6-digit OTP is generated
4. OTP is sent via email (or displayed for testing)
5. User is redirected to OTP verification page

### OTP Verification
1. User enters the 6-digit OTP
2. System validates OTP and expiry time (5 minutes)
3. If valid, user is authenticated and redirected to dashboard
4. User can request a new OTP if needed

## Development Mode

When `DISABLE_EMAIL=True` in `.env`:
- OTP is displayed in flash messages instead of being sent via email
- No email configuration is required
- Perfect for development and testing

## Production Setup

For production use:
1. Set `DISABLE_EMAIL=False` in `.env`
2. Configure email settings:
   - `MAIL_SERVER=smtp.gmail.com`
   - `MAIL_PORT=587`
   - `MAIL_USERNAME=your_email@gmail.com`
   - `MAIL_PASSWORD=your_app_password`
3. Change `SECRET_KEY` to a secure random string
4. Use a production database instead of SQLite

## Security Features

- Password hashing with bcrypt
- Session-based authentication
- OTP expiration (5 minutes)
- Input validation and sanitization
- CSRF protection via Flask sessions
- Secure cookie configuration

## File Structure

```
project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment configuration
├── database.db           # SQLite database (auto-created)
└── templates/
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── verify_otp.html   # OTP verification page
    └── success.html      # Dashboard/success page
```

## Troubleshooting

1. **Database Issues**: Delete `database.db` and restart the application
2. **Email Issues**: Check your email configuration or use development mode
3. **OTP Not Working**: Ensure system time is correct and OTP hasn't expired
4. **Port Issues**: Change the port in `app.run()` if 5000 is occupied

## License

This project is for educational purposes.
2. Configure your email in `app.py`
3. Run: `python app.py`
