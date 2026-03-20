import os
import httpx

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")


def main() -> None:
    signup = httpx.post(
        f"{BASE_URL}/signup",
        json={"username": "jeremy", "email": "jeremy@example.com", "password": "testpass123"},
    )
    if signup.status_code not in (200, 201, 400):
        raise SystemExit(f"Signup failed: {signup.status_code} {signup.text}")

    login = httpx.post(
        f"{BASE_URL}/login",
        data={"username": "jeremy", "password": "testpass123"},
    )
    login.raise_for_status()
    token = login.json()["access_token"]

    expenses = httpx.get(f"{BASE_URL}/expenses", headers={"Authorization": f"Bearer {token}"})
    expenses.raise_for_status()

    print("Smoke OK:", len(expenses.json()), "expenses")


if __name__ == "__main__":
    main()
