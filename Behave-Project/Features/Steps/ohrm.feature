Feature: OrangeHRM Logo
    Scenario: Logo Presence on OrangeHRM home page
        Given Launch Chrome Browser
        When Open Orange hrm homepage
        Then Verify that the logo is present on page
        And Close Browser