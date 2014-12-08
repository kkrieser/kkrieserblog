from behave import given, when, then

@given('a user')
def step_impl(context):
    from django.contrib.auth.models import User
    u = User(username ='kkrieser', email='kkrieser@unomaha.edu')
    u.set_password('kotton18')

@when('I log in')
def step_impl(context):
    br = context.browser
    br.open(context.browser_url('/admin))
    br.select_form(nr=0)
    br.form['username'] = 'kkrieser'
    br.form['password'] = 'bar'
    br.submit()

@then(I see my account summary')
def step_impl(context):
    br = context.browser
    response = br.response()
    assert response.code == 200
    assert br.geturl().endswith('/admin')

@then('I see a warm and welcoming message')
def step_impl(context):
    soup = context.parse_soup()
    msg = str(soup.findAll('h2', attrs={'class': 'welcome'})[0])
    assert "Welcome, kkrieser" in msg

