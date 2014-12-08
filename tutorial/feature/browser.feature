Feature: Logging into the app

    Scenario: a user logs in
      given a user
      when I log in
      then I see my account summary
      then I see a warm and welcoming message
