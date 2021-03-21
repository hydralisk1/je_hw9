# Created by Joonil at 3/21/21
Feature: Test Scenarios for searching for an item on an Amazon Department

  Scenario: User can search for an item on an Amazon Department
    Given Open Amazon page
    When Search for "Watches" in the "Electronics" department
    Then Verify "Watches" is shown in the result page

  Scenario: User can see deals when mouse cursor hovers over an navigation menu in a product page
    Given Open "B074TBCSC8" product page
    When Mouse cursor hovers over New Arrivals menu
    Then Verify deals are shown