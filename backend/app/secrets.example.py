DJANGO_SECRET_KEY = "your django secret key"
POSTGRES_PASSWORD = "your postgres password"
JWT_SECRET_KEY = "your jwt secret key"
GOOGLE_CLIENT_ID = "your google client id"
GOOGLE_CLIENT_SECRET = "your google secret"

$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "username" = "abuahmed1"
    "email" = "abuahmed0821@gmail.com"
    "password1" = "complexpassword123"
    "password2" = "complexpassword123"
} | ConvertTo-Json

Invoke-WebRequest -Uri 'http://localhost:8000/api/register/' -Method POST -Headers $headers -Body $body

 $headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "username" = "abuahmed1"
    "email" = "abuahmed0821@gmail.com"
    "password" = "complexpassword123"
} | ConvertTo-Json

Invoke-WebRequest -Uri 'http://localhost:8000/api/login/' -Method POST -Headers $headers -Body $body