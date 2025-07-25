# Referral System API

Bu loyiha telefon raqami orqali avtorizatsiya va foydalanuvchilar o‘rtasida referral (invayt) kodlar orqali bog‘lanishni ta’minlovchi oddiy backend API hisoblanadi. Django + DRF asosida qurilgan.

## Acknowledgements

- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [How to write a Good README](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

---

## API Reference

### 🔐 1. Yuborish – Telefon raqam orqali avtorizatsiya boshlanishi

```http
POST /api/send-code/
```
#### Request Body
```json
{
  "phone_number": "998901234567"
}
```
#### Response
```json
{
  "message": "Code sent successfully"
}
```
### 🔐 2. Tasdiqlash – Telefon raqam orqali avtorizatsiyani tasdiqlash

```http
POST /api/verify-code/
```
#### Request Body
```json
{
  "phone_number": "998901234567",
  "code": "123456"
}
```
#### Response
```json
{
  "message": "Code verified successfully",
}
```
### 🔗 3. Referral – Show profile

```http
GET /api/profile/?phone=998901234567
```

#### Response
```json
{
  "phone_number": "998901234567",
  "invite_code": "A1B2C3",
  "used_invite_code": "Z9Y8X7",
  "referrals": [
    "998911112233",
    "998944445566"
  ]
}
```
### 🔗 4. Activating another user's invite code

```http
POST /api/use-invite/?phone_number=998901234567
```
#### Request Body
```json
{
  "code": "A1B2C3"
}
```
#### Response
```json
{
  "message": "Invite code used successfully"
}
```
#### Response (if invite code is already used)
```json
{
  "message": "Invite code already used"
}
```

## 🧪 Running Locally
```bash
python -m venv venv && source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```
## 📦 Docker
```bash
docker build -t referral-system-api .
```

```bash
docker run -p 8000:8000 referral-system-api
```
## 📦 Docker Compose
```bash
docker-compose build
```

```bash
docker-compose up
```
## 📦 Docker Compose (with PostgreSQL)
```bash
docker-compose -f docker-compose-postgres.yml build
```

```bash
docker-compose -f docker-compose-postgres.yml up
```
