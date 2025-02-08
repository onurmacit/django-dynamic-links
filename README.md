# Django Dynamic Links

This repository demonstrates how to create dynamic links in Django, allowing users to share content and be redirected to specific pages within your application. It includes features like device-specific redirection (iOS, Android, Web), secure link verification, and customizable dynamic link generation. You can access the article about this repo here.

## Features
- **Dynamic Link Generation**: Generate shareable links for specific content.
- **Device-Specific Redirection**: Redirect users based on their device (iOS, Android, Web).
- **Secure Link Verification**: Use `assetlinks.json` and `apple-app-site-association` for secure redirection on Android and iOS.
- **Customizable**: Easily adapt the logic for your specific use case.
- **SEO-Friendly**: Dynamic links improve user experience and make your application more shareable.
- **Testing Suite**: Includes unit tests, integration tests, and edge case testing.

---

## Table of Contents
1. [Installation](#installation)
2. [Setup](#setup)
3. [API Endpoints](#api-endpoints)
4. [Usage Examples](#usage-examples)
5. [Best Practices](#best-practices)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher
- Django Rest Framework (DRF)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/your-username/django-dynamic-links.git
cd django-dynamic-links
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python manage.py migrate
```

4. Create a `.env` file in the root directory and add your configuration:
```plaintext
SECRET_KEY=your-secret-key-here
DEBUG=True
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Setup

### Environment Variables
Create a `.env` file in the root directory and add the following:
```plaintext
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Run Migrations
Apply the database migrations:
```bash
python manage.py migrate
```

### Start the Server
Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### 1. Create an Item
- **URL**: `/api/items/`
- **Method**: `POST`
- **Request Body**:
```json
{
  "title": "Test Item",
  "description": "This is a test item."
}
```
- **Response**:
```json
{
  "id": 1,
  "title": "Test Item",
  "description": "This is a test item.",
  "share_link": "http://example.com/item_detail/1/"
}
```

### 2. Redirect to Item Detail
- **URL**: `/item_detail/<int:item_id>/`
- **Method**: `GET`
- **Response**:
  - **iOS**: Redirects to the App Store.
  - **Android**: Redirects to the Google Play Store.
  - **Web**: Redirects to the item detail page.

## Usage Examples

### Create an Item
```bash
curl -X POST http://127.0.0.1:8000/api/items/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Test Item",
  "description": "This is a test item."
}'
```

### Redirect to Item Detail
```bash
curl -X GET http://127.0.0.1:8000/item_detail/1/
```


## Testing

### Running Tests
To run the test suite, use the following command:

```bash
python manage.py test links
```

### Test Coverage

The test suite includes:

- Unit tests for models, views, and serializers.

- Integration tests for the entire flow (creation, link generation, redirection).

- Edge cases (e.g., invalid item IDs, empty fields).


## Best Practices
- **Secure Link Verification**: Use `assetlinks.json` and `apple-app-site-association` for secure redirection on Android and iOS.
- **HTTPS**: Always use HTTPS in production to encrypt data transmitted between the client and server.
- **Device Detection**: Use reliable user-agent parsing to ensure accurate device detection.
- **Testing**: Regularly test dynamic links on different devices and browsers to ensure compatibility.
- **Error Handling**: Handle invalid item IDs and edge cases gracefully (e.g., return 404 for invalid IDs).

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature or fix"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

Please ensure your code follows **PEP 8** guidelines and includes tests.

## License
This project is licensed under the **MIT License**. See the LICENSE file for details.

## Acknowledgments
- Thanks to the **Django community** for their excellent documentation and support.
- Inspired by **Firebase Dynamic Links**, but implemented as a self-hosted solution.

## Contact
For questions or feedback, feel free to reach out:

- [**Linkedin**](https://www.linkedin.com/in/onur-macit-b42a19223/)
- [**GitHub**](https://github.com/onurmacit)
