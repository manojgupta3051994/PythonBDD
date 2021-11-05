Feature: OrangeHRM Logo

    Background: Common Steps
        Given Launch new Chrome Browser
        When Open an Orange hrm homepage

    Scenario: Login to OrangeHRM home page
        And Enter username "admin" and password "admin123"
        And Click on Login Button
        Then User is successfully logged in

    Scenario Outline: Login to OrangeHRM home page
        And Enter username "<username>" and password "<password>"
        And Click on Login Button
        Then User is successfully logged in
        Examples:
            | username  | password    | 
            | admin     | admin123    |  
            | admin123  | admi        |
            | admin     | admin12344  |
            | adminxyz  | akd         |
