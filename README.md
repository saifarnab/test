# RESEND

##### -- Build on python 3.8.10

```
How to run:
1. Create a virtual env & activate it 
2. RUN --> pip3 install -r requirements.txt
1. Make a .env from sample.env (set variables of the env)
2. In the resources directory upload the required dataset (FYI: name must be similar)
3. RUN --> python3 manage.py migrate
3. RUN --> python3 manage.py runscript config_init
4. RUN --> python3 manage.py runscript insert_contacts
5. RUN --> python3 manage.py runscript insert_connected_accounts
5. RUN --> python3 manage.py runscript send_emails (perodically run it)
5. RUN --> python3 manage.py runscript send_followup_emails (perodically run it)
```

```
Generate user
1. RUN --> python3 manage.py createsuperuser
```

```
Run project:
1. RUN --> python3 manage.py runserver 0.0.0.0:8000
```

```
Portal:
1. VISIT --> http://0.0.0.0:8000/portal
```
