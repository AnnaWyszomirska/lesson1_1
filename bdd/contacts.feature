Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <lastname>, <address>, <home> and <mobile>
    When I add the contact to the list
    Then the new contact list is equal to the old contact list with the added contact

    Examples:
    |firstname |lastname |address |home |mobile |work
    |Zbigniew |Nowak |newadress |13241 |412341 |412341324
    |Jan |Kowalski |address1412341 |43214124|43241234 |123412341
    |Anna |Joanna |addressssss |111111 |2222222 |3333333

Scenario Outline: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old contact list without the deleted contact

Scenario Outline: Change a contact
    Given a non-empty contact list
    Given a random contact from the list to edit
    When I change the contact from the list
    Then the new contacts list is equal to the old contacts list

    Examples:
    |firstname |lastname |address |home |mobile |work
    |Zbigniew1 |Nowak1 |newadress1 |13241 |412341 |412341324
