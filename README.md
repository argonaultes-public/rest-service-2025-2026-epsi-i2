## Poste développeur

Aller à https://googlechromelabs.github.io/chrome-for-testing/

Télécharger le binaire de la version du navigateur à tester

Télécharger le binaire du driver du navigateur correspondant

```python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()

options.binary_location = '/path/to/chrome-linux64/chrome'

service = Service(executable_path='/path/to/chromedriver-linux64/chromedriver')

driver = webdriver.Chrome(options=options, service=service)

```

## Chaine d'intégration

Créer et démarrer un conteneur Selenium Grid pour tester la future utilisation au sein d'une CI.

```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
```

```python
from selenium.webdriver.firefox.options import Options


driver = webdriver.Remote(command_executor='http://localhost:4444', options=Options())

```

Pour accéder au bureau à distance via le navigateur, aller à http://localhost:7900.
Le mot de passe par défaut est `secret`.